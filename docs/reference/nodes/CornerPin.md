# CornerPin

Provides controls for mapping textures to an output window by repositioning the image corners.

It is the most simple and easy to use mapping nodes at SPARCK's disposal

<figure markdown>
![CornerPin Node](../../assets/images/nodes/CornerPin.png){ width="300" }
</figure> 

!!! success "Quick Rectangular Mapping"
    CornerPin lets you quickly match a rectangular video texture onto simple planar surfaces by dragging four corner handles. It's the fastest way to align projection content when you don't need complex geometric correction — ideal for flat walls, screens, and simple rectangular surfaces.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `edit` | - | sets the focus of the editor window to this node |
    | `reset` | - | resets the corner pins to their default positions |
    | `drawto` | - | set the render group. Capture/Beamer/3DViewer have an equivalent in which you can choose which group to render. |
    | `viewport` | - | select viewport this cornerpin is directly rendered to. Inside the viewport node you should set the mesh to 'off' |
    | `object color` | - | object color |
    | `corner radius` | - | size of the handles |
    | `drawcorners` | - | draws to handles in the final rendering |
    | `layer` | - | depth layer (works best with depth-buffering off) |
    | `smooth` | - | smooth rendering |
    | `blend` | - | enables blendmode |
    | `blendmode` | - | choose blendmode: <li>alphablend <li>add <li>multiply <li>screen <li>exclusion <li>colorblend <li>coloradd <li>alphaadd |
    | `interpolate` | - | use interpolation |
    | `preserve aspect` | - | preserve aspect ratio |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|


---

## Basic Setup

!!! example "Wall Projection Workflow"
    Set up a simple wall projection with CornerPin:
    
    1. Create a [Window](Window.md) node and configure your output display
    2. Create a [ViewPort](ViewPort.md) node and set `mesh` to **none**
    3. Link the ViewPort to the Window
    4. Create a **CornerPin** node
    5. Set CornerPin's `viewport` to reference your ViewPort
    6. Connect your texture source (Video, [SpoutReceiver](SpoutReceiver.md), etc.) to CornerPin's texture inlet
    7. Click `edit` to open the corner editor and adjust the four corners

!!! warning "ViewPort Mesh Setting"
    When using CornerPin, set the ViewPort's `mesh` property to **none**. The CornerPin node handles all geometric mapping — using both would create conflicts.

## Corner Editor

!!! tip "Adjusting Corners"
    Click `edit` to open the CornerPin editor window:
    
    - **Drag corners** to reposition them and match your projection surface
    - Adjust `corner radius` to change handle size for easier selection
    - Enable `drawcorners` to see handles in the final output (useful during setup)
    - Click `reset` to return corners to their default rectangular positions
    
    The editor provides a visual interface where you can see the texture and drag each of the four corners independently.

## Display Options

!!! info "Rendering Settings"
    Fine-tune how the mapped texture is displayed:
    
    | Property | Effect |
    |----------|--------|
    | **smooth** | Enable smooth/antialiased rendering |
    | **interpolate** | Use texture interpolation for smoother scaling |
    | **preserve aspect** | Maintain original texture aspect ratio |
    | **layer** | Set depth ordering when using multiple CornerPins |
    | **blend/blendmode** | Control transparency and blending with background |

## CornerPin vs MeshWarp

!!! note "Choosing the Right Tool"
    | Feature | CornerPin | [MeshWarp](MeshWarp.md) |
    |---------|-----------|-------------------------|
    | **Control points** | 4 corners | Full lattice grid |
    | **Surface types** | Flat, rectangular | Curved, irregular |
    | **Setup time** | Very quick | More involved |
    | **Geometric correction** | Perspective only | Full mesh deformation |
    | **Best for** | Walls, screens, simple surfaces | Domes, curved screens, complex shapes |
    
    Use **CornerPin** when you need fast, simple alignment on flat surfaces. Use **MeshWarp** when projecting onto curved or irregular geometries.

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with CornerPin in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **CornerPin**

    ---
    * [:octicons-arrow-right-24: MeshWarp](MeshWarp.md) 
    * [:octicons-arrow-right-24: ViewPort](ViewPort.md)
    * [:octicons-arrow-right-24: Window](Window.md)
    * [:octicons-arrow-right-24: SpoutReceiver](SpoutReceiver.md)

  
-   :material-video-box:{ .lg .middle } __Tutorials__

    ---

    * [:octicons-arrow-right-24: Wall Projection](../../start/tutorials/01_Wall_Projection/Wall_Projection.md)
    
    [:octicons-arrow-right-24: Watch Now](../../start/tutorials/videos.md){ .md-button .md-button--primary }

-   :material-forum:{ .lg .middle } __Community__

    ---

    [:octicons-arrow-right-24: Join Now](https://github.com/immersive-arts/Sparck2/discussions){ .md-button .md-button--primary }


</div>

---

!!! question "Need help or want to suggest improvements?"
       
    [:fontawesome-brands-github: Report an issue](../../contributing/reporting-a-bug.md){ .md-button }
    [:fontawesome-brands-github: Improve the Docs](../../contributing/reporting-a-docs-issue.md){ .md-button }


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/CornerPin.md)*