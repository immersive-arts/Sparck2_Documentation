# SPARCK CORE

In order to make SPARCK work within Max and its patching environment, the SPARCK CORE [abstraction](https://docs.cycling74.com/userguide/abstractions/) needs to be in the root patcher. This is to make sure that all the properties of the nodes used inside the sub patchers are properly stored, which happens when the root patcher is saved.

!!! example "Tutorial"
    [Getting Started](../start/tutorials/01_Getting_Started/Getting_Started.md)

## CORE - TOOLBAR

![CORE_Toolbar](../assets/images/core/CORE_ToolBar.png)

The Core Toolbar contains the backbone of the SPARCK System. Its UI provides the needed access to its functionality.

| Title | ICON | Description |
|-------|------|-------------|
| Switch |![CORE_Toolbar](../assets/images/core/CORE_Toolbar_MainSwitch.png){width=100} | The Main Switch starts and stops the rendering engine. |
| FPS | ![CORE_Toolbar](../assets/images/core/CORE_Toolbar_FPS.png)| The FPS Widget shows the current running fps and the desired fps. Clicking on the 'fps'- button opens a live graph of the stability of the current frame rate. |
| Refresh | ![CORE_Toolbar](../assets/images/core/CORE_Toolbar_ManualRefresh.png){width=100} | It is possible to set the refresh of some Nodes to manual - this can reduces the performance load in some circumstances where there is only the need for an initial render pass - like a texture that is loaded from a file and only needs to be once send through the pipe line. The manual button will execute all those nodes afresh.|
| Workspace | ![CORE_Toolbar](../assets/images/core/CORE_Toolbar_Patcher.png){width=100} | As mentioned above, is a conveniece button to open the subpatcher 'Workspace' |
| 3DViewer | ![CORE_Toolbar](../assets/images/core/CORE_Toolbar_StageView.png){width=100} | Opens and enables the 3DViewer. |
| RenderGroup | ![CORE_Toolbar](../assets/images/core/CORE_Toolbar_StageView_RenderGroup.png)| Used to select which render group to render within the 3DViewer. |
| Preferences | ![CORE_Toolbar](../assets/images/core/CORE_Toolbar_Preferences.png){width=100} | Opens the preferences |
| Introspection | ![CORE_Toolbar](../assets/images/core/CORE_Toolbar_Reflection.png){width=100} | Allows you to see all the properties of all the SPARCK nodes and their values |

!!! info "3DViewer Mouse Navigation:"
    * rotation: <cmd> - mouse drag
    * shift: <shift> - mouse drag
    * zoom: <ctr> - mouse drag

## CORE - Patcher Setup

When putting the SPARCK CORE into a patcher via the context menu it would look like this.

![CORE](../assets/images/core/CORE_Overview.png)

---

![CORE_component_Toolbar](../assets/images/core/CORE_component_ToolBar.png)

The main component in play here is obviously the Toolbar that also contains the backbone functionality of SPARCK. But there are more max [objects](https://docs.cycling74.com/userguide/objects/) that are essential for SPARCK Core to be working:

---

![CORE_component_Toolbar](../assets/images/core/CORE_component_Workspace.png)

The **Workspace** patcher is a [subpatcher](https://docs.cycling74.com/userguide/subpatchers/) there for convenience.

![CORE_Toolbar_Patcher](../assets/images/core/CORE_Toolbar_Patcher.png)

Clicking this Icon in the toolbar opens the **Workspace** patcher.

---

![CORE_component_Toolbar](../assets/images/core/CORE_component_ossia.png)

The object [sparck.device sparck] is a [fork of libosssia](https://github.com/immersive-arts/Sparck2_libossia) and used for managing all the properties of the SPARCK nodes. This object is essential for the function of the SPARCK ecosystem and should not be removed or disconnected from the Toolbar in anyway. 

---

![CORE_component_Toolbar](../assets/images/core/CORE_component_pattrstorage.png)

The object [[pattrstorage](https://docs.cycling74.com/reference/pattrstorage/)] uses the Max buildin pattrstore system to store any max objexts within this patcher hierarchy that have a [script](https://docs.cycling74.com/userguide/scripting_overview/) name and an [[autopattr](https://docs.cycling74.com/reference/autopattr/)] object with the respective patcher.  

---

![CORE_component_Toolbar](../assets/images/core/CORE_component_savebang.png)

Together with the [[savebang](https://docs.cycling74.com/reference/savebang/)] and [[closebang](https://docs.cycling74.com/reference/closebang/)] objects, this setup makes sure that the pattr and ossia managed properties are automatically stored with the patcher.

---

![CORE_component_Toolbar](../assets/images/core/CORE_component_loadbang.png)

The [[loadbang](https://docs.cycling74.com/reference/loadbang/)] executes the SPARCK CORE once the complete patch is loaded. This is another essential object that should not be removed.
