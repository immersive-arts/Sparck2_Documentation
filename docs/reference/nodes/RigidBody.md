# RigidBody

The Rigidbody Node represents a transformation (position, rotation and scale) in 3D space received from the [OptiTrack] node. It can be connected to almost all nodes that have a representation in 3D space.

It can also be used to establish parent-child relationships in a hirarchical transformation structure, where child nodes are transformed relative to their parents

<figure markdown>
![TfmNode Node](../../assets/images/nodes/RigidBody.png){ width="300" }
</figure> 

!!! success "Motion Capture to SPARCK"
    RigidBody bridges real-world tracking data with SPARCK's 3D scene. It receives transformation data from the [OptiTrack](OptiTrack.md) node and applies it to any SPARCK node with a 3D representation — enabling **tracked match between virtual and physical worlds** for Spatial Augmented Reality installations.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `stream` | - | link to stream provided by the [OptiTrack] node |
    | `position` | (local transformation) | position x y z |
    | `rotation` | (local transformation) | rotation x y z |
    | `scale` | (local transformation) | scale x y z |
    | `leap forward` | [milliseconds] | if value is positive, it calculates forward predicted position. If value is negative, it queues the transformation for the amout of time (i.e. to make it synchronous with video feed that takes longer to capture) |
    | `leap filter` | - | noise filter |
    | `scale` | - | scaling of translation values only |
    | `marker draw` | - | if marker information is sent, it can be drawn to this render groups |
    | `marker color` | - | if marker are drawn, color of marker |
    | `marker size` | - | if marker are drawn, size of marker |

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

!!! info "Connection and Stream Indicators"
    The two boxes behind the `stream` property indicate connection status:
    
    - **First box**: Connection to the OptiTrack system (via NatNet2OSC)
    - **Second box**: Data stream is alive and receiving updates

[OptiTrack]: ./OptiTrack.md


## Connecting to OptiTrack

!!! example "Basic Workflow"
    To track a physical object and apply its transformation to a SPARCK node:
    
    1. In **Motive** (OptiTrack software), create a rigid body from your markers
    2. Ensure **NatNet2OSC** is running and bridging data to SPARCK
    3. In the [OptiTrack](OptiTrack.md) node, assign the rigid body to a stream (1-8)
    4. Create a **RigidBody** node
    5. Set the `stream` property to match the OptiTrack stream number
    6. Set the RigidBody as the `parent` of your target node (e.g., [Canvas](Canvas.md))
    
    The target node will now follow the tracked physical object in real-time.

## Latency Compensation

!!! tip "Leap Forward Prediction"
    The `leap forward` property compensates for system latency:
    
    | Value | Behavior |
    |-------|----------|
    | **Positive** (e.g., 20) | Predicts position forward by N milliseconds — use for fast-moving objects where projection lag is visible |
    | **Negative** (e.g., -50) | Delays transformation by N milliseconds — use to sync with video feeds that have capture latency |
    | **0** | No compensation |
    
    Use `leap filter` to smooth noisy prediction data when using positive leap forward values.

## Parent-Child Hierarchies

!!! info "Transformation Inheritance"
    RigidBody can establish parent-child relationships in a hierarchical structure:
    
    - Child nodes are transformed **relative to their parent**
    - Multiple RigidBody nodes can be chained for complex articulated structures
    - Local `position`, `rotation`, and `scale` offsets are applied after the tracked transformation
    
    This allows precise alignment between tracked markers and projection content — for example, if markers are offset from the projection surface.

## Marker Visualization

!!! tip "Debugging with Marker Display"
    When OptiTrack sends individual marker positions (not just rigid body transforms):
    
    1. Set `marker draw` to a render group (e.g., 3DViewer)
    2. Adjust `marker color` and `marker size` for visibility
    3. View markers in the 3DViewer to verify tracking quality
    
    The `dump` outlet also outputs `markerlist` when markers are received.

## Querying Transformation Data

!!! info "Getting Transform Values"
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

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with RigidBody in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **RigidBody**

    ---
    * [:octicons-arrow-right-24: OptiTrack](OptiTrack.md)
    * [:octicons-arrow-right-24: TfmNode](TfmNode.md)
    * [:octicons-arrow-right-24: Canvas](Canvas.md)
    * [:octicons-arrow-right-24: Beamer](Beamer.md)
    * [:octicons-arrow-right-24: SpatialShadery](SpatialShadery.md)

  
-   :material-video-box:{ .lg .middle } __Tutorials__

    ---

    * [:octicons-arrow-right-24: Spatial Augmented Reality](../../start/tutorials/06_Spatial_Augmented_Reality/Spatial_Augmented_Reality.md)
    
    [:octicons-arrow-right-24: Watch Now](../../start/tutorials/videos.md){ .md-button .md-button--primary }

-   :material-forum:{ .lg .middle } __Community__

    ---

    [:octicons-arrow-right-24: Join Now](https://github.com/immersive-arts/Sparck2/discussions){ .md-button .md-button--primary }


</div>

---

!!! question "Need help or want to suggest improvements?"
       
    [:fontawesome-brands-github: Report an issue](../../contributing/reporting-a-bug.md){ .md-button }
    [:fontawesome-brands-github: Improve the Docs](../../contributing/reporting-a-docs-issue.md){ .md-button }


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/RigidBody.md)*