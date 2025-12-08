# ShaderTexStitch

Can be used for multiple single textures and CubeMaps.

<figure markdown>
![ShaderTexStitch Node](../../assets/images/nodes/ShdrTexStitch.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `stitches` | - | number of textures to stitch |
    | `width` | - | width of final texture |
    | `height` | - | height of final texture |
    | `render pass` | - | render pass |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (left) |
    | texture | texture | texture two (front) |
    | texture | texture | texture three (right) |
    | texture | texture | texture four (back) |
    | texture | texture | texture five (top) |
    | texture | texture | texture six (bottom) |
    | texture | texture | texture list |
    | boxmap | boxmap | boxmap (list) |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | stitched | texture | stitched texture |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderTexStitch.md)*
