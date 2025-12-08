# SpatialShadery

This shader is spatialy aware and is used for multi projector installation where the use of softedge is necessary.

It is mainly used for Spatial Augmented Reality installations where there is the need for the creation of dynamic softedges.

<figure markdown>
![SpatialShadery Node](../../assets/images/nodes/SpatialShadery.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `shader` | - | the shader type: <li>'edge' is used in combination with the BlendSoftedge node <li>'edge & blend' calculates softedge combined with the blending. |
    | `project to` | - | projection type: <li>'canvas' is used to render the projector weights <li>'baked texture' implements all render passes for generating the final pixel. |
    | `BeamerA-F` | - | Select the Camera/Beamer from where to project. |
    | `occlusion` | - | tries to adjust for occlusions of objects. |
    | `depth dim` | - | depth texture size of the occlusion pass. |
    | `projection` | - | use only front, back or both side of the canvas |
    | `angle mode` | - | angle differentiation: <li>'viewray' will differentiate based on the angle between the surface normal and the viewray, <li>'direction' will differentiate based on the angle between the surface normal and the camera direction |
    | `spread` | - | spread factor will increase the differentiation between overlapping projections |
    | `distance` | - | use distance as an additional differentiator. It will show its influence when the spread is increased. (0 = no influence) |
    | `blend bg` | - | enables blending with the background |
    | `interpolation` | - | interpolation |
    | `angle limit` | - | angle limit (how much of the visible surface area is considered, 0 = no limit) |
    | `angle falloff` | - | angle-limit falloff (defines the size of the angle blend transition at the angle limit) {/sparck/node ::<nodename>::property::angleFalloff <float>} |
    | `bevel size` | - | bevel size |
    | `bevel curve` | - | bevel curve |
    | `bevel round` | - | use rounded bevel |
    | `offcolor` | - | surface color of uncovered areas |
    | `output` | - | display mode of the model on which this shader is applied onto. <li>'result' shows the final texture <li>'content' shows the input texture <li>'mask' shows the Beamer weights |
    | `power` | - | blend power - softegde blend parameter |
    | `luminance` | - | luminance - softegde blend parameter |
    | `gradient curve` | - | adjusts the softedge curve |
    | `gamma` | - | gamma correction |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture list with depth pass |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/SpatialShadery.md)*
