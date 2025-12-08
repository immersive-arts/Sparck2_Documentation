# ShaderAnaglyph

The TextureAnaglyph node takes two input textures, usually a stereo pair, and merges them into a anaglyph texture

The TextureAnaglyph node can be either applied as a shader to a 3d object or a ViewPort node, or used as an explicit texture renderpass to create the anaglyph texture.

<figure markdown>
![ShaderAnaglyph Node](../../assets/images/nodes/ShdrAnaglyph.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `contrast` | - | contrast between left and right |
    | `deghost` | - | deghosting value |
    | `stereo` | - | stereo texture spread |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture left |
    | texture | texture | texture right |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderAnaglyph.md)*
