# ViewPort

In its most basic mode it takes a texture and displays it in its designated slice of the connected Window

More advanced usage includes the use of custom meshes or the result of a MeshWarp node (also a mesh) and/or using a second texture and applying a shader

<figure markdown>
![ViewPort Node](../../assets/images/nodes/ViewPort.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `window` | - | select the Window-node |
    | `slice` | - | select the slice inside the Window for output |
    | `mesh` | - | choose the type of mesh. <li>'default' is a simple mesh <li>'warp' links to a MeshWarp-node <li>'file' loads custom mesh <li>'none' no mesh at all. used with Cornerpin-node |
    | `fx shader` | - | choose a shader to be applied to the viewport mesh |
    | `transform` | - | the way the mesh is displayed inside the ViewPort's slice |
    | `position` | - | move the mesh in x and y axis |
    | `rotation` | - | rotate the mesh in z axis |
    | `scale` | - | scale the mesh in x and y axis |
    | `blend` | - | use the textures alphachannel for blending |
    | `depth` | - | use depth layering |
    | `show mesh` | - | show only the face-lines |
    | `object color` | only available with 'show mesh' | choose the meshes color |
    | `filewatch` | - | if using a loaded custom mesh, load the mesh once the file was changed. |
    | `Reset` | - | Resets the node to ist default state |

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
    
    Inside ViewPort the last renderpass is executed before the result is sent to the output devices like a projector, display or VR-goggles. Since it performative sensible to reduce the number of renderpasses, ViewPort has all these features to do different corrections in one go, like a warp and a colorcorrection at the same time.
    Notes on viewport - mesh:
    - when using a custom file, use the wavefront-obj format.
    - using no mesh makes only sense when working with CornerPin or MeshWarp nodes

!!! info "File Locations"
    
    ```
    ~/_assets/_projectors/     # Calibration files
    ~/_assets/_model/          # Calibration models (.obj)
    ```

---


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with ViewPort in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **ViewPort**

    ---
    * [:octicons-arrow-right-24: Window](Window.md) 
    * [:octicons-arrow-right-24: Monitor](Monitor.md) 
    * [:octicons-arrow-right-24: MeshWarp](MeshWarp.md) 
    * [:octicons-arrow-right-24: CornerPin](CornerPin.md) 

  
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

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ViewPort.md)*
