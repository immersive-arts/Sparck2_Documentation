# QueScript

Que Script is SPARCK own super powerfull [scripting language](../quescript/QS1-Introduction.md).

The implementation of QueScript inside SPARCK follows certain idiosyncracies that are described down below.

<figure markdown>
![QueScript Node](../../assets/images/nodes/QueScript.png){ width="300" }
</figure> 


## Properties

The following properties can be configured for this node:

=== "Reference"

    | Property | Type | Description |
    |----------|------|-------------|
    | `scriptfile` | - | load and execute que script |
    | `fileWatch` | - | reloads the script file if it has changed by an external editor. Usually a good idea while you are editing. |
    | `ques` | - | lists all ques inside the script and allows you to manually execute the chosen one. |
    | `progress..` | - | shows how each que is progressing |
    | `pause / play` | - | pauses / plays the execution |
    | `stop` | - | stops the execution |
    | `Editor` | - | select your prefered editor or add your own. |
    | `edit` | - | edit the loaded file. You can set your prefered editor inside properties. |
    | `update mode` | - | there are two modes to choose: <li>automatic will update the script with each frame-pass. <li>custom will allow you to set your own update frequency. |
    | `frequency` | - | custom update frequency |
    | `osc send` | - | Que script can create OSC messages, but needs an OscSend node to send them to. |
    | `debug` | - | will output debug information to the console |

=== "Workflow"

    1. TBD


---

## Important Notes


!!! info "File Locations"
    
    ```
    ~/_assets/_scripts/_ques     # Que files
    ```

---


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with QueScript in minutes
    
    [:octicons-arrow-right-24: Project Examples](../../start/examples/project_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **QueScript**

    ---
    * [:octicons-arrow-right-24: OscSend](OscSend.md) 

  
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

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/QueScript.md)*
