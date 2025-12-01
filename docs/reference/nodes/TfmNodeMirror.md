# TfmNodeMirror

The Mirror transformation takes two transformation nodes: One where to set the mirror, and a second one to be mirrored.

the mirrored transformation can also be a Beamer or a Camera -  in this case the node becomes a mirrored Beamer or Camera node and can be used by a Capture node.

<figure markdown>
![TfmNodeMirror Node](../../assets/images/nodes/TfmMirror.png){ width="300" }
</figure> 


## Properties

The following properties can be configured for this node:

=== "Reference"

    | Property | Type | Description |
    |----------|------|-------------|
    | `mirror` | - | mirror node |
    | `mirrored` | - | mirrored node - can also be a Beamer or Camera node |
    | `mode` | - | the kind of mirror transformation |
    | `mirrorplane` | - | set which two axis become the mirror plane |
    | `transformation pass` | - | select transfromation pass |

=== "Workflow"

    1. TBD


---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with TfmNodeMirror in minutes
    
    [:octicons-arrow-right-24: Calibration Guide](../../start/tutorials/201/calibration.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **TfmNodeMirror**

    ---
    * [:octicons-arrow-right-24: TfmNode](TfmNode.md) 
    * [:octicons-arrow-right-24: TfmNodeLookAt](TfmNodeLookAt.md) 
    * [:octicons-arrow-right-24: Beamer](Beamer.md) 
    * [:octicons-arrow-right-24: SceneCamera](SceneCamera.md) 

  
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

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/TfmNodeMirror.md)*
