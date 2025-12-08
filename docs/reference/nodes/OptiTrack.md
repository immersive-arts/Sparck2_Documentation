# OptiTrack

Optitrack is a commercialy available optical tracking system.

In order to use it with SPARCK, you need the NatNet2Osc App.

<figure markdown>
![OptiTrack Node](../../assets/images/nodes/OptiTrack.png){ width="300" }
</figure> 


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

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/OptiTrack.md)*
