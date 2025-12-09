# CORE Patcher Setup

When you add the SPARCK CORE to a patcher via the context menu, it creates several interconnected objects. This page explains what each component does and which ones are essential.

![CORE overview in patcher](../assets/images/core/CORE_Overview.png)

## Essential Components

!!! warning "Do not remove"
    The following components are essential for SPARCK to function. Do not delete them or disconnect them from the toolbar.

### CORE Toolbar

![CORE Toolbar component](../assets/images/core/CORE_component_ToolBar.png)

The main component containing SPARCK's backbone functionality. The toolbar provides the user interface and coordinates all other components.

### sparck.device

![sparck.device component](../assets/images/core/CORE_component_ossia.png)

!!! warning "Do not remove"
    The `sparck.device sparck` object is essential for SPARCK. It manages all node properties. Do not delete it or disconnect it from the toolbar.

This object is a [fork of libossia](https://github.com/immersive-arts/Sparck2_libossia) and handles property management for all SPARCK nodes.

### pattrstorage

![pattrstorage component](../assets/images/core/CORE_component_pattrstorage.png)

!!! warning "Do not remove"
    The `pattrstorage` object is essential for saving Max object properties within the patcher hierarchy.

The [pattrstorage](https://docs.cycling74.com/reference/pattrstorage/) object uses Max's built-in system to store properties for any Max objects that have a [script](https://docs.cycling74.com/userguide/scripting_overview/) name and an [autopattr](https://docs.cycling74.com/reference/autopattr/) object within the patcher.

### savebang / closebang

![savebang and closebang components](../assets/images/core/CORE_component_savebang.png)

!!! warning "Do not remove"
    The `savebang` and `closebang` objects ensure properties are automatically stored when you save or close the patcher.

Together with the pattrstorage and sparck.device objects, these ensure that both pattr-managed and ossia-managed properties are automatically saved with your patcher.

- [savebang](https://docs.cycling74.com/reference/savebang/) — triggers when the patcher is saved
- [closebang](https://docs.cycling74.com/reference/closebang/) — triggers when the patcher is closed

### loadbang

![loadbang component](../assets/images/core/CORE_component_loadbang.png)

!!! warning "Do not remove"
    The `loadbang` object initializes SPARCK when the patcher opens. Without it, SPARCK won't start automatically.

The [loadbang](https://docs.cycling74.com/reference/loadbang/) executes the SPARCK CORE once the complete patch is loaded.

## Optional Components

### Workspace

![Workspace component](../assets/images/core/CORE_component_Workspace.png)

The **Workspace** is a [subpatcher](https://docs.cycling74.com/userguide/subpatchers/) provided for your convenience. It's the recommended place to add your SPARCK nodes, keeping the root patcher clean and organized.

![Workspace toolbar button](../assets/images/core/CORE_Toolbar_Patcher.png)

Click the Workspace icon in the toolbar to open it.

**Benefits of using the Workspace:**

- Keeps SPARCK nodes organized in one place
- Avoids clutter in the root patcher
- Easier to navigate complex projects

!!! note
    Using the Workspace is recommended but not required. You can place SPARCK nodes anywhere in the patcher hierarchy.
