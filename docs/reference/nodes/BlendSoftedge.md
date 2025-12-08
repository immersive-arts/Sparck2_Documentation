# BlendSoftedge

Blends color textures with softedge textures

<figure markdown>
![BlendSoftedge Node](../../assets/images/nodes/BlendSoftedge.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `ouput` | - | output mode: <li>result shows the final blend <li>texture one shows the color texture <li>texture two shows the blend texture |
    | `power` | - | blend power |
    | `luminance` | - | blend luminance |
    | `output` | - | enable texture shader pass. the outlet that appears below will output the resulting texture. |
    | `gradient` | - | custom gradient curve |
    | `gamma` | - | gamma correction |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | main | texture | main texture (content texture) |
    | mask | texture | mask texture (alpha mask) |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | blended | texture | blended texture |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/BlendSoftedge.md)*
