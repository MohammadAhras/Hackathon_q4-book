#!/usr/bin/env python3

"""
Publisher Node for ROS 2 Fundamentals Example

This node publishes a simple message to a topic at regular intervals.
It demonstrates the basic concept of a ROS 2 publisher node.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):
    """
    A simple publisher node that publishes messages to a topic.
    """

    def __init__(self):
        # Initialize the node with a name
        super().__init__('publisher_node')
        
        # Create a publisher to send String messages on the 'chatter' topic
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        
        # Create a timer to publish messages at a fixed rate (0.5 seconds)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # Counter to track the number of messages published
        self.i = 0
        
        self.get_logger().info('Publisher node initialized')

    def timer_callback(self):
        """
        Callback function that executes at regular intervals to publish messages.
        """
        # Create a String message
        msg = String()
        msg.data = f'Hello ROS 2! Message count: {self.i}'
        
        # Publish the message
        self.publisher_.publish(msg)
        
        # Log the published message
        self.get_logger().info(f'Publishing: "{msg.data}"')
        
        # Increment the counter
        self.i += 1


def main(args=None):
    """
    Main function to initialize and run the publisher node.
    """
    # Initialize the ROS 2 Python client library
    rclpy.init(args=args)

    # Create an instance of the publisher node
    publisher_node = PublisherNode()

    # Run the node until it's shut down
    try:
        rclpy.spin(publisher_node)
    except KeyboardInterrupt:
        pass

    # Clean up and shut down the node
    publisher_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()