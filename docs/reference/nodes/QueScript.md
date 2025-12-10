# QueScript

Que Script is SPARCK own super powerfull [scripting language](../quescript/QS1-Introduction.md).

The implementation of QueScript inside SPARCK follows certain idiosyncracies that are described down below.

<figure markdown>
![QueScript Node](../../assets/images/nodes/QueScript.png){ width="300" }
</figure> 

!!! success "Nonlinear Animation Scripting"
    QueScript is SPARCK's built-in nonlinear animation scripting language. With a few commands you can create many **parallel running scripts** to control any aspect of SPARCK or beyond. It's designed for timeline-based animations, interactive triggers, and automated show control.

## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `scriptfile` | - | load and execute que script |
    | `fileWatch` | - | reloads the script file if it has changed by an external editor. Usually a good idea while you are editing. |
    | `ques` | - | lists all ques inside the script and allows you to manually execute the chosen one. |
    | `progress..` | - | shows how each que is progressing |
    | `pause / play` | - | pauses / plays the execution |
    | `stop` | - | stops the execution |
    | `Editor` | - | select your prefered editor or add your own. |
    | `edit` | - | edit the loaded file. You can set your prefered editor inside properties. |
    | `update mode` | - | there are two modes to choose: <li>automatic will update the script with each frame-pass. <li>custom will allow you to set your own update frequency. |
    | `frequency` | - | custom update frequency |
    | `debug` | - | will output debug information to the console |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | 'trigger | message | 'trigger &lt;triggername>' / 'play &lt;quename>' / 'var &lt;varname> &lt;varvalue>' - messages |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | out | message | out messages |
    | osc | message | osc messages |
    | trigger | message | trigger messages |


---

## Script Structure

!!! example "Basic QueScript Example"
    QueScript uses an XML-based syntax with `<que>` elements containing timers, animations, and commands:
    
```xml
    <script>
      <que name="myQue">
        <timer/>
        <send>/address list with strings and numbers 0 2.45 56</send>
        <wait timer="5s"/>
        <print>timer has passed</print>
      </que>
      <que name="my2ndQue">
        <anim name="simpleRamp" duration="5s" fadeout="2s">
          <track name="t1">0. 1.</track>
          <send>/address ramp {t1}</send>
        </anim>
        <wait anim="simpleRamp"/>
      </que>
    </script>
```
    
    Key elements:
    
    - **`<que>`**: A named sequence of actions that can run in parallel with other ques
    - **`<timer>`**: Time-based execution block
    - **`<anim>`**: Animation block with duration, fadeout, and tracks
    - **`<track>`**: Defines interpolation values (e.g., `0. 1.` ramps from 0 to 1)
    - **`<send>`**: Sends OSC messages to SPARCK or external applications
    - **`<wait>`**: Pauses execution until a timer or animation completes
    - **`<print>`**: Outputs debug messages to the console

## Controlling SPARCK Properties

!!! tip "OSC Address Format"
    QueScript uses OSC messages to control any SPARCK node property. The address format is:
    
    ```
    node/<nodeName>/<propertyPath> <value(s)>
    ```
    
    Examples:
    ```xml
    <send>toSparck node/Grid/tfm/local/posX 4.</send>
    <send>toSparck node/Beamer/render/texture/dim/size 1920. 1080.</send>
    ```

    In this case the &lt;[send](../quescript/QS1-send-cmd.md)&gt; command sends the message to SPARCK.
    
    Use the **[Introspection](../core_toolbar.md#toolbar-controls)** button in SPARCK's toolbar to discover all available node [properties](../node_anatomy.md#property-paths) and their current values.

## Triggering and Playback

!!! info "Inlet Messages"
    Control QueScript execution via the trigger inlet:
    
    | Message | Description |
    |---------|-------------|
    | `trigger <triggername>` | Fire a named trigger defined in the script |
    | `play <quename>` | Start executing a specific que by name |
    | `var <varname> <value>` | Set a script variable dynamically |
    
    The `ques` dropdown in the node UI also allows manual execution of any que.

## Development Workflow

!!! tip "Live Editing"
    For efficient script development:
    
    1. Enable `fileWatch` to auto-reload when the script file changes
    2. Set your preferred `Editor` (VS Code, Sublime, etc.)
    3. Click `edit` to open the script in your editor
    4. Enable `debug` to see execution details in the Max console
    5. Use `pause / play` and `stop` to control execution during testing

---

## Important Notes

!!! warning "OSC Output Routing"
    QueScript can generate OSC messages, but needs an [udpsend](https://docs.cycling74.com/reference/udpsend/) object to transmit them externally. Connect the QueScript's `osc` outlet to an udpsend object.

!!! info "File Locations"
    
    ```
    ~/_assets/_scripts/_ques     # QueScript files (.xml)
    ```

---


<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Quick Start__

    ---

    Get started with QueScript in minutes
    
    * [:octicons-arrow-right-24: Project Examples](../../start/examples/project/project_examples.md)
    * [:octicons-arrow-right-24: Node Examples](../../start/examples/nodes/node_examples.md)

-   :material-file-document:{ .lg .middle } __Complementing__ **QueScript**

    ---
    * [:octicons-arrow-right-24: QueScript Language Guide](../quescript/QS1-Introduction.md)

  
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


*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/QueScript.md)*