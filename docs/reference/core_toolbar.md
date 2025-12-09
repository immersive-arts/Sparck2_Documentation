# CORE Toolbar

The CORE Toolbar provides quick access to SPARCK's main functions. It appears at the top of the CORE abstraction.

![CORE Toolbar](../assets/images/core/CORE_ToolBar.png)

## Toolbar Controls

| Title | Icon | Description |
|-------|------|-------------|
| **Switch** | ![Main switch](../assets/images/core/CORE_Toolbar_MainSwitch.png){width=100} | Starts and stops the rendering engine. |
| **FPS** | ![FPS display](../assets/images/core/CORE_Toolbar_FPS.png) | Shows current and target frame rate. Click the 'fps' button to open a live graph showing frame rate stability. |
| **Refresh** | ![Manual refresh](../assets/images/core/CORE_Toolbar_ManualRefresh.png){width=100} | Triggers a refresh for nodes set to manual update mode. Useful for reducing performance load when nodes only need an initial render pass (e.g., a texture loaded from file). |
| **Workspace** | ![Workspace button](../assets/images/core/CORE_Toolbar_Patcher.png){width=100} | Opens the Workspace subpatcher where you can organize your SPARCK nodes. |
| **3DViewer** | ![3DViewer button](../assets/images/core/CORE_Toolbar_StageView.png){width=100} | Opens and enables the 3DViewer for previewing your scene. |
| **RenderGroup** | ![Render group selector](../assets/images/core/CORE_Toolbar_StageView_RenderGroup.png) | Selects which render group to display in the 3DViewer. |
| **Preferences** | ![Preferences button](../assets/images/core/CORE_Toolbar_Preferences.png){width=100} | Opens the SPARCK preferences panel. |
| **Introspection** | ![Introspection button](../assets/images/core/CORE_Toolbar_Reflection.png){width=100} | Shows all SPARCK node properties and their current values. Useful for scripting and debugging. |

## 3DViewer Navigation

When the 3DViewer is open, use these mouse controls to navigate:

| Action | Control |
|--------|---------|
| **Rotation** | ++cmd++ + mouse drag |
| **Shift** | ++shift++ + mouse drag |
| **Zoom** | ++ctrl++ + mouse drag |
