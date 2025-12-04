# TfmNodeInfo

This node allows to get info about a transformation hierarchy.

<figure markdown>
![TfmNodeInfo Node](../../assets/images/nodes/TfmNodeInfo.png){ width="300" }
</figure> 


## Properties

The following properties can be configured for this node:

=== "Reference"

    | Property | Type | Description |
    |----------|------|-------------|
    | `parent` | - | parent transformation node |
    | `RenderGroup` | - | set the render group. Capture/Beamer/3DViewer have an equivalent in which you can choose which group to render. |
    | `draw position` | - | draws the position of the node |
    | `draw rotation` | - | draws the rotation of the node |
    | `draw parent link` | - | draws the link to the parent node |
    | `color` | - | display color |
    | `dump1` | worldpos, worldquat, worldscale | sends this infos to the 'dump' outlet |
    | `dump2` | parentpos, parentquat, parentscale | sends this infos to the 'dump' outlet |
    | `dump3` | local pos, quat, scale | sends this infos to the 'dump' outlet |
    | `dump4` | worldtransformation matrix | sends this infos to the 'dump' outlet |
    | `dump5` | inverse worldtransformation matrix | sends this infos to the 'dump' outlet |
    | `low freq dump` | - | uses the low frequency metro (can be set inside preferences) |

=== "Workflow"

    1. TBD


---


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with TfmNodeInfo in minutes
    
    [:octicons-arrow-right-24: Project Examples](../../start/examples/project_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **TfmNodeInfo**

    ---
    * [:octicons-arrow-right-24: TfmNode](TfmNode.md) 
    * [:octicons-arrow-right-24: TfmNodeMirror](TfmNodeMirror.md) 
    * [:octicons-arrow-right-24: TfmNodeLookAt](TfmNodeLookAt.md) 
    * [:octicons-arrow-right-24: OscMessage](OscMessage.md) 

  
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

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/TfmNodeInfo.md)*
