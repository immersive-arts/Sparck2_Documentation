# ShaderColormap

Can be also used as a texture render pass, for two textures.

<figure markdown>
![ShaderColormap Node](../../assets/images/nodes/ShdrColormap.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `factor` | - | factor |
    | `map dim` | - | color map dimension |
    | `interpolate` | - | use interpolation on the output texture |
    | `enable` | - | use this node as a texture render pass node. |
    | `red` | - | color map for red channel |
    | `green` | - | color map for green channel |
    | `blue` | - | color map for blue channel |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (also used for shader) |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |
    | texture | texture | texture two altered |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderColormap.md)*
