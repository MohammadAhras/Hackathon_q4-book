# Quickstart Guide: Digital Twin Simulation with Gazebo & Unity

## Prerequisites

Before starting this module, ensure you have:

1. Basic understanding of robotics concepts and simulation
2. Familiarity with command-line interfaces
3. Understanding of 3D visualization concepts
4. A computer capable of running Gazebo and Unity (minimum 8GB RAM recommended)

## Environment Setup

### Option 1: Native Installation (Recommended for regular use)
1. Install ROS 2 Humble Hawksbill following the official installation guide
2. Install Gazebo Harmonic (or Fortress if using with ROS 2 Humble):
   - Follow the installation guide at: https://gazebosim.org/docs/harmonic/install
3. Install Unity 2022.3 LTS Hub from: https://unity.com/download
4. Set up your ROS 2 workspace:
   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws
   colcon build
   source install/setup.bash
   ```

### Option 2: Docker-based Environment (Recommended for initial exploration)
1. Install Docker on your system
2. Pull the ROS 2/Gazebo development image:
   ```bash
   docker pull osrf/ros:humble-desktop-full
   ```
3. Run the container with GUI support:
   ```bash
   docker run -it \
     --env="DISPLAY" \
     --env="QT_X11_NO_MITSHM=1" \
     --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
     --privileged \
     --device=/dev/dri:/dev/dri \
     osrf/ros:humble-desktop-full
   ```

## Running the Examples

1. Clone this repository:
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. Navigate to the examples directory:
   ```bash
   cd static/examples/gazebo_worlds
   ```

3. Source your ROS 2 environment:
   ```bash
   source /opt/ros/humble/setup.bash  # If using native install
   # OR if using colcon workspace
   source ~/ros2_ws/install/setup.bash
   ```

4. Run a basic Gazebo simulation:
   ```bash
   # Launch the basic physics example
   gazebo --verbose basic_physics.world
   ```

5. For Unity examples:
   - Open Unity Hub
   - Import the provided Unity scenes from `static/examples/unity_scenes`
   - Run the scenes to view the visual environment

## Module Navigation

1. Start with Chapter 1: Physics Simulation with Gazebo
2. Proceed to Chapter 2: High-Fidelity Environments with Unity
3. Complete with Chapter 3: Sensor Simulation

Each chapter builds upon the previous one, so we recommend following the sequence for optimal learning.

## Simulation Setup and Running Examples

### Setting up and using Gazebo examples

1. Navigate to the Gazebo examples directory:
   ```bash
   cd static/examples/gazebo_worlds
   ```

2. Source your ROS 2 environment:
   ```bash
   source /opt/ros/humble/setup.bash  # If using native install
   # OR if using colcon workspace
   source ~/ros2_ws/install/setup.bash
   ```

3. Run a basic Gazebo simulation:
   ```bash
   # Launch the basic physics example
   gazebo --verbose basic_physics.world
   ```

### Setting up and using Unity examples

1. Open Unity Hub
2. Create a new 3D project or open an existing one
3. Import the provided Unity scenes from `static/examples/unity_scenes`
4. To run the scenes:
   - Select the scene file in the Project panel
   - Press the Play button in the Unity editor
   - Or go to File > Build and Run to create an executable

### Setting up and using sensor configuration examples

1. Navigate to the sensor configuration directory:
   ```bash
   cd static/examples/sensor_configs
   ```

2. Use these configuration files when setting up your sensors in Gazebo models or ROS 2 nodes
3. Each configuration file contains realistic parameters for the respective sensor type

## Troubleshooting

### Common Issues

**Problem**: Gazebo crashes or doesn't start properly
**Solution**: Ensure your graphics drivers are up to date and you have sufficient RAM.

**Problem**: Unity scenes don't load properly
**Solution**: Verify that your Unity version matches the project requirements (2022.3 LTS).

**Problem**: Sensor data doesn't appear realistic
**Solution**: Check the sensor configuration files in `static/examples/sensor_configs`.

For additional help, check the detailed documentation in each chapter or visit the Gazebo and Unity community forums.