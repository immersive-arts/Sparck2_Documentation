# Texture

Texture node can load a variety of image files: TIFF, GIF, JPEG, PNG

<figure markdown>
![Texture Node](../../assets/images/nodes/Texture.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `file` | (drag'n drop) | load image file |
    | `default` | - | default texture if no texture is loaded |
    | `render pass` | - | render pass |
    | `flip` | - | flips texture |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | image | texture | image texture |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/Texture.md)*
