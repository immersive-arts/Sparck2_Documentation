# MeshWarp

Reads and draws 2D model Wavefront OBJ

It is used for mesh warping and can be directly rendered into a ViewPort

<figure markdown>
![MeshWarp Node](../../assets/images/nodes/MeshWarp.png){ width="300" }
</figure> 

!!! success "Complex Surface Warping"
    MeshWarp provides advanced geometric correction for projection mapping onto curved or irregular surfaces. Unlike simple [CornerPin](CornerPin.md) adjustments, MeshWarp uses a **lattice deformation system** that allows fine-grained control over mesh vertices, enabling smooth warping across complex geometries.



## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `mesh` | drag n' drop | select the 3d model file to draw. the file needs to be located inside the ~/_assets/_models/_warps folder. you can also drag'n drop files, which will be copied into the _warps folder and autmatically selected. It needs to be of type Wavefront OBJ. |
    | `lattice` | - | SPARCKs own MeshWarp file format. It contains the mesh data plus the lattice data. You need to save this file if you want to keep your modifications. |
    | `new lattice` | - | creates a new lattice that is applied on the loaded mesh. |
    | `edit` | - | focuses the editor on this node |
    | `subdivision` | - | subdivides the mesh for nicer warpings. Works only on quad faces |
    | `export` | - | exports the final mesh (Wavefront OBJ) to the ~/_export folder. The file will be named after the node. |
    | `RenderGroup` | - | set the render group. Capture/Beamer/3DViewer have an equivalent in which you can choose which group to render. |
    | `transform` | - | Modelview and projection transform reset flag (default = 0) When the flag is set, the modelview and projection transforms are set to the identity transform before rendering the object. This is useful for sprite or billboard overlays, or automatic scaling to window size. The transform_reset flag modes are: <li>0 = do nothing (default) <li>1 = proportional orthographic glOrtho(-aspect, aspect, -1.0, 1.0, near_clip, far_clip) <li>2 = orthographic normalized glOrtho(-1.0, 1.0, -1.0, 1.0, near_clip, far_clip) <li>3 = proportional perspective with near clip = 0.001 gluPerspective(lens_angle, aspect, 0.001/*near_clip*/, far_clip) <li>4 = normalized perspective with near clip = 0.001 gluPerspective(lens_angle, 1.0, 0.001/*near_clip*/, far_clip); |
    | `parent` | - | parent transformation node |
    | `position` | (local transformation) | position x y z |
    | `rotation` | (local transformation) | rotation x y z |
    | `scale` | (local transformation) | scale x y z |
    | `shader` | - | link to Shader Node |
    | `color` | - | object color |
    | `depth` | - | depth buffering |
    | `blend` | - | enables blendmode |
    | `blendmode` | - | choose blendmode: <li>alphablend <li>add <li>multiply <li>screen <li>exclusion <li>colorblend <li>coloradd <li>alphaadd |
    | `displaylist` | - | enables displaylist - can speed up drawing |
    | `cachemode` | - | choose cachemode: <li>vertexarray <li>displaylist <li>vertexbuffer <li>immediate |
    | `polymode` | draw.. | <li>polygons - only faces <li>lines - only lines <li>points - only vertices |
    | `axes` | - | show axes of the models origin |
    | `fileWatch` | - | watches the model file. when it changes, it will be autmatically reloaded |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | main | texture | main texture |



---

## Lattice Workflow

!!! example "Creating and Editing a Warp"
    The lattice system allows interactive mesh deformation:
    
    1. Load a base mesh (OBJ file) via the `mesh` property or drag-and-drop
    2. The base mesh should be a 2d mesh on the XY plane, origin at (0,0,0) and the individual vertices located within a unit square (-1 to 1 in X and Y)
    3. Click `new lattice` to create a deformable lattice grid over the mesh
    4. Click `edit` to open the lattice editor
    5. Drag lattice control points to warp the mesh
    6. Save the `lattice` file to preserve your modifications
    
    The lattice file stores both the original mesh data and your deformations, so you can reload and continue editing later.


=== "Lattice Editor"

    <figure markdown>
    ![MeshWarp Node](../../assets/images/nodes/MeshWarp/LatticeEdit_MeshWarp.png){ width="300" }
    </figure> 

=== "Mesh Editor"

    <figure markdown>
    ![MeshWarp Node](../../assets/images/nodes/MeshWarp/MeshEdit_MeshWarp.png){ width="300" }
    </figure> 

=== "Lattice UV-Editor"

    <figure markdown>
    ![MeshWarp Node](../../assets/images/nodes/MeshWarp/LatticeUVEdit_MeshWarp.png){ width="300" }
    </figure> 

=== "UV Editor"

    <figure markdown>
    ![MeshWarp Node](../../assets/images/nodes/MeshWarp/UVEdit_MeshWarp.png){ width="300" }
    </figure> 


