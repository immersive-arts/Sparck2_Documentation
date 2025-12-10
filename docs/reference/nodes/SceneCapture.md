# SceneCapture

The SceneCapture node is needed to render the view from a [SceneCamera](SceneCamera.md).

While SceneCamera represents the virtual camera chassis, SceneCapture represents the virtual film: For capturing the textures SceneCapture is needed.

<figure markdown>
![SceneCapture Node](../../assets/images/nodes/Capture.png){ width="300" }
</figure> 

!!! info "Camera + Capture Relationship"
    SceneCapture works in tandem with camera nodes:
    
    - **[SceneCamera](SceneCamera.md)** or **[LookAtCamera](LookAtCamera.md)**: Defines the viewpoint — the "camera chassis"
    - **SceneCapture** (this node): Renders the scene from that viewpoint — the "virtual film"
    
    Set the `parent` property to link to your camera node. The capture inherits lens settings and stereo configuration from the camera.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `capture` | - | render group to draw. Model/Canvas/MeshWarp/Grid have an equivalent in which you can choose which group to draw to. |
    | `parent` | - | select the camera node from where to render. |
    | `type` | (set by the Camera selection) | can be one of the following: <li>off <li>camera capture <li>beamer capture <li>beamer mirror <li>special capture <li>special mirror |
    | `stereo` | (set by the Camera selection) | shows if the linked camera is stereo. If it is stereo, the Capture-node will have two texture outlets. |
    | `dim` | - | sets the texture size of this render pass. Beware: If used in conjunction with a Camera, the Camera will set the aspect ratio. Dim will only define the resolution of the rendered texture. |
    | `shader` | - | Applies this shader to all objects rendered in this renderpass. |
    | `bgcolor` | - | the background color |
    | `pass` | - | Renderpass. This defines when in a frame-pass (see reference) this Capure node does the rendering. A manual renderpass will only be executed right after loading a project or when pressing the 'manual renderpass button' in the main menu. |
    | `blend` | - | use alpha channels in textures |
    | `antialias` | - | render with antialias |
    | `flip image` | - | flips the rendered image |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | captured | texture | captured texture (left if stereo) |
    | if stereo | texture | if stereo: captured right texture |


---

## Render Groups

!!! tip "Controlling What Gets Rendered"
    The `capture` property determines which [render group(s)](../nodes_and_connections.md#render-groups) this node captures:
    
    - Objects ([Canvas](Canvas.md), [Model](Model.md), [Grid](Grid.md), etc.) have a `drawto` property that assigns them to render groups
    - SceneCapture's `capture` property selects which groups to render
    - Use multiple render groups to separate content for different outputs
    
    This allows the same scene to be rendered differently by different captures — for example, one capture for projection and another for preview.

## Capture Types

!!! info "Understanding Type Modes"
    The `type` property is automatically set based on the linked camera:
    
    | Type | Description |
    |------|-------------|
    | **off** | Capture disabled |
    | **camera capture** | Standard capture from [SceneCamera](SceneCamera.md) or [LookAtCamera](LookAtCamera.md) |
    | **beamer capture** | Capture from [Beamer](Beamer.md) (calibrated projector view) |
    | **beamer mirror** | Mirror/reflection of Beamer view |
    | **special capture** | Special rendering modes |
    | **special mirror** | Mirror of special capture |

## Render Pass Timing

!!! tip "Optimizing Performance with Pass Modes"
    The `pass` property [controls](../render_groups_and_passes.md#render-passes) when rendering occurs:
    
    | Pass Mode | Behavior | Use Case |
    |-----------|----------|----------|
    | **Automatic** | Renders every frame | Dynamic content, animations |
    | **Manual** | Renders once on load, or when triggered | Static content, textures, performance optimization |
    
    For static content that doesn't change, use **manual** mode to reduce GPU load. Trigger a manual refresh using the **Refresh** button in SPARCK's toolbar.

## Resolution and Quality

!!! example "Configuring Output Quality"
    Control the rendered texture quality:
    
    - **dim**: Sets texture resolution (e.g., 1920×1080). The camera determines aspect ratio; `dim` only sets pixel count.
    - **antialias**: Enable for smoother edges (higher GPU cost)
    - **blend**: Enable alpha channel support for transparency
    - **bgcolor**: Set the background color for areas not covered by objects

!!! warning "Resolution vs Aspect Ratio"
    When linked to a camera, the camera's `ratio` property controls aspect ratio of the view frustum. The `dim` property only sets the resolution — if you set dim to 1920×1080 but the camera ratio is 4:3, the output resolution will still be 1920×1080.

## Stereo Output

!!! info "Stereo Rendering"
    When the linked camera has `stereo` enabled:
    
    - The `stereo` property automatically shows "on"
    - SceneCapture outputs **two textures**: left eye and right eye
    - Connect both outlets to [ShaderAnaglyph](ShaderAnaglyph.md) for anaglyph 3D output
    - Or route to separate displays for VR goggles or 3D projection

## Global Shader Effects

!!! tip "Applying Shaders to Entire Capture"
    The `shader` property applies a shader to **all objects** in this render pass:
    
    - Useful for global color correction, post-processing effects
    - The shader affects everything rendered by this capture
    - For per-object shaders, use the shader property on individual Canvas/Model nodes instead

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with SceneCapture in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **SceneCapture**

    ---
    * [:octicons-arrow-right-24: SceneCamera](SceneCamera.md) 
    * [:octicons-arrow-right-24: LookAtCamera](LookAtCamera.md)
    * [:octicons-arrow-right-24: ShaderAnaglyph](ShaderAnaglyph.md)
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

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/SceneCapture.md)*