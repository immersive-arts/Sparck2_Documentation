# DrawMask

Loads and saves texures. The modification of textures is only black and white. The main purpose is the use for mask in combination with Texture-Effect-Nodes.

The saved texture will be a PNG.

<figure markdown>
![DrawMask Node](../../assets/images/nodes/DrawMask.png){ width="300" }
</figure> 

!!! success "Create Custom Masks for Texture Effects"
    DrawMask provides a simple black-and-white drawing editor for creating alpha masks. These masks can be used with texture effect nodes like [ShaderTexOP](ShaderTexOP.md) to control where effects are applied, hide projector overlap regions, or create custom vignettes.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `image file` | - | load image (TIFF. GIF, JPEG, PNG) and save mask |
    | `filewatch` | - | reloads texture automatically if file changes. |
    | `dimension` | - | default dimensions. used to create default mask. |
    | `planes` | - | The loaded image is a black and white-texture. This has to be transformed into a ARGB-texture and the planes defines how the black/white values are set for a 4-channel ARGB texture. <li>'mmmm' will set all channels to the bw-values. <li>'mwww' will only set the Alpha-channel to the bw-value, while the RGB-channels will be set to white (1.0) <li>'wmmm' will set the Alpha-channel to white and the RGB-channels to the bw-value. |
    | `edit` | - | sets the focus of the editor window to this node |
    | `render pass` | - | render pass. default is a manual render pass since the loaded texture needs only passed on once because of its static nature. |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture out |


---

## Plane Modes

!!! tip "Understanding Plane Settings"
    The `planes` property controls how black/white values are mapped to ARGB channels:
    
    | Mode | Alpha | Red | Green | Blue | Use Case |
    |------|-------|-----|-------|------|----------|
    | **mmmm** | mask | mask | mask | mask | Grayscale mask affecting all channels |
    | **mwww** | mask | white | white | white | Alpha-only mask (common for transparency) |
    | **wmmm** | white | mask | mask | mask | RGB mask with full opacity |
    
    Choose based on how your target effect node interprets the mask texture.

??? tip "DrawMask Editor Controls"
    The DrawMask editor has three modes: **Line**, **Polygon**, and **Color**. Press ++tab++ to cycle between modes.
    
    **General Controls:**
    
    | Key | Action |
    |-----|--------|
    | ++tab++ | Cycle through edit modes (Line → Polygon → Color → Line) |
    | ++h++ | Toggle help overlay |
    | ++s++ | Save mask to file |
    | ++space++ | Swap foreground/background colors |
    
    **Line Mode** — Freehand drawing:
    
    | Key | Action |
    |-----|--------|
    | :material-mouse-left-click: | Set starting point |
    | :material-mouse-left-click: - drag | Draw continuous line |
    | ++arrow-up++ | Increase line thickness |
    | ++arrow-down++ | Decrease line thickness |
    
    **Polygon Mode** — Filled polygon drawing:
    
    | Key | Action |
    |-----|--------|
    | :material-mouse-left-click: | Add polygon vertex |
    | ++enter++ | Complete polygon and start new one |
    | ++space++ | Finish current polygon (swaps colors) |
    
    **Color Mode** — Canvas operations:
    
    | Key | Action |
    |-----|--------|
    | ++c++ | Clear entire canvas |

## Workflow

!!! example "Creating a Mask"
    1. Set `dimension` to match your target texture size
    2. Click `edit` to open the drawing editor
    3. Use **Line mode** for freehand edges or **Polygon mode** for filled areas
    4. White areas = visible/applied, Black areas = hidden/masked
    5. Press `S` to save the mask as PNG
    6. Connect the texture outlet to your effect node's mask inlet

---

## Important Notes

!!! warning "Save Your Work"
    
    After modifying the texture with the editor, you must press `S` to save. Changes are **not automatically saved** and will be lost when the project is closed.

!!! info "File Locations"
    
    ```
    ~/_assets/_textures/     # Mask texture files (PNG)
    ```

---


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with DrawMask in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **DrawMask**

    ---
    * [:octicons-arrow-right-24: Texture](Texture.md) 
    * [:octicons-arrow-right-24: ShaderTexOP](ShaderTexOP.md) 
    * [:octicons-arrow-right-24: BlendSoftedge](BlendSoftedge.md)
    * [:octicons-arrow-right-24: SpatialShadery](SpatialShadery.md)

  
-   :material-video-box:{ .lg .middle } __Tutorials__

    ---
    
    [:octicons-arrow-right-24: Watch Now](../../start/tutorials/videos.md){ .md-button .md-button--primary }

-   :material-forum:{ .lg .middle } __Community__

    ---

    [:octicons-arrow-right-24: Join Now](https://github.com/immersive-arts/Sparck2/discussions){ .md-button .md-button--primary }


</div>

---

!!! question "Need help or want to suggest improvements?"
       
    [:fontawesome-brands-github: Report an issue](../../contributing/reporting-a-bug.md){ .md-button }
    [:fontawesome-brands-github: Improve the Docs](../../contributing/reporting-a-docs-issue.md){ .md-button }


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/DrawMask.md)*