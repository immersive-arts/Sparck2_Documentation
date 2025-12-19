# Tent Projection
This article explains how to set up a SPARCK project for a use case in which two calibrated projectors are used to project onto a tent (dome). The projected content is genarated real time from a game engine. In the game engine a 360° virtual camera is used and capture the virtual environment from a single point of view (equirectangular prjection).

In this setup, first SPARCK calibrates two projectors installed on each side of the tent. The tent is positioned diagonally, in such a way that two of its corner points toward the two projectors.

Once calibrated, SPARCK knows the exact position and orientation of each projector and determines the visible area (its view frustum). It accounts for each projector’s native resolution and technical characteristics, allowing precise content alignment on physical objects and surfaces.

Calibration is performed by selecting co‑planar vertices on a highly accurate 3D model of the room and using reference markers placed within the space.

Since both the virtual and physical spaces are aligned through projector calibration, SPARCK can correctly project computer‑generated (CG) content onto the tent. In this instance we use a [TextureProjectory] node in combination with a [BoxMapCamera] node.

TODO: Martin check this out

The [BoxMapCamera] converts the incoming 360° capture into a box/cubemap-style environment representation. This is advantageous because the environment can then be sampled by a 3D direction vector with minimal distortion and without relying on a custom UV layout for the tent mesh.

The [TextureProjectory] uses the calibrated projector pose (position, orientation, frustum, and resolution) to perform projective texturing onto the tent geometry. For each projector pixel, SPARCK computes where that ray intersects the tent surface and then samples the [BoxMapCamera] environment in the corresponding direction from the 360° capture point. This produces viewpoint-correct content for each projector, ensuring that the same virtual environment aligns consistently across the physical tent surface and between multiple projectors.

The blending of the mapping is then handled by the [SpatialShadery] node, which computes how much of the content each projector should display and how bright each pixel should be for smooth colour blending.

Download the project files here: [Tent_Projection.zip](https://github.com/immersive-arts/Sparck2/releases/download/1.0.0) TODO: add link to files

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
[RigidBody]: ../../../reference/nodes/RigidBody.md
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
[TextureProjectory]: ../../../reference/nodes/TextureProjectory.md
[TfmLookAt]: ../../../reference/nodes/TfmLookAt.md
[TfmMerge]: ../../../reference/nodes/TfmMerge.md
[TfmMirror]: ../../../reference/nodes/TfmMirror.md
[TfmNode]: ../../../reference/nodes/TfmNode.md
[Video]: ../../../reference/nodes/Video.md
[Viewport]: ../../../reference/nodes/ViewPort.md
[Window]: ../../../reference/nodes/Window.md