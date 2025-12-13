# Projects

When you create a SPARCK patcher, SPARCK generates its own folder structure next to where the patcher is stored. This keeps your project self-contained and portable.

## Project Folder Structure

```
projectPath/
├── your_sparck_patcher.maxpat
├── _assets/
│   ├── _scripts/
│   │   └── _ques/
│   ├── _shaders/
│   │   └── _raymarch/
│   ├── _textures/
│   │   ├── _volumes/
│   │   └── _cubemaps/
│   ├── _videos/
│   │   └── _hap/
│   ├── _materials/
│   ├── _warps/
│   ├── _models/
│   │   ├── _calib/
│   │   └── _warps/
│   ├── _projectors/
│   │   └── _calib/
│   ├── _nodes/
│   ├── _paths/
│   │   ├── _ledstrips/
│   │   └── _animations/
│   └── _patchers/
├── _tmp/
└── _export/
    ├── _textures/
    ├── _projectors/
    └── _warps/
```

## Why This Structure?

While standard Max objects find their content anywhere in the search path, SPARCK nodes expect files in specific folders. This design ensures your SPARCK project is always complete when you move the project folder — similar to and compatible with Max [Projects](https://docs.cycling74.com/userguide/projects/).

## Key Folders

| Folder | Purpose |
|--------|---------|
| `_assets/` | Main container for all project assets |
| `_scripts/_ques/` | QueScript files |
| `_shaders/` | Custom shader files |
| `_textures/` | Image textures, including volumes and cubemaps |
| `_videos/` | Video files, with a subfolder for HAP-encoded videos |
| `_materials/` | Material definitions |
| `_warps/` | Warp mesh files |
| `_models/` | 3D model files |
| `_projectors/` | Projector calibration data |
| `_nodes/` | Custom node definitions |
| `_paths/` | Path data for LED strips and animations |
| `_patchers/` | Additional Max patchers |
| `_tmp/` | Temporary files |
| `_export/` | Some nodes can export files. When you use this feature, you will find those files here |

## Finding the Right Folder

Each SPARCK node's tooltip indicates:

- Which folder it looks into
- Which file types are supported

!!! tip "Asset discovery"
    If you place a file in the correct folder but it doesn't appear in the node's menu, click the **refresh** button next to the file selector to rescan the folders.

## Best Practices

- **Keep everything inside the project folder**. Any other approach wont work.
- **Use the provided subfolders**. Inside those folders you can organize your own structure
- **Check tooltips** when unsure where to place specific file types
