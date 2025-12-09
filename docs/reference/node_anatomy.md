# Node Anatomy

SPARCK Nodes are Max abstractions with a standardized UI and behavior. Regardless of their specific function (model, canvas, camera, shader, etc.), they share common features described on this page.

## Node Examples

| [TfmNode]{ data-preview } | [Canvas]{ data-preview } | [SceneCapture]{ data-preview } | [ShaderRaymarcher]{ data-preview } |
|----------|--------|---------|--------|
| ![TfmNode example](../assets/images/nodes/TfmNode.png){width=200} | ![Canvas example](../assets/images/nodes/Canvas.png){width=200} | ![SceneCapture example](../assets/images/nodes/Capture.png){width=200} | ![ShaderRaymarcher example](../assets/images/nodes/ShdrReymarcher.png){width=200} |

## Common Features

All SPARCK Nodes share these features:

- An **enable** button
- Editable **properties**
- **Inlets** for receiving data via patch cords
- **Outlets** for sending data via patch cords
- A **title** that can be changed (must be unique within the project)
- A **menu** providing access to additional functions

---

## Enable Button

The enable button activates or deactivates the node. When disabled, the node:

- Is not rendered into its render group
- Does not process or modify textures (for shader nodes)
- Does not play video (for video nodes)
- Does not execute scripts (for script nodes)

---

## Properties

All visible properties can be edited and are stored when you save the project.

### Universal Properties

Every node has properties that can be viewed and edited directly in the node interface or in a floating properties window.

### Additional Edit Windows

Some nodes provide additional windows for specific configuration tasks. These include:

- [Beamer] — projector calibration interface
- [MeshWarp] — mesh editing interface

Some nodes open their edit window automatically when they require that form of interaction.

---

## Property Paths

Each property can be addressed via its property path. This is useful for:

- Controlling nodes through scripts
- Sending Max messages to nodes
- Remote control via OSC from external applications

### Finding Property Paths

You can find property paths in two ways:

1. **Tooltips** — hover over a property to see its path
2. **Introspection** — use the [Introspection](core_toolbar.md) tool in the CORE toolbar to query all nodes for their properties, paths, and current values

### Example: Setting a Property

Assume you have a [Grid] node and want to change its local X position. The Introspection tool shows the absolute property path:

![Introspection panel showing property path](../assets/images/core/Introspection.png)

```
set node/Grid/tfm/local/posX 0.
```

Once you've identified the property path, you can control it in two ways:

#### Option A: Via a patch cord to the node

Create a message with:

```
set tfm/local/posX 4.
```

Connect this message to the leftmost inlet (properties inlet) of your Grid node.

!!! note
    When sending a message directly to a node, omit the `node/Grid` prefix — you only need the property path relative to that node.

#### Option B: Via `send toSparck` (from anywhere)

Create a [send](https://docs.cycling74.com/reference/send/) object with its name set to `toSparck`.

Create a message with:

```
set node/Grid/tfm/local/posX 4.
```

Connect it to the send object.

!!! note
    When sending a message via `send toSparck`, include the full path with `node/Grid` to identify which node receives the message.

![Property path setter example](../assets/images/core/set_property_grid_posX.png)

---

## Inlets

Inlets allow patch-cord-based interaction with the rest of the Max environment.

- **Leftmost inlet** — typically the properties inlet for receiving control messages
- **Other inlets** — vary by node type (texture inputs, triggers, etc.)

---

## Outlets

Outlets allow patch-cord-based interaction with the rest of the Max environment.

- **Texture outlets** — send textures to other SPARCK nodes
- **Data outlets** — send values, triggers, or status information to Max objects

---

## Node Menu

Click the menu button on a node to access:

| Option | Description |
|--------|-------------|
| **Properties** | Opens a floating properties window |
| **Rename** | Change the node's title |
| **Help** | Opens the node reference documentation |
| **Collapse/Expand** | Shows or hides all properties in the node |
| **Fold/Unfold** | Shows or hides less important properties |

---

## Floating Properties Window

When you open properties via the menu, a floating window displays all the node's properties.

- The window disappears when you click outside it
- **Pin** the window to keep it visible
- Click **[-]** to minimize it to the right edge of the screen
- Click **[+]** to expand it alongside other floating property windows

[LookAtCamera]: ../reference/nodes/LookAtCamera.md
[Grid]: ../reference/nodes/Grid.md
[Hook]: ../reference/nodes/Hook.md
[Texture]: ../reference/nodes/Texture.md
[SkyBox]: ../reference/nodes/SkyBox.md
[Canvas]: ../reference/nodes/Canvas.md
[TfmNode]: ../reference/nodes/TfmNode.md
[Model]: ../reference/nodes/Model.md
[SceneCamera]: ../reference/nodes/SceneCamera.md
[SceneCapture]: ../reference/nodes/SceneCapture.md
[ShaderRaymarcher]: ../reference/nodes/ShaderRaymarcher.md
[Beamer]: ../reference/nodes/Beamer.md
[MeshWarp]: ../reference/nodes/MeshWarp.md
