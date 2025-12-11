# ShaderTexZoom

Can be also used as a texture render pass, for two textures.

<figure markdown>
![ShaderTexZoom Node](../../assets/images/nodes/ShdrZoom.png){ width="300" }
</figure> 

!!! success "Scale and Reposition Textures"
    ShaderTexZoom provides independent control over texture scaling and positioning for both source (input region) and destination (output region). Use it to zoom into texture regions, reposition content, crop textures, or create picture-in-picture effects. Supports processing two textures simultaneously.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `src scale` | - | source x and y scale |
    | `src pos` | - | source x and y position |
    | `dest scale` | - | dest x and y scale |
    | `dest pos` | - | dest x and y position |
    | `interpolate` | - | use interpolation on output texture |
    | `texture one` | - | use this node as texture render pass |
    | `texture two` | - | use this node as texture render pass |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (also used for texture fx) |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |
    | texture | texture | texture two altered |


---

## Source vs Destination

!!! info "Understanding Scale and Position"
    ShaderTexZoom uses a source-to-destination mapping model:
    
    | Property | Controls | Effect |
    |----------|----------|--------|
    | **src scale** | Input region size | Which portion of the source texture is sampled |
    | **src pos** | Input region position | Where in the source texture to sample from |
    | **dest scale** | Output region size | How large the result appears in the output |
    | **dest pos** | Output region position | Where the result is placed in the output |
    
    Think of it as: "Take *this region* from the source (src) and place it *here* in the output (dest)."

## Zoom and Pan Effects

!!! example "Zooming Into a Texture Region"
    To zoom into a specific area of a texture:
    
    1. Connect your texture to the first texture inlet
    2. Set `src scale` to less than 1.0 (e.g., 0.5, 0.5) to select a smaller region
    3. Adjust `src pos` to center on the area of interest
    4. Set `dest scale` to 1.0 to fill the output
    5. Enable `interpolate` for smooth scaling
    
    Result: The selected region is enlarged to fill the output.

!!! example "Picture-in-Picture"
    To create a small inset of one texture:
    
    1. Connect your texture to the first inlet
    2. Keep `src scale` at 1.0 (use full source)
    3. Set `dest scale` to a smaller value (e.g., 0.25, 0.25)
    4. Set `dest pos` to position the inset (e.g., corner placement)
    
    Result: The full texture appears as a small inset at the specified position.

## Dual Texture Processing

!!! tip "Processing Two Textures"
    ShaderTexZoom can apply the same zoom/pan transformation to two textures simultaneously:
    
    - Connect textures to both texture inlets
    - Enable `texture one` and/or `texture two` to include them in the render pass
    - Both outlets provide the transformed versions
    
    This is useful when you need to apply identical spatial transformations to related texture pairs (e.g., color and depth, left and right stereo).

## Interpolation

!!! tip "Smooth vs Sharp Scaling"
    The `interpolate` property controls texture filtering:
    
    | Setting | Effect |
    |---------|--------|
    | **On** | Smooth, bilinear filtering (better for photographic content) |
    | **Off** | Nearest-neighbor, sharp pixels (better for pixel art or when preserving hard edges) |
    
    Enable interpolation when scaling up to avoid blocky artifacts.

## Texture Render Pass Mode

!!! info "Using as a Render Pass"
    Enable `texture one` or `texture two` to use ShaderTexZoom as part of a texture render pass:
    
    - The node will process textures during the render pipeline
    - Useful for integrating zoom effects into complex texture processing chains
    - Ensure proper render pass ordering if source textures come from other render operations

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with ShaderTexZoom in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **ShaderTexZoom**

    ---
    * [:octicons-arrow-right-24: ShaderTexOP](ShaderTexOP.md) 
    * [:octicons-arrow-right-24: ShaderTexColorMap](ShaderTexColorMap.md) 
    * [:octicons-arrow-right-24: ShaderTexBlur](ShaderTexBlur.md)
    * [:octicons-arrow-right-24: ShaderTexStitch](ShaderTexStitch.md)

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderTexZoom.md)*