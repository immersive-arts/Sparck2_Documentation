# DrawMask

Loads and saves texures. The modification of textures is only black and white. The main purpose is the use for mask in combination with Texture-Effect-Nodes.

The saved texture will be a PNG.

<figure markdown>
![DrawMask Node](../../assets/images/nodes/DrawMask.png){ width="300" }
</figure> 


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
    | properties | messages      | direct access to internal properties   |
    | texture    | texture       | texture applied to ...                 |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | messages      | direct access to internal properties   |
    | texture    | texture       | texture applied to ...                 |


---

## Important Notes

!!! warning "Calibration Requirements"
    
    After a modification of the texture with the editor, the file needs to be saved, otherwise the changes get lost.

!!! info "File Locations"
    
    ```
    ~/_assets/_projectors/     # Calibration files
    ~/_assets/_model/          # Calibration models (.obj)
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
    * [:octicons-arrow-right-24: TextureOP](TextureOP.md) 
    * [:octicons-arrow-right-24: BlendSoftedge](BlendSoftedge.md) 

  
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


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/DrawMask.md)*
