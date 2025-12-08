# ShaderTexOP

The TextureOP node applies either a binary operator to two input textures, or a unary operator to the left input texture

<figure markdown>
![ShaderTexOP Node](../../assets/images/nodes/ShdrOP.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `mode` | - | operation mode (see details down below) |
    | `in1scale` | - | scale scalar for texture left |
    | `in2scale` | - | scale scalar for texture right |
    | `in1offset` | - | offset scalar for texture left |
    | `in2offset` | - | offset scalar for texture right |
    | `outScale` | - | output offset |
    | `enable` | - | use node for a texture effect render pass |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | result | texture | result of 1 op 2 (left op right) |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderTexOP.md)*
