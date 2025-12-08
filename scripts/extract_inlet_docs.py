import os
import json
import re
import fnmatch

def get_node_name_from_filename(filename):
    # Extract the * part from bs.node.*.maxpat
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
        hint_val = args[hint_idx + 1] if len(args) > hint_idx + 1 else ""
        shorthand = get_shorthand(hint_val)
        hint_val = hint_val.replace("|", "&#124;")
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
    inlets.sort(key=lambda x: int(x["sort_key"]) if str(x["sort_key"]).isdigit() else x["sort_key"])
    outlets.sort(key=lambda x: int(x["sort_key"]) if str(x["sort_key"]).isdigit() else x["sort_key"])
    return node_name, inlets, outlets

def main(root_folder, output_file):
    all_nodes = []
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
                    print(f"Error processing {filepath}: {e}")

    all_nodes.sort(key=lambda x: x[0].lower())

    with open(output_file, "w") as f:
        for node_name, inlets, outlets in all_nodes:
            f.write(f"# {node_name}\n\n")
            f.write('=== "Inlets"\n\n')
            f.write("    | Inlet      | Type          | Description                            |\n")
            f.write("    |------------|---------------|----------------------------------------|\n")
            for inlet in inlets:
                f.write(f"    | {inlet['shorthand']} | {inlet['type']} | {inlet['hint']} |\n")
            f.write('\n=== "Outlets"\n\n')
            f.write("    | Outlet      | Type          | Description                            |\n")
            f.write("    |------------|---------------|----------------------------------------|\n")
            for outlet in outlets:
                f.write(f"    | {outlet['shorthand']} | {outlet['type']} | {outlet['hint']} |\n")
            f.write("\n\n")

if __name__ == "__main__":
    root_folder = "/Volumes/Ddrive/00_core/MaxMSP_Packages/Sparck2/patchers/nodes/ossia"
    output_file = "all_nodes.md"
    main(root_folder, output_file)