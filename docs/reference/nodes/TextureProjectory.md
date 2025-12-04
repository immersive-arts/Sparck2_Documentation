# TextureProjectory

Projects textures outwards from the location of the Camera

This is a shader and can be applied to any model node.

<figure markdown>
![TextureProjectory Node](../../assets/images/nodes/TextureProjectory.png){ width="300" }
</figure> 


## Properties

The following properties can be configured for this node:

=== "Reference"

    | Property | Type | Description |
    |----------|------|-------------|
    | `shader` | - | choose between the different projection types. <li>'single' to project one texture <li>'multiblend' to project multiple textures <li>'360VR.single' project equirectangular textures. For this the camera needs to be a BoxMapCamera <li>'360VR.multiblend' project normal and equirectangular textures. To project a equirectangular texture, the camera needs to be a BoxMapCamera <li>'boxmap' for projecting boxmap textures |
    | `project to` | - | <li>'canvas' to us it as a standard shader <li>'bake texture' to bake the result into a texture. |
    | `projectionA-F` | - | select the SceneCamera or BoxMapCamera |
    | `3d viewer` | - | display mode of the model on which this shader is applied onto. <li>'Textured' shows the projected texture(s) <li>'Colored' shows the projections in colors <li>'Overlap' shows the amount of overlap <li>'Map' shows the differentiation <li>'BeamX' shows projection X |
    | `project on` | - | Onto which face of the model this texture is projected: <li>'back' <li>'both sides' <li>'front' |
    | `blend bg` | - | benables blending with the background |
    | `use bgcolor` | - | use this color if no specific background texture is used |
    | `bgcolor` | - | color if no projected texture reaches the surface |
    | `angle mode` | - | angle differentiation: <li>'viewray' will differentiate based on the angle between the surface normal and the viewray, <li>'direction' will differentiate based on the angle between the surface normal and the camera direction. |
    | `spread` | - | spread factor will increase the differentiation between overlapping projections (1 = full spread) |
    | `distance` | - | use distance as an additional differentiator. It will show its influence when the spread is increased. (0 = no influence) |
    | `angle limit` | - | angle limit, how much of the visible surface area is considered (0 = no limit) |
    | `angle falloff` | - | size of falloff gradient at the angle limit |
    | `bevel size` | - | bevel size. it creates a gradient falloff defined by the frustum cone of the camera |
    | `bevel curve` | - | bevel gradient shape |
    | `bevel rounded` | - | use rounded bevel |
    | `interpolation` | - | interpolation correction. if strange artefacts start to appear, raise the value until the artefacts disappear. the artefacts are a result of interpolation errors between the vertex and fragment shader and occur close to the local x-y plane of the camera. increasing the subdivisions of the model can help, too |

=== "Workflow"

    1. TBD


---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with TextureProjectory in minutes
    
    [:octicons-arrow-right-24: Project Examples](../../start/examples/project_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **TextureProjectory**

    ---
    * [:octicons-arrow-right-24: SceneCamera](SceneCamera.md) 
    * [:octicons-arrow-right-24: BoxMapCamera](BoxMapCamera.md) 
    * [:octicons-arrow-right-24: SceneCapture](SceneCapture.md) 

  
-   :material-video-box:{ .lg .middle } __Tutorials__

    ---
    
    [:octicons-arrow-right-24: Watch Now](../../start/tutorials/videos.md){ .md-button .md-button--primary }

-   :material-forum:{ .lg .middle } __Community__

    ---

    [:octicons-arrow-right-24: Join Now](https://github.com/immersive-arts/Sparck2/discussions){ .md-button .md-button--primary }


</div>

---

!!! question "Need help or want to suggest improvements?"
       
    [:fontawesome-brands-github: Report an issue](../../contributing/reporting-a-bug.md){ .md-button }
    [:fontawesome-brands-github: Improve the Docs](../../contributing/reporting-a-docs-issue.md){ .md-button }


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/TextureProjectory.md)*
