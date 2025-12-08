# Hook

A helper to get Jitter objects draw and tranform with SPARCKS render and transform nodes

<figure markdown>
![Grid Node](../../assets/images/nodes/Hook.png){ width="300" }
</figure> 


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

*Last updated: 2025-12-04 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/Hook.md)*
