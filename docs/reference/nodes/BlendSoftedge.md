# BlendSoftedge

Blends color textures with softedge textures

<figure markdown>
![BlendSoftedge Node](../../assets/images/nodes/BlendSoftedge.png){ width="300" }
</figure> 

!!! note "Two-Stage vs Integrated Soft-Edge Blending"
    BlendSoftedge is used for **two-stage soft-edge blending** workflows where the edge mask and content are processed separately. This approach offers more control over the blending parameters.
    
    Alternatively, the [SpatialShadery](SpatialShadery.md) node can perform **integrated soft-edge blending** when its shader is set to `edge & blend` — computing both the softedge weights and final blend in a single pass. Use SpatialShadery's `(soft)edge` mode when you want to use BlendSoftedge for the final compositing step.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `ouput` | - | output mode: <li>result shows the final blend <li>texture one shows the color texture <li>texture two shows the blend texture |
    | `power` | - | blend power |
    | `luminance` | - | blend luminance |
    | `output` | - | enable texture shader pass. the outlet that appears below will output the resulting texture. |
    | `gradient` | - | custom gradient curve |
    | `gamma` | - | gamma correction |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | main | texture | main texture (content texture) |
    | mask | texture | mask texture (alpha mask) |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | blended | texture | blended texture |


---

## Usage Modes

!!! tip "Shader vs Texture Shader Pass"
    This node can operate in two modes:
    
    - **As a shader**: Apply directly to geometry for real-time blending
    - **As a texture shader pass**: Enable the `output` toggle to generate a blended texture that can be passed to other nodes
    
    Use texture shader pass mode when you need the blended result as input for additional processing stages.

!!! tip "Blending Parameters"
    Fine-tune your soft-edge transitions with these key parameters:
    
    - **power**: Controls the steepness of the blend curve. Higher values create sharper transitions; lower values create smoother gradients
    - **luminance**: Adjusts overall brightness balance in the blended region. Use this to compensate for overlapping projector brightness
    - **gradient**: Custom curve for non-linear blend falloff
    - **gamma**: Applies gamma correction to the final output for color accuracy

## Workflow with SpatialShadery

!!! info "Two-Stage Workflow"
    When using [SpatialShadery](SpatialShadery.md) with its shader set to `edge` mode, it outputs per-projector weight masks. These masks can then be fed into BlendSoftedge for the final compositing step:
    
    1. **SpatialShadery** (shader: `edge`) → outputs edge weight textures
    2. **BlendSoftedge** → combines content texture with edge weights
    
    This separation allows independent control over edge calculation and final blending parameters.

---

## Important Notes

!!! warning "Usage Considerations"
    
    This node can be used as a shader or as a texture shader pass. When used as a texture shader pass, ensure the `output` toggle is enabled to expose the texture outlet.

!!! info "File Locations"
    
    ```
    ~/_assets/_projectors/     # Calibration files
    ~/_assets/_model/          # Calibration models (.obj)
    ```

---


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with BlendSoftedge in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **BlendSoftedge**

    ---
    * [:octicons-arrow-right-24: SpatialShadery](SpatialShadery.md) 
    * [:octicons-arrow-right-24: Beamer](Beamer.md) 
    * [:octicons-arrow-right-24: ViewPort](ViewPort.md) 
    * [:octicons-arrow-right-24: Canvas](Canvas.md)
    * [:octicons-arrow-right-24: DrawMask](DrawMask.md)
    * [:octicons-arrow-right-24: ShaderTexOP](ShaderTexOP.md)

  
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

    
*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/BlendSoftedge.md)*