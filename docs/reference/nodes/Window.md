# Window

Used to display the rendered result to an output device like a screen or projector.

The window node can slice its frame into (so called) viewports, arranged in rows and columns. Each slice (viewport) can be addressed with a ViewPort-node.

With the display-setup tool you can easily define the windows output size and postion relative to the desktop display.

<figure markdown>
![Window Node](../../assets/images/nodes/Output.png){ width="300" }
</figure> 


## Properties

The following properties can be configured for this node:

=== "Reference"

    | Property | Type | Description |
    |----------|------|-------------|
    | `position` | - | switch between the 'ouput' position and the 'desktop' position |
    | `columns and rows` | - | slice the window into the designated amount of rows (max 2) and columns (max 12) |
    | `vsync` | - | tries to sync the output framerate with the displays update frequency. not recomended. |
    | `antialias` | - | render with antialiasing. |
    | `floating` | - | for 'desktop': window will always stay on the foreground |
    | `border` | - | for 'desktop': when selected the windows borders are shown when positioned on the desktop. |
    | `escape` | - | for 'output': when pressing 'esc' the Window will swithc to 'desktop' position. |
    | `interact` | - | exposes an internal transformation node for direct 3d handling similar to the 3DViewer. The transformation node needs to be attached to a Camera-node, and its Capture-node renders out to this Window. |
    | `display` | - | opens the display-settings tool to define the 'output' position of this window. |
    | `desktop` | - | the 'desktop' position of this window. Is set automatically by draging and resizing the window |
    | `output` | - | the 'output' position of this window. Is set via display settings. |

=== "Workflow"

    1. TBD


---


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with Window in minutes
    
    [:octicons-arrow-right-24: Calibration Guide](../../start/tutorials/201/calibration.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **Window**

    ---
    * [:octicons-arrow-right-24: ViewPort](ViewPort.md) 
    * [:octicons-arrow-right-24: Monitor](Monitor.md) 

  
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

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/Window.md)*
