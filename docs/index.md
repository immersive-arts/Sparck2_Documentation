# Welcome to
<style>
:root {
  --sparck-primary: #00d4aa;
  --sparck-secondary: #6366f1;
  --sparck-accent: #f43f5e;
  --sparck-dark: #0f172a;
}

.sparck-hero {
  background: linear-gradient(135deg, var(--sparck-dark) 0%, #1a1f35 50%, var(--sparck-dark) 100%);
  border-radius: 1.5rem;
  padding: 4rem 2rem;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.sparck-hero::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 20% 80%, rgba(0, 212, 170, 0.15) 0%, transparent 50%),
    radial-gradient(circle at 80% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 50%);
  pointer-events: none;
}

.sparck-hero-content {
  position: relative;
  z-index: 1;
}

.sparck-logo {
  font-size: 4.5rem;
  font-weight: 800;
  letter-spacing: -0.04em;
  background: linear-gradient(135deg, var(--sparck-primary) 0%, var(--sparck-secondary) 50%, var(--sparck-accent) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.5rem;
  text-shadow: 0 0 80px rgba(0, 212, 170, 0.5);
}

.sparck-tagline {
  font-size: 1.15rem;
  color: #94a3b8;
  font-weight: 400;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  margin-bottom: 1.5rem;
}

.sparck-description {
  font-size: 1.25rem;
  color: #e2e8f0;
  max-width: 600px;
  margin: 0 auto;
  line-height: 1.7;
}
</style>

<div class="sparck-hero">
  <div class="sparck-hero-content">
    <img src="./assets/icons.iconset/icon_512x512.png" alt="SPARCK Logo" style="width: 200px; margin-bottom: 1rem;">
    <div class="sparck-logo">SPARCK</div>
    <div class="sparck-tagline">SPatial Augmented Reality Construction Kit</div>
    <p class="sparck-description">
      A powerful node-based toolkit for projection mapping, multi-projector calibration, and  <br>immersive spatial installations <br> -- <br> built for Max/MSP.
    </p>
  </div>
</div>


[Get Started :material-rocket-launch:](./start/tutorials/01_Getting_Started/Getting_Started.md){ .md-button .md-button--primary }
[Node Reference :material-book-open-variant:](./reference/node_anatomy.md){ .md-button }
[GitHub :fontawesome-brands-github:](https://github.com/immersive-arts/Sparck2){ .md-button }

---

## What is SPARCK?

Create, calibrate and run advanced spatial augmented reality and projection-mapping setups – directly inside Max.

Whether you're lighting up a single wall, mapping projections onto complex surfaces, calibrating multi-projector setups or building a multi-projector interactive immersive space, SPARCK brings together real-time 3D rendering, projection mapping, tracking, scripting and multi-display output into one cohesive workflow and provides an intuitive workflow with real-time 3D preview.


<div class="grid cards" markdown>

-   :material-projector:{ .lg .middle } **Multi-Projector Calibration**

    ---

    Calibrate multiple projectors using OpenCV-based algorithms. Define calibration vertices on 3D models and achieve pixel-perfect alignment with realtime calculated soft-edge blending.

-   :material-cube-scan:{ .lg .middle } **Spatial Mapping**

    ---

    Project onto any surface with Canvas nodes. Support for OBJ, Collada, and 30+ 3D formats with real-time texture baking and shader effects.

-   :material-connection:{ .lg .middle } **Node-Based Workflow**

    ---

    Build complex projection systems visually by connecting specialized nodes. Each node handles a specific task — from input to transformation to output.

-   :material-monitor-eye:{ .lg .middle } **Real-Time 3D Preview**

    ---

    Visualize your entire projection setup in the built-in 3DViewer. See projector frustums, calibration accuracy, and content placement before going live.

-   :material-broadcast:{ .lg .middle } **Live Input Integration**

    ---

    Receive real-time content via Spout and Syphon from engines like TouchDesigner, Unity, Unreal, or Notch. Full support for HAP video and point-clouds via rgb-d videos.

-   :material-script-text:{ .lg .middle } **QueScript Automation**

    ---

    Automate shows with SPARCK's built-in scripting language. Trigger cues, animate parameters, and orchestrate complex sequences with precision timing.

</div>

---

## Core Capabilities

<div class="grid cards" markdown>

-   :material-tune-vertical: Corner Pin Mapping
-   :material-vector-polygon: Mesh Warping
-   :material-gradient-horizontal: Soft-Edge Blending
-   :material-camera-control: Camera Calibration
-   :material-cube-send: Texture Projection
-   :material-motion-outline: Motion Tracking
-   :material-access-point: OSC Control
-   :material-axis-arrow: 3D Transformations

</div>

---

## Getting Started

!!! tip "Prerequisites"
    Make sure you have Max installed and the SPARCK package properly set up before continuing.

=== "Step 1"

    **Install Max + SPARCK**
    
    Download Max from Cycling '74 and install the SPARCK package from the Package Manager.

=== "Step 2"

    **Create a Patcher**
    
    Open Max, create a new patcher, and add the SPARCK CORE from the context menu (right-click → SPARCK → CORE).

=== "Step 3"

    **Save & Reopen**
    
    Save the patcher into a new, empty folder. Close and reopen it — SPARCK will create the project folder structure.

=== "Step 4"

    **Add Nodes & Calibrate**
    
    Build your projection system by adding nodes for input, processing, calibration, and output. Use the Beamer node to calibrate projectors.

[:octicons-arrow-right-24: Follow the Quickstart Guide](./start/tutorials/01_Getting_Started/Getting_Started.md){ .md-button .md-button--primary }

---

## Project Organization

When you save a SPARCK patcher, it automatically creates a portable project structure:

```
your-project/
├── your_sparck_patcher.maxpat
├── _assets/
│   ├── _textures/          # Images, cubemaps, volumes
│   ├── _videos/            # Video files (HAP recommended)
│   ├── _models/            # 3D models for projection surfaces
│   ├── _shaders/           # Custom GLSL shaders
│   ├── _projectors/        # Projector calibration data
│   ├── _scripts/_ques/     # QueScript automation files
│   └── ...
└── _export/                # Output files
```

Everything stays self-contained, making projects easy to move between machines.

[:octicons-arrow-right-24: Learn about File Structure](./reference/file_structure.md){ .md-button }

---

## Node Categories

SPARCK organizes its nodes into logical categories:

| Category | Purpose | Key Nodes |
|----------|---------|-----------|
| **Input** | Bring content into SPARCK | Texture, Video, SpoutReceiver, SyphonReceiver |
| **Canvas & Space** | Define projection surfaces | Canvas, Model, Grid, SkyBox |
| **Mapping** | Map content to outputs | CornerPin, MeshWarp, ViewPort |
| **Calibration** | Configure projectors | Beamer, CalibrationCross |
| **Effects** | Process and blend | SpatialShadery, BlendSoftedge, ShaderPointCloud |
| **Transform** | Position elements in 3D | TfmNode, TfmLookAt, TfmMirror |
| **Output** | Send to displays | Window, SpoutSender, SyphonSender |
| **Utility** | Scripting and control | QueScript, Hook |

[:octicons-arrow-right-24: Browse All Nodes](./reference/node_anatomy.md){ .md-button }

---

## Use Cases

<div class="grid cards" markdown>

-   :material-cube-outline:{ .lg .middle } **Projection Mapping**

    ---

    Map visuals onto buildings, stages, sculptures, and architectural elements with precise calibration.

-   :material-floor-plan:{ .lg .middle } **Floor Projections**

    ---

    Create interactive floor installations with multiple overhead projectors and soft-edge blending.

-   :material-panorama-sphere:{ .lg .middle } **Immersive Rooms**

    ---

    Build 360° immersive environments with synchronized multi-wall projection.

-   :material-motion-play:{ .lg .middle } **Live Performances**

    ---

    Integrate with live visual engines for real-time show control and cue-based automation.

</div>

---

## Ready to Create?

Jump into the documentation and start building your first spatial projection.

[Start the Quickstart :material-arrow-right:](./start/tutorials/01_Getting_Started/Getting_Started.md){ .md-button .md-button--primary }

---

<div class="grid cards" markdown>

-   :material-video-box:{ .lg .middle } **Tutorials**

    ---

    Step-by-step video guides for common setups
    
    [:octicons-arrow-right-24: Watch Now](./start/tutorials/videos.md)

-   :material-forum:{ .lg .middle } **Community**

    ---

    Ask questions and share projects
    
    [:octicons-arrow-right-24: GitHub Discussions](https://github.com/immersive-arts/Sparck2/discussions)

-   :material-bug:{ .lg .middle } **Report Issues**

    ---

    Found a bug? Let us know
    
    [:octicons-arrow-right-24: Open an Issue](./contributing/reporting-a-bug.md)

-   :material-source-pull:{ .lg .middle } **Contribute**

    ---

    Help improve SPARCK
    
    [:octicons-arrow-right-24: Contribution Guide](./contributing/index.md)

</div>

---

!!! info "Developed by Immersive Arts Space"
    SPARCK is developed and maintained by the [Immersive Arts Space](http://immersive-arts.ch) at Zurich University of the Arts (ZHdK). It's designed for artists, designers, and technicians working with spatial media.