# ShaderPointCloud

Renders ShaderPointClouds in the format of an RGB-D image, where the image is split into the rgb information and the depth encoded information. Works best with [Space-Stream], a python based app that takes live feed from the most common 3d cameras and transfers it into the rgb-d format. [Space-Stream] can stream the video directly via [SpoutReceiver] or [SyphonReceiver] to a SPARCK project. 

![RGB-D](../../assets/images/nodes/ShaderPointCloud_frame-uniform-hue.png)

[Space-Stream]: https://github.com/cansik/space-stream
[SpoutReceiver]: SpoutReceiver.md
[SyphonReceiver]: SyphonReceiver.md

<figure markdown>
![Canvas Node](../../assets/images/nodes/ShaderPointCloud.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `drawto` | - | set the render group. Capture/Beamer/3DViewer have an equivalent in which you can choose which group to render. |
    | `resolution` | [px] | resolution of the rgb-image (half the width of the received stream) |
    | `encoded` | - | recomended format is 'uniform hue'. choose from 'linear 8bit', 'linear 16bit', 'uniform hue', 'inverse hue', 'hsv' |
    | `point size` | [px] | size of a point in the cloud |
    | `hole detect` | - | tries to fix holes in the point cloud |
    | `principal point` | - | intrinsic lense setting |
    | `focal point` | - | intrinsic lense setting |
    | `distance min` | - | min distance from where the depth encoding starts |
    | `distance max` | - | max distance to where the depth encoding stops |
    | `cull near` | - | min distance from where the points are rendered |
    | `cull far` | - | max distance to where the points are rendered |
    | `frontface` | draw.. | <li>polygons - only faces <li>lines - only lines <li>points - only vertices |
    | `backface` | draw.. | <li>polygons - only faces <li>lines - only lines <li>points - only vertices |
    | `cullface` | - | choose cullface: <li>0=Off <li>1=Back <li>2=Front |
    | `parent` | - | parent transformation node |
    | `position` | (local transformation) | position x y z |
    | `rotation` | (local transformation) | rotation x y z |
    | `scale` | (local transformation) | scale x y z |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (also used for shader) |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|


---

## Important Notes

!!! warning "Parameter Matchings"

    To have the best results receiving ShaderPointClouds encoded in the rgb-d format, you have to make sure the intrisic and depth properties are a match:

    * Resolution
    * Principle Points
    * Focal Point
    * Min Distance
    * Max Distance

    [Space-Stream] stores some of the properties normalized, while this shader takes them absolute. you can get to the absolute values by disabling 'normalized intrinsics' in the UI of [Space-Stream].

---

!!! info Reference

    The algorithm of this shader is base on this intel [whitepaper](https://dev.realsenseai.com/docs/depth-image-compression-by-colorization-for-intel-realsense-depth-cameras). Though at the time of our reading we detected a bug in their math - this is in this implementation corrected.


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with ShaderPointCloud in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **Canvas**

    ---
    * [:octicons-arrow-right-24: SpoutReceiver](SpoutReceiver.md) 
    * [:octicons-arrow-right-24: SyphonReceiver](SyphonReceiver.md) 
  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/Canvas.md)*
