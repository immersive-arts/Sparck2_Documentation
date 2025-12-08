# CornerPin

Provides controls for mapping textures to an output window by repositioning the image corners.

It is the most simple and easy to use mapping nodes at SPARCK's disposal

<figure markdown>
![CornerPin Node](../../assets/images/nodes/CornerPin.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `edit` | - | sets the focus of the editor window to this node |
    | `reset` | - | resets the corner pins to their default positions |
    | `drawto` | - | set the render group. Capture/Beamer/3DViewer have an equivalent in which you can choose which group to render. |
    | `viewport` | - | select viewport this cornerpin is directly rendered to. Inside the viewport node you should set the mesh to 'off' |
    | `object color` | - | object color |
    | `corner radius` | - | size of the handles |
    | `drawcorners` | - | draws to handles in the final rendering |
    | `layer` | - | depth layer (works best with depth-buffering off) |
    | `smooth` | - | smooth rendering |
    | `blend` | - | enables blendmode |
    | `blendmode` | - | choose blendmode: <li>alphablend <li>add <li>multiply <li>screen <li>exclusion <li>colorblend <li>coloradd <li>alphaadd |
    | `interpolate` | - | use interpolation |
    | `preserve aspect` | - | preserve aspect ratio |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/CornerPin.md)*
