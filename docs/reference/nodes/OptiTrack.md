# OptiTrack

Optitrack is a commercialy available optical tracking system.

In order to use it with SPARCK, you need the [NatNet2Osc](https://github.com/immersive-arts/NatNetFour2OSC) App.

<figure markdown>
![OptiTrack Node](../../assets/images/nodes/OptiTrack.png){ width="300" }
</figure> 

!!! success "Real-Time Tracking for Spatial Augmented Reality"
    The OptiTrack node enables SPARCK to receive real-time transformation data from the OptiTrack motion capture system. This data drives virtual objects to move synchronously with their physical counterparts, providing a tracked match between virtual and physical worlds — essential for Spatial Augmented Reality installations.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `reply indicator` | - | lights up when bidirectional connection to motive works |
    | `connection indicator` | - | lights up when optitrack data is received |
    | `stream 1 - 8` | - | chosen optitrack rigidbody to be used with rigidbody abstraction |
    | `in port` | - | listening port, port where the NatNet2Osc-app send the osc stream. |
    | `out port` | - | sending port, NatNetThree2Osc-app listening port to receive commands. |
    | `out port IP` | - | sending IP address, where the NatNetThree2Osc-app runs. |
    | `leap forward` | - | calculate forward prediction. [ms] |
    | `leap filter` | - | smooth forward prediction. [%] |
    | `parent` | - | parent transformation node |
    | `scale` | (local transformation) | scale in x y z |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | raw | message | raw motive data stream |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | raw | message | raw motive data stream |


---

## Setup Requirements

!!! warning "NatNet2OSC Bridge Required"
    OptiTrack streams data in its proprietary **NatNet** format. SPARCK cannot receive NatNet directly — you need the **NatNet2OSC** application as a bridge:
    
    1. Download [NatNet2OSC](https://github.com/immersive-arts/NatNetFour2OSC) from GitHub
    2. Run NatNet2OSC on the same machine as Motive (or on the network)
    3. Configure NatNet2OSC to listen to Motive's NatNet stream
    4. NatNet2OSC converts the data to OSC and sends it to SPARCK
    
    The OptiTrack node listens for this OSC stream on the configured `in port`.

## Connection Setup

!!! tip "Network Configuration"
    Configure the ports and IP addresses to establish communication:
    
    | Property | Purpose | Typical Value |
    |----------|---------|---------------|
    | `in port` | Port where SPARCK receives OSC data from NatNet2OSC | 1511 |
    | `out port` | Port where SPARCK sends commands to NatNet2OSC | 1512 |
    | `out port IP` | IP address of the machine running NatNet2OSC | 127.0.0.1 (local) or network IP |
    
    The **reply indicator** lights up when bidirectional communication is established.
    The **connection indicator** lights up when tracking data is actively being received.

## Working with RigidBodies

!!! example "Tracking Objects Workflow"
    To track physical objects and move virtual geometry accordingly:
    
    1. **In Motive**: Define rigid bodies for each object you want to track. Give them unique names/IDs.
    2. **In OptiTrack node**: Assign each rigid body to a stream slot (stream 1–8)
    3. **Add RigidBody nodes**: Create a [RigidBody](RigidBody.md) node for each tracked object
    4. **Link streams**: Set each RigidBody's `stream` property to the corresponding OptiTrack stream
    5. **Parent geometry**: Set the RigidBody as parent for your [Canvas](Canvas.md) or other nodes
    
    The virtual objects will now follow the physical tracked objects in real-time.

## Latency Compensation

!!! info "Leap Forward Prediction"
    Fast-moving tracked objects can cause visible jitter or lag. The `leap forward` and `leap filter` properties help compensate:
    
    - **leap forward** [ms]: Predicts where the object will be X milliseconds in the future. Start with small values (10-50ms) and increase as needed.
    - **leap filter** [%]: Smooths the prediction to reduce jitter. Higher values = smoother but less responsive.
    
    These settings are also available on individual [RigidBody](RigidBody.md) nodes for per-object tuning.

---

## Important Notes

!!! info "Data Flow Architecture"
    ```
    OptiTrack Cameras → Motive → NatNet Stream → NatNet2OSC → OSC Stream → SPARCK OptiTrack Node → RigidBody Nodes → Canvas/Model Nodes
    ```

!!! tip "Calibration with Motion Capture"
    You can calibrate [Beamer](Beamer.md) nodes while the projector is attached to a motion capture rigid body. Enable **implement parent transformation** in the Beamer's calibration settings to automatically calculate the local offset from the rigid body to the projector's lens position.

---


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with OptiTrack in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **OptiTrack**

    ---
    * [:octicons-arrow-right-24: RigidBody](RigidBody.md)
    * [:octicons-arrow-right-24: TfmNode](TfmNode.md)
    * [:octicons-arrow-right-24: Canvas](Canvas.md)
    * [:octicons-arrow-right-24: Beamer](Beamer.md)
    * [:octicons-arrow-right-24: SpatialShadery](SpatialShadery.md)

  
-   :material-video-box:{ .lg .middle } __Tutorials__

    ---

    * [:octicons-arrow-right-24: Spatial Augmented Reality](../../start/tutorials/03_Spatial_Augmented_Reality/Spatial_Aumented_Reality.md)
    
    [:octicons-arrow-right-24: Watch Now](../../start/tutorials/videos.md){ .md-button .md-button--primary }

-   :material-forum:{ .lg .middle } __Community__

    ---

    [:octicons-arrow-right-24: Join Now](https://github.com/immersive-arts/Sparck2/discussions){ .md-button .md-button--primary }


</div>

---

!!! question "Need help or want to suggest improvements?"
       
    [:fontawesome-brands-github: Report an issue](../../contributing/reporting-a-bug.md){ .md-button }
    [:fontawesome-brands-github: Improve the Docs](../../contributing/reporting-a-docs-issue.md){ .md-button }


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/OptiTrack.md)*