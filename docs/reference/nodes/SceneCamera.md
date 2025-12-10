# SceneCamera

Stereo Camera in 3D space.

SceneCamera represents the virtual camera chassis, while [SceneCapture](SceneCapture.md) represents the virtual film: For capturing the textures SceneCapture is needed.

<figure markdown>
![SceneCamera Node](../../assets/images/nodes/SceneCamera.png){ width="300" }
</figure> 

!!! info "Camera + Capture Relationship"
    In SPARCK, cameras and captures work as a pair:
    
    - **SceneCamera** (this node): Defines the viewpoint, lens properties, and stereo configuration — the "camera chassis"
    - **[SceneCapture](SceneCapture.md)**: Renders the scene from the camera's viewpoint — the "virtual film"
    
    You always need both nodes to render a view. Connect SceneCapture's `parent` property to this SceneCamera.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `gizmo` | - | show Camera icon in selected render group |
    | `parent` | - | parent transformation node |
    | `position` | (local transformation) | position x y z |
    | `rotation` | (local transformation) | rotation x y z |
    | `scale` | (local transformation) | scale x y z |
    | `dimension` | - | suggested captured texture size. |
    | `lens` | - | lens type. |
    | `ratio` | - | render image ratio. |
    | `angle` | - | field of view [deg] |
    | `near` | - | near frustum clip |
    | `far` | - | far frustum clip |
    | `stereo` | - | set stereo mode. |
    | `spread` | (only stereo mode) | sets spread between two eyes |
    | `rotate` | (only stereo mode) | sets rotation between two eyes |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | camera | message | camera intrinsics [p_patrix, frustum] |


---

## Lens and Frustum Settings

!!! tip "Configuring the View"
    Control how the camera sees the scene:
    
    | Property | Description |
    |----------|-------------|
    | **lens** | Lens type (perspective, orthographic, etc.) |
    | **angle** | Field of view in degrees — wider angles capture more but with more distortion |
    | **ratio** | Aspect ratio of the rendered image (e.g., 16:9, 4:3) |
    | **near** | Near clipping plane — objects closer than this are not rendered |
    | **far** | Far clipping plane — objects further than this are not rendered |
    
    The `dimension` property suggests the texture resolution for the [SceneCapture](SceneCapture.md), which determines the final render quality.

## Stereo Rendering

!!! example "Creating Stereo 3D Content"
    SceneCamera supports stereo rendering for 3D glasses, VR goggles, or anaglyph displays:
    
    1. Enable `stereo` mode on the SceneCamera
    2. Adjust `spread` to set the eye separation distance (interpupillary distance)
    3. Optionally adjust `rotate` for toe-in convergence
    4. The connected [SceneCapture](SceneCapture.md) will automatically output **two textures** (left and right eye)
    
    For anaglyph output, connect both textures to a [ShaderAnaglyph](ShaderAnaglyph.md) node.

!!! tip "Stereo Parameters"
    | Parameter | Effect |
    |-----------|--------|
    | **spread** | Distance between virtual eyes — increase for more dramatic 3D effect |
    | **rotate** | Toe-in angle between cameras — use for convergence at specific depth |
    
    For comfortable viewing, match the spread to real human interpupillary distance (~63mm) scaled to your scene.

## Positioning the Camera

!!! info "Transformation Hierarchy"
    SceneCamera uses the standard SPARCK transformation system:
    
    - **parent**: Link to a [TfmNode](TfmNode.md) or [RigidBody](RigidBody.md) for hierarchical positioning
    - **position/rotation/scale**: Local transformations relative to parent
    
    For tracked cameras in motion capture setups, set a [RigidBody](RigidBody.md) as the parent to have the camera follow a physical object.

## Camera Gizmo

!!! tip "Visualizing Camera Position"
    Enable `gizmo` to display a camera icon in the 3DViewer:
    
    - Helps visualize camera position and orientation during setup
    - Select which render group displays the gizmo
    - Useful for debugging multi-camera setups

---

## SceneCamera vs Other Cameras

!!! note "Choosing the Right Camera"
    SPARCK offers several camera types for different purposes:
    
    | Camera Type | Best For |
    |-------------|----------|
    | **SceneCamera** | General-purpose rendering, stereo 3D content |
    | **[LookAtCamera](LookAtCamera.md)** | CAVE-like VR, controlled cuts through objects |
    | **[BoxMapCamera](BoxMapCamera.md)** | 360° captures, raymarching, dome projections |
    | **[Beamer](Beamer.md)** | Physical projector simulation with calibration |

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with SceneCamera in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **SceneCamera**

    ---
    * [:octicons-arrow-right-24: SceneCapture](SceneCapture.md) 
    * [:octicons-arrow-right-24: ShaderAnaglyph](ShaderAnaglyph.md)
    * [:octicons-arrow-right-24: LookAtCamera](LookAtCamera.md)
    * [:octicons-arrow-right-24: BoxMapCamera](BoxMapCamera.md) 
    * [:octicons-arrow-right-24: TfmNode](TfmNode.md) 

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/SceneCamera.md)*