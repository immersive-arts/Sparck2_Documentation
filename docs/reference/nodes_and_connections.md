# Nodes & Connections

SPARCK Nodes can be connected in several ways, depending on what you need to achieve. This page explains the different connection mechanisms available.

## Connection Types Overview

1. **Patch cords** — for passing textures between SPARCK nodes
2. **Linking** — Transform, shader & material parenting for hierarchical relationships
3. **Render groups** — for controlling which content is rendered where and when
4. **File selection** — for nodes that load external assets

---

## Patch Cords (Textures)

The most familiar way to connect SPARCK Nodes is with [patch cords](https://docs.cycling74.com/userguide/patch_cords/).

Between SPARCK nodes, patch cords are primarily used to pass textures. Other inlets and outlets are usually for interacting with the broader Max environment (control values, triggers, etc.).

**Use patch cords when:** You want to send a texture from one SPARCK Node to another.

## Linking

### Transformations

![Transformation chain example](../assets/images/core/NodeTransformationChain.png)

Nodes can be linked via their transformation hierarchy. In the example above, the **Model** node is parented to a **TfmNode**, which in turn is parented to a **TfmPathNode**.

### Cameras, Shaders & Materials

The same linking mechanism is used to attach:

- **Shaders** — apply visual effects
- **Materials** — apply surface properties to model nodes
- **Cameras** — apply camera properties to capture nodes

**Use transformation parenting when:** You want one node's position, rotation, or scale to be relative to another, 

**Use shader and material linking** when you want to apply shaders/materials to content nodes.

**Use camera linking** to tell capture nodes (see also below) from where to look at the 3d scene.

!!! tip "Refreshing menus"
    The node menus list all valid nodes you can connect to. If the menu doesn't show a node you expect, click the **refresh** button next to the menu to let SPARCK rescan for valid selections.

---

## Render Groups

Render groups control how content nodes and capturing nodes work together to create rendered output.

### Content Nodes

![Content nodes render group interface](../assets/images/RenderGroup_Content.png)

Content nodes place objects in the 3D scene to be rendered. These include:

- [Model]
- [Canvas]
- [Grid]
- [CornerPin]
- [SkyBox]
- [MeshWarp]

For content nodes, the render group interface indicates *where* the content is drawn. This property is called **drawto**.

### Capturing Nodes

![Capturing nodes render group interface](../assets/images/RenderGroup_Renderer.png)

Capturing nodes render 3D scenes from a specific viewpoint (defined by a camera node). These include:

- [SceneCapture][^1]
- [BoxMapCapture][^2]
- [Beamer]

For capturing nodes, the render group interface indicates *which groups* are rendered. This property is called **capture**.

### Other Render Group Uses

Some nodes use render groups for different purposes. For example, [SceneCamera] has a **gizmo** render group that controls where the camera gizmo is drawn in the 3D viewer.

---

## Files

Some nodes load external files such as textures, models, or videos. If valid files are available in the expected folder, they appear in the node's file menu.

**Use files when:** You need to load assets like 3D models, images, videos, or shaders.

!!! tip "Missing files?"
    If your files don't appear in the menu, press **refresh** to rescan the project folders. Make sure your files are in the correct subfolder with a supported file type. Check the node's tooltip for folder and format requirements.

---

## Connecting Jitter Objects to SPARCK

It's possible to render existing Jitter patches inside the SPARCK ecosystem. Use the [Hook] node for this purpose — it ensures your Jitter objects are drawn into the correct context and render group.

!!! info "Advanced: Render contexts"
    For deeper integration with Jitter, see [Render Contexts](render_contexts.md) to understand how SPARCK manages its internal rendering pipeline.

[LookAtCamera]: ../reference/nodes/LookAtCamera.md
[Grid]: ../reference/nodes/Grid.md
[Hook]: ../reference/nodes/Hook.md
[SkyBox]: ../reference/nodes/SkyBox.md
[Canvas]: ../reference/nodes/Canvas.md
[Model]: ../reference/nodes/Model.md
[SceneCamera]: ../reference/nodes/SceneCamera.md
[SceneCapture]: ../reference/nodes/SceneCapture.md
[BoxMapCamera]: ../reference/nodes/BoxMapCamera.md
[BoxMapCapture]: ../reference/nodes/BoxMapCapture.md
[Beamer]: ../reference/nodes/Beamer.md
[CornerPin]: ../reference/nodes/CornerPin.md
[MeshWarp]: ../reference/nodes/MeshWarp.md

[^1]: —> needs in turn a link to a [SceneCamera] or [LookAtCamera]
[^2]: —> needs in turn a link to a [BoxMapCamera]