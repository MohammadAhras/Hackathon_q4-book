# Quickstart Guide: ROS 2 Humanoid Robotics Education Module

## Prerequisites

Before starting this module, ensure you have:

1. Basic understanding of Python programming
2. Familiarity with command-line interfaces
3. Understanding of fundamental robotics concepts
4. A computer running Ubuntu 22.04 LTS or ROS 2 Docker container

## Environment Setup

### Option 1: Native Installation (Recommended for regular use)
1. Install ROS 2 Humble Hawksbill following the official installation guide
2. Set up your ROS 2 workspace:
   ```bash
   mkdir -p ~/ros2_ws/src
   cd ~/ros2_ws
   colcon build
   source install/setup.bash
   ```

### Option 2: Docker-based Environment (Recommended for initial exploration)
1. Install Docker on your system
2. Pull the ROS 2 Humble development image:
   ```bash
   docker pull osrf/ros:humble-desktop
   ```
3. Run the container:
   ```bash
   docker run -it osrf/ros:humble-desktop
   ```

## Setting up the Educational Module

1. Clone this repository:
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the Docusaurus development server:
   ```bash
   npm start
   ```

4. Your educational module will be available at http://localhost:3000

## Running the Examples

### ROS 2 Examples

1. Navigate to the examples directory:
   ```bash
   cd static/examples/ros2_nodes
   ```

2. Source your ROS 2 environment:
   ```bash
   source /opt/ros/humble/setup.bash  # If using native install
   # OR if using colcon workspace
   source ~/ros2_ws/install/setup.bash
   ```

3. Run a basic publisher/subscriber example:
   ```bash
   # Terminal 1 - start the publisher
   python3 publisher_node.py

   # Terminal 2 - start the subscriber
   python3 subscriber_node.py
   ```

### URDF Models

1. Navigate to the URDF models directory:
   ```bash
   cd static/examples/urdf_models
   ```

2. View the models using a URDF viewer or ROS 2 tools:
   ```bash
   # Install required dependencies if not already installed
   sudo apt install ros-humble-xacro ros-humble-joint-state-publisher-gui

   # Visualize the simple humanoid model
   ros2 run xacro xacro simple_humanoid.urdf
   ```

## Module Navigation

1. Start with Chapter 1: ROS 2 Fundamentals
2. Proceed to Chapter 2: Python Agents with rclpy
3. Complete with Chapter 3: Humanoid Modeling with URDF

Each chapter builds upon the previous one, so we recommend following the sequence for optimal learning.

## Interactive Components API

The educational module includes interactive components accessible via API endpoints:

1. Get example information:
   ```bash
   curl -X GET http://localhost:3000/api/examples/publisher_subscriber_basic
   ```

2. Run simulations (if backend is implemented):
   ```bash
   curl -X POST http://localhost:3000/api/simulation/run \
     -H "Content-Type: application/json" \
     -d '{"example_id": "publisher_subscriber_basic", "parameters": {}, "timeout": 30}'
   ```

## Troubleshooting

### Docusaurus Issues

**Problem**: Cannot start the documentation server
**Solution**: Make sure Node.js and npm are installed and dependencies are installed:
```bash
npm install
npm start
```

**Problem**: Pages not loading correctly
**Solution**: Clear Docusaurus cache:
```bash
npm run clear
npm start
```

### Common ROS 2 Issues

**Problem**: Command not found - `ros2`
**Solution**: Make sure you've sourced the ROS 2 setup file:
```bash
source /opt/ros/humble/setup.bash
```

**Problem**: Permission denied when running ROS 2 commands
**Solution**: Add your user to the docker group (if using Docker) or ensure ROS 2 is properly installed in your user space.

**Problem**: Python modules not found
**Solution**: Ensure you're using Python 3 and that the rclpy package is installed:
```bash
pip3 install roslibpy  # If not available through ROS 2 install
```

For additional help, check the detailed documentation in each chapter or visit the ROS 2 community forums.