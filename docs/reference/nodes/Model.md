# Model

Reads and draws a variety of 3D model formats such as OBJ and Collada (see complete list under notes)

Only tesselated polygons are drawn and surfaces that are not tesselated are converted before drawing

the model node is primarily used for drawing models, while its sister-node 'Canvas' should be used for virtual projections.

<figure markdown>
![Model Node](../../assets/images/nodes/Model.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `file` | drag n' drop | select the model file to draw. the file needs to be located inside the ~/_assets/_model folder. you can also drag'n drop file, which will be copied into the _model folder and autmatically selected. |
    | `parent` | - | parent transformation node |
    | `RenderGroup` | - | set the render group. Capture/Beamer/3DViewer have an equivalent in which you can choose which group to render. |
    | `position` | (local transformation) | position x y z |
    | `rotation` | (local transformation) | rotation x y z |
    | `scale` | (local transformation) | scale x y z |
    | `normalize` | - | normalizes the model |
    | `shader` | - | link to Shader Node |
    | `material` | - | link to Material Node |
    | `defaut texture` | - | default texture |
    | `texture map` | - | generates texture map |
    | `materialmode` | - | choose material mode |
    | `autmaterial` | - | can improove rendering result |
    | `color` | - | object color |
    | `diffuse` | - | diffuse color |
    | `specular` | - | specular color |
    | `ambient` | - | ambient color |
    | `emission` | - | emission color |
    | `lighting` | - | lets the model react to light sources |
    | `shadowcaster` | - | lets the model cast shadows |
    | `depth` | - | depth buffering |
    | `layer` | - | depth layer (works best with depth-buffering off) |
    | `smooth` | - | smooth rendering |
    | `angle` | - | edge angle for smooth rendering |
    | `blend` | - | enables blendmode |
    | `blendmode` | - | choose blendmode: <li>alphablend <li>add <li>multiply <li>screen <li>exclusion <li>colorblend <li>coloradd <li>alphaadd |
    | `displaylist` | - | enables displaylist - can speed up drawing |
    | `cachemode` | - | choose cachemode: <li>vertexarray <li>displaylist <li>vertexbuffer <li>immediate |
    | `cullface` | - | choose cullface: <li>0=Off <li>1=Back <li>2=Front |
    | `drawgroup` | - | if the model has drawgroups, choose. |
    | `polymode` | draw.. | <li>polygons - only faces <li>lines - only lines <li>points - only vertices |
    | `antialias` | - | use antialias |
    | `axes` | - | show axes of the models origin |
    | `nodeaxes` | - | if modesl has nodes, show axes of the nodes |
    | `matrixouput` | - | ouputs the faces as a jitter matrix on the dumpout outlet |
    | `fileWatch` | - | watches the model file. when it changes, it will be autmatically reloaded |
    | `publish transformation` | - | publishes this mode transformation as a transformation node |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | main | texture | main texture |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/Model.md)*
