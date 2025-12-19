# Chapter 2: Python Agents with rclpy

## Introduction to rclpy

rclpy is the Python client library for ROS 2. It provides a Python API that allows you to create ROS 2 nodes, publish and subscribe to topics, make service calls, and create action clients and servers. With rclpy, you can leverage Python's expressiveness and vast ecosystem of libraries to build sophisticated robotic applications.

## Creating ROS 2 Nodes with Python

In this chapter, we'll explore how to create ROS 2 nodes using Python and the rclpy library. We'll build on the concepts introduced in Chapter 1 and demonstrate how to connect AI logic to robot controllers.

### Basic Node Structure

The basic structure of a ROS 2 Python node includes:

1. Import statements for rclpy and message types
2. A Node class that inherits from rclpy.node.Node
3. The main function that initializes the ROS 2 client library and spins the node

### Initializing a ROS 2 Node

To create a ROS 2 node in Python, you must:

1. Initialize the rclpy library
2. Create an instance of your custom node class
3. Run the node using rclpy.spin() or spin_until_future_complete()
4. Cleanly shut down when done

## Connecting AI Logic to Robot Controllers

One of the primary benefits of ROS 2 is its ability to connect high-level AI logic with low-level robot controllers. This connection enables AI agents to send commands to robots and receive sensor data in a standardized way, regardless of the specific hardware implementation.

### Publishing Sensor Data

In many robotic applications, you'll need to publish sensor data from your AI node to other parts of your robot system. This might include:

- Camera images
- LIDAR scans
- IMU data
- Joint states
- Odometry information

### Subscribing to Commands

Your AI node might also subscribe to commands from other parts of your system, such as:

- Path planning outputs
- Navigation goals
- Direct motion commands
- Task-level instructions

### Service Requests and Responses

For more synchronous operations, you might use ROS 2 services to:

- Request specific robot behaviors
- Query robot state
- Trigger calibration procedures
- Request planning services

## Advanced rclpy Concepts

### Parameters

Parameters in ROS 2 allow you to configure your nodes at runtime. They can be set at launch time, or changed dynamically while the node is running. Parameters are especially useful for AI agents that need to adjust their behavior based on environmental conditions.

### Timers

Timers allow you to execute callbacks at regular intervals. This is useful for AI agents that need to periodically process sensor data or send commands to the robot at a specific frequency.

### Quality of Service (QoS)

QoS settings let you configure how messages are delivered in terms of reliability, durability, and history. This is particularly important for AI agents that have specific requirements for data freshness and delivery guarantees.

## Practical Example: AI Controller Node

To demonstrate connecting AI logic to robot controllers, we'll implement an example AI controller node that:

1. Subscribes to sensor data from the robot
2. Processes this data using a simple AI algorithm
3. Publishes commands back to the robot
4. Uses parameters to adjust the AI behavior at runtime

We'll build upon the basic publisher/subscriber examples from Chapter 1 to create more complex behaviors.

## Best Practices for AI-Robot Integration

When connecting AI logic to robot controllers, consider these best practices:

1. **Ensure Safety**: Implement safety checks to prevent harmful robot behaviors
2. **Handle Failures**: Plan for sensor failures, communication issues, and other potential problems
3. **Maintain Timing**: Ensure that control loops run at the required frequencies
4. **Validate Inputs**: Always validate data received from sensors before using it in AI algorithms
5. **Consider Latency**: Account for communication delays between AI and robot systems

## Exercises

Now that you've learned about Python agents with rclpy, try these exercises to reinforce your understanding:

### Exercise 1: Run the AI Controller Node
1. Run the AI controller node that subscribes to sensor data and publishes commands:
   ```bash
   python3 ai_controller_node.py
   ```
2. Simulate a robot with laser scanner and observe how the AI controller navigates.

### Exercise 2: Modify the AI Algorithm
1. Change the obstacle avoidance behavior in the AI controller
2. Adjust the target direction algorithm to follow a different pattern
3. Add additional sensor inputs to improve the AI's decision making

### Exercise 3: Create a Custom AI Node
1. Create a new node that implements a different AI behavior (e.g., wall following)
2. Subscribe to different sensor types (e.g., camera, IMU)
3. Publish commands to different robot interfaces

### Exercise 4: Parameter Tuning
1. Add parameters to control the AI behavior at runtime
2. Use ROS 2's parameter system to adjust AI behavior without restarting
3. Test different parameter values to optimize the robot's performance

## Summary

In this chapter, you've learned how to create Python-based ROS 2 nodes using rclpy and connect AI logic to robot controllers. You now understand how to use publishers, subscribers, services, parameters, and timers to create sophisticated robotic applications.

[Previous: Chapter 1 - ROS 2 Fundamentals](./chapter-1-ros2-fundamentals.md) | [Next: Chapter 3 - Humanoid Modeling with URDF](./chapter-3-urdf-modeling.md)