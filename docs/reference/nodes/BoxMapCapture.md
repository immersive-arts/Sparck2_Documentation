# BoxMapCapture

The BoxMapCapture Node is needed to render the view from a [BoxMapCamera](BoxMapCamera.md).

While BoxMapCamera represents the virtual camera chassis, the BoxMapCapture represents the virtual film: For capturing the textures the BoxMapCapture is needed.

A BoxMap is similar to an OpenGL-CubeMap, but instead consists of a list of 6 unique textures, each representing the view of one box side. The term BoxMap is used in order to make sure it is not confused with a CubeMap.

<figure markdown>
![BoxMapCapture Node](../../assets/images/nodes/BoxMapCapture.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `capture` | - | render group to draw. Model/Canvas/MeshWarp/Grid have an equivalent in which you can choose which group to draw to. |
    | `parent` | - | select the camera node from where to render. |
    | `dim` | - | sets the texture size of this render pass. Try using sizes like 256x256, 512x512, 1024x1024, 2048x2048. |
    | `bgcolor` | - | the background color |
    | `mode` | - | the result of the renderpass. 'split' will render our all the different directions as seperate textures, 'line' renders then out in one texture [-x, -z, x, z, -y, y] and 'cross' in one texture in the shape of the cubmap cross |
    | `pass` | - | Renderpass. This defines when in a frame-pass (see reference) this Capure node does the rendering. A manual renderpass will only be executed right after loading a project or when pressing the 'manual renderpass button' in the main menu. |
    | `blend` | - | allows blending. |
    | `antialias` | - | antialiases the output. |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | left | texture | left texture |
    | front | texture | front texture |
    | right | texture | right texture |
    | back | texture | back texture |
    | top | texture | top texture |
    | bottom | texture | bottom texture |
    | boxmap | boxmap | boxmap (texture list &lt;texL> &lt;texF> &lt;texR> &lt;texB> &lt;texT> &lt;texG>) |
    | texture | texture | texture list with only active textures (texture &lt;tex1> ...) |
    | single | texture | single texture with all box sides backed together |


---

## Output Modes

!!! tip "Choosing the Right Mode"
    The `mode` property determines how the six captured faces are output:
    
    | Mode | Output | Use Case |
    |------|--------|----------|
    | **split** | 6 separate texture outlets | When you need individual face access for custom processing |
    | **line** | Single texture with faces in a row `[-x, -z, x, z, -y, y]` | Horizontal strip format for certain external tools |
    | **cross** | Single texture in cubemap cross layout | Standard cubemap format for export or compatibility |
    
    The `boxmap` outlet always outputs a texture list regardless of mode, which can be directly connected to [TextureProjectory](TextureProjectory.md) or other BoxMap-aware nodes.

## Resolution Recommendations

!!! info "Texture Dimensions"
    For best performance and compatibility, use power-of-two dimensions:
    
    - **256×256**: Low quality, fast rendering — good for previews
    - **512×512**: Medium quality — balanced for most real-time applications
    - **1024×1024**: High quality — recommended for production
    - **2048×2048**: Very high quality — use when detail is critical
    
    Remember that BoxMapCapture renders **6 faces**, so a 1024×1024 setting means 6× the render work compared to a single camera capture.

## Use with TextureProjectory

!!! example "360° Projection Workflow"
    BoxMapCapture is commonly used with [TextureProjectory](TextureProjectory.md) for 360° content projection:
    
    1. Set up a [BoxMapCamera](BoxMapCamera.md) at your desired viewpoint
    2. Connect BoxMapCapture to the camera via the `parent` property
    3. Connect the `boxmap` outlet to TextureProjectory's boxmap inlet
    4. In TextureProjectory, set shader to `boxmap` or `360VR.single`/`360VR.multiblend`
    
    This enables seamless 360° scene capture from internal rendering or external engines (via Spout/Syphon) projected onto domes, cylinders, or custom geometries.

---

## Important Notes

!!! warning "Render Pass Ordering"
    If textures appear black or outdated, ensure BoxMapCapture renders in an earlier pass than nodes that consume its output. Adjust the `pass` property to control render ordering. See [Render Groups & Passes](../../concepts/render_groups_and_passes.md) for details.

!!! info "Performance Consideration"
    BoxMapCapture renders the scene 6 times per frame (once per face). For complex scenes, consider:
    
    - Reducing `dim` resolution
    - Using the `directions` property on [BoxMapCamera](BoxMapCamera.md) to render only needed faces
    - Using a manual render pass for static content

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with BoxMapCapture in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **BoxMapCapture**

    ---
    * [:octicons-arrow-right-24: BoxMapCamera](BoxMapCamera.md) 
    * [:octicons-arrow-right-24: TextureProjectory](TextureProjectory.md)
    * [:octicons-arrow-right-24: ShaderRaymarcher](ShaderRaymarcher.md)
    * [:octicons-arrow-right-24: SceneCapture](SceneCapture.md)
    * [:octicons-arrow-right-24: CubeMap](CubeMap.md)

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/BoxMapCapture.md)*