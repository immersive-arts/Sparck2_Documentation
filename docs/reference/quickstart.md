# Quickstart

This guide walks you through creating your first SPARCK patch in just a few steps.

!!! note "Prerequisites"
    Make sure you have Max [installed]{ data-preview } and the SPARCK package properly [setup]{ data-preview } before continuing.

## Creating Your First Patch

### Step 1: Create an empty patcher

Open Max and create a new, empty patcher.

### Step 2: Add the SPARCK CORE

Right-click inside the patcher and choose **SPARCK → CORE** from the context menu.

![Max context menu showing SPARCK nodes](../assets/images/core/ContextMenuSelectNodes.png)

### Step 3: Save the patcher

Save the patcher into a new, empty folder. This folder will become your project folder.

### Step 4: Close and reopen the patcher

Close the patcher completely, then reopen it.

At this point, SPARCK has created the project folder structure and the CORE is ready.

```
Start with empty patcher
         ↓
Select CORE from context menu
         ↓
Save patcher in new folder
         ↓
Close the patcher
         ↓
Reopen the patcher
         ↓
SPARCK is open for business ✓
```

## What Happens Next?

When you reopen the patcher, you'll notice that SPARCK has generated a folder structure next to your patch file. This is where all your project assets will live. See [Projects & File Structure](file_structure.md) for details.

You can now start adding SPARCK Nodes to build your project.

## Adding Your First Nodes

Once you've reopened your SPARCK patcher, you can start adding Nodes:

1. It's recommended to use the provided **Workspace** subpatcher (click the Workspace button in the CORE toolbar), but you can place nodes anywhere in the patcher hierarchy.

2. To add a node, right-click in a patcher and select the node you need from the SPARCK section of the context menu.

!!! tip "Learn more"
    - See [The Anatomy of a SPARCK Node](node_anatomy.md) for a detailed overview of node UI and behavior.
    - See [Nodes & Connections](nodes_and_connections.md) to understand how to wire nodes together.
    - See [CORE Overview](core_overview.md) to learn about the SPARCK CORE toolbar and components.

[installed]: ../start/setup/prerequisites.md
[setup]: ../start/setup/installation.md