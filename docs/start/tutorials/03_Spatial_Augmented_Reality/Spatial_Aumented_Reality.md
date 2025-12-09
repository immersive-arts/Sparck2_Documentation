# Spatial Augmented Reality
This article explains how to set up a SPARCK project for a use case in which four projectors are calibrated to project onto moving objects inside a Motion Capture (optical system) volume, creating a Spatial Augmented Reality (SAR) environment.

In this setup, SPARCK calibrates four projectors installed in the corners of a room at mid‑height, enabling projection on moving objects as well as on the floor.

Once calibrated, SPARCK knows the exact position and orientation of each projector and determines the visible area (its view frustum). It accounts for each projector’s native resolution and technical characteristics, allowing precise content alignment on physical objects and surfaces.

Calibration is performed by selecting co‑planar vertices on a highly accurate 3D model of the room and using reference markers placed within the space.

After calibration, SPARCK uses the [OptiTrack] node to receive [OSC2NatNet](https://github.com/tecartlab/app_NatNet2OSC) mocap data, which provides the real‑time position and orientation of tracked objects.

Since both the virtual and physical spaces are aligned through projector calibration, SPARCK can correctly project computer‑generated (CG) content onto moving objects and the floor.

This mapping is primarily handled by the [SpatialShadery] node, which computes how much of the content each projector should display and how bright each pixel should be for smooth colour blending.

Download the project files here: [SAR_Projection.zip](https://github.com/immersive-arts/Sparck2/releases/) TODO: Upload them here

## SAR Setup with 4 Projectors
Start by adding [SPARCK] to your Max patch. See the [Getting Started](https://immersive-arts.github.io/Sparck2_Documentation/start/tutorials/01_Getting_Started) documentation for more information.

![SPARCK APP](images/image-8.png)<br>
*SPARCK*

The image below shows the Max subpatcher **p Workspace**, which contains all necessary SPARCK nodes for this configuration.

![p Workspace subpatch](images/image-22-1024x678.png)<br>
*p Workspace subpatch*

In white: a highly precise simplified 3D [Model] of the Immersive Arts Space.
In black: a floor plane (using a [Canvas] node) with a [Grid] node.
In colour: four wireframes representing calibrated projector positions.

![3DViewer window](images/image-7-1024x593.png)<br>
*3DViewer preview of the virtual setup*

Four frames correspond to the calibrated view of each projector. Projectors are color‑coded via the **identify** toggle in the [Beamer] node.

![Output preview](images/image-11-768x309.png)<br>
*Output preview (4 columns, 1 row)*

## Nodes Configuration
The following sections explain how to correctly configure all nodes required for a Spatial Augmented Reality setup.


### Window Node
> TODO: Rename images from *Output* to *Window* where necessary.

The [Window] node outputs SPARCK’s rendered result to the projectors. It determines how content is distributed across the four projector outputs.

![Window node](images/image-1.png)<br>
*Window node — 1_UTILITY > WINDOW.maxpat*

**position**: Switch between **Output** (content displayed on projectors) and **Desktop** (content preview).

**columns and rows**: Defines how the [Window] is divided. Set **4 columns** and **1 row** for four projectors.

**display**: Opens the display setup tool. Select the projector displays (orange), then click **Store and Close**.

![Output setup](images/image-9-768x260.png)<br>
*Display selection interface*

Example: The system has two monitors (1920×1200, greyed out) and four projectors (2560×1600, orange). Only the projectors are selected.


### Beamer Node
The [Beamer] node creates a virtual projector in SPARCK’s **3DViewer**. It is essential for calibrating the projector’s spatial position, orientation, and lens properties. See the [Calibration](../02_Calibration/calibration.md) guide for details.

![Beamer node](images/image-3.png)<br>
*Beamer — 2_SPACE > BEAMER.maxpat*

**capture**: Select the render layer for each Beamer. Each Beamer must use a different small turquoise square.

**calibfile**: Saves calibration data to a `.xml` file.

**calibrate**: Opens the calibration editor.

**identify**: Displays a colour background in both **Output** and **Desktop** to identify the projector.

**gizmo**: Shows the projector’s position in the **3DViewer**.


### Viewport Node
This node creates a texture displayed in a designated slice of the [Window]. When connected to a [Beamer], it outputs that Beamer’s point of view.

TODO: Replace image

![Viewport](images/image-10.png)<br>
*Viewport — 1_UTILITY > VIEWPORT.maxpat*

**window**: Select the [Window] node.

**slice**: Assign each Viewport to a unique slice: **column 1–4**, all using **row 1**.


### Model Node
The [Model] node displays a simplified but accurate model of the Immersive Arts Space, helping visualize the positions of projectors, the floor plane, and tracked objects.

![Model](images/image-20.png)<br>
*Model — 2_SPACE > MODEL.maxpat*

**drawto**: Selects the render layer (large turquoise square). Here, the Model appears only in the **3DViewer**.

**meshfile**: Loads a 3D model from `Sparck/_assets/_models`. Ensure polygon count is reasonable for performance.


### Grid Node
The [Grid] node displays a grid useful for verifying projector calibration. If grid lines overlap sharply across projections, calibration is correct; doubled or misaligned lines indicate mismatch.

![Grid](images/image-14.png)<br>
*Grid — 2_SPACE > GRID.maxpat*

**drawto**: Shows the grid in the **3DViewer**. It can also be shown through projectors by enabling small squares.

**scale**: Here set to the IAS floor size: 6m × 12m.

**render gridsize**: Adjusts subdivision size.

**showaxis**: Enables or disables axis display.


### SpatialShadery Node
The [SpatialShadery] node is at the core of Spatial Augmented Reality. It computes per‑projector pixel visibility and brightness, producing soft‑edge blending across all projectors.

![SpatialShadery](images/image-21.png)<br>
*SpatialShadery — 7_EFFECTS > SPATIAL.SHADERY.maxpat*

**shader**: Use **edge & blend** for soft‑edge merging.

**project to**: Set to **baked textures**.

**Beamer A–D**: Assign each [Beamer].

**projection**: Use **front side**.

**spread**: Controls the distribution of pixel blending between overlapping projections. 0 = no spread, 1 = full spread. Typical value: **0.54**.

**output**: Set to **result** to display final blended output.

**power**: Controls the soft-edge blending power. Find a good balance that fit your situation.

**luminance**: Adjusts the brightness balance. Find a good balance that fit your situation.


### OptiTrack Node
The [OptiTrack] node receives rigidbody motion capture data from **NatNet2OSC**. It distributes this positional data inside SPARCK so virtual models and shapes can follow physical tracked objects.

![OptiTrack](images/image-16.png)<br>
*OptiTrack — 4_TRANSFORM > OT.RECEIVER.maxpat*

**stream 1–8**: Select a rigidbody from Motive. Ensure unique names/IDs.

**in port**: Port where mocap data is received.

**out port**: Port where data is forwarded.

**out IP**: Destination IP for mocap forwarding.

**leap forward**: Predictive smoothing to reduce jitter from fast‑moving tracked objects.


### SpoutReceiver Node
The [SpoutReceiver] node receives real‑time textures from applications such as TouchDesigner, Unity, Unreal, or Notch via Spout.

![SpoutReceiver](images/image-17.png)<br>
*SpoutReceiver — 5_INPUT > SPOUT.RECEIVER.maxpat*

**sender**: Select the Spout stream.

**flip x / flip y**: Flip texture orientation if needed.


### Canvas Node
The [Canvas] node draws basic 3D shapes (plane, cube, sphere, custom mesh). It is lighter than the [Model] node and contains no material or lighting properties.

![Canvas](images/image-19.png)<br>
*Canvas — 2_SPACE > CANVAS.maxpat*

**drawto**: Selects the render layer. Here shown in **3DViewer** and on [Beamer] layers.

**shape**: Select the geometry. For SAR floors, a **plane** is used.

**shader**: Assign the [SpatialShadery] shader for multi‑projector blended projection.

**scale**: Here set to the IAS floor dimensions: 6m × 12m.


## Customize the Project
You can extend this project by adding additional tracked objects, projection domes, or moving structures.

In this example, a tracked movable wall is added. It receives projection content (video, Spout stream, or static image). Add a **p Wall** subpatch to your Max project.

![p Patcher](images/image-23.png)<br>
*p Wall subpatch*

Inside, add a **RigidBody**, **Video**, and [Canvas] node.

![subpatch](images/image-24.png)<br>
*Setup for one tracked plane displaying looping video*

### Video Node
(Section to be completed — describe video loading, looping, texture output.)

### RigidBody Node
(Section to be completed — describe linking OptiTrack rigidbody to Canvas transform.)

[Beamer]: ../../../reference/nodes/Beamer.md
[BlendSoftedge]: ../../../reference/nodes/BlendSoftedge.md
[BoxMapCamera]: ../../../reference/nodes/BoxMapCamera.md
[BoxMapCapture]: ../../../reference/nodes/BoxMapCapture.md
[CalibrationCross]: ../../../reference/nodes/CalibrationCross.md
[Canvas]: ../../../reference/nodes/Canvas.md
[CornerPin]: ../../../reference/nodes/CornerPin.md
[DrawMask]: ../../../reference/nodes/DrawMask.md
[Grid]: ../../../reference/nodes/Grid.md
[Hook]: ../../../reference/nodes/Hook.md
[Light]: ../../../reference/nodes/Light.md
[LookAtCamera]: ../../../reference/nodes/LookAtCamera.md
[Material]: ../../../reference/nodes/Material.md
[MeshWarp]: ../../../reference/nodes/MeshWarp.md
[Model]: ../../../reference/nodes/Model.md
[OptiTrack]: ../../../reference/nodes/OptiTrack.md
[QueScript]: ../../../reference/nodes/QueScript.md
[SceneCamera]: ../../../reference/nodes/SceneCamera.md
[SceneCapture]: ../../../reference/nodes/SceneCapture.md
[ShaderAnaglyph]: ../../../reference/nodes/ShaderAnaglyph.md
[ShaderBlur]: ../../../reference/nodes/ShaderBlur.md
[ShaderBrCoSa]: ../../../reference/nodes/ShaderBrCoSa.md
[ShaderColormap]: ../../../reference/nodes/ShaderColormap.md
[ShaderPointCloud]: ../../../reference/nodes/ShaderPointCloud.md
[ShaderRaymarcher]: ../../../reference/nodes/ShaderRaymarcher.md
[ShaderSelection]: ../../../reference/nodes/ShaderSelection.md
[ShaderTexStitch]: ../../../reference/nodes/ShaderTexStitch.md
[ShaderTexZoom]: ../../../reference/nodes/ShaderTexZoom.md
[ShdrTexOP]: ../../../reference/nodes/ShaderTexOP.md
[SkyBox]: ../../../reference/nodes/SkyBox.md
[SPARCK]: ../../../reference/sparck_core.md
[SpatialShadery]: ../../../reference/nodes/SpatialShadery.md
[SpoutReceiver]: ../../../reference/nodes/SpoutReceiver.md
[SpoutSender]: ../../../reference/nodes/SpoutSender.md
[SyphonSender]: ../../../reference/nodes/SyphonSender.md
[Texture]: ../../../reference/nodes/Texture.md
[TextureProjectury]: ../../../reference/nodes/TextureProjectory.md
[TfmLookAt]: ../../../reference/nodes/TfmLookAt.md
[TfmMerge]: ../../../reference/nodes/TfmMerge.md
[TfmMirror]: ../../../reference/nodes/TfmMirror.md
[TfmNode]: ../../../reference/nodes/TfmNode.md
[Video]: ../../../reference/nodes/Video.md
[Viewport]: ../../../reference/nodes/ViewPort.md
[Window]: ../../../reference/nodes/Window.md