# CORE Overview

The SPARCK CORE is the central component that makes SPARCK work within Max. It must be placed in the root patcher to ensure all node properties are properly stored when you save your project.

!!! example "Tutorial"
    [Getting Started]{ data-preview }

[Getting Started]: ../start/tutorials/01_Getting_Started/Getting_Started.md

## What the CORE Does

The CORE provides:

- **Rendering engine control** — Start and stop the SPARCK rendering pipeline
- **Property management** — Stores and recalls all node settings
- **Project organization** — Creates and maintains the project folder structure
- **3D preview** — Built-in 3DViewer for monitoring your scene
- **Centralized access** — Quick access to workspace, preferences, and introspection tools

## CORE Placement

The CORE must be placed in the **root patcher** of your project. While it might technically work in other locations, this has not been tested and is not recommended.

!!! warning "Important"
    The CORE abstraction must remain in the root patcher. Moving it to a subpatcher may cause property storage to fail.

## Adding SPARCK to an Existing Patcher

It's possible to add the SPARCK CORE to an existing Max patcher. However, be aware that once you save the patcher, SPARCK will create its folder structure next to the patcher file.

For cleanest results, start with an empty patcher in a new folder, as described in the [Quickstart](quickstart.md) guide.

## Saving and Loading

SPARCK automatically saves all node properties when you save the root patcher. This happens through a combination of:

- The `sparck.device` object (manages SPARCK node properties)
- The `pattrstorage` object (manages Max object properties)
- `savebang` and `closebang` objects (trigger saving at the right moment)
- `loadbang` (initializes SPARCK when the patcher opens)

You don't need to interact with these objects directly — they work automatically as long as they remain connected to the CORE toolbar.

## Next Steps

- Learn about the [CORE Toolbar](core_toolbar.md) interface
- Understand the [CORE Patcher Setup](core_patcher_setup.md) and its essential components
