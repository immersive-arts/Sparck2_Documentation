# CubeMap

Loads images files and transforms them into cubemaps.

Cubemaps are used by the SkyBox and Material nodes.

<figure markdown>
![CubeMap Node](../../assets/images/nodes/CubeMap.png){ width="300" }
</figure> 

!!! success "Environment Mapping for 3D Scenes"
    CubeMap loads and converts image files into OpenGL cubemap textures. These 6-faced environment maps are essential for creating skyboxes (360° backgrounds) and reflective materials. Load pre-made cubemap images or generate them dynamically from cross-shaped texture inputs.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `imagefile` | - | loads the file from ~_assets/_textures/_cubemaps |
    | `filewatch` | - | loads automaticaly a changed image file |
    | `pass` | - | select the renderpass |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | cross | texture | cross shape texture holding the 6 faces of the cube |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | cubemap | cubemap | cubemap texture |


---

## How Cubemaps Work

!!! info "Six-Faced Environment Texture"
    A cubemap consists of 6 square textures representing the inside faces of a cube:
    
    | Face | Direction | Description |
    |------|-----------|-------------|
    | **+X** | Right | Positive X axis |
    | **-X** | Left | Negative X axis |
    | **+Y** | Top | Positive Y axis (up) |
    | **-Y** | Bottom | Negative Y axis (down) |
    | **+Z** | Front | Positive Z axis |
    | **-Z** | Back | Negative Z axis |
    
    When rendered on a [SkyBox](SkyBox.md), these create a seamless 360° environment around the viewer.

## Cross Layout Format

!!! tip "Understanding the Cross Shape"
    Cubemap images are typically stored in a "cross" layout:
    
    ```
          [+Y]
    [-X] [+Z] [+X] [-Z]
          [-Y]
    ```
    
    This unfolds the cube into a flat image. When loading via the `cross` inlet, provide a texture in this arrangement, and CubeMap will automatically extract and orient the six faces.

## Loading Cubemaps

!!! example "Two Ways to Load"
    
    **From file:**
    
    1. Place your cubemap image in `~/_assets/_textures/_cubemaps/`
    2. Select the file via the `imagefile` property
    3. Enable `filewatch` to auto-reload if the file changes
    
    **From texture inlet:**
    
    1. Generate or load a cross-shaped texture (e.g., from [BoxMapCapture](BoxMapCapture.md) in "cross" mode)
    2. Connect it to the `cross` inlet
    3. The CubeMap node converts it to a proper cubemap format

## CubeMap vs BoxMap

!!! note "Understanding the Difference"
    | Feature | CubeMap | BoxMap |
    |---------|---------|--------|
    | **Format** | Single OpenGL cubemap texture | 6 separate textures |
    | **Source** | Image file or cross texture | [BoxMapCapture](BoxMapCapture.md) output |
    | **Use with** | [SkyBox](SkyBox.md), [Material](Material.md) | SPARCK internal rendering |
    | **Best for** | Pre-rendered environments | Real-time 360° capture |
    
    BoxMap is SPARCK's internal format for 360° rendering. CubeMap is the standard OpenGL format for environment mapping.

## Common Uses

!!! info "Where to Use Cubemaps"
    
    **Skybox backgrounds:**
    
    - Connect CubeMap to [SkyBox](SkyBox.md) to create immersive 360° backgrounds
    - The skybox renders behind all other 3D content
    
    **Reflective materials:**
    
    - Connect CubeMap to [Material](Material.md) nodes for environment reflections
    - Creates realistic shiny/metallic surface appearances

---

## Important Notes

!!! info "File Locations"
    
    ```
    ~/_assets/_textures/_cubemaps/     # Cubemap image files
    ```
    
    Supported formats: Standard image formats (PNG, JPG, TIFF, etc.) in cross layout.

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with CubeMap in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **CubeMap**

    ---
    * [:octicons-arrow-right-24: SkyBox](SkyBox.md) 
    * [:octicons-arrow-right-24: Material](Material.md)
    * [:octicons-arrow-right-24: BoxMapCapture](BoxMapCapture.md)
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/CubeMap.md)*