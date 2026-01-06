# ViewPort

In its most basic mode it takes a texture and displays it in its designated slice of the connected [Window](Window.md).

More advanced usage includes the use of custom meshes or the result of a [MeshWarp](MeshWarp.md) node (also a mesh) and/or using a second texture and applying a shader

<figure markdown>
![ViewPort-Node](../../assets/images/nodes/ViewPort.png){ width="300" }
</figure> 

!!! info "Final Render Stage"
    ViewPort is the **last renderpass** before content is sent to output devices like projectors, displays, or VR goggles. Since reducing render passes is important for performance, ViewPort combines multiple corrections in a single pass — including warping, color correction, and shader effects.

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
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | main | texture | main texture |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|


---

## Window and Slice Configuration

!!! example "Basic Setup"
    To display content through a ViewPort:
    
    1. Create a [Window](Window.md) node and configure its columns and rows
    2. Create a ViewPort node for each output slice
    3. Set the `window` property to reference the Window node
    4. Set the `slice` property to the appropriate column and row (e.g., column_1, row_1)
    5. Connect a texture source (typically from a [Beamer](Beamer.md)) to the main inlet


## Mesh Types

!!! tip "Choosing the Right Mesh Mode"
    The `mesh` property determines how the texture is mapped to the output:
    
    | Mode | Description | Use Case |
    |------|-------------|----------|
    | **default** | Simple rectangular mesh | Basic output without geometric correction |
    | **warp** | Links to a [MeshWarp](MeshWarp.md) node | Complex surface warping with lattice control |
    | **file** | Loads custom OBJ mesh | Pre-created warp meshes |
    | **none** | No mesh rendered | Use with [CornerPin](CornerPin.md) for simple 4-corner mapping |
    
    For projecting onto non-flat surfaces, use `warp` or `file` mode with a mesh that matches your projection surface geometry.

## Combining with Mapping Tools

!!! example "CornerPin Workflow"
    For simple 4-corner projection mapping:
    
    1. Set ViewPort `mesh` to **none**
    2. Create a [CornerPin](CornerPin.md) node
    3. Set CornerPin's `viewport` to reference this ViewPort
    4. Use CornerPin's `edit...` button to adjust corners visually
    
    This is ideal for projecting onto rectangular surfaces that just need corner adjustment.

!!! example "MeshWarp Workflow"
    For complex surface warping:
    
    1. Create a [MeshWarp](MeshWarp.md) node
    2. Load or create a warp mesh
    3. Use MeshWarp's lattice editor to adjust control points
    4. In ViewPort, set `mesh` to **warp** and link to the MeshWarp node
    
    This is ideal for curved surfaces, irregular shapes, or multi-projector edge blending.

## Shader Effects

!!! info "Post-Processing with FX Shaders"
    The `fx shader` property allows applying shader effects to the viewport output:
    
    - Color correction
    - Gamma adjustment
    - Soft-edge blending
    - Custom GLSL effects
    
    Since ViewPort is the final render stage, these effects are applied after all other processing, making it ideal for final color grading and output correction.

---

## Important Notes

!!! warning "Mesh Format"
    
    When using custom mesh files:
    
    - Use **Wavefront OBJ format** only
    - Place files in `~/_assets/_warps/` or `~/_assets/_models/_warps/`
    - Using `mesh: none` only makes sense when working with [CornerPin](CornerPin.md) nodes

!!! info "File Locations"
    
    ```
    ~/_assets/_warps/              # Warp mesh files (.obj)
    ~/_assets/_models/_warps/      # Alternative location for warp meshes
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
    * [:octicons-arrow-right-24: Beamer](Beamer.md)
    * [:octicons-arrow-right-24: MeshWarp](MeshWarp.md) 
    * [:octicons-arrow-right-24: CornerPin](CornerPin.md)
    * [:octicons-arrow-right-24: Monitor](Monitor.md)

  
-   :material-video-box:{ .lg .middle } __Tutorials__

    ---

    * [:octicons-arrow-right-24: Wall Projection](../../start/tutorials/01_Wall_Projection/Wall_Projection.md)
    * [:octicons-arrow-right-24: Floor Projection](../../start/tutorials/05_Floor_Projection/Floor_Projection.md)
    
    [:octicons-arrow-right-24: Watch Now](../../start/tutorials/videos.md){ .md-button .md-button--primary }

-   :material-forum:{ .lg .middle } __Community__

    ---

    [:octicons-arrow-right-24: Join Now](https://github.com/immersive-arts/Sparck2/discussions){ .md-button .md-button--primary }


</div>

---

!!! question "Need help or want to suggest improvements?"
       
    [:fontawesome-brands-github: Report an issue](../../contributing/reporting-a-bug.md){ .md-button }
    [:fontawesome-brands-github: Improve the Docs](../../contributing/reporting-a-docs-issue.md){ .md-button }


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ViewPort.md)*