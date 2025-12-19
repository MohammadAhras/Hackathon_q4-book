# Data Model: Digital Twin Simulation with Gazebo & Unity

## Educational Content Entities

### Module
- **Name**: Module identifier and title
- **Description**: Overview of the module's learning objectives
- **Target Audience**: AI and robotics students building simulated physical environments
- **Learning Path**: Sequence of chapters and prerequisites
- **Assessment Methods**: How student progress is measured
- **Duration**: Estimated time to complete the module

### Chapter
- **Title**: Chapter name and topic
- **Learning Objectives**: Specific skills/knowledge to be acquired
- **Content Sections**: Individual topics within the chapter
- **Code Examples**: Associated runnable examples
- **Exercises**: Practical tasks for students
- **Assessment Questions**: Knowledge check questions

### Content Section
- **Title**: Section name and topic
- **Type**: Text, code example, diagram, video, etc.
- **Content**: The actual text/description
- **Difficulty Level**: Beginner, intermediate, advanced
- **Prerequisites**: What knowledge is required before this section
- **Related Sections**: Cross-references to related content

### Simulation Example
- **Title**: Name of the simulation example
- **Type**: Gazebo world, Unity scene, or ROS 2 configuration
- **Purpose**: What concept the example demonstrates
- **Files**: List of source files that constitute the example
- **Dependencies**: Gazebo/Unity/ROS 2 packages required
- **Execution Instructions**: How to run the example
- **Expected Output**: What students should see when running

### Exercise
- **Title**: Name of the exercise
- **Description**: What the student should accomplish
- **Difficulty Level**: Beginner, intermediate, advanced
- **Required Resources**: Hardware, software, or other materials
- **Submission Requirements**: What needs to be submitted
- **Grading Criteria**: How the exercise will be assessed

## Simulation-Specific Entities

### Gazebo World
- **Name**: Identifier for the Gazebo world
- **Description**: What the environment simulates
- **Models**: List of robot and object models in the world
- **Physics Properties**: Gravity, friction, and other physical parameters
- **Sensor Configurations**: Types and positions of sensors in the world
- **Lighting**: Environmental lighting setup

### Unity Scene
- **Name**: Identifier for the Unity scene
- **Description**: What the scene visualizes
- **Objects**: List of 3D models and their properties
- **Materials**: Textures, lighting, and visual properties
- **Cameras**: Camera positions and configurations
- **Lighting**: Scene lighting setup
- **Interaction Points**: Areas where user interaction is possible

### Sensor Configuration
- **Type**: LiDAR, depth camera, IMU, etc.
- **Model**: Specific sensor being simulated (e.g., Hokuyo UST-10LX)
- **Parameters**: Field of view, range, resolution, noise characteristics
- **Mounting Position**: Where on the robot the sensor is placed
- **Orientation**: Rotation and alignment of the sensor
- **Output Format**: Data format and structure of the sensor output

## Navigation Entities

### Navigation Menu
- **Menu Items**: List of all modules and their chapters
- **Current Location**: Which item is currently selected
- **Breadcrumb Path**: Path to current location for easy navigation
- **Next/Previous Links**: Links to adjacent items in learning sequence

### Search Index
- **Content ID**: Unique identifier for each content piece
- **Title**: Searchable title
- **Keywords**: Additional search terms
- **Category**: Module, chapter, or section classification
- **Metadata**: Difficulty, prerequisites, related topics