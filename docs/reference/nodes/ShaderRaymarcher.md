# ShaderRaymarcher

Loads and applies Raymarching GLSL shaders in 3D space. Shaders of the likes you can find on ShaderToy.org

<figure markdown>
![ShaderRaymarcher Node](../../assets/images/nodes/ShdrReyMarcher.png){ width="300" }
</figure> 

!!! success "Immersive Volumetric Effects"
    ShaderRaymarcher enables real-time raytracing-like volumetric rendering in SPARCK. Create amazing immersive spaces with procedural geometry, infinite fractals, volumetric clouds, and other effects commonly found on [ShaderToy](https://www.shadertoy.com). The shader rays are cast outward from a [BoxMapCamera](BoxMapCamera.md), allowing full 360° volumetric environments.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `shader` | (drag'n drop) | shader file. Needs to be in the MaxJitter format for GLSL shaders |
    | `filewatch` | - | use filewatch |
    | `camera` | - | BoxMapCamera node. From here are the rays cast outward. |
    | `editor name` | - | choose prefered editor |
    | `edit` | - | open shader with chosen editor |
    | `time` | - | use time |
    | `speed` | - | set speed |
    | `reset time` | - | resets time to zero |
    | `reference` | - | additional transformation node to refer to. |
    | `position` | - | local translations |
    | `rotation` | - | local rotation |
    | `scale` | - | local scale |
    | `texture one` | - | open input for additional texture |
    | `texture two` | - | open input for additional texture |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | texture | texture | texture 0 &lt;param name=tex0 type=int default=0 /> |
    | texture | texture | texture 1 &lt;param name=tex1 type=int default=0 /> |
    | texture | texture | texture 2 &lt;param name=tex2 type=int default=0 /> |
    | texture | texture | texture 3 &lt;param name=tex3 type=int default=0 /> |
    | texture | texture | texture 4 &lt;param name=tex4 type=int default=0 /> |
    | texture | texture | texture 5 &lt;param name=tex5 type=int default=0 /> |
    | texture | texture | texture 6 &lt;param name=tex6 type=int default=0 /> |
    | texture | texture | texture 7 &lt;param name=tex7 type=int default=0 /> |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | texture | texture | texture one altered |
    | texture | texture | texture two altered |


---

## Setup Requirements

!!! tip "BoxMapCamera Required"
    ShaderRaymarcher requires a [BoxMapCamera](BoxMapCamera.md) to define the viewpoint from which rays are cast:
    
    1. Create a [BoxMapCamera](BoxMapCamera.md) node
    2. Position it at your desired viewpoint in the scene
    3. In ShaderRaymarcher, set the `camera` property to reference this BoxMapCamera
    4. Add a [BoxMapCapture](BoxMapCapture.md) to render the raymarched output
    
    The rays are cast outward from the BoxMapCamera position, creating a full 360° volumetric environment.

## Working with Shaders

!!! example "Development Workflow"
    For efficient shader development:
    
    1. Place your GLSL shader files in `~/_assets/_shaders/_raymarch/`
    2. Select or drag-and-drop the shader file to load it
    3. Enable `filewatch` to auto-reload when the shader changes
    4. Set your preferred `editor name` (VS Code, Sublime, etc.)
    5. Click `edit` to open the shader in your editor
    6. Use `time` and `speed` to control time-based animations
    7. Connect textures via the 8 texture inlets for additional inputs

## Time and Animation

!!! info "Time-Based Effects"
    Many raymarching shaders use time for animation. Control time with:
    
    - **time**: Enable/disable time progression
    - **speed**: Multiplier for time speed (1.0 = normal, 0.5 = half speed, 2.0 = double speed)
    - **reset time**: Reset the time counter to zero
    
    For more complex animation control, use [QueScript](QueScript.md) to animate the `speed` or `position`/`rotation`/`scale` properties.

---

!!! warning "Implementation: Difficult"
    
    Unfortunately it is not a simple copy-paste process to transform a ShaderToy-shader into a RayMarching-node shader. While 95% of the code can usually be reused, the shader needs to be embedded inside a Max-Jitter style GLSL shader file, plus some adjustments need to be made in order make a shader to work in a 3d context.
    
    Check out the [Project Examples](../../start/examples/project/project_examples.md) for a selection of about 25 favourite ShaderToy shaders which have already been translated for this node.

    ??? info "Shader Format"
        Shaders must be in the [Max-Jitter GLSL format](https://docs.cycling74.com/userguide/jitter/jxs_file_format/) format, not raw ShaderToy format. The following is a basic template to get you started. Follow the comments for necessary adjustments:
        
        ```xml
        <jittershader name="ray.template.jxs">
            <description>SPARCK - ShaderTemplate - (c) 2017 by maybites</description>

            <param name="sprk_screenMatrix" type="mat4" state="WORLD_MATRIX" />
            <param name="sprk_rotMatrix" type="mat4" default="0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0." />
            <param name="sprk_viewPos" type="vec3" default="0. 0. 0." description="test"/>
            <param name="sprk_worldRefPos" type="vec3" default="0. 0. 0." description="test"/>
            <param name="sprk_globalTime" type="float" default="0." />
            <param name="sprk_scale" type="float" default="1." />

            <!-- COMMENT: add here your own parameters... 
            
            copy and modify the following lines outsite of this comment section:

            <param name="myVeryOwnFloat" type="float" default="1." description="Use_underscore_for_spaces_to_seperate_'words'"/>
            <param name="myVeryOwnVec3" type="vec3" default="0. 0. 0." description="text with spaces will only show up as 'text'"/>
            
            you can use parameters of the following types:
            
                TYPES       GUI     QUE

                -float      y       y   
                -vec2       y       y
                -vec3       y       y
                -vec4       y       y
                -mat3       -       y
                -mat4       -       y
                
                DON'T USE int: it is reserved for textures!!

            GUI: The RayMarching Node will scan the parameters and tries to make them accessible through the userinterface
            QUE: These parameters can be sent to this shader via OSC or QueScript.
            
            ...Dont forget to bind it the shader: END OF COMMENT-->

            <language name="glsl" version="1.2">
                <bind param="sprk_screenMatrix" program="vp" />
                <bind param="sprk_rotMatrix" program="fp" />
                <bind param="sprk_scale" program="fp" />
                <bind param="sprk_viewPos" program="fp" />
                <bind param="sprk_worldRefPos" program="fp" />
                <bind param="sprk_globalTime" program="fp" />

                <!-- COMMENT: bind your own parameters here to the vertex shader (vp) and/or fragment shader (fp)

                copy and modify the following lines outsite of this comment section:
                
                <bind param="myVeryOwnFloat" program="fp" />
                <bind param="myVeryOwnVec3" program="fp" />
            
                ...until here.-->

                <program name="vp" type="vertex">
        <![CDATA[

        // >>>>> ================================
        // >>>>> DO NOT CHANGE ANYTHING FROM HERE
        // >>>>> ================================

        #version 120

        uniform mat4 sprk_screenMatrix;

        varying vec3 sprk_normal;	// surface normal
        varying vec3 sprk_worldPos;	// vertex world position

        void main(void)
        {
            // perform standard transform on vertex (general approach)
            gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
            
            gl_TexCoord[0]  = gl_TextureMatrix[0] * gl_MultiTexCoord0;
            
            sprk_normal = normalize(mat3(sprk_screenMatrix) * gl_Normal);
            sprk_worldPos = vec3(sprk_screenMatrix * gl_Vertex);
        }

        ]]>		
                </program>
                <program name="fp" type="fragment">
        <![CDATA[

        uniform vec3 sprk_viewPos; 			// point of view position
        uniform vec3 sprk_worldRefPos;      // reference position of this virtual world
        uniform mat4 sprk_rotMatrix; 		// rotation matrix
        uniform float sprk_scale;			// viewline scale
        uniform float sprk_globalTime; 		// time

        varying vec3 sprk_normal;			// surface normal
        varying vec3 sprk_worldPos;			// vertex world position

        // ================================= <<<<<<
        // ...................... UNTIL HERE <<<<<<
        // ================================= <<<<<<

        // From here onwards will be your custom code...

        // *************************************************************************
        //
        // Created by: 
        //
        //
        // *************************************************************************

        // Add here your own parameters

        uniform float myVeryOwnFloat;
        uniform vec3 myVeryOwnVec3;

        // If your old shader code came from shadertoy.com and used mouse interaction, 
        // these values will usually lead to good results
        // since we dont need them anymore they can be static.

        vec2 iMouse = vec2(0.5, 0.5);
        vec2 iResolution = vec2(1000, 1000);
        float iGlobalTime = sprk_globalTime;

        // >>>>>>>>>>>>>>>>>>>>>>
            
            
        // YOUR CODE HERE 
            
            
        // <<<<<<<<<<<<<<<<<<<<<<


        // the main function needs to look like this:

        void main() {
            // It should start with the following code block
            
            // =================  DO NOT CHANGE THIS CODE  =============================
            vec4 sprk_vl_raw = vec4(sprk_worldPos - sprk_viewPos - sprk_worldRefPos, 1);
            vec3 sprk_vl_dir = (sprk_rotMatrix * sprk_vl_raw).xyz;
            vec3 sprk_ray    = normalize(sprk_vl_dir) * sprk_scale;
            // =================  DO NOT CHANGE THIS CODE  =============================
            
            // usefull variables that are controlled by the RayMarching Node are:
        
            //  sprk_ray        (vec3) -> it is THE RAY
            //  sprk_viewPos;   (vec3) -> the world postion of your eye
            //  sprk_worldPos   (vec3) -> the place where the ray hits the canvas.
            //  sprk_rotMatrix  (mat4) -> rotates the ray around itself
            //  sprk_scale      (float)-> scales the ray
            //  sprk_globalTime (float)-> the global time in seconds
            
            // >>>>>>>>>>>>>>>>>>>>>>
            
            
            // YOUR CODE HERE 
            
            
            // <<<<<<<<<<<<<<<<<<<<<<

            // setting the fragments color:
            gl_FragColor = vec4(sprk_ray, fract(sprk_globalTime));
        }


        ]]>
                </program>		
            </language>
        </jittershader>

        ```
            
        Study the included examples in `~/_assets/_shaders/_raymarch/` to understand the required format.

!!! info "File Locations"
    
    ```
    ~/_assets/_shaders/_raymarch/     # Raymarching GLSL shader files
    ```

---


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with ShaderRaymarcher in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **ShaderRaymarcher**

    ---
    * [:octicons-arrow-right-24: BoxMapCamera](BoxMapCamera.md) 
    * [:octicons-arrow-right-24: Canvas](Canvas.md)

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderRaymarcher.md)*