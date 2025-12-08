# ShaderTexZoom

Can be also used as a texture render pass, for two textures.

<figure markdown>
![ShaderTexZoom Node](../../assets/images/nodes/ShdrZoom.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `src scale` | - | source x and y scale |
    | `src pos` | - | source x and y position |
    | `dest scale` | - | dest x and y scale |
    | `dest pos` | - | dest x and y position |
    | `interpolate` | - | use interpolation on output texture |
    | `texture one` | - | use this node as texture render pass |
    | `texture two` | - | use this node as texture render pass |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (also used for texture fx) |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |
    | texture | texture | texture two altered |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderTexZoom.md)*
