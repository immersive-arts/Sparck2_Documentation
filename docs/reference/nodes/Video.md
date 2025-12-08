# Video

Video node can playback a variety of video codecs. Most prominently Mov, Avi, Mpg Mpg4 and Hap

Please notice: 
If you want to use the HAP codec running on the GPU, place the video inside the ~/_assets/_videos/_hap folder (recommended). Otherwise the HAP codec will run on the CPU (slower).

<figure markdown>
![Video Node](../../assets/images/nodes/Video.png){ width="300" }
</figure> 


## Reference

The following properties can be configured for this node:

=== "Properties"

    | Property | Type | Description |
    |----------|------|-------------|
    | `file` | - | load and playback file |
    | `dispose` | - | dispose the loaded file |
    | `start` | - | start the video file |
    | `stop` | - | stop the video file |
    | `loop` | - | loop mode |
    | `render pass` | - | select render pass |
    | `rate` | - | playback rate (default = 1) |
    | `autostart` | - | autostart the video after loading it |
    | `volume` | - | if the video has a audio track, adjust it here. |
    | `unique` | - | unique |
    | `frame` | - | choose framenumber |
    | `interp` | - | interpolate |
    | `cache_size` | - | sets the cache size for the video engine. Reverse playback stutters may be the result of insufficient cache_size. Care should be taken when adjusting the cache_size, if the frame cache exceeds the available memory, the application may crash. |
    | `colormode` | - | colormode |
    | `loopreport` | - | reports the end of a loop |
    | `frame endtrigger` | - | sets the trigger in number of frames before the video has reached its end |
    | `time endtrigger` | - | sets the trigger in milliseconds before the video has reached its end |
    | `framereport` | - | reports framenumber and drives the playbar. CAREFULL!! the playbar is resource hungry. |
    | `timereport` | - | reports time in milliseconds. |
    | `filewatch` | - | reloads automatically file if file changes. |

=== "Inlets"

    | Inlet      | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | direct | message | direct messages to control video: enable &#124; start &#124; stop &#124; dispose &#124; frame refresh &#124; frame time &#124; frame duration &#124; frame framecount &#124; frame seekframe &#124; frame seeknotify |
    | properties | properties | properties &#124; use message [set &lt;propertyPath> &lt;value(s)>] (without node/&lt;nodeName> at the beginning) to set internal properties |

=== "Outlets"

    | Outlet     | Type          | Description                            |
    |------------|---------------|----------------------------------------|
    | video | texture | video texture |
    | audio | audio | audio left |
    | audio | audio | audio right |
    | dump | message | dump |


---

*Last updated: 2025-12-01 | [Edit this page on GitHub](https://github.com/immersive-arts/Sparck2/edit/main/docs/nodes/Video.md)*