??? tip "Editor Keyboard Shortcuts"
    The MeshWarp editor has four editors: 

       * Two editors for modifiying the mesh: 
         * **Lattice Select** (for lattice control points) and 
         * **Mesh Select** (for direct manipulation of mesh vertices). 
         * Press ++tab++ to switch between these two editors.
       * Two UV editors: 
         * **Lattice UV Edit** and 
         * **UV Edit**. 
         * Press ++tab++ to switch between these two editors.
       * press ++shift++ + ++tab++ to switch between the mesh editors and the UV editors.
    
    **General Controls:**
    
    | Key | Action |
    |-----|--------|
    | ++tab++ | Switch between Lattice and Mesh edit modes |
    | ++shift+tab++ | Switch between UV and Mesh edit modes |
    | ++h++ | Toggle help overlay |
    | ++shift+h++ | Change help overlay color |
    | ++f++ | Save current warp |
    
    **Lattice Select Mode:**
    
    | Key | Action |
    |-----|--------|
    | :material-mouse-left-click: | Select lattice point |
    | ++shift++ + :material-mouse-left-click: | Add to selection |
    | ++a++ | Select all lattice points |
    | ++g++ | Grab/move selected points (click to confirm) |
    | ++arrow-up++ ++arrow-down++ ++arrow-left++ ++arrow-right++ | Nudge selected points |
    | ++i++ | Reset selected vertices to original position |
    | ++z++ | Undo |
    | ++shift+z++ | Redo |
    
    **Mesh Select Mode:**
    
    | Key | Action |
    |-----|--------|
    | :material-mouse-left-click: | Select mesh vertex |
    | ++shift++ + :material-mouse-left-click: | Add to selection |
    | ++a++ | Select all vertices |
    | ++x++ | Delete selected vertices (can be undone) |
    | ++g++ | Grab/move selected vertices (click to confirm) |
    | ++s++ | Scale selected vertices (click to confirm) |
    | ++r++ | Rotate selected vertices (click to confirm) |
    | ++arrow-up++ ++arrow-down++ ++arrow-left++ ++arrow-right++ | Nudge selected vertices |
    | ++i++ | Reset selected vertices to original position |
    | ++q++ | Set cursor position |
    | ++p++ | Store current selection (then press 0-9) |
    | ++0++ - ++9++ | Recall stored selection |
    | ++z++ | Undo |
    | ++shift+z++ | Redo |

!!! warning "Save Your Work"
    Lattice modifications are **not automatically saved** with the patch. Save the `lattice` file regularly by pressing ++f++ while editing.

## Connecting to ViewPort

!!! tip "Rendering MeshWarp Output"
    MeshWarp can be directly rendered into a [ViewPort](ViewPort.md):
    
    1. Create a MeshWarp node and configure your warp
    2. In ViewPort, set `mesh` to **warp**
    3. Link the ViewPort's warp reference to this MeshWarp node
    4. The warped mesh will be rendered in the ViewPort's designated Window slice
    
    This is ideal for curved projection screens, domes, or irregular architectural surfaces.

## Export and Reuse

!!! info "Exporting Final Meshes"
    After editing, you can export the warped mesh:
    
    - Click `export` to save the final deformed mesh as a Wavefront OBJ file
    - The file is saved to `~/_export/` with the node's name
    - Exported meshes can be used in other applications or reimported as base meshes

## MeshWarp vs CornerPin

!!! note "Choosing the Right Tool"
    | Feature | MeshWarp | [CornerPin](CornerPin.md) |
    |---------|----------|---------------------------|
    | **Control points** | Full lattice grid | 4 corners only |
    | **Surface types** | Curved, irregular | Flat, rectangular |
    | **Complexity** | Higher | Lower |
    | **Setup time** | More involved | Quick |
    | **File format** | SPARCK lattice + OBJ | Internal |
    
    Use **CornerPin** for simple rectangular surfaces. Use **MeshWarp** for curved screens, domes, or surfaces requiring smooth geometric correction.

---

## Important Notes

!!! warning "Supported File Format"
    
    - **Wavefront OBJ (.obj)** is the only supported mesh format
    - The mesh should have all its vertices on the XY plane. 
    - The origin should be at (0,0,0) 
    - The individual vertices should be located within a unit square (-1 to 1 in X and Y)
    - Place mesh files in `~/_assets/_models/_warps/` or drag-and-drop to auto-copy
    - Enable `fileWatch` to automatically reload when the source file changes

!!! info "File Locations"
    
    ```
    ~/_assets/_models/_warps/     # Source warp meshes (.obj)
    ~/_assets/_warps/             # location for warp meshes enhanced with lattice data
    ~/_export/                    # Exported warped meshes
    ```

---


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with MeshWarp in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **MeshWarp**

    ---
    * [:octicons-arrow-right-24: ViewPort](ViewPort.md) 
    * [:octicons-arrow-right-24: CornerPin](CornerPin.md)
    * [:octicons-arrow-right-24: Window](Window.md)
    * [:octicons-arrow-right-24: Beamer](Beamer.md)

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/MeshWarp.md)*