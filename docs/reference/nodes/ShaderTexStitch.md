# ShaderTexStitch

Can be used for multiple single textures and CubeMaps.

<figure markdown>
![ShaderTexStitch Node](../../assets/images/nodes/ShdrTexStitch.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `stitches` | - | number of textures to stitch |
    | `width` | - | width of final texture |
    | `height` | - | height of final texture |
    | `render pass` | - | render pass |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (left) |
    | texture | texture | texture two (front) |
    | texture | texture | texture three (right) |
    | texture | texture | texture four (back) |
    | texture | texture | texture five (top) |
    | texture | texture | texture six (bottom) |
    | texture | texture | texture list |
    | boxmap | boxmap | boxmap (list) |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | stitched | texture | stitched texture |


---

div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with ShaderTexStitch in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **ShaderTexStitch**

    ---
    * [:octicons-arrow-right-24: BoxMapProjection](BoxMapProjection.md) 
    * [:octicons-arrow-right-24: BoxMapCapture](BoxMapCapture.md) 
    * [:octicons-arrow-right-24: Texture](Texture.md) 

  
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
    
*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderTexStitch.md)*
