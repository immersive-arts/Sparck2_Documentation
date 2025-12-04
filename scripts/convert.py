#!/usr/bin/env python3
"""
SPARCK Node Documentation Generator
Generates Material for MkDocs pages from SPARCK node JSON reference files
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any


class SPARCKDocGenerator:
    """Generate MkDocs documentation from SPARCK JSON reference files"""
    
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def clean_node_name(self, filename: str) -> str:
        """Extract clean node name from filename"""
        # Remove extensions and suffixes: Window.en.sparckref.json -> Window
        # Also handle: 1764581970338_Beamer_en_sparckref.json -> Beamer
        
        # First remove .json extension
        name = filename.replace('.json', '')
        
        # Remove .en.sparckref suffix if present
        if '.en.sparckref' in name:
            name = name.replace('.en.sparckref', '')
        
        # Remove _en_sparckref suffix if present (for underscore format)
        if '_en_sparckref' in name:
            name = name.replace('_en_sparckref', '')
        
        # If there's a timestamp prefix with underscore, extract the node name
        parts = name.split('_')
        if len(parts) > 1 and parts[0].isdigit():
            # Return the part after the timestamp
            return parts[1]
        
        # Otherwise return the cleaned name
        return name
    
    def format_property_table(self, properties: Dict[str, Any]) -> str:
        """Format properties as a markdown table"""
        if not properties:
            return "*No properties defined*"
        
        rows = []
        rows.append("| Property | Type | Description |")
        rows.append("|----------|------|-------------|")
        
        for prop_name, prop_data in properties.items():
            digest = prop_data.get('digest', '').strip()
            descript = prop_data.get('descript', '').strip()
            
            # Clean up description for table
            descript = descript.replace('\n', ' ').replace('\t', ' ')
            descript = ' '.join(descript.split())  # Remove extra whitespace
            
            # Escape pipe characters in descriptions
            descript = descript.replace('|', '\\|')
            
            prop_type = digest if digest else '-'
            
            rows.append(f"| `{prop_name}` | {prop_type} | {descript} |")
        
        return '\n    '.join(rows)
    
    def format_property_details(self, properties: Dict[str, Any]) -> str:
        """Format properties as detailed descriptions"""
        if not properties:
            return "*No properties defined*"
        
        details = []
        for prop_name, prop_data in properties.items():
            digest = prop_data.get('digest', '').strip()
            descript = prop_data.get('descript', '').strip()
            
            details.append(f"**`{prop_name}`**")
            if digest:
                details.append(f": *{digest}*")
            details.append(f"\n: {descript}\n")
        
        return '\n    '.join(details)
    
    def format_rig_table(self, rig_ref: Dict[str, Any]) -> str:
        """Format RIG reference as a markdown table"""
        if not rig_ref:
            return "*No RIG configuration available*"
        
        rows = []
        rows.append("| Parameter | Type | Description |")
        rows.append("|-----------|------|-------------|")
        
        for param_name, param_data in rig_ref.items():
            digest = param_data.get('digest', '').strip()
            descript = param_data.get('descript', '').strip()
            
            # Clean up description
            descript = descript.replace('\n', ' ').replace('\t', ' ')
            descript = ' '.join(descript.split())
            descript = descript.replace('|', '\\|')
            
            param_type = digest if digest else '-'
            
            rows.append(f"| `{param_name}` | {param_type} | {descript} |")
        
        return '\n    '.join(rows)
    
    def format_see_also(self, see_also: Dict[str, str]) -> str:
        """Format see also section as links"""
        if not see_also:
            return "*No related nodes*"
        
        links = []
        for node_name in see_also.keys():
            links.append(f"    - [**{node_name}**]({node_name}.md) - Related node")
        
        return '\n'.join(links)
    
    def format_notes(self, notes: Dict[str, str]) -> str:
        """Format notes section"""
        if not notes:
            return "*No additional notes*"
        
        note_list = []
        for note in notes.values():
            if note and note != "...":
                # Handle HTML-like list items
                if '<li>' in note:
                    # Extract list items
                    items = note.replace('<li>', '').split('\n')
                    for item in items:
                        item = item.strip()
                        if item:
                            note_list.append(f"    - {item}")
                else:
                    note_list.append(f"    {note}")
        
        return '\n'.join(note_list) if note_list else "*No additional notes*"
    
    def format_feedback(self, feedback: Dict[str, str]) -> str:
        """Format feedback section"""
        if not feedback:
            return ""
        
        feedback_text = []
        for text in feedback.values():
            if text:
                feedback_text.append(f"    {text}")
        
        return '\n    \n    '.join(feedback_text)
    
    def format_description(self, description: Dict[str, str]) -> str:
        """Format description section"""
        desc_parts = []
        for key in sorted(description.keys()):
            if description[key]:
                desc_parts.append(description[key])
        return '\n\n'.join(desc_parts)
    
    def generate_page(self, json_file: Path) -> None:
        """Generate a documentation page from a JSON file"""
        
        # Load JSON data
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract node name
        node_name = self.clean_node_name(json_file.name)
        
        # Get data sections
        digest = data.get('digest', 'No description available')
        description = self.format_description(data.get('description', {}))
        properties = data.get('PropertyReference', {})
        node_ref = data.get('NodeReference', {})
        rig_ref = data.get('RIGReference', {})
        see_also = data.get('seealso', {})
        links = data.get('links', {})
        notes = data.get('Notes', {})
        feedback = data.get('Feedback', {})
        
        # Build the markdown content
        md_content = f"""# {node_name}

