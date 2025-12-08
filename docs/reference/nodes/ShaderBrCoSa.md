# ShaderBrCoSa

Can be also used as a texture render pass, for two textures.

<figure markdown>
![ShaderBrCoSa Node](../../assets/images/nodes/ShdrBrCoSa.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `brightness` | - | brightness amount |
    | `contrast` | - | contrast amount |
    | `saturation` | - | saturation amount |
    | `alpha` | - | alpha amount |
    | `average luma` | - | average luma amount |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |
    | texture | texture | texture two altered |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderBrCoSa.md)*
