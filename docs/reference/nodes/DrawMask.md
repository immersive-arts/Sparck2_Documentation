# DrawMask

Loads and saves texures. The modification of textures is only black and white. The main purpose is the use for mask in combination with Texture-Effect-Nodes.

The saved texture will be a PNG.

<figure markdown>
![DrawMask Node](../../assets/images/nodes/DrawMask.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `image file` | - | load image (TIFF. GIF, JPEG, PNG) and save mask |
    | `filewatch` | - | reloads texture automatically if file changes. |
    | `dimension` | - | default dimensions. used to create default mask. |
    | `planes` | - | The loaded image is a black and white-texture. This has to be transformed into a ARGB-texture and the planes defines how the black/white values are set for a 4-channel ARGB texture. <li>'mmmm' will set all channels to the bw-values. <li>'mwww' will only set the Alpha-channel to the bw-value, while the RGB-channels will be set to white (1.0) <li>'wmmm' will set the Alpha-channel to white and the RGB-channels to the bw-value. |
    | `edit` | - | sets the focus of the editor window to this node |
    | `render pass` | - | render pass. default is a manual render pass since the loaded texture needs only passed on once because of its static nature. |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture out |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/DrawMask.md)*
