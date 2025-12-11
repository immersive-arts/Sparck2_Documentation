# LookAtCamera

Camera in 3D space with buildin lookat functionality. The node  will orient the camera in such a way, that the near-clip plane will lie on the lookat plane. To be used to create controlled cuts through objects or cave-like VR experiences

LookAtCamera represents the virtual camera chassis, while [SceneCapture](SceneCapture.md) represents the virtual film: For capturing the textures SceneCapture is needed.

<figure markdown>
![LookAtCamera Node](../../assets/images/nodes/LookAtCamera.png){ width="300" }
</figure> 

!!! success "CAVE-Style VR and Cross-Section Views"
    LookAtCamera is designed for specialized viewing scenarios where the camera must always face a specific plane or target. The near-clip plane aligns with the look-at plane, enabling:
    
    - **CAVE-like VR experiences**: Viewers tracked in real-time see perspective-correct projections on walls
    - **Controlled cuts through objects**: Create cross-section views that reveal internal structures
    - **Head-tracked installations**: Combined with Kinect and [HeadRoom](https://github.com/tecartlab/HeadRoom), visitors see correctly perspectived content without wearing any devices

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `gizmo` | - | show Camera icon on 3DViewer |
    | `look at` | - | transformation node to look at |
    | `orient to` | - | local lookat plane orientation |
    | `plane up vector` | - | local lookat plane up vector |
    | `parent` | - | parent transformation node |
    | `tfm pass` | - | select transformation pass |
    | `position` | (local transformation) | position x y z |
    | `rotation` | (local transformation) | rotation x y z |
    | `scale` | (local transformation) | scale x y z |
    | `dimension` | - | suggested capture dimension |
    | `lens` | - | lens type |
    | `adapt` | - | automatically adapt frustum to distance from lookat plane |
    | `adapt factor` | - | adjust the adaptation |
    | `ratio` | - | view ratio |
    | `angle` | - | field of view |
    | `width` | - | width |
    | `height` | - | height |
    | `near` | - | near frustum clip |
    | `far` | - | far frustum clip |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | camera | message | camera intrinsics [vi_matrix, v_matrix, p_patrix, worldpos, worldquat, frustum] |


---

## Look-At Configuration

!!! tip "Setting Up the Look-At Target"
    The `look at` property defines what the camera points toward:
    
    1. Create a [TfmNode](TfmNode.md) at your target location (e.g., center of a projection wall)
    2. Set LookAtCamera's `look at` to reference that TfmNode
    3. The camera will automatically orient to face this target
    4. Use `orient to` and `plane up vector` to fine-tune the plane alignment

!!! info "Plane Orientation"
    | Property | Description |
    |----------|-------------|
    | **look at** | The transformation node that defines the target plane position |
    | **orient to** | Controls the local orientation of the look-at plane |
    | **plane up vector** | Defines which direction is "up" on the look-at plane |
    
    These settings ensure the near-clip plane aligns exactly with your projection surface.

## Adaptive Frustum

!!! example "Auto-Adapting to Distance"
    When `adapt` is enabled, the camera frustum automatically adjusts based on distance from the look-at plane:
    
    - As the viewer moves closer, the field of view expands to maintain coverage
    - As the viewer moves farther, the field of view narrows
    - Adjust `adapt factor` to control the strength of this adaptation
    
    This is essential for head-tracked installations where the viewer's distance from the screen varies.

## Transformation Pass

!!! info "Execution Order"
    The `tfm pass` property controls when this camera's transformation is calculated:
    
    - Some transformation nodes (like [TfmLookAt](TfmLookAt.md)) produce matrices that depend on other transformations
    - If LookAtCamera depends on a transformation from another tree, set the appropriate pass to ensure correct execution order
    - Default pass works for most simple setups

---

## LookAtCamera vs SceneCamera

!!! note "Choosing the Right Camera"
    | Feature | LookAtCamera | [SceneCamera](SceneCamera.md) |
    |---------|--------------|-------------------------------|
    | **Orientation** | Always faces a target plane | Free rotation |
    | **Near-clip alignment** | Aligns with look-at plane | Standard frustum |
    | **Stereo support** | Yes | Yes |
    | **Best for** | CAVE, head-tracking, cross-sections | General rendering, stereo 3D |
    | **Frustum adaptation** | Yes (distance-based) | No |

---

<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with LookAtCamera in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **LookAtCamera**

    ---
    * [:octicons-arrow-right-24: SceneCapture](SceneCapture.md) 
    * [:octicons-arrow-right-24: SceneCamera](SceneCamera.md)
    * [:octicons-arrow-right-24: BoxMapCamera](BoxMapCamera.md) 
    * [:octicons-arrow-right-24: TfmNode](TfmNode.md) 
    * [:octicons-arrow-right-24: TfmLookAt](TfmLookAt.md) 

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/LookAtCamera.md)*