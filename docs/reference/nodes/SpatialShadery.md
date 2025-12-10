# SpatialShadery

This shader is spatialy aware and is used for multi projector installation where the use of softedge is necessary.

It is mainly used for Spatial Augmented Reality installations where there is the need for the creation of dynamic softedges.

<figure markdown>
![SpatialShadery Node](../../assets/images/nodes/SpatialShadery.png){ width="300" }
</figure> 

!!! success "Core of Spatial Augmented Reality"
    SpatialShadery is at the heart of SPARCK's multi-projector capabilities. It computes **per-projector pixel visibility and brightness** in real-time, producing smooth soft-edge blending across up to **6 projectors** simultaneously. This enables dynamic softedges that automatically adapt as projection surfaces or projectors move.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `shader` | - | the shader type: <li>'edge' is used in combination with the BlendSoftedge node <li>'edge & blend' calculates softedge combined with the blending. |
    | `project to` | - | projection type: <li>'canvas' is used to render the projector weights <li>'baked texture' implements all render passes for generating the final pixel. |
    | `BeamerA-F` | - | Select the [Beamer](Beamer.md) or [SceneCapture](SceneCapture.md) node from where to project. |
    | `occlusion` | - | tries to adjust for occlusions of objects. |
    | `depth dim` | - | depth texture size of the occlusion pass. |
    | `projection` | - | use only front, back or both side of the canvas |
    | `angle mode` | - | angle differentiation: <li>'viewray' will differentiate based on the angle between the surface normal and the viewray, <li>'direction' will differentiate based on the angle between the surface normal and the camera direction |
    | `spread` | - | spread factor will increase the differentiation between overlapping projections |
    | `distance` | - | use distance as an additional differentiator. It will show its influence when the spread is increased. (0 = no influence) |
    | `blend bg` | - | enables blending with the background |
    | `interpolation` | - | interpolation |
    | `angle limit` | - | angle limit (how much of the visible surface area is considered, 0 = no limit) |
    | `angle falloff` | - | angle-limit falloff (defines the size of the angle blend transition at the angle limit) |
    | `bevel size` | - | bevel size |
    | `bevel curve` | - | bevel curve |
    | `bevel round` | - | use rounded bevel |
    | `offcolor` | - | surface color of uncovered areas |
    | `output` | - | display mode of the model on which this shader is applied onto. <li>'result' shows the final texture <li>'content' shows the input texture <li>'mask' shows the Beamer weights |
    | `power` | - | blend power - softegde blend parameter |
    | `luminance` | - | luminance - softegde blend parameter |
    | `gradient curve` | - | adjusts the softedge curve |
    | `gamma` | - | gamma correction |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture list with depth pass |


---

## Shader Modes

!!! tip "Choosing the Right Shader Mode"
    SpatialShadery offers two shader modes for different workflow requirements:
    
    | Mode | Description | Use Case |
    |------|-------------|----------|
    | **edge** | Outputs per-projector weight masks only | Two-stage workflow with [BlendSoftedge](BlendSoftedge.md) for final compositing |
    | **edge & blend** | Computes edge weights AND final blended result | Single-pass workflow for simpler setups |
    
    For most Spatial Augmented Reality setups, use **edge & blend** with `project to` set to **baked textures** for best results.

## Typical Configuration

!!! example "Floor Projection Setup"
    For a typical multi-projector floor projection:
    
    1. **shader**: `edge & blend`
    2. **project to**: `baked textures`
    3. **Beamer A–D**: Assign each calibrated [Beamer](Beamer.md)
    4. **projection**: `both side` (or `front side` for single-sided surfaces)
    5. **output**: `result`
    
    Then fine-tune the blending parameters:
    
    - **spread**: Start around `0.5` — controls pixel distribution between overlapping projectors (0 = no spread, 1 = full spread)
    - **distance**: Add if spread alone isn't enough differentiation
    - **power**: Adjust soft-edge curve steepness
    - **luminance**: Balance brightness between projectors

## Debugging Output Modes

!!! info "Visualizing Projection Coverage"
    Use the `output` property to debug your multi-projector setup:
    
    - **result**: Final blended output (use for production)
    - **content**: Shows the input texture without blending
    - **mask**: Shows the per-projector weight distribution — useful for visualizing which projector covers which area and identifying overlap regions

---

!!! warning "IMPORTANT: Projection Selection"
    This shader is usually applied to a [Canvas](Canvas.md) which in turn is rendered (or captured) by a capture node (be it a [Beamer](Beamer.md) or [SceneCapture](SceneCapture.md)). It is of **utmost** importance that the 'projection' selection points to the capture node that renders the canvas this shader is applied to, otherwise this shader will not work as intended.

!!! tip "Calibration is Essential"
    SpatialShadery relies on accurate projector calibration to compute correct pixel visibility. Ensure all [Beamer](Beamer.md) nodes are properly calibrated to get best results.

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with SpatialShadery in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **SpatialShadery**

    ---
    * [:octicons-arrow-right-24: BlendSoftedge](BlendSoftedge.md) 
    * [:octicons-arrow-right-24: Beamer](Beamer.md)
    * [:octicons-arrow-right-24: SceneCapture](SceneCapture.md)
    * [:octicons-arrow-right-24: Canvas](Canvas.md)
    * [:octicons-arrow-right-24: TextureProjectory](TextureProjectory.md)

  
-   :material-video-box:{ .lg .middle } __Tutorials__

    ---

    * [:octicons-arrow-right-24: Floor Projection](../../start/tutorials/05_Floor_Projection/Floor_Projection.md)
    * [:octicons-arrow-right-24: Spatial Augmented Reality](../../start/tutorials/03_Spatial_Augmented_Reality/Spatial_Aumented_Reality.md)
    
    [:octicons-arrow-right-24: Watch Now](../../start/tutorials/videos.md){ .md-button .md-button--primary }

-   :material-forum:{ .lg .middle } __Community__

    ---

    [:octicons-arrow-right-24: Join Now](https://github.com/immersive-arts/Sparck2/discussions){ .md-button .md-button--primary }


</div>

---

!!! question "Need help or want to suggest improvements?"
       
    [:fontawesome-brands-github: Report an issue](../../contributing/reporting-a-bug.md){ .md-button }
    [:fontawesome-brands-github: Improve the Docs](../../contributing/reporting-a-docs-issue.md){ .md-button }


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/SpatialShadery.md)*