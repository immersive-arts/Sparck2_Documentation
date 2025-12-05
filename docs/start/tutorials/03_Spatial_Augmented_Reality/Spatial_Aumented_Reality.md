# Spatial Augmented Reality
This article showcase how to seutp a Sparck project for the use case where 4 projectors are calibrated to project on moving objects within a Motion Capture (optical system) volume, creating in this manner a Spatial Agumented Reality (SAR) project.

In this context Sparck is used to calibrate 4 projecros that are installed on the 4 corners of a room at a middle high, allowing for moving objects and floor projection. 

Once calibrated, Sparck calculates the exact position of each projector and determines what area each projector can see (its view). This takes into account the projector's resolution and other technical settings, allowing precise content alignment on moving objects and surfaces.

This is done using co-planar vertices selection on a highly accurate 3D model of the entire room and reference markers positioned in the room at the time of calibration.

Once the projectors are calibrated, Sparck uses the **OptiTrack** node to receive [OSC2NatNet](https://github.com/tecartlab/app_NatNet2OSC) mocap data to determin where and how each tracked object is positioned in the space. 

And since both the virtual and phisical space are alignd thanks to the calibration of the projectors, Sparck then uses this information to correctly display computer-generated (CG) visual content on each tracked objects and on the floor.

This last part is essentially handley by the **SpatialShadery** node which calculate how much of the content (in pixel) should be shown from each projectors, as well as how bright (the pixel) should be to make sure the colours blend smoothly.

## Setup 4 Projectors
First add the Sparck app to your Max patch. See the [Getting Started](https://immersive-arts.github.io/Sparck2_Documentation/start/tutorials/01_Getting_Started) documentation for more information on how to start.

![Sparck APP](images/image-8.png)<br>
*Sparck APP.*

The image below shows the overall Max subpatcher **p Workspace**. Inside it we place all the Sparks nodes required for this configuration.

![p Workspace subpatch](images/image-22-1024x678.png)
*p Workspace subpatch.*

In white a highly precise simplified 3D model of the Immersive Arts Space. In black, a floor plane (see **Canvas** node) with a **Grid** (also a node). And 4 colored wireframes, displaying the positions of the projectors situated in the corner of the virtual room after performing the projectors calibration. 

![3D view](images/image-7-1024x593.png)<br>
*3D viewer of Sparck. Preview of the virtual setup.*

![Output preview](images/image-11-768x309.png)<br>
*Output preview of Sparck (4 col, 1 row).*

Four frames are sticked together corresponding on the 3D view from each projector position after calibration. To distinguish then four different colors are used to identify each beamers (see **Beamer** node with indentify **toggled**).

## Nodes basic configurations
The following text explains and shows how to correctly setup all the differents nodes for a Spatial Augmented Reality setup.

### Output Node
This node is used to output the rendered result of Sparck to some output deivices, in this case the 4 projectors, basically it handles how the content is distributed for each outputs.

![Output node](images/image-1.png)<br>
*Output node, can be found under 1_UTILITY > WINDOW.maxpat*

[TODO: Tell Martin to write in all his node reference how to find it since the node is not called Output but Window. also I would suggest to have only one place where it can be found and not many sub menus... see notch documentation https://manual.notch.one/1.0/en/docs/reference/nodes/]

**position**: switch between the **Output** or **Desktop**. Where **Output** display the visual content on the configured projectors and **Desktop** create a window that preview how the visual content is distributed.

**columns and row**: slices the output into designated frames. In this case we set the colums to 4 and the rows to 1. As shown the the picture above about the Preview of Sparck

**display**: pressing **setting...** opens up the display setup tool to configure the Output overall pixel amount used for projection. Select the displays you wish to use for projection. Once selected thy become orange. Now, **Store and Close** to close the configurations.

![Output setup](images/image-9-768x260.png)<br>
*Settings... interface to select and configure which display is used for projection.*

In this instance, the computer is connected to 2 monitors of 1920 x 1200 pixels (grayed) and 4 projectors of 2560 x 1600 pixels (orange). Only the orange ones will be used for projecion.

### Beamer Node
The beamer node will create a virtual world projector inside of Sparck's 3D viewer. This node is essential since is used to calibrate the projector to register its position, orientations and lenses properties in respect of the virtual-physical space.

![Beamer node](images/image-3.png)<br>
*Beamer node, availabe under 2_SPACE > BEAMER.maxpat*

**capture**: select in which render layer the beamer will be displayed. Make sure to select only one of the little squares (1), every time select a different ones for the other beamers. 

**calibfile**: create and save a .xml file in which the projector information about its position in 3D space, and lenses will be stored.

**calibrate**: is a button that will launch the window editor to calibrate the projector.

**identify**: if enabled, helps identify which projector is, in the **Output** and **Desktop** since it display a specific background color registerd in the **calibfile**.

[TODO: Ask Martin why not to use the bgcolor for it...]

**gizmo**: If enabled (turqois big square), it displays on the **3D viewer** the projector at the position registered in the **calibfile**.

### Viewport Node
This node create a texture that is diplayed in a designated slice of the Window. Connected to a **Beamer** node makes sure to output the point of view of this beamer to a slice of the overal Window/Output.

![Viewport](images/image-10.png)<br>
*Viewport, available under 1_UTILITY > VIEWPORT.maxpat*

**window**: select the Output. For each Viewport connected to a Beamer nodes, target the **Output** node.

**slice**: select the designated slice wehre to output the visual content. In this case make sure to target for each Viewport nodes a different colum_x (eg. 1, 2, 3, 4) but all target the same row_1.

### Model node
In this context the **Model** node is used to display in Sparck's 3D viewer a symplified but higly precise model of the Immersive Arts Space. This model helps referencing where projectors, floor and tracked object are located.

![Model](images/image-20.png)<br>
*Model, available under 2_SPACE > MODEL.maxpat*

**drawto**: selects the render layer where the model is rendered (turqouis big square). In this case the model is only displayed on the Sparck's 3D preview and not outputted on the projectors.

**meshfile**: selects a 3D model mesh file to load and use. To import a 3D model, place it inside the Sparck forlder directory under Sparck/_assets/_models. Then update the menu by clicling on the round weel. Make sure your 3D model doesn't have too many polygons since this will have and inpact on Sparck frame rate.

### Grid Node
The **grid** node is a helper used to display a grid in Sparck's 3D viewer.

![Grid](images/image-14.png)<br>
*Grid, available under 2_Space > GRID.maxpat*

**drawto**: if enabled (turqois big square), selects the render layer where the model is rendered. In this case the model is only displayed on the Sparck's preview and not outputted on the projectors. Some times we want to see it olso trough the projectors, then toggle the small quares for each projectors, as in the **Beamer** nodes.

**scale**: 1 Sparck unit equal to 1 meter (100cm). In this case the scale is set on the size of IAS floor plan, 6m whide and 12m long.

**render gridsize**: changes the grid slice size.

**showaxis**: anable/disable the axis display.

### SpatialShadery node
The **SpatialShadery** node is an essential component for Spatial Augmented Reality. It is used to calculate the spatial relationship between the projectors and the scene. Essentially, it determines — from the point of view of each projector — which pixels should be rendered by which projector and how intense each pixel should be. In this way, it produces a soft-edge blend shader for the **Output**, ensuring that the content from multiple projectors merges smoothly into a single coherent projection.

![SpatialShadery](images/image-21.png)<br>
*SpatialShadery, available under 7_EFFECTS > SPATIAL.SHADERY.maxpat*

**shader**: select the shader type, in this case we use **edge & blend** which calculated the soft-edge combined with the blending.

**project to**: set to **baked textures** implements all render passes for generating all the pixel color and brightnes.

**Beamer A-D**: for each BeamerX target a different **Beamer** node from where to project.

**projection**: set to **front side**.

**spread**: set to 0.5400 which is the factor for differentiation between the overlapping projections, achieving in this manner the soft-edge blending. Set to 0 equals no spread at all, and to 1 full spread. Find a good balance that fit your situation.

**output**: is the display mode of the shader, in this case is set to **result** which show the final baked texture, how bright and colored all the pixel are.

**power**: is the soft-edge blending power. Find a good balance that fit your situation.

**luminance**: is the soft-edge blending luminance. Find a good balance that fit your situation.

### Optitrack node
The Optitrack node listen to NatNet2OSC to get motion capture data from Optitrack. Is an essential node for Spatial Agmented Reality since it handles how the Optitack rigidbodies positional data is distributed inside of Sparck.

![Optitrack](images/image-16.png)<br>
*Optitrack, available under 4_TRANSFORM > OT.RECEIVER.maxpat*
**stream 1-8**: select an Optritack rigidbody stream. If the rigidbody is registered inside of Motive (Optitrack software), it will become available in the dropdown menu. It is important to differently ID (and name) each rigidbodies inside of Motive. Use **refetch...** button if you register new rigidbodies.

**in port**: set the port number at which the mocap stream is being received.

**out port**: set the port number at which the mocap stream is sent.

**out IP**: set the IP adress. In this case, the IP correspond to where Motive/Optitrack is sending the mocap.

**leap forward**: increases the forward prediction of the position and rotation of the rigidbodies. Since the speed at wich the projection refresh is lower from the speed of at which objects move in the physical space. It reduces gitters on the projected visual content of traked objects.

### SpoutReceiver node
The **SpoutReceiver** node receive [Spout](https://spout.zeal.co/) textures. Generally, is an animated texture that is real time generated by a visual or game engine, such as TouchDesigner, Unity, Unreal, Notch etc.

![SpoutReceiver](images/image-17.png)<br>
*SpoutReceiver, available under 5_INPUT > SPOUT.RECEIVER.maxpat*

**sender**: select a Spout video stream.

**flip x**: flip the video stream horizontally.

**flip y**: flip the video stream vertically.

### Canvas node
The **Canvas** node draw a variety of basic 3d shapes, such as plane, cube, sphere, a custom 3D mesh etc. Is a light version node of the **Model** node, the difference is that the **Canvas** node doesn't contains additional settings such as material, lighting, shadow, etc.

![Canvas](images/image-19.png)<br>
*Canvas, available under 2_SPACE > CANVAS.maxpat*

**drawto**: selects the render layer where the canvas is rendered. In this case the canvas is displayed on the Sparck preview and also on the projectors layers for ouput (big and small turqois squares). 

**shape**: select a basic shape to use. In this case is a basic plane but could be a sphere, torus, cylinder, ect.

**shader**: select the shader to use. In this case the **SpatialShadery** shader is used. Since we want to make sure each projectors is used to project on that surface from all angles, calculating is this way how each pixel is rendered with soft-egde blending. This canvas is used to project on the floor covering the entierity for the space.

**scale**: 1 Sparck unit is 1 meter (100cm). In this case, the scale is set on the size of IAS whole floor plan, 6m whide and 12m long.

## Costumize project
Add Max subpacthes accordingly to costumize the project, e.g add additionals tracked object for SAR, or add a projection dome, etc.

In this case we add a simple physical muvable wall that is being traked by Optitrack that is used to project a video (it can also be a Spout stream). Add to your Max patch a **p Wall**  subpatch.

![p Patcher](images/image-23.png)<br>
*p Wall subpatch, contains additional Sparck nodes to project on a tracked plane surface.*

Open it up and inside insert a **RigidBody** node, **Video** node and **Canvas** node.

![subpatch](images/image-24.png)<br>
*Inside the p Wall subpatch, basic nodes setup for 1 traked plane displaying a looping video.*

### Video node


### RigidBody node