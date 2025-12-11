# TfmMirror

The Mirror transformation takes two transformation nodes: One where to set the mirror, and a second one to be mirrored.

the mirrored transformation can also be a Beamer or a Camera -  in this case the node becomes a mirrored Beamer or Camera node and can be used by a Capture node.

<figure markdown>
![TfmMirror Node](../../assets/images/nodes/TfmMirror.png){ width="300" }
</figure> 

!!! success "Reflect Transformations Across a Plane"
    TfmMirror creates a reflected/mirrored version of any transformation. It can mirror standard transformations, but also works with [Beamer](Beamer.md) and [SceneCamera](SceneCamera.md) nodes — making it possible to render reflections, symmetric projections, or virtual camera views through mirrors.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `mirror` | - | mirror node |
    | `mirrored` | - | mirrored node - can also be a Beamer or Camera node |
    | `mode` | - | the kind of mirror transformation |
    | `mirrorplane` | - | set which two axis become the mirror plane |
    | `transformation pass` | - | select transfromation pass |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|


---

## How It Works

!!! info "Mirror and Mirrored Nodes"
    TfmMirror requires two inputs:
    
    | Property | Purpose |
    |----------|---------|
    | **mirror** | The transformation that defines the mirror plane's position and orientation |
    | **mirrored** | The transformation to be reflected across the mirror plane |
    
    The output is a new transformation representing the mirrored position of the `mirrored` node, as if reflected in a mirror placed at the `mirror` node.

## Mirror Plane Configuration

!!! tip "Setting the Mirror Plane"
    The `mirrorplane` property defines which two axes form the reflective surface:
    
    | Mirror Plane | Reflects Across |
    |--------------|-----------------|
    | **XY** | Reflects across the XY plane (mirrors Z axis) |
    | **XZ** | Reflects across the XZ plane (mirrors Y axis) |
    | **YZ** | Reflects across the YZ plane (mirrors X axis) |
    
    The mirror plane is positioned and oriented according to the `mirror` node's transformation.

## Basic Setup

!!! example "Creating a Mirrored Transformation"
    To mirror an object's transformation:
    
    1. Create a [TfmNode](TfmNode.md) to define the mirror plane position/orientation
    2. Identify the transformation you want to mirror (TfmNode, RigidBody, etc.)
    3. Create a **TfmMirror** node
    4. Set `mirror` to reference the mirror plane TfmNode
    5. Set `mirrored` to reference the source transformation
    6. Select the appropriate `mirrorplane` axis
    7. Use TfmMirror as the parent for objects that should appear reflected

## Mirroring Cameras and Beamers

!!! example "Creating Reflection Renders"
    TfmMirror has a special capability: when the `mirrored` node is a [Beamer](Beamer.md) or [SceneCamera](SceneCamera.md), the TfmMirror node itself becomes a mirrored camera/beamer that can be used with [SceneCapture](SceneCapture.md):
    
    1. Create a mirror plane [TfmNode](TfmNode.md)
    2. Create a **TfmMirror** node
    3. Set `mirror` to the mirror plane
    4. Set `mirrored` to your Beamer or SceneCamera
    5. In a [SceneCapture](SceneCapture.md), set `parent` to the TfmMirror node
    6. The capture type will show as **beamer mirror** or **camera mirror**
    
    This renders the scene as seen from a virtual camera reflected in the mirror — useful for real-time mirror/reflection effects.

## Use Cases

!!! info "Common Applications"
    - **Real-time reflections**: Render mirrored camera views for reflective surfaces
    - **Symmetric projections**: Mirror a calibrated Beamer for symmetric projection setups
    - **Virtual mirrors**: Create the illusion of mirrors in projection-mapped environments
    - **Symmetric object placement**: Position objects symmetrically across a plane

## Transformation Pass

!!! info "Execution Order"
    Like [TfmLookAt](TfmLookAt.md), TfmMirror produces a transformation matrix that is **detached from its transformation hierarchy**. If other transformations depend on TfmMirror's result, they must execute in a later [transformation pass](../render_groups_and_passes.md#render-passes).

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with TfmMirror in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **TfmMirror**

    ---
    * [:octicons-arrow-right-24: TfmNode](TfmNode.md) 
    * [:octicons-arrow-right-24: TfmLookAt](TfmLookAt.md)
    * [:octicons-arrow-right-24: SceneCapture](SceneCapture.md)
    * [:octicons-arrow-right-24: Beamer](Beamer.md) 
    * [:octicons-arrow-right-24: SceneCamera](SceneCamera.md) 

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/TfmMirror.md)*