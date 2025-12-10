# Render Passes

!!! info "Advanced Topic"
    This page covers advanced concepts for users who need fine-grained control over rendering order. For most projects, the default settings work well and you don't need to change these values.

The render and transform pass settings define how nodes interact with the SPARCK rendering pipeline. Understanding these concepts is useful when you need precise control over the order of operations within a frame.

## How Passes Work

Each frame in SPARCK is the result of multiple passes — both transformation passes and render passes — that execute in a specific sequence. There are theoretically 30 passes that can happen in each frame.

The pass settings allow you to control:

- When a node's transformation is calculated
- When a node is rendered

## When Do You Need This?

While default settings handle most use cases, there are circumstances where you need to explicitly control pass order.

<div class="grid cards" markdown>

-   ![Render pass example](../assets/images/RenderPass.png)

    **Render Pass Example**
    
    If the result of rendering one node (nodeA) produces a texture that is needed as input for another node (nodeB), nodeA must be rendered before nodeB. The render pass setting controls this sequence.

-   ![Transformation pass example](../assets/images/TransformationPass.png)

    **Transformation Pass Example**
    
    While standard transformation trees evaluate in hierarchy order, some transformation nodes produce matrices that are detached from the tree (like [TfmLookAt] or [TfmMirror]). If transformation treeB relies on the result of a [TfmLookAt] in treeA, treeB needs to execute after treeA.

</div>

## Complete Pass Overview

![Overview of all passes in a frame](../assets/images/RenderPasses.png)

Not all passes can be accessed through node configuration settings. Some are for internal use only, but are shown here for completeness:

<div class="grid cards" markdown>

!!! info "Script Passes"
    * 1. Script-Update
    * 2. Script-Execute

!!! info "Transform Passes"
    * 3. Pre-Transform
    * 4. Pre-Transform Update
    * 5. Transform: pass1
    * 6. Transform: pass2
    * 7. Transform: pass3
    * 8. Post-Transform

!!! info "Misc Passes"
    * 9. Pre Physics
    * 10. Depth
    * 11. Pre Bake
    * 12. Manual Bake
    * 13. Bake
    * 14. Post Bake

!!! info "Manual Render Passes"
    * 15. Render Pass Manual A
    * 16. Render Pass Manual B
    * 17. Render Pass Manual C
    * 18. Render Pass Manual D

!!! info "Render Passes"
    * 19. Pre Render Pass
    * 20. Main Render Pass A
    * 21. Main Render Pass B
    * 22. Main Render Pass C
    * 23. Main Render Pass D
    * 24. Main Render Pass E
    * 25. Main Render Pass F
    * 26. Main Render Pass G
    * 27. Main Render Pass H
    * 28. Beamer Render Pass
    * 29. Post Render Pass
    * 30. Preview Render Pass

</div>

## Tips for Working with Passes

- Start with default settings and only adjust if you encounter ordering issues
- If a texture appears black or outdated, check if the source node renders in an earlier pass
- For transformation dependencies, ensure the source transform evaluates before the dependent one
- Use the lowest pass number that achieves the correct ordering to maintain predictable behavior

[TfmLookAt]: ../reference/nodes/TfmLookAt.md
[TfmMirror]: ../reference/nodes/TfmMirror.md
