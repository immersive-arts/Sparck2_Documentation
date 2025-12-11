# ShaderColormap

Can be also used as a texture render pass, for two textures.

<figure markdown>
![ShaderColormap Node](../../assets/images/nodes/ShdrColormap.png){ width="300" }
</figure> 

!!! success "Per-Channel Color Remapping"
    ShaderColormap applies lookup table (LUT) transformations to each color channel independently. Use it for color grading, contrast adjustments, gamma correction, color inversion, posterization, and other color manipulation effects. Each channel (red, green, blue) has its own customizable response curve.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `factor` | - | factor |
    | `map dim` | - | color map dimension |
    | `interpolate` | - | use interpolation on the output texture |
    | `enable` | - | use this node as a texture render pass node. |
    | `red` | - | color map for red channel |
    | `green` | - | color map for green channel |
    | `blue` | - | color map for blue channel |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (also used for shader) |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |
    | texture | texture | texture two altered |


---

## How Color Mapping Works

!!! info "Lookup Table Transformation"
    Color mapping uses a lookup table (LUT) to transform input values to output values:
    
    - For each pixel, the input color value (0-255) is used as an index
    - The LUT returns a new value at that index
    - This allows arbitrary remapping of brightness and color response
    
    Each channel (red, green, blue) has its own independent curve, enabling complex color transformations.

## Channel Curves

!!! tip "Configuring Color Maps"
    Each channel has its own color map that defines the input-to-output relationship:
    
    | Property | Channel | Effect |
    |----------|---------|--------|
    | **red** | Red | Remaps red channel values |
    | **green** | Green | Remaps green channel values |
    | **blue** | Blue | Remaps blue channel values |
    
    The `map dim` property sets the resolution of the lookup table (higher = more precision).

## Common Effects

!!! example "Typical Color Transformations"
    
    **Increase Contrast:**
    
    - Steepen the curve in the middle range
    - Darks become darker, lights become lighter
    
    **Gamma Correction:**
    
    - Apply a power curve to compensate for display characteristics
    - Useful for matching projector output to expected brightness
    
    **Color Inversion (Negative):**
    
    - Reverse the curve direction (255→0, 0→255)
    - Creates a photographic negative effect
    
    **Posterization:**
    
    - Use a stepped/quantized curve
    - Reduces the number of distinct color levels
    
    **Channel Swap/Shift:**
    
    - Different curves per channel create color shifts
    - Useful for creative color grading

## Dual Texture Processing

!!! tip "Processing Two Textures"
    ShaderColormap can apply the same color transformation to two textures simultaneously:
    
    - Connect textures to both inlets
    - Both outlets provide the color-mapped versions
    - Useful when you need identical color correction on related texture pairs

## Interpolation

!!! info "Smooth vs Stepped Output"
    The `interpolate` property controls how values between LUT entries are handled:
    
    | Setting | Effect |
    |---------|--------|
    | **On** | Smooth interpolation between LUT values |
    | **Off** | Nearest-neighbor lookup (can create banding) |
    
    Enable interpolation for smooth gradients; disable for intentional posterization effects.

## Render Pass Mode

!!! info "Using as a Texture Render Pass"
    Enable the `enable` property to use ShaderColormap as part of a texture render pass:
    
    - The node processes textures during the render pipeline
    - Useful for integrating color correction into complex rendering chains
    - The `factor` property controls the effect intensity

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with ShaderColormap in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **ShaderColormap**

    ---
    * [:octicons-arrow-right-24: ShaderTexOP](ShaderTexOP.md) 
    * [:octicons-arrow-right-24: ShaderTexBlur](ShaderTexBlur.md) 
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderColormap.md)*