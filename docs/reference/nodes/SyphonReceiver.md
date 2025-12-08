# SyphonReceiver

Receives Syphon textures (OSX only - see SpoutReceive for Windows) for further processing inside SPARCK

<figure markdown>
![SyphonReceiver Node](../../assets/images/nodes/SyphonReceiver.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `server name` | - | select syphon server |
    | `app name` | - | select syphon app |
    | `flip` | - | flip recieved texture in x / y axis |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | video | texture | video texture |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/SyphonReceiver.md)*
