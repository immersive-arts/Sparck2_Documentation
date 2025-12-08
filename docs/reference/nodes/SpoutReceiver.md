# SpoutReceiver

Receives Spout textures (Windows only - see SyphonReceive for OSX) for further processing inside SPARCK

<figure markdown>
![SpoutReceiver Node](../../assets/images/nodes/SpoutReceiver.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `sender name` | - | select spout sender |
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

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/SpoutReceiver.md)*
