#!/usr/bin/env python3

"""
Subscriber Node for ROS 2 Fundamentals Example

This node subscribes to messages published on the 'chatter' topic.
It demonstrates the basic concept of a ROS 2 subscriber node.
"""

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SubscriberNode(Node):
    """
    A simple subscriber node that listens to messages on a topic.
    """

    def __init__(self):
        # Initialize the node with a name
        super().__init__('subscriber_node')
        
        # Create a subscription to receive String messages on the 'chatter' topic
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10)  # Queue size
        
        # Make sure the subscription is properly created
        self.subscription  # prevent unused variable warning
        
        self.get_logger().info('Subscriber node initialized')

    def listener_callback(self, msg):
        """
        Callback function to process incoming messages.
        """
        # Log the received message
        self.get_logger().info(f'I heard: "{msg.data}"')


def main(args=None):
    """
    Main function to initialize and run the subscriber node.
    """
    # Initialize the ROS 2 Python client library
    rclpy.init(args=args)

    # Create an instance of the subscriber node
    subscriber_node = SubscriberNode()

    # Run the node until it's shut down
    try:
        rclpy.spin(subscriber_node)
    except KeyboardInterrupt:
        pass

    # Clean up and shut down the node
    subscriber_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()