# Beamer

A Beamer represents a real world projector inside SPARCK's 3D space.

It has a calibration mode to find the orientation and lense properties (extrinsic and intrinsic transformations) of the projector.

<figure markdown>
![Beamer Node](../../assets/images/nodes/Beamer.png){ width="300" }
</figure> 


## Properties

The following properties can be configured for this node:

=== "Reference"

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

=== "Workflow"

    1. **Create Calibration File**: Select 'save as..' and choose a file name to create a new calibration file
    2. **Select Calibration File**: Once a file exists, select it in the `calibfile` property
    3. **Enable Calibration**: The calibration button becomes enabled after selecting a valid file
    4. **Open Calibrator**: Click the `calibrate` button to open the calibration editor
    5. **Configure & Save**: Adjust settings and save your calibration


---

## RIG Configuration

??? abstract "Advanced RIG Settings"
    
    The RIG (Rendering Interface Group) provides advanced configuration options for projector calibration:
    
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


## Important Notes

!!! warning "Calibration Requirements"
    
    - Calibration files must be saved before the calibration button becomes active
    - All calibration files are stored in `~/_assets/_projectors`
    - Ensure the correct projector resolution is set before enabling calibration
    - The calibration process requires a physical calibration model (OBJ format)

!!! info "File Locations"
    
    ```
    ~/_assets/_projectors/     # Calibration files
    ~/_assets/_model/          # Calibration models (.obj)
    ```

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with Beamer in minutes
    
    [:octicons-arrow-right-24: Project Examples](../../start/examples/project_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **Beamer**

    ---
    * [:octicons-arrow-right-24: SceneCapture](SceneCapture.md) 
    * [:octicons-arrow-right-24: TfmNodeMirror](TfmNodeMirror.md)
    * [:octicons-arrow-right-24: TfmNodeLookAt](TfmNodeLookAt.md)
  
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

*Last updated: 2024-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/Beamer.md)*