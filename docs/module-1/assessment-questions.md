# Assessment Questions for Module 1: The Robotic Nervous System (ROS 2)

## Chapter 1: ROS 2 Fundamentals

### Question 1
What is the primary difference between a ROS 2 topic and a ROS 2 service?
A) Topics are for communication between nodes, services are for communication with hardware
B) Topics provide asynchronous, many-to-many communication; services provide synchronous, one-to-one communication
C) Topics are used for sensor data, services are used for actuator commands
D) Topics use TCP, services use UDP

### Question 2
Which of the following is a key component of a ROS 2 node?
A) Publisher and Subscriber
B) Topic and Message
C) Driver and Sensor
D) Algorithm and Data

### Question 3
What does DDS stand for in the context of ROS 2?
A) Distributed Data System
B) Data Distribution Service
C) Device Discovery System
D) Dynamic Data Sharing

### Question 4
Which ROS 2 communication pattern is best suited for long-running tasks with continuous feedback?
A) Topic
B) Service
C) Action
D) Parameter

## Chapter 2: Python Agents with rclpy

### Question 5
Which Python library is used to create ROS 2 nodes in Python?
A) rospy
B) rclpy
C) roslibpy
D) pyros

### Question 6
In rclpy, how do you create a timer that executes a callback every 0.5 seconds?
A) `create_timer(0.5, callback)`
B) `create_rate(2, callback)`
C) `create_timer(500, callback)`
D) `create_wall_timer(0.5, callback)`

### Question 7
What is the purpose of Quality of Service (QoS) settings in ROS 2?
A) To limit the computational resources used by nodes
B) To configure how messages are delivered in terms of reliability, durability, and history
C) To enforce security protocols between nodes
D) To define the API contract between nodes

### Question 8
Which of the following is NOT a valid QoS policy in ROS 2?
A) Reliability
B) Durability
C) Security
D) History

## Chapter 3: Humanoid Modeling with URDF

### Question 9
What does URDF stand for?
A) Unified Robot Description Format
B) Universal Robot Definition Framework
C) Unified Robotics Development Format
D) Universal Robot Description File

### Question 10
In a URDF file, what element connects two links?
A) connection
B) joint
C) bond
D) linkage

### Question 11
Which of the following is NOT a valid joint type in URDF?
A) revolute
B) continuous
C) prismatic
D) rotational

### Question 12
What is the purpose of the `<inertial>` tag in a URDF link definition?
A) To define the visual appearance of the link
B) To define the collision properties of the link
C) To define the physical properties (mass, center of mass, inertia) of the link
D) To specify how the link connects to other links

## Answers
1. B - Topics provide asynchronous, many-to-many communication; services provide synchronous, one-to-one communication
2. A - Publisher and Subscriber
3. B - Data Distribution Service
4. C - Action
5. B - rclpy
6. D - `create_wall_timer(0.5, callback)`
7. B - To configure how messages are delivered in terms of reliability, durability, and history
8. C - Security
9. A - Unified Robot Description Format
10. B - joint
11. D - rotational
12. C - To define the physical properties (mass, center of mass, inertia) of the link