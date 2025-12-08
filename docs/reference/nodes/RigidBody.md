# RigidBody

The Rigidbody Node represents a transformation (position, rotation and scale) in 3D space received from the [OptiTrack] node. It can be connected to almost all nodes that have a representation in 3D space.

It can also be used to establish parent-child relationships in a hirarchical transformation structure, where child nodes are transformed relative to their parents

<figure markdown>
![TfmNode Node](../../assets/images/nodes/RigidBody.png){ width="300" }
</figure> 


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

!!! info Connection and Stream indicators
    The two boxes behind the 'stream' property indicate if there is a connection to the OptiTrack system and if the data is alive.

[OptiTrack]: ./OptiTrack.md

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

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/TfmNode.md)*