{description}

<figure markdown>
![{node_name} Node](../../assets/images/nodes/{node_name}.png){{ width="300" }}
</figure> 


## Properties

The following properties can be configured for this node:

=== "Reference"

    {self.format_property_table(properties)}

=== "Workflow"

    1. TBD


---
"""

        # Add RIG Reference if available
        if rig_ref:
            md_content += f"""
## RIG Configuration

??? abstract "Advanced RIG Settings"
    
    The RIG (Rendering Interface Group) provides advanced configuration options:
    
    {self.format_rig_table(rig_ref)}

---

"""

        # Add Notes if available
        notes_content = self.format_notes(notes)
        if notes_content and notes_content != "*No additional notes*":
            md_content += f"""
## Important Notes

!!! warning "Calibration Requirements"
    
{notes_content}

!!! info "File Locations"
    
    ```
    ~/_assets/_projectors/     # Calibration files
    ~/_assets/_model/          # Calibration models (.obj)
    ```

---

"""

        # Format see_also for card grid
        see_also_links = ""
        if see_also:
            for related_node in see_also.keys():
                see_also_links += f"    * [:octicons-arrow-right-24: {related_node}]({related_node}.md) \n"
        else:
            see_also_links = "    * No related nodes defined"
        
        # Add card grid section
        md_content += f"""
<div class="grid cards" markdown>

-   :material-clock-fast:{{ .lg .middle }} __Quick Start__

    ---

    Get started with {node_name} in minutes
    
    [:octicons-arrow-right-24: Project Examples](../../start/examples/project_examples.md)

-   :material-file-document:{{ .lg .middle }} __Complementing__ **{node_name}**

    ---
{see_also_links}
  
-   :material-video-box:{{ .lg .middle }} __Tutorials__

    ---
    
    [:octicons-arrow-right-24: Watch Now](../../start/tutorials/videos.md){{ .md-button .md-button--primary }}

-   :material-forum:{{ .lg .middle }} __Community__

    ---

    [:octicons-arrow-right-24: Join Now](https://github.com/immersive-arts/Sparck2/discussions){{ .md-button .md-button--primary }}


</div>

---

!!! question "Need help or want to suggest improvements?"
       
    [:fontawesome-brands-github: Report an issue](../../contributing/reporting-a-bug.md){{ .md-button }}
    [:fontawesome-brands-github: Improve the Docs](../../contributing/reporting-a-docs-issue.md){{ .md-button }}


---

*Last updated: {datetime.now().strftime('%Y-%m-%d')} | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/{node_name}.md)*
"""

        # Write to output file
        output_file = self.output_dir / f"{node_name}.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"✓ Generated: {output_file.name}")
    
    def generate_all(self) -> None:
        """Generate documentation for all JSON files in input directory"""
        json_files = list(self.input_dir.glob("*.json"))
        
        if not json_files:
            print(f"No JSON files found in {self.input_dir}")
            return
        
        print(f"Found {len(json_files)} node reference files")
        print("Generating documentation pages...\n")
        
        for json_file in json_files:
            try:
                self.generate_page(json_file)
            except Exception as e:
                print(f"✗ Error processing {json_file.name}: {e}")
        
        print(f"\n✓ Documentation generated in: {self.output_dir}")
        print(f"✓ Total pages created: {len(list(self.output_dir.glob('*.md')))}")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Generate MkDocs documentation from SPARCK JSON reference files'
    )
    parser.add_argument(
        'input_dir',
        help='Directory containing JSON reference files'
    )
    parser.add_argument(
        'output_dir',
        help='Directory to write markdown documentation files'
    )
    
    args = parser.parse_args()
    
    generator = SPARCKDocGenerator(args.input_dir, args.output_dir)
    generator.generate_all()


if __name__ == '__main__':
    main()