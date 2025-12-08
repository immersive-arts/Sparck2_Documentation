# TfmNodePath

This node allows to load animation paths exported from blender.

The file is created inside Blender with the LedStrip-Exporter script.

<figure markdown>
![TfmNodePath Node](../../assets/images/nodes/TfmNodePath.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `drawto` | - | set the render group. Capture/Beamer/3DViewer have an equivalent in which you can choose which group to render. |
    | `file` | - | animation path file |
    | `fileWatch` | - | reload animation path file if it was changes |
    | `segment` | - | segment inside pathfile |
    | `closeSegment` | - | force closing the segement if it has a gap between the first and the last vertice |
    | `playbar` | - | relative position on path. Best animated with QueScript |
    | `parent` | - | parent transformation node |
    | `position` | (local transformation) | position x y z |
    | `rotation` | (local transformation) | rotation x y z |
    | `scale` | (local transformation) | scale x y z |
    | `object color` | - | display color |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/TfmNodePath.md)*
