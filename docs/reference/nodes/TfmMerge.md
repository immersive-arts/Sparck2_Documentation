# TfmMerge

The node merges different transformational parts of two differen transformation nodes into one.

<figure markdown>
![TfmMerge Node](../../assets/images/nodes/TfmMerge.png){ width="300" }
</figure> 

!!! success "Combine Transformations from Multiple Sources"
    TfmMerge allows you to selectively combine position, rotation, and scale from two different transformation sources into a single output transformation. This is useful when you need an object to follow one source's position while inheriting rotation from another, or any other combination of transformation components.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `parentA` | - | parent A transformation node |
    | `parentB` | - | parent B transformation node |
    | `pos` | - | select the translational part from one of the parents |
    | `rot` | - | select the rotation from one of the parents |
    | `scale` | - | select the scale part from one of the parents |
    | `transformation pass` | - | transformation pass |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|


---

## How It Works

!!! info "Selective Component Merging"
    TfmMerge takes two parent transformations (A and B) and lets you pick which parent provides each component:
    
    | Component | Options |
    |-----------|---------|
    | **pos** | Position from parentA or parentB |
    | **rot** | Rotation from parentA or parentB |
    | **scale** | Scale from parentA or parentB |
    
    The result is a new transformation that combines the selected components from each source.

## Basic Setup

!!! example "Merging Two Transformations"
    To create a merged transformation:
    
    1. Create or identify two transformation sources ([TfmNode](TfmNode.md), [RigidBody](RigidBody.md), [TfmLookAt](TfmLookAt.md), etc.)
    2. Create a **TfmMerge** node
    3. Set `parentA` to reference the first transformation
    4. Set `parentB` to reference the second transformation
    5. Set `pos`, `rot`, and `scale` to select which parent provides each component
    6. Use TfmMerge as the parent for your target object

## Use Cases

!!! tip "Common Applications"
    
    **Position from tracking, rotation from look-at:**
    
    - `parentA`: [RigidBody](RigidBody.md) (tracked position)
    - `parentB`: [TfmLookAt](TfmLookAt.md) (orientation toward target)
    - `pos`: A, `rot`: B, `scale`: A
    
    **Stabilized rotation with moving position:**
    
    - `parentA`: Moving object transformation
    - `parentB`: Fixed orientation reference
    - `pos`: A, `rot`: B, `scale`: A
    
    **Independent scale control:**
    
    - `parentA`: Animated transformation
    - `parentB`: Scale controller
    - `pos`: A, `rot`: A, `scale`: B

## Transformation Pass

!!! info "Execution Order"
    Like other advanced transformation nodes, TfmMerge has a `transformation pass` setting to control execution order:
    
    - **pass1**: Default, executes first
    - **pass2**: Executes after pass1
    - **pass3**: Executes after pass2
    
    If parentA or parentB are computed transformations (like [TfmLookAt](TfmLookAt.md)), ensure TfmMerge executes in a later pass than its sources.

---

## TfmMerge vs Other Transformation Nodes

!!! note "When to Use TfmMerge"
    | Node | Purpose |
    |------|---------|
    | **[TfmNode](TfmNode.md)** | Simple position/rotation/scale with hierarchy |
    | **TfmMerge** | Combine components from two different sources |
    | **[TfmLookAt](TfmLookAt.md)** | Orient toward a target point |
    | **[TfmMirror](TfmMirror.md)** | Mirror/reflect a transformation |
    
    Use TfmMerge when you need to "mix and match" transformation components from different sources that can't be achieved with simple parenting.

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with TfmMerge in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **TfmMerge**

    ---
    * [:octicons-arrow-right-24: TfmNode](TfmNode.md) 
    * [:octicons-arrow-right-24: TfmNodeInfo](TfmNodeInfo.md) 
    * [:octicons-arrow-right-24: TfmLookAt](TfmLookAt.md) 
    * [:octicons-arrow-right-24: TfmMirror](TfmMirror.md)
    * [:octicons-arrow-right-24: RigidBody](RigidBody.md)

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/TfmMerge.md)*