#!/usr/bin/env python3

"""
AI Controller Node for Python Agent Development Example

This node demonstrates an AI agent that processes sensor data and sends commands to a robot.
It subscribes to sensor data, processes it with a simple AI algorithm, and publishes commands.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Float64
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import math


class AIControllerNode(Node):
    """
    An AI controller node that subscribes to sensor data, processes it with AI logic,
    and publishes commands to control a robot.
    """

    def __init__(self):
        # Initialize the node with a name
        super().__init__('ai_controller_node')
        
        # Create a publisher to send velocity commands to the robot
        self.cmd_vel_publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Create a subscription to receive sensor data (e.g., laser scan)
        self.sensor_subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.sensor_callback,
            10
        )
        
        # Create a subscription to receive additional sensor data (e.g., battery level)
        self.battery_subscription = self.create_subscription(
            Float64,
            '/battery_level',
            self.battery_callback,
            10
        )
        
        # Create a timer to run the AI algorithm at 10 Hz
        self.timer = self.create_timer(0.1, self.ai_control_loop)
        
        # Store sensor data
        self.laser_data = None
        self.battery_level = 100.0  # Default to full battery
        
        # Robot state for the AI algorithm
        self.target_direction = 0.0  # Radians
        self.avoiding_obstacle = False
        
        self.get_logger().info('AI Controller node initialized')

    def sensor_callback(self, msg):
        """
        Process incoming laser scan data.
        """
        self.laser_data = msg.ranges  # Store the ranges array
        
        # Log a summary of the sensor data
        if self.laser_data:
            min_distance = min([d for d in self.laser_data if not math.isinf(d) and not math.isnan(d)], default=float('inf'))
            self.get_logger().info(f'Closest obstacle: {min_distance:.2f}m')

    def battery_callback(self, msg):
        """
        Process incoming battery level data.
        """
        self.battery_level = msg.data
        self.get_logger().info(f'Battery level: {self.battery_level:.2f}%')

    def ai_control_loop(self):
        """
        Main AI control loop that processes sensor data and sends commands.
        """
        if self.laser_data is None:
            # No sensor data yet, send stop command
            self.send_stop_command()
            return

        # Simple AI algorithm: avoid obstacles and navigate toward a target
        cmd_vel = Twist()
        
        # Check for obstacles in front of the robot (within 1 meter)
        front_ranges = self.laser_data[315:405]  # Assuming 360-degree scan, front is centered
        min_front_distance = min([d for d in front_ranges if not math.isinf(d) and not math.isnan(d)], default=float('inf'))
        
        if min_front_distance < 1.0:  # Obstacle detected
            self.avoiding_obstacle = True
            # Turn away from the obstacle
            cmd_vel.linear.x = 0.0
            cmd_vel.angular.z = 0.5  # Turn right
            self.get_logger().info('Obstacle detected - turning to avoid')
        else:
            self.avoiding_obstacle = False
            # Move forward with a slight turn toward the target
            cmd_vel.linear.x = 0.5
            cmd_vel.angular.z = 0.1 * self.target_direction  # Follow target direction
        
        # Consider battery level - reduce activity when battery is low
        if self.battery_level < 20.0:
            cmd_vel.linear.x *= 0.5  # Slow down when battery is low
            self.get_logger().info('Battery low - reducing speed')
        
        # Publish the command
        self.cmd_vel_publisher.publish(cmd_vel)

    def send_stop_command(self):
        """
        Send a stop command to the robot.
        """
        cmd_vel = Twist()
        cmd_vel.linear.x = 0.0
        cmd_vel.angular.z = 0.0
        self.cmd_vel_publisher.publish(cmd_vel)


def main(args=None):
    """
    Main function to initialize and run the AI controller node.
    """
    # Initialize the ROS 2 Python client library
    rclpy.init(args=args)

    # Create an instance of the AI controller node
    ai_controller_node = AIControllerNode()

    # Run the node until it's shut down
    try:
        rclpy.spin(ai_controller_node)
    except KeyboardInterrupt:
        pass

    # Clean up and shut down the node
    ai_controller_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()