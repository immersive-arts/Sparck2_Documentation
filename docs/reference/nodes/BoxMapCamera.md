# BoxMapCamera

BoxMapCamera creates rig for a BoxMapCapture Node

BoxMapCamera represents the virtual camera chassis, while the BoxMapCapture represents the virtual film: For capturing the textures the BoxMapCapture is needed.

A BoxMap is similar to an OpenGL-CubeMap, but instead consists of a list of 6 unique textures, each representing the view of one box side. The term BoxMap is used in order to make sure it is not confused with a CubeMap.

<figure markdown>
![BoxMapCamera Node](../../assets/images/nodes/BoxMapCamera.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `directions` | - | sets which of the 6 Box-sides need to rendered |
    | `near` | - | near frustum clip |
    | `far` | - | far frustum clip |
    | `parent` | - | parent transformation node |
    | `position` | (local transformation) | position x y z |
    | `rotation` | (local transformation) | rotation x y z |
    | `scale` | (local transformation) | scale x y z |
    | `gizmo` | - | show Camera icon on 3DViewer |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/BoxMapCamera.md)*
