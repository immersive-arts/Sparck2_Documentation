# TfmLookAt

The LookAt transformation takes two transformation nodes: One where to look-from, and one where to look-at.

<figure markdown>
![TfmLookAt Node](../../assets/images/nodes/TfmLookAt.png){ width="300" }
</figure> 

!!! success "Dynamic Orientation Between Two Points"
    TfmLookAt creates a transformation that automatically orients to face from one point toward another. This is useful for billboards that always face the camera, spotlights that track targets, or any object that needs to maintain orientation toward a moving reference point.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `look from` | - | from where to look |
    | `look at` | - | where to look at |
    | `orientation` | - | axis orientation |
    | `direction` | - | look from look-from to look-at or from look-at to look-from |
    | `transformation pass` | - | select transfromation pass |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | send | message | send direct message to anim object: 'bang' for forced transformation bang. OR 'getlist' &lt;get...> items for dump out current values (needs a bang). Possible &lt;get...> items: getposition, getquat, getscale, getworldpos, getworldquat, getworldscale, gettransform, getinvtransform, getworldtransform |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | dump | message | dump of 'anim' , output of the requested &lt;get...> values and transformation bang from the above inlet. also outputs 'markerlist' if markers are received. |


---

## Basic Setup

!!! example "Creating a Look-At Transformation"
    To make an object always face a target:
    
    1. Create two [TfmNode](TfmNode.md) nodes: one for the source position, one for the target
    2. Create a **TfmLookAt** node
    3. Set `look from` to reference the source TfmNode
    4. Set `look at` to reference the target TfmNode
    5. Use TfmLookAt as the `parent` for any object that should face the target
    
    The orientation will automatically update as either node moves.

## Configuration Options

!!! tip "Direction and Orientation"
    | Property | Description |
    |----------|-------------|
    | **direction** | Controls which way the look-at vector points: from source→target or target→source |
    | **orientation** | Sets which local axis aligns with the look-at direction (e.g., Z-forward, Y-up) |
    
    Adjust these settings to match your object's natural orientation and desired facing direction.

## Transformation Pass

!!! info "Execution Order"
    TfmLookAt produces a transformation matrix that is **detached from the its own transformation hierarchy**. If other transformations depend on TfmLookAt's result, they must execute in a later [transformation pass](../render_groups_and_passes.md#render-passes).
    
## Use Cases

!!! info "Common Applications"
    - **Billboard effects**: Objects that always face the camera
    - **Spotlight tracking**: Lights that follow moving targets
    - **Turret/gimbal systems**: Objects that aim at targets
    - **Camera constraints**: Cameras that track subjects
    - **Connecting motion capture points**: Orient based on tracked marker positions

## Querying Transformation Data

!!! tip "Getting Transform Values"
    Send messages to the `send` inlet to query current transformation:
    
    | Message | Returns |
    |---------|---------|
    | `getposition` | Local position x y z |
    | `getquat` | Rotation as quaternion |
    | `getscale` | Local scale x y z |
    | `getworldpos` | World position |
    | `getworldquat` | World rotation as quaternion |
    | `getworldscale` | World scale |
    | `gettransform` | Full transformation matrix |
    | `getinvtransform` | Inverse transformation matrix |
    | `getworldtransform` | Full world transformation matrix |
    
    Send `bang` after the getlist message to output values via the `dump` outlet.

---

## TfmLookAt vs LookAtCamera

!!! note "Choosing the Right Node"
    | Feature | TfmLookAt | [LookAtCamera](LookAtCamera.md) |
    |---------|-----------|--------------------------------|
    | **Purpose** | General transformation orientation | Camera with look-at + frustum alignment |
    | **Output** | Transformation matrix | Camera intrinsics + frustum |
    | **Near-clip alignment** | No | Yes (aligns with look-at plane) |
    | **Use with** | Any object needing orientation | SceneCapture for rendering |
    | **Best for** | Billboards, spotlights, tracking | CAVE VR, head-tracked displays |

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with TfmLookAt in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **TfmLookAt**

    ---
    * [:octicons-arrow-right-24: TfmNode](TfmNode.md) 
    * [:octicons-arrow-right-24: TfmMerge](TfmMerge.md) 
    * [:octicons-arrow-right-24: TfmNodeInfo](TfmNodeInfo.md) 
    * [:octicons-arrow-right-24: TfmMirror](TfmMirror.md)
    * [:octicons-arrow-right-24: LookAtCamera](LookAtCamera.md)

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/TfmLookAt.md)*