# Beamer

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | background | texture | background texture for camera calibration |
    | custom | type | custom commands. message 'createToXY' creates a new model with calibration vertices relative to the XY-plane: 'createToX  x1  y1  z1  x2  y2  z2  x3  y3  z3  ...'. &#124; message 'addToXY' adds calibration vertices relative to the XY-plane: 'addToX  x1  y1  z1  x2  y2  z2  x3  y3  z3  ...' |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | captured | texture | captured texture (left if stereo) |
    | captured | warping | captured texture (right if stereo) |
    | dump | type | dump (transform, frustum) |


# BlendSoftedge

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | main | texture | main texture (content texture) |
    | mask | texture | mask texture (alpha mask) |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | blended | texture | blended texture |


# BoxMapCamera

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# BoxMapCapture

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | left | texture | left texture |
    | front | texture | front texture |
    | right | texture | right texture |
    | back | texture | back texture |
    | top | texture | top texture |
    | bottom | texture | bottom texture |
    | boxmap | boxmap | boxmap (texture list <texL> <texF> <texR> <texB> <texT> <texG>) |
    | texture | texture | texture list with only active textures (texture <tex1> ...) |
    | single | texture | single texture with all box sides backed together |


# CalibrationCross

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# Canvas

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | main | texture | main texture. press to reset to default |
    | custom | matrix | custom jit.matrix |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | baked | texture | baked texture(s) |
    | baked | texture | baked texture used in current renderpass |


# CornerPin

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | texture | texture | texture |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# CubeMap

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | cross | texture | cross shape texture holding the 6 faces of the cube |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | cubemap | cubemap | cubemap texture |


# DrawMask

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture out |


# FaceStream

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | main | texture | main texture |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | baked | texture | baked texture(s) |


# Grid

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# Hook

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | link | type | link to object to place it into the sparck-context. It  sends 'enable' 'drawto' 'shader' material' |
    | link | type | link to object to connect it to sparck transformation. It sends 'anim' message |


# Light

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# LookAtCamera

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | camera | type | camera intrinsics [vi_matrix, v_matrix, p_patrix, worldpos, worldquat, frustum] |


# Material

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | diffuse | texture | diffuse texture |
    | specular | texture | specular texture |
    | ambient | texture | ambient texture |
    | emission | texture | emission texture |
    | normal | texture | normal texture |
    | cubemap | cubemap | cubemap texture |
    | heightmap | texture | heightmap texture |
    | glossmap | texture | glossmap texture |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# MeshWarp

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | main | texture | main texture |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# Model

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | main | texture | main texture |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# OptiTrack

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | raw | type | raw motive data stream |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | raw | type | raw motive data stream |


# QueScript

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | 'trigger | type | 'trigger <triggername>' / 'play <quename>' / 'var <varname> <varvalue>' - messages |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | out | type | out messages |
    | osc | type | osc messages |
    | trigger | type | trigger messages |


# RigidBody

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | send | type | send direct message to anim object: 'bang' for forced transformation bang. OR 'getlist' <get...> items for dump out current values (needs a bang). Possible <get...> items: getposition, getquat, getscale, getworldpos, getworldquat, getworldscale, gettransform, getinvtransform, getworldtransform |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | dump | type | dump of 'anim' , output of the requested <get...> values and transformation bang from the above inlet. also outputs 'markerlist' if markers are received. |


# SceneCamera

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | camera | type | camera intrinsics [p_patrix, frustum] |


# SceneCapture

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | captured | texture | captured texture (left if stereo) |
    | if | texture | if stereo: captured right texture |


# ShaderAnaglyph

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | texture | texture | texture left |
    | texture | texture | texture right |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |


# ShaderBlur

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | main | texture | main texture |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | main | texture | main texture blured |


# ShaderBrCoSa

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |
    | texture | texture | texture two altered |


# ShaderColormap

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (also used for shader) |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |
    | texture | texture | texture two altered |


# ShaderPointCloud

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (also used for shader) |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# ShaderRaymarcher

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | texture | texture | texture 0 <param name=tex0 type=int default=0 /> |
    | texture | texture | texture 1 <param name=tex1 type=int default=0 /> |
    | texture | texture | texture 2 <param name=tex2 type=int default=0 /> |
    | texture | texture | texture 3 <param name=tex3 type=int default=0 /> |
    | texture | texture | texture 4 <param name=tex4 type=int default=0 /> |
    | texture | texture | texture 5 <param name=tex5 type=int default=0 /> |
    | texture | texture | texture 6 <param name=tex6 type=int default=0 /> |
    | texture | texture | texture 7 <param name=tex7 type=int default=0 /> |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |
    | texture | texture | texture two altered |


# ShaderSelection

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# ShaderTexOP

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | result | texture | result of 1 op 2 (left op right) |


# ShaderTexStitch

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (left) |
    | texture | texture | texture two (front) |
    | texture | texture | texture three (right) |
    | texture | texture | texture four (back) |
    | texture | texture | texture five (top) |
    | texture | texture | texture six (bottom) |
    | texture | texture | texture list |
    | boxmap | boxmap | boxmap (list) |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | stitched | texture | stitched texture |


# ShaderTexZoom

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | texture | texture | texture one (also used for texture fx) |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |
    | texture | texture | texture two altered |


# SkyBox

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | main | cubemap | main texture |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# SpatialBakery

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture list with depth pass |


# SpatialShadery

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture list with depth pass |


# SpoutReceiver

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | video | texture | video texture |


# SpoutSender

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | video | texture | video texture |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# SyphonReceiver

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | video | texture | video texture |


# SyphonSender

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | video | texture | video texture |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# Texture

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | image | texture | image texture |


# TextureProjectory

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | boxmap | boxmap | boxmap (list) |
    | camera | texture | camera A - texture one (mono, if stereo -> left texture) |
    | camera | texture | camera A - texture two (if stereo -> right texture) |
    | camera | texture | camera A - texture one (mono, if stereo -> left texture) |
    | camera | texture | camera A - texture two (if stereo -> right texture) |
    | camera | texture | camera A - texture one (mono, if stereo -> left texture) |
    | camera | texture | camera A - texture two (if stereo -> right texture) |
    | camera | texture | camera A - texture one (mono, if stereo -> left texture) |
    | camera | texture | camera A - texture two (if stereo -> right texture) |
    | camera | texture | camera A - texture one (mono, if stereo -> left texture) |
    | camera | texture | camera A - texture two (if stereo -> right texture) |
    | camera | texture | camera A - texture one (mono, if stereo -> left texture) |
    | camera | texture | camera A - texture two (if stereo -> right texture) |
    | Background | texture | Background texture |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# TfmLookAt

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | send | type | send direct message to anim object: 'bang' for forced transformation bang. OR 'getlist' <get...> items for dump out current values (needs a bang). Possible <get...> items: getposition, getquat, getscale, getworldpos, getworldquat, getworldscale, gettransform, getinvtransform, getworldtransform |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | dump | type | dump of 'anim' , output of the requested <get...> values and transformation bang from the above inlet. also outputs 'markerlist' if markers are received. |


# TfmMerge

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# TfmMirror

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# TfmNode

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | send | type | send direct message to anim object: 'bang' for forced transformation bang. OR 'getlist' <get...> items for dump out current values (needs a bang). Possible <get...> items: getposition, getquat, getscale, getworldpos, getworldquat, getworldscale, gettransform, getinvtransform, getworldtransform |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | dump | type | dump of 'anim' , output of the requested <get...> values and transformation bang from the above inlet. also outputs 'markerlist' if markers are received. |


# TfmNodePath

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# Video

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | direct | type | direct messages to control video: enable &#124; start &#124; stop &#124; dispose &#124; frame refresh &#124; frame time &#124; frame duration &#124; frame framecount &#124; frame seekframe &#124; frame seeknotify |
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | video | texture | video texture |
    | audio | audio | audio left |
    | audio | audio | audio right |
    | dump | type | dump |


# Viewport

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |
    | main | texture | main texture |
    | texture | texture | texture two |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


# Window

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set <propertyPath> <value(s)>] (without node/<nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|


