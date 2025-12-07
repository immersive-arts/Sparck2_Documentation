# ShaderRaymarcher

Loads and applies Raymarching GLSL shaders in 3D space. Shaders of the likes you can find on ShaderToy.org

<figure markdown>
![ShaderRaymarcher Node](../../assets/images/nodes/ShdrReyMarcher.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `shader` | (drag'n drop) | shader file. Needs to be in the MaxJitter format for GLSL shaders |
    | `filewatch` | - | use filewatch |
    | `camera` | - | BoxMapCamera node. From here are the rays cast outward. |
    | `editor name` | - | choose prefered editor |
    | `edit` | - | open shader with chosen editor |
    | `time` | - | use time |
    | `speed` | - | set speed |
    | `reset time` | - | resets time to zero |
    | `reference` | - | additional transformation node to refer to. |
    | `position` | - | local translations |
    | `rotation` | - | local rotation |
    | `scale` | - | local scale |
    | `texture one` | - | open input for additional texture |
    | `texture two` | - | open input for additional texture |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | messages      | direct access to internal properties   |
    | texture    | texture       | texture applied to ...                 |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | messages      | direct access to internal properties   |
    | texture    | texture       | texture applied to ...                 |


---

## Important Notes

!!! warning "Implementation: Difficult"
    
    Unfortunately it is not a simple copy-paste process to transform a ShaderToy-shader into a RayMarching-node shader. While 95% of the code can usually be reused, the shader needs to be embedded inside a Max-Jitter style GLSL shader file, plus some adjustments need to be made in order make a shader to work in a 3d context.
    Check out the SparckExamples for a selection of about 25 of my favourite shadertoy shaders which I already translated for this node.

!!! info "File Locations"
    
    ```
    ~/_assets/_shaders/_raymarch/     # glsl files
    ```

---


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with ShaderRaymarcher in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **ShaderRaymarcher**

    ---
    * [:octicons-arrow-right-24: BoxMapCamera](BoxMapCamera.md) 
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


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderRaymarcher.md)*
