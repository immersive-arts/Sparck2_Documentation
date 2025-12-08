# QueScript

Que Script is SPARCK own super powerfull [scripting language](../quescript/QS1-Introduction.md).

The implementation of QueScript inside SPARCK follows certain idiosyncracies that are described down below.

<figure markdown>
![QueScript Node](../../assets/images/nodes/QueScript.png){ width="300" }
</figure> 


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
    | `osc send` | - | Que script can create OSC messages, but needs an OscSend node to send them to. |
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

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/QueScript.md)*
