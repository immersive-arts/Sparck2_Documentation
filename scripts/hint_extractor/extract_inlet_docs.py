import os
import json
import re
import fnmatch
import subprocess
from pathlib import Path

# --- CONFIGURATION ---
# Set these paths as needed
root_folder = "/Volumes/Ddrive/00_core/MaxMSP_Packages/Sparck2/patchers/nodes/ossia"
reference_folder = "/Volumes/Ddrive/04_projects/I.A[projects]/1508_SPARCK/07_MkDocs/docs/reference/nodes"
repo_root = "/Volumes/Ddrive/04_projects/I.A[projects]/1508_SPARCK/07_MkDocs"
output_file = "all_nodes.md"

def check_git_clean(repo_path):
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=repo_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.returncode != 0:
            print("Error: Could not check git status:", result.stderr)
            return False
        if result.stdout.strip():
            print("Repository has uncommitted changes. Please commit or stash them before running this script.")
            return False
        return True
    except Exception as e:
        print(f"Error running git: {e}")
        return False

def get_node_name_from_filename(filename):
    match = re.match(r'bs\.node\.([^.]+)\.maxpat$', filename)
    return match.group(1) if match else None

def get_shorthand(hint):
    return hint.split()[0] if hint else ""

def extract_info(box):
    args = box.get("args", [])
    if len(args) < 6:
        return None
    try:
        hint_idx = args.index("@hint")
        type_val = args[3] if len(args) > 3 else ""
        # Replace 'type' with 'message' for type_val
        if type_val == "type":
            type_val = "message"
        hint_val = args[hint_idx + 1] if len(args) > hint_idx + 1 else ""
        shorthand = get_shorthand(hint_val)
        # Escape '|' and '<' in hint_val
        hint_val = hint_val.replace("|", "&#124;").replace("<", "&lt;")
        sort_key = args[2] if len(args) > 2 else 0
        return {
            "shorthand": shorthand,
            "type": type_val,
            "hint": hint_val,
            "sort_key": sort_key
        }
    except ValueError:
        return None

def process_file(filepath, filename):
    with open(filepath, "r") as f:
        data = json.load(f)
    node_name = get_node_name_from_filename(filename)
    patcher = data.get("patcher", {})
    inlets, outlets = [], []
    for box_wrap in patcher.get("boxes", []):
        box = box_wrap.get("box", {})
        varname = box.get("varname", "")
        if varname.startswith("vpl_inlet["):
            info = extract_info(box)
            if info:
                inlets.append(info)
        elif varname.startswith("vpl_outlet["):
            info = extract_info(box)
            if info:
                outlets.append(info)

    def safe_sort_key(x):
        try:
            return int(x["sort_key"])
        except (ValueError, TypeError):
            return str(x["sort_key"])

    inlets.sort(key=safe_sort_key)
    outlets.sort(key=safe_sort_key)

    return node_name, inlets, outlets

def format_inlets_outlets_md(inlets, outlets):
    md = []
    md.append('=== "Inlets"\n')
    md.append("    | Inlet      | Type          | Description                            |")
    md.append("    |------------|---------------|----------------------------------------|")
    for inlet in inlets:
        md.append(f"    | {inlet['shorthand']} | {inlet['type']} | {inlet['hint']} |")
    md.append('\n=== "Outlets"\n')
    md.append("    | Outlet     | Type          | Description                            |")
    md.append("    |------------|---------------|----------------------------------------|")
    for outlet in outlets:
        md.append(f"    | {outlet['shorthand']} | {outlet['type']} | {outlet['hint']} |")
    md.append("")
    return "\n".join(md)

def replace_inlets_outlets_in_markdown(md_text, new_inlets_outlets):
    # Find the "## Reference" section
        # Find the first === "Inlets"
        inlets_start = re.search(r'^=== "Inlets".*$', md_text, re.MULTILINE)
        if not inlets_start:
            return None
        start = inlets_start.start()

        # Find all === "Outlets" blocks
        outlets_blocks = [m for m in re.finditer(r'^=== "Outlets".*$', md_text, re.MULTILINE)]
        if not outlets_blocks:
            return None
        # Use the last one
        last_outlets = outlets_blocks[-1]
        # Find the last indented line after the last === "Outlets"
        after_outlets = md_text[last_outlets.end():]
        indented_lines = list(re.finditer(r'^(    .*\n?)+', after_outlets, re.MULTILINE))
        if indented_lines:
            end = last_outlets.end() + indented_lines[-1].end()
        else:
            # If no indented lines, just go to the end of the outlets block
            end = last_outlets.end()

        # Replace the block
        new_md = md_text[:start] + new_inlets_outlets + md_text[end:]
        return new_md

def main():
    if not check_git_clean(repo_root):
        return

    all_nodes = []
    log = []
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".p.maxpat"):
                continue
            node_name = get_node_name_from_filename(filename)
            if node_name:
                filepath = os.path.join(dirpath, filename)
                try:
                    node_name, inlets, outlets = process_file(filepath, filename)
                    all_nodes.append((node_name, inlets, outlets))
                except Exception as e:
                    log.append(f"{node_name}: Failed to extract inlets/outlets: {e}")

    all_nodes.sort(key=lambda x: x[0].lower())

    # Write all_nodes.md for reference (optional)
    with open(output_file, "w") as f:
        for node_name, inlets, outlets in all_nodes:
            f.write(f"# {node_name}\n\n")
            f.write(format_inlets_outlets_md(inlets, outlets))
            f.write("\n\n")

    # Now update the markdown files
    for node_name, inlets, outlets in all_nodes:
        md_path = os.path.join(reference_folder, f"{node_name}.md")
        if not os.path.exists(md_path):
            log.append(f"{node_name}: Reference file not found: {md_path}")
            continue
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                md_text = f.read()
            new_inlets_outlets = format_inlets_outlets_md(inlets, outlets)
            new_md = replace_inlets_outlets_in_markdown(md_text, new_inlets_outlets)
            if new_md is None:
                log.append(f"{node_name}: Could not find inlets/outlets section in {md_path}")
                continue
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(new_md)
            log.append(f"{node_name}: Successfully updated {md_path}")
        except Exception as e:
            log.append(f"{node_name}: Failed to update {md_path}: {e}")

    print("\nUpdate log:")
    for entry in log:
        print(entry)

if __name__ == "__main__":
    main()