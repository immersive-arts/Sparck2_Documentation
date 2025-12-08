# BoxMapCapture

The BoxMapCapture Node is needed to render the view from a BoxMapCamera.

While BoxMapCamera represents the virtual camera chassis, the BoxMapCapture represents the virtual film: For capturing the textures the BoxMapCapture is needed.

A BoxMap is similar to an OpenGL-CubeMap, but instead consists of a list of 6 unique textures, each representing the view of one box side. The term BoxMap is used in order to make sure it is not confused with a CubeMap.

<figure markdown>
![BoxMapCapture Node](../../assets/images/nodes/BoxMapCapture.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `capture` | - | render group to draw. Model/Canvas/MeshWarp/Grid have an equivalent in which you can choose which group to draw to. |
    | `parent` | - | select the camera node from where to render. |
    | `dim` | - | sets the texture size of this render pass. Try using sizes like 256x256, 512x512, 1024x1024, 2048x2048. |
    | `bgcolor` | - | the background color |
    | `mode` | - | the result of the renderpass. 'split' will render our all the different directions as seperate textures, 'line' renders then out in one texture [-x, -z, x, z, -y, y] and 'cross' in one texture in the shape of the cubmap cross |
    | `pass` | - | Renderpass. This defines when in a frame-pass (see reference) this Capure node does the rendering. A manual renderpass will only be executed right after loading a project or when pressing the 'manual renderpass button' in the main menu. |
    | `blend` | - | allows blending. |
    | `antialias` | - | antialiases the output. |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | left | texture | left texture |
    | front | texture | front texture |
    | right | texture | right texture |
    | back | texture | back texture |
    | top | texture | top texture |
    | bottom | texture | bottom texture |
    | boxmap | boxmap | boxmap (texture list &lt;texL> &lt;texF> &lt;texR> &lt;texB> &lt;texT> &lt;texG>) |
    | texture | texture | texture list with only active textures (texture &lt;tex1> ...) |
    | single | texture | single texture with all box sides backed together |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/BoxMapCapture.md)*
