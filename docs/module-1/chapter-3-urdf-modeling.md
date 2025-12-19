# Chapter 3: Humanoid Modeling with URDF

## Introduction to URDF

Unified Robot Description Format (URDF) is an XML-based format used in ROS to describe robot models. URDF allows you to define the physical and visual properties of a robot, including its links, joints, and sensors. This description is essential for both simulation and real-world robot control.

## Understanding Robot Anatomy

Humanoid robots have specific anatomical features that need to be properly represented in URDF:

- **Torso**: The main body of the robot
- **Head**: Contains sensors like cameras and IMUs
- **Arms**: With multiple joints for manipulation tasks
- **Legs**: With joints for locomotion
- **End effectors**: Such as hands for grasping

## Links, Joints, and Sensors

### Links

Links represent the rigid parts of the robot. Each link has:

- Physical properties (mass, inertia, center of mass)
- Visual properties (shape, color, texture for visualization)
- Collision properties (shape for collision detection)

### Joints

Joints connect links and define how they move relative to each other. Common joint types include:

- **Revolute**: Rotational joint with limits
- **Continuous**: Rotational joint without limits
- **Prismatic**: Linear sliding joint
- **Fixed**: No movement (used for attaching sensors)
- **Floating**: 6 DOF joint (rarely used)

### Sensors

Sensors in URDF describe where sensors are mounted on the robot. They include:

- **Gazebo plugins**: For simulation
- **ROS interfaces**: For real robot communication
- **Physical properties**: Position and orientation on the robot

## Creating a Humanoid Robot Model

When building a humanoid robot model, follow these steps:

1. **Start with the base**: Usually the torso or pelvis
2. **Add major body parts**: Head, arms, legs
3. **Include joints**: With proper limits and dynamics
4. **Add sensors**: Cameras, IMUs, force/torque sensors
5. **Validate the model**: Check for collisions and proper kinematics

### Torso Definition

The torso is typically the root of the robot model and contains:

- Main computer and power systems
- IMU sensors for orientation
- Possibly cameras in the head

### Limb Construction

Each limb follows a similar pattern:

- Define each segment as a link
- Connect segments with appropriate joints
- Position each joint according to the robot's kinematics
- Add end effectors where appropriate

## URDF's Role in Simulation and Control

### Simulation

URDF models are crucial for:

- Physics simulation in Gazebo
- Visualization in RViz
- Testing robot behaviors before deployment
- Generating synthetic training data for AI

### Real Robot Control

URDF models enable:

- Forward and inverse kinematics
- Motion planning algorithms
- Robot state visualization
- Sensor fusion algorithms

## Practical Example: Simple Humanoid Model

In this section, we'll create a simple humanoid model with:

- A torso with a head
- Two arms with simple hands
- Two legs
- Basic sensors

We'll define each component in URDF format and explain the rationale behind each design decision.

## Advanced URDF Concepts

### Transmission Elements

Transmission elements define how actuators connect to joints, which is important for simulation and real robot control.

### Gazebo-Specific Tags

Tags like `<gazebo>` allow you to specify simulation-specific properties without affecting the core robot description.

### Materials and Colors

Using materials and colors makes your robot model more visually appealing and easier to identify in visualization tools.

## Best Practices for URDF Modeling

When creating humanoid robot models in URDF:

1. **Start Simple**: Begin with a basic skeleton and add complexity gradually
2. **Use Proper Units**: Consistently use meters for lengths and kilograms for mass
3. **Validate Mass and Inertia**: Ensure physical properties are realistic
4. **Test in Simulation**: Verify that your model behaves correctly in simulation
5. **Document Design Decisions**: Keep track of why certain modeling choices were made

## Exercises

Now that you've learned about humanoid modeling with URDF, try these exercises to reinforce your understanding:

### Exercise 1: Visualize the Humanoid Models
1. Use a URDF viewer to visualize the simple humanoid model
2. Load the model with sensors and compare the differences
3. Experiment with different visualization tools in ROS 2

### Exercise 2: Modify the Robot Model
1. Add another joint to one of the limbs
2. Change the physical properties (mass, size) of a link
3. Adjust the joint limits to change the robot's range of motion

### Exercise 3: Add New Sensors
1. Add a LIDAR sensor to the robot model
2. Include the sensor in both the URDF and Gazebo simulation
3. Test that the sensor publishes data correctly

### Exercise 4: Create a Custom Robot
1. Design a completely new humanoid robot with different proportions
2. Ensure all physical properties are realistic
3. Validate the model using URDF checking tools

## Summary

In this chapter, you've learned how to model humanoid robots using URDF. You now understand how to represent robot anatomy with links and joints, include sensors, and use URDF models for both simulation and real-world robot control.

[Previous: Chapter 2 - Python Agents with rclpy](./chapter-2-python-agents.md)

This completes Module 1 of the AI-Spec Driven Technical Book. You now have a foundation in ROS 2 fundamentals, Python agents with rclpy, and humanoid robot modeling with URDF. You're well-prepared to apply AI algorithms to control humanoid robots using the ROS 2 middleware.