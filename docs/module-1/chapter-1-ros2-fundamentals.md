# Chapter 1: ROS 2 Fundamentals

## Introduction to ROS 2

Robot Operating System 2 (ROS 2) is a flexible framework for writing robot software. It's a collection of tools, libraries, and conventions that aim to simplify the task of creating complex and robust robot behavior across a wide variety of robot platforms.

ROS 2 is designed to be the middleware for robotics applications, providing services designed for a heterogeneous computer cluster such as hardware abstraction, low-level device control, implementation of commonly used functionality, message-passing between processes, and package management.

## Key Concepts in ROS 2

### Nodes

A node is a process that performs computation. ROS 2 is designed to be a distributed system where nodes written in different programming languages can run on different machines. In ROS 2, nodes are implemented as objects that live within a process. Multiple nodes can be contained in a single process, but they must be written in the same programming language.

### Topics and Messages

Topics are named buses over which nodes exchange messages. A topic has a typed interface, specified by a message definition. A node can subscribe to a topic to receive data, or publish to a topic to send data. Topic-based communication is unidirectional: one or more nodes publish to a topic and one or more nodes subscribe to a topic.

### Services

While topics allow for asynchronous, many-to-many communication, services provide synchronous, request-response communication. A service is defined by a pair of messages: one for the request and one for the response. Services can only be used in a synchronous, one-to-one manner (one service client sends a request to one service server).

### Actions

Actions are another communication paradigm in ROS 2. They are similar to services but designed for long-running tasks. Actions have three parts: a goal (request), feedback (stream), and result (response).

## The ROS 2 Communication Model

ROS 2 uses a Data Distribution Service (DDS) as its middleware. DDS provides a publish-subscribe pattern and service discovery mechanisms. Each node in ROS 2 has its own DDS participant, which handles message passing between nodes.

### Communication Patterns

1. **Publish/Subscribe**: Unidirectional communication where publishers send messages to subscribers without knowing who receives them.
2. **Request/Response**: Synchronous communication between a client and a server.
3. **Action-based**: Asynchronous communication for long-running tasks with feedback.

## Role of ROS 2 in Physical AI

ROS 2 serves as the middleware enabling AI agents to control humanoid robots. It provides:

- **Hardware Abstraction**: Hides the details of underlying hardware from the application
- **Device Interfaces**: Standardized interfaces for sensors and actuators
- **Communication Infrastructure**: Reliable communication between different parts of a robot system
- **Tool Ecosystem**: Visualization, debugging, and monitoring tools
- **Community and Packages**: Thousands of open-source packages for common robotics tasks

This middleware approach allows AI researchers to focus on developing algorithms and intelligence rather than low-level hardware interfaces and communication protocols.

## Practical Example: Creating a Simple Publisher and Subscriber

Let's look at a simple example of ROS 2 communication using publisher and subscriber nodes. This example will demonstrate:

- Creating a ROS 2 node
- Publishing messages
- Subscribing to messages
- Using the ROS 2 communication model in practice

We'll implement this example using Python with the rclpy library, which is the Python client library for ROS 2.

## Exercises

Now that you've learned about ROS 2 fundamentals, try these exercises to reinforce your understanding:

### Exercise 1: Run the Publisher and Subscriber Nodes
1. In one terminal, run the publisher node:
   ```bash
   python3 publisher_node.py
   ```
2. In another terminal, run the subscriber node:
   ```bash
   python3 subscriber_node.py
   ```
3. Observe the communication between the nodes as messages flow from publisher to subscriber.

### Exercise 2: Modify the Publisher Node
1. Change the message content in the publisher node to include your name
2. Adjust the timer period to publish messages at a different rate
3. Run the modified publisher with the original subscriber to see your changes

### Exercise 3: Run the Service Example
1. In one terminal, run the service server:
   ```bash
   python3 service_node.py
   ```
2. In another terminal, run the service client:
   ```bash
   python3 service_node.py client
   ```
3. Observe the request-response communication between client and server.

### Exercise 4: Create a New Message Type
1. Create a custom message definition file (e.g., containing a string and an integer)
2. Modify the publisher and subscriber to use your custom message type
3. Test that the communication still works with your custom message

## Summary

In this chapter, you've learned about the fundamental concepts of ROS 2 including nodes, topics, services, and actions. You now understand the ROS 2 communication model and the role ROS 2 plays as middleware for physical AI applications.

[Next: Chapter 2 - Python Agents with rclpy](./chapter-2-python-agents.md)