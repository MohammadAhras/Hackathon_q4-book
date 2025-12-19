# Assessment Questions for Module 2: The Digital Twin (Gazebo & Unity)

## Chapter 1: Physics Simulation with Gazebo

### Question 1
What is the primary purpose of the physics engine in Gazebo?
A) To render the visual elements of the simulation
B) To calculate how objects move and interact based on physical laws
C) To handle user interface elements
D) To manage network communications

### Question 2
In Gazebo, what are the two main phases of collision detection?
A) Visual phase and rendering phase
B) Setup phase and execution phase
C) Broad phase and narrow phase
D) Initialization phase and runtime phase

### Question 3
Which of the following is NOT a typical parameter for configuring gravity in a Gazebo world file?
A) Direction vector (usually negative Z for downward pull)
B) Magnitude (typically 9.81 m/s² for Earth)
C) Color of gravitational field
D) Enabled/disabled status

### Question 4
What is the role of the SDF format in Gazebo simulations?
A) It's a special lighting effect
B) It's a scripting language for animations
C) It's the Simulation Description Format for defining worlds and models
D) It's a compression algorithm for simulation data

## Chapter 2: High-Fidelity Environments with Unity

### Question 5
What does PBR stand for in Unity's material system?
A) Physics-Based Rendering
B) Programmable Buffer Rendering
C) Physically-Based Rendering
D) Polygon-Based Rendering

### Question 6
Which Unity system is used to capture and store lighting information for small objects that move through a scene?
A) Light baking
B) Light Probes
C) Real-time GI
D) Reflection Probes

### Question 7
In the dual-engine approach with Gazebo and Unity:
A) Unity handles physics and Gazebo handles visualization
B) Gazebo handles physics and Unity handles visualization
C) Both engines handle both physics and visualization
D) Neither engine handles physics; it's handled externally

### Question 8
What is the main benefit of using LOD (Level of Detail) systems in Unity?
A) Improved lighting quality
B) Better audio processing
C) Optimized performance by adjusting detail based on distance
D) Enhanced physics simulation

## Chapter 3: Sensor Simulation

### Question 9
Which of the following is a key characteristic of LiDAR sensors?
A) They only measure distance in 2D
B) They measure distance and angle in 2D
C) They measure depth for entire image pixels
D) They measure only acceleration

### Question 10
What do IMU sensors measure?
A) Distance to objects only
B) Linear acceleration and angular velocity
C) Visual information only
D) Radio frequency signals

### Question 11
In sensor simulation, what is the "simulation-to-reality gap"?
A) The difference in processing speeds between simulation and reality
B) The difference between simulated and real-world sensor behavior
C) The physical distance between simulated and real objects
D) The time difference between simulation and reality

### Question 12
Which type of noise is characterized by slow-changing systematic offsets in IMUs?
A) White noise
B) Random walk
C) Bias instability
D) Quantization noise

## Answers
1. B - Physics engine calculates how objects move and interact based on physical laws
2. C - Broad phase and narrow phase
3. C - Color of gravitational field
4. C - Simulation Description Format for defining worlds and models
5. C - Physically-Based Rendering
6. B - Light Probes
7. B - Gazebo handles physics and Unity handles visualization
8. C - Optimized performance by adjusting detail based on distance
9. B - They measure distance and angle in 2D
10. B - Linear acceleration and angular velocity
11. B - The difference between simulated and real-world sensor behavior
12. C - Bias instability