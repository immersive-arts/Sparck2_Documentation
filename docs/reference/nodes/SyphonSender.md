# SyphonSender

Sends Syphon textures (OSX only - see SpoutSend for Windows) for further processing outside SPARCK. Technically it creates a Syphon Server with its node name. The App name will be SPARCK.

<figure markdown>
![SyphonSender Node](../../assets/images/nodes/SyphonSender.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `flip` | - | flip texture in x / y axis before sending |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | video | texture | video texture |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/SyphonSender.md)*
