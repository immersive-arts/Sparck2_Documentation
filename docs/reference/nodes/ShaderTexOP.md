# ShaderTexOP

The TextureOP node applies either a binary operator to two input textures, or a unary operator to the left input texture

<figure markdown>
![ShaderTexOP Node](../../assets/images/nodes/ShdrOP.png){ width="300" }
</figure> 

!!! success "Texture Math and Compositing"
    ShaderTexOP performs pixel-by-pixel mathematical operations between two textures. Use it for compositing, masking, blending, color manipulation, and creating complex texture effects by combining simpler inputs.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `mode` | - | operation mode (see details down below) |
    | `in1scale` | - | scale scalar for texture left |
    | `in2scale` | - | scale scalar for texture right |
    | `in1offset` | - | offset scalar for texture left |
    | `in2offset` | - | offset scalar for texture right |
    | `outScale` | - | output offset |
    | `enable` | - | use node for a texture effect render pass |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (left operand) |
    | texture | texture | texture two (right operand) |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | result | texture | result of 1 op 2 (left op right) |


---

## Operation Modes

!!! info "Binary Operators (Two Textures)"
    These operations combine texture 1 (left) and texture 2 (right):
    
    | Mode | Operation | Description |
    |------|-----------|-------------|
    | **mult** | Multiplication | `tex1 × tex2` — Darkens, useful for masking |
    | **div** | Division | `tex1 ÷ tex2` — Brightens based on inverse |
    | **add** | Addition | `tex1 + tex2` — Brightens, combines light |
    | **sub** | Subtraction | `tex1 - tex2` — Difference between textures |
    | **mod** | Modulo | `tex1 % tex2` — Remainder operation |
    | **min** | Minimum | `min(tex1, tex2)` — Darker of the two |
    | **max** | Maximum | `max(tex1, tex2)` — Lighter of the two |
    | **avg** | Average | `(tex1 + tex2) / 2` — Blend 50/50 |
    | **absdiff** | Absolute Difference | `|tex1 - tex2|` — Highlight differences |

!!! info "Unary Operators (Single Texture)"
    These operations work on texture 1 (left) only:
    
    | Mode | Operation | Description |
    |------|-----------|-------------|
    | **abs** | Absolute Value | `|tex1|` — Remove negative values |
    | **pass** | Pass-through | Output texture 1 unchanged (with scale/offset) |

## Input Scaling and Offset

!!! tip "Adjusting Input Values"
    Before the operation is applied, each input can be scaled and offset:
    
    ```
    adjusted_value = (input × scale) + offset
    ```
    
    | Property | Effect |
    |----------|--------|
    | **in1scale** | Multiply texture 1 values (1.0 = unchanged) |
    | **in2scale** | Multiply texture 2 values (1.0 = unchanged) |
    | **in1offset** | Add to texture 1 values (0.0 = unchanged) |
    | **in2offset** | Add to texture 2 values (0.0 = unchanged) |
    | **outScale** | Scale the final output |
    
    Use these to normalize inputs or create specific blending ratios.

## Common Use Cases

!!! example "Masking with Multiply"
    Apply a mask to a texture:
    
    - **Texture 1**: Your content texture
    - **Texture 2**: Mask from [DrawMask](DrawMask.md) (white = visible, black = hidden)
    - **Mode**: mult
    
    Result: Content is visible where mask is white, hidden where mask is black.

!!! example "Combining Textures with Add"
    Layer multiple light sources or effects:
    
    - **Texture 1**: First light/effect
    - **Texture 2**: Second light/effect
    - **Mode**: add
    
    Result: Additive blending (good for light effects, glow).

!!! example "Finding Differences"
    Highlight what changed between two textures:
    
    - **Texture 1**: Reference texture
    - **Texture 2**: Comparison texture
    - **Mode**: absdiff
    
    Result: White where textures differ, black where they match.

## Render Pass Mode

!!! info "Enable for Texture Effect Pass"
    Set `enable` to use ShaderTexOP as part of a texture effect render pass. When enabled, the node processes textures during the render pipeline rather than on-demand.

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with ShaderTexOP in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **ShaderTexOP**

    ---
    * [:octicons-arrow-right-24: DrawMask](DrawMask.md)
    * [:octicons-arrow-right-24: ShaderTexBlur](ShaderTexBlur.md) 
    * [:octicons-arrow-right-24: ShaderTexColorMap](ShaderTexColorMap.md) 
    * [:octicons-arrow-right-24: ShaderTexZoom](ShaderTexZoom.md) 

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderTexOP.md)*