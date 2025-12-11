# Hook

A helper to get Jitter objects draw and tranform with SPARCKS render and transform nodes

<figure markdown>
![Hook Node](../../assets/images/nodes/Hook.png){ width="300" }
</figure> 

!!! success "Bridge Jitter Objects into SPARCK"
    Hook integrates standard Max/Jitter GL objects (like `jit.gl.mesh`, `jit.gl.gridshape`, `jit.gl.model`, etc.) into the SPARCK ecosystem. It handles context management, render group assignment, and transformation linking automatically — so your existing Jitter patches can render alongside SPARCK content without manual configuration.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `drawto` | - | set the render group. Capture/Beamer/3DViewer have an equivalent in which you can choose which group to render. |
    | `material` | - | select one of sparcks material nodes |
    | `shader` | - | select one of spracks shader nodes |
    | `parent` | - | parent transformation node |
    | `position` | (local transformation) | position x y z |
    | `rotation` | (local transformation) | rotation x y z |
    | `scale` | (local transformation) | scale x y z |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | link | message | link to object to place it into the sparck-context. It  sends 'enable' 'drawto' 'shader' material' |
    | link | message | link to object to connect it to sparck transformation. It sends 'anim' message |


---

## How It Works

!!! info "Two-Outlet Connection System"
    Hook provides two outlets that connect to different aspects of your Jitter object:
    
    | Outlet | Purpose | Messages Sent |
    |--------|---------|---------------|
    | **First outlet** | Rendering context and appearance | `enable`, `drawto`, `shader`, `material` |
    | **Second outlet** | Transformation control | `anim` message |
    
    Connect both outlets to your Jitter GL object to fully integrate it into SPARCK.

## Basic Setup

!!! example "Connecting a Jitter Object"
    To integrate an existing Jitter GL object (e.g., `jit.gl.mesh`):
    
    1. Create a **Hook** node
    2. Connect Hook's **first outlet** to your Jitter object (for context/rendering)
    3. Connect Hook's **second outlet** to your Jitter object (for transformation)
    4. Set `drawto` to choose which render groups display your object
    5. Optionally set `parent` to link to a SPARCK transformation hierarchy
    6. Optionally assign a SPARCK `material` or `shader`
    
    Your Jitter object now renders in the SPARCK context and responds to SPARCK transformations.

## Render Group Control

!!! tip "Controlling Visibility"
    Use `drawto` to specify where your Jitter object appears:
    
    - Enable the **3DViewer** checkbox to see it in the preview
    - Enable **Beamer** checkboxes to include it in projector outputs
    - The render group system works identically to native SPARCK content nodes like [Canvas](Canvas.md) and [Model](Model.md)

## Transformation Integration

!!! tip "Using SPARCK Transformations"
    Hook provides full transformation support:
    
    - **parent**: Link to any SPARCK transformation node ([TfmNode](TfmNode.md), [RigidBody](RigidBody.md), etc.)
    - **position/rotation/scale**: Apply local transformations
    
    Your Jitter object inherits the full transformation hierarchy, including motion capture data if parented to a [RigidBody](RigidBody.md).

## Material and Shader Assignment

!!! info "SPARCK Materials and Shaders"
    Apply SPARCK rendering features to your Jitter objects:
    
    - **material**: Assign a SPARCK [Material](Material.md) node for consistent lighting/appearance
    - **shader**: Assign a SPARCK shader node for custom effects
    
    This allows Jitter objects to benefit from SPARCK's shader system, including projection mapping shaders like [SpatialShadery](SpatialShadery.md).

---

## Why Use Hook?

!!! warning "Always Use Hook for Jitter Integration"
    When connecting Jitter objects to SPARCK, always use the Hook node rather than trying to specify contexts manually. SPARCK manages multiple rendering contexts:
    
    - **Sparck-Context**: Main rendering context
    - **Viewer-Context**: 3DViewer display
    - **Output-Context 1-4**: Final output windows
    
    Hook ensures your Jitter objects render to the correct context and integrate properly with SPARCK's rendering pipeline.

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with Hook in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **Hook**

    ---
    * [:octicons-arrow-right-24: TfmNode](TfmNode.md) 
    * [:octicons-arrow-right-24: Material](Material.md)
    * [:octicons-arrow-right-24: Canvas](Canvas.md)
    * [:octicons-arrow-right-24: Model](Model.md)

  
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


*Last updated: 2025-12-04 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/Hook.md)*