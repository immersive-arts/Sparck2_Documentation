# Render Contexts

!!! info "Advanced Topic"
    This page covers the internal rendering architecture of SPARCK. Understanding render contexts is helpful when integrating complex Jitter patches or troubleshooting advanced rendering scenarios. For typical usage, you don't need to modify these settings.

SPARCK uses multiple Jitter render contexts internally to manage different aspects of the rendering pipeline.

## Context Overview

![Diagram of SPARCK render contexts](../assets/images/RenderContexts.png)

SPARCK maintains 8 render contexts in the background:

| Context | Purpose |
|---------|---------|
| **Sparck-Context** | Main context where content is rendered (includes your Jitter objects when using [Hook]) |
| **Viewer-Context** | Displays the 3DViewer |
| **Editor-Context** | Used for editor interfaces |
| **Output-Context 1–4** | Managed by [Window] nodes for final output |
| **Special-Context** | Handles texture inputs like Video or Spout/Syphon |

## Output Contexts and Projector Count

The 4 output contexts are where the final render passes happen before output to windows. However, this doesn't limit you to 4 projectors:

- Each [Window] can be split into up to 24 [Viewport] sections
- This allows for up to **96 theoretical screens** across all windows
- Actual capacity depends on your graphics card's capabilities

## When Contexts Matter

Understanding contexts becomes important when you:

- Integrate existing Jitter patches using the [Hook] node
- Need to render to specific outputs
- Debug rendering issues where content appears in the wrong place
- Work with external texture sources (Spout, Syphon, video)

## Using the Hook Node

The [Hook] node is designed to bridge standard Jitter objects into the SPARCK ecosystem. It ensures your Jitter objects render into the correct context and render group without manual context management.

!!! tip "Jitter Integration"
    When connecting Jitter objects to SPARCK, always use the [Hook] node rather than trying to specify contexts manually. This ensures compatibility with SPARCK's rendering pipeline.

[Hook]: ../reference/nodes/Hook.md
[Window]: ../reference/nodes/Window.md
[Viewport]: ../reference/nodes/ViewPort.md
