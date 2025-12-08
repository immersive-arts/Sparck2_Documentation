# ShaderBlur

Blur Textures

<figure markdown>
![ShaderBlur Node](../../assets/images/nodes/ShdrBlur.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `blur` | - | blur amount |
    | `iterations` | - | how many times the blur operation is applied (higher number gives better results but is more resource intensive) |
    | `base` | - | base (each iteration increases the blur, the base controlls how much more the amount is increased for each iteration) |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |
    | main | texture | main texture |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | main | texture | main texture blured |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/ShaderBlur.md)*
