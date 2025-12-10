---
icon: lucide/bug-play
---

# Reproduction

A reproduction is a simplified version of a bug that demonstrates the specific scenario in which the bug occurred. It includes all necessary minimal settings and instructions and should be as simple as possible while still demonstrating the issue. It also makes sure that the developer trying to fix the bug can easily and quickly reproduce the issue on their own machine. This helps immensily to bring a fix for the bug faster.

Issues containing a minimal reproduction have been solved within a few days which shows that investing time in creating a reproduction is worth the effort. What is more, the process of creating a reproduction can sometimes
already help identify where the problem lies, so you may not even need to file a bug report if, for example, it is due to a mistake made in the configuration or in a customization.

## Create a reproduction

### Update the environment

The first step in producing a reproduction is to making sure you are running the latest versions of SPARCK and MAX. 

### Create new minimal project

To ensure that your reproduction does not contain any customizations you may have in your project, please start with a fresh SPARCK project as desicribed in the [Quick Start](../../start/quickstart.md) guide.

### Add only what is needed

Work through the patcher and leave only those objects and SPARCK nodes that are required to reproduce the issue you are facing. Add just enough example content to be able to show the behavior that you think is wrong. Repeat this step until the bug you want to report can be observed.

### Document the environment

Document what packages are installed in your virtual environment by opening the **About** dialog in Max and click on **Copy Support Information to clipboard**. Paste this information into a text file and include it in your reproduction package.

### Double check to be sure

As a last step, before packing everything into a `.zip` file, double-check all settings and documents if they are essential to the reproduction, which means that the bug does not occur when they are omitted.

### Pack up and submit

Pack up the project directory in a `.zip` file.