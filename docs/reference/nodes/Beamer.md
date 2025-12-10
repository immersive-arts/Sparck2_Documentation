# Beamer

A Beamer represents a real world projector inside SPARCK's 3D space.

It has a calibration mode to find the orientation and lense properties (extrinsic and intrinsic transformations) of the projector.

It uses the opencv [calibrateCamera()](https://docs.opencv.org/4.x/d9/d0c/group__calib3d.html#ga3207604e4b1a1758aa66acb6ed5aa65d) method to calculate the tranformation and projection matrix of a projector. 

For this to work the node needs a calibration model (3D object) and a set of manually set calibration vertices that correspond to points on the calibration model.

!!! example "Tutorial: Beamer Calibration"
    The Tutorial [Beamer Calibration](../../start/tutorials/02_Calibration/calibration.md) walks you through the calibration process step-by-step.

## 
<figure markdown>
![Beamer Node](../../assets/images/nodes/Beamer.png){ width="300" }
</figure> 


!!! info "Fun Fact"
    Beamer is another word for projector, mainly used in German-speaking countries - and apparently in Australia as well. The reason for this choice of name is to distinguish it from the real world projector hardware of which it is its virtual representation. And also to distinguish it from the TextureProjectory shader that also does a projection, though a purely virtual one.

!!! note "Beamer vs TextureProjectory"
    The **Beamer** node represents a physical projector that outputs to real-world displays. In contrast, the [TextureProjectory](TextureProjectory.md) shader projects textures virtually onto 3D surfaces within the scene — useful for techniques like virtual projection mapping or texture baking. Both can work together in complex setups.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `parent` | Reference | Reference to parent transformation node |
    | `calibfile` | File | Select the transformation RIG. The file needs to be located inside the `~/_assets/_projectors` folder |
    | `calibrate` | Button | Opens the calibration editor |
    | `dimensions` | Size | Sets the texture size of this render pass |
    | `bgcolor` | Color | The background color |
    | `stereo` | Boolean | Creates two renderpasses for each stereo texture |
    | `blend` | Boolean | Enables blending |
    | `antialias` | Boolean | Enables antialiasing |
    | `identify` | Boolean | Use the calibration-color as background color |
    | `gizmo` | Integer | Set the render group to draw the gizmo to |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | background | texture | background texture for camera calibration. Instead of setting the calibration vertices on real world targets, you can set the calibration vertices on the camera feed targets. The result is the same: Beamer node evaluates the video camera's intrinsic and extrinsic parameters. |
    | custom | message | custom commands. message 'createToXY' creates a new model with calibration vertices relative to the XY-plane: 'createToX  x1  y1  z1  x2  y2  z2  x3  y3  z3  ...'. &#124; message 'addToXY' adds calibration vertices relative to the XY-plane: 'addToX  x1  y1  z1  x2  y2  z2  x3  y3  z3  ...' |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | captured | texture | captured texture (left if stereo) |
    | captured | warping | captured texture (right if stereo) |
    | dump | message | dump (transform, frustum) |


---

## Calibration Window

??? abstract "Calibration Settings"
    
    The calibration window provides advanced configuration options for projector calibration:
    
    | Parameter | Type | Description |
    |-----------|------|-------------|
    | `Color` | Color | Identifies the Beamer/Calibrator in the 3DViewer |
    | `Model` | File | Calibration model. Needs to be of type Wavefront OBJ |
    | `use Model transformation` | Toggle | Additional transformations on the calibration model to place it correctly to the world reference |
    | `implement parent transformation` | Toggle | You can calibrate the beamer while attached to a mocap rigidbody that is referenced by the parent transformation node |
    | `focus editor` | Button | Opens the editor window and focuses it to this calibration |
    | `gather 3DViewer lookat` | Button | Takes the current 3DViewer point of view and applies it as a temporary solution |
    | `display..` | Button | Opens the display window to select the display the projector is currently connected to |
    | `width` | Integer [px] | Projector resolution width |
    | `height` | Integer [px] | Projector resolution height |
    | `enable calibration` | Toggle | Enables the calibration button. Only enable once the correct resolution is set |
    | `show/hide` | Button | Shows / hides calibration flags |
    | `frustum` | Display | Shows the solution's frustum |
    | `transformation` | Matrix | Shows the solution's transformation matrix |
    | `reset` | Button | Resets values |
    | `save and close` | Button | Saves the solution and closes the calibration window |

    !!! tip "Calibration with Motion Capture"
        If you're calibrating while the projector is attached to a motion capture rigid body, enable **implement parent transformation**. This automatically calculates the local transformation offset from the rigid body to the projector's lens position.

---

## Multi-Projector Setups

!!! tip "Soft-Edge Blending with Multiple Beamers"
    When using multiple Beamer nodes for overlapping projections, use the [SpatialShadery](SpatialShadery.md) shader to automatically compute per-projector pixel visibility and brightness. This produces smooth soft-edge blending across all projectors — essential for Spatial Augmented Reality installations.
    
    Key parameters for multi-projector blending:
    
    - **spread**: Controls the distribution of pixel blending between overlapping projections (0 = no spread, 1 = full spread)
    - **distance**: Additional differentiator based on distance from projector
    - **power**: Controls the soft-edge blending power
    - **luminance**: Adjusts brightness balance between projectors

!!! tip "Identify Mode for Debugging"
    Enable the **identify** toggle on each Beamer to display a unique calibration color as the background. This helps visually identify which projector is outputting to which display — particularly useful when configuring multi-projector setups in the [Window](Window.md) node's display settings.

---

## Important Notes

!!! bug "Known Issues"
    - On Windows systems, the calibrattion is not working when max's gfxengine is set to its default setting 'glcore'. The node will respond with a warnning message and ask to switch to 'gl2'. This will require a restart of max. Save your work before switching.
  
!!! warning "Calibration Requirements"
    
    - Calibration files must be saved before the calibration button becomes active
    - All calibration files are stored in `~/_assets/_projectors`
    - Ensure the correct projector resolution is set before enabling calibration
    - The calibration process requires a calibration model in OBJ format that represents the real world object against which the projector is calibrated and referenced to.

!!! info "File Locations"
    
    ```
    ~/_assets/_projectors/          # Beamer Calibration files (.xml & .json)
    ~/_assets/_projectors/_calib    # Target vertex files (.xml)
    ~/_assets/_model/_calib         # Calibration models (.obj)
    ```

!!! info "Render Pipeline"
    The Beamer node operates in a dedicated **Beamer Render Pass** (#28 in the SPARCK render pipeline). This ensures that Beamer captures occur after main render passes but before the final preview pass. See [Render Groups & Passes](../../reference/render_groups_and_passes.md) for details on render ordering.

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with Beamer in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md#4_mapping)

-   :material-file-document:{ .lg .middle } __Complementing__ **Beamer**

    ---
    * [:octicons-arrow-right-24: SceneCapture](SceneCapture.md) 
    * [:octicons-arrow-right-24: ViewPort](ViewPort.md)
    * [:octicons-arrow-right-24: Window](Window.md)
    * [:octicons-arrow-right-24: SpatialShadery](SpatialShadery.md)
    * [:octicons-arrow-right-24: TextureProjectory](TextureProjectory.md)
    * [:octicons-arrow-right-24: Canvas](Canvas.md)
  
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


*Last updated: 2024-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/Beamer.md)*