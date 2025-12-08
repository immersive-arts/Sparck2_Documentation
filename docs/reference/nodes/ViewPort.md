# ViewPort

In its most basic mode it takes a texture and displays it in its designated slice of the connected Window

More advanced usage includes the use of custom meshes or the result of a MeshWarp node (also a mesh) and/or using a second texture and applying a shader

<figure markdown>
![ViewPort Node](../../assets/images/nodes/ViewPort.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `window` | - | select the Window-node |
    | `slice` | - | select the slice inside the Window for output |
    | `mesh` | - | choose the type of mesh. <li>'default' is a simple mesh <li>'warp' links to a MeshWarp-node <li>'file' loads custom mesh <li>'none' no mesh at all. used with Cornerpin-node |
    | `fx shader` | - | choose a shader to be applied to the viewport mesh |
    | `transform` | - | the way the mesh is displayed inside the ViewPort's slice |
    | `position` | - | move the mesh in x and y axis |
    | `rotation` | - | rotate the mesh in z axis |
    | `scale` | - | scale the mesh in x and y axis |
    | `blend` | - | use the textures alphachannel for blending |
    | `depth` | - | use depth layering |
    | `show mesh` | - | show only the face-lines |
    | `object color` | only available with 'show mesh' | choose the meshes color |
    | `filewatch` | - | if using a loaded custom mesh, load the mesh once the file was changed. |
    | `Reset` | - | Resets the node to ist default state |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | main | texture | main texture |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ViewPort.md)*
