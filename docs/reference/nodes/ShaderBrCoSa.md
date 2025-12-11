# ShaderBrCoSa

Can be also used as a texture render pass, for two textures.

<figure markdown>
![ShaderBrCoSa Node](../../assets/images/nodes/ShdrBrCoSa.png){ width="300" }
</figure> 

!!! success "Quick Color Adjustments"
    ShaderBrCoSa (Brightness/Contrast/Saturation) provides intuitive controls for common image adjustments. Unlike complex color mapping, these controls work like familiar image editing tools — adjust brightness to lighten/darken, contrast to increase/decrease tonal range, and saturation to control color intensity.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `brightness` | - | brightness amount |
    | `contrast` | - | contrast amount |
    | `saturation` | - | saturation amount |
    | `alpha` | - | alpha amount |
    | `average luma` | - | average luma amount |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |
    | texture | texture | texture two altered |


---

## Adjustment Controls

!!! tip "Understanding Each Parameter"
    | Property | Neutral Value | Effect |
    |----------|---------------|--------|
    | **brightness** | 0 | Adds/subtracts from all pixel values. Positive = lighter, negative = darker |
    | **contrast** | 1 | Multiplies the difference from middle gray. >1 = more contrast, <1 = less contrast |
    | **saturation** | 1 | Controls color intensity. 0 = grayscale, 1 = normal, >1 = vivid colors |
    | **alpha** | 1 | Controls overall transparency. 0 = fully transparent, 1 = fully opaque |
    | **average luma** | - | Reference luminance for contrast calculations |

## Common Adjustments

!!! example "Typical Use Cases"
    
    **Matching projector brightness:**
    
    - Adjust `brightness` to compensate for projector differences
    - Lower brightness for overly bright projectors
    
    **Increasing visual punch:**
    
    - Slightly increase `contrast` (e.g., 1.1-1.3)
    - Slightly increase `saturation` (e.g., 1.1-1.2)
    
    **Desaturated/moody look:**
    
    - Reduce `saturation` toward 0 for grayscale
    - Adjust `contrast` for tonal control
    
    **Fade to black:**
    
    - Reduce `brightness` to darken the entire image
    - Combine with `alpha` reduction for fade-out effects

## Dual Texture Processing

!!! info "Processing Two Textures"
    ShaderBrCoSa can apply identical adjustments to two textures simultaneously:
    
    - Connect textures to both inlets
    - Both outlets provide the adjusted versions
    - Useful for matching color characteristics across texture pairs (e.g., stereo left/right)

## Average Luma

!!! info "Contrast Reference Point"
    The `average luma` property sets the luminance value around which contrast adjustments pivot:
    
    - Contrast expands/compresses values relative to this reference
    - Default uses a standard mid-gray reference
    - Adjust for images with unusual brightness distributions

---

## ShaderBrCoSa vs ShaderColormap

!!! note "When to Use Each"
    | Feature | ShaderBrCoSa | [ShaderColormap](ShaderColormap.md) |
    |---------|--------------|-------------------------------------|
    | **Controls** | Simple sliders | Per-channel curves |
    | **Ease of use** | Very easy | More complex |
    | **Precision** | Good for quick adjustments | Full control over response |
    | **Best for** | Brightness/contrast matching | Color grading, gamma, LUT effects |
    
    Use **ShaderBrCoSa** for quick, intuitive adjustments. Use **ShaderColormap** when you need precise per-channel control or complex color transformations.

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with ShaderBrCoSa in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **ShaderBrCoSa**

    ---
    * [:octicons-arrow-right-24: ShaderColormap](ShaderColormap.md)
    * [:octicons-arrow-right-24: ShaderTexOP](ShaderTexOP.md) 
    * [:octicons-arrow-right-24: ShaderTexZoom](ShaderTexZoom.md)
    * [:octicons-arrow-right-24: ViewPort](ViewPort.md)

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderBrCoSa.md)*