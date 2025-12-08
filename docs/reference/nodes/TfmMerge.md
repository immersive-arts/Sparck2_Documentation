# TfmMerge

The node merges different transformational parts of two differen transformation nodes into one.

<figure markdown>
![TfmMerge Node](../../assets/images/nodes/TfmMerge.png){ width="300" }
</figure> 


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

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/TfmMerge.md)*
