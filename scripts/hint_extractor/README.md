# Node Inlet/Outlet Extractor

This Python script scans a folder (and its subfolders) for MaxMSP `.maxpat` files matching the pattern `bs.node.<NodeName>.maxpat` (where `<NodeName>` contains no dots). It extracts information about inlets and outlets from each node and generates a single Markdown file summarizing all nodes.

## What the Script Does

- **Recursively searches** for files named `bs.node.<NodeName>.maxpat` (excluding files like `bs.node.Foo.bar.maxpat` and any ending with `.p.maxpat`).
- **Parses each file** as JSON and looks for `"box"` elements with `"varname"` starting with `vpl_inlet[` or `vpl_outlet[`.
- **Extracts**:
  - The 4th value in the `"args"` list (type).
  - The value after `"@hint"` in `"args"` (description, with `|` escaped for Markdown).
  - The 3rd value in `"args"` (used for sorting).
- **Sorts** inlets and outlets by the 3rd value in `"args"`.
- **Uses the node name** from the filename (the part between `bs.node.` and `.maxpat`).
- **Outputs** a single Markdown file (`all_nodes.md`) with a section for each node, listing its inlets and outlets in tables.

## How to Use

1. **Requirements**: Python 3.x.
2. **Place the script** in your workspace.
3. **Edit the script** to set the correct folder to scan:
    ```python
    root_folder = "/path/to/your/patchers/nodes"
    output_file = "all_nodes.md"
    ```
4. **Run the script**:
    ```sh
    python your_script_name.py
    ```
5. **Result**: The script creates `all_nodes.md` in the current directory, containing a summary of all node inlets and outlets.

## Example Output

```
# Beamer

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture    | int           | captured texture (left if stereo)      |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture    | int           | captured texture (left if stereo)      |
```

## Notes

- Only files matching `bs.node.<NodeName>.maxpat` (no extra dots) are processed.
- Inlets and outlets are sorted numerically by their index.
- The script escapes `|` in descriptions to avoid breaking Markdown tables.

---

Let me know if you want any more details or examples!