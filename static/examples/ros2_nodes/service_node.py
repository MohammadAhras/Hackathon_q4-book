#!/usr/bin/env python3

"""
Service Server and Client Nodes for ROS 2 Fundamentals Example

This file contains examples of both a service server and a service client node.
It demonstrates the basic concept of ROS 2 services for synchronous request-response communication.
"""

import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class ServiceServerNode(Node):
    """
    A simple service server node that adds two integers.
    """

    def __init__(self):
        # Initialize the node with a name
        super().__init__('service_server_node')
        
        # Create a service that uses the AddTwoInts interface
        self.srv = self.create_service(
            AddTwoInts, 
            'add_two_ints', 
            self.add_two_ints_callback
        )
        
        self.get_logger().info('Service server node initialized')

    def add_two_ints_callback(self, request, response):
        """
        Callback function to handle service requests.
        """
        # Perform the addition
        response.sum = request.a + request.b
        
        # Log the request and response
        self.get_logger().info(f'Incoming request: {request.a} + {request.b}')
        self.get_logger().info(f'Sending response: {response.sum}')
        
        return response


class ServiceClientNode(Node):
    """
    A simple service client node that requests the addition of two integers.
    """

    def __init__(self):
        # Initialize the node with a name
        super().__init__('service_client_node')
        
        # Define the client for the AddTwoInts service
        self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        
        # Wait for the service to be available
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service not available, waiting again...')
        
        self.req = AddTwoInts.Request()
        
        self.get_logger().info('Service client node initialized')

    def send_request(self, a, b):
        """
        Send a request to the service server.
        """
        self.req.a = a
        self.req.b = b
        
        # Asynchronously call the service
        self.future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, self.future)
        
        return self.future.result()


def server_main(args=None):
    """
    Main function to initialize and run the service server node.
    """
    # Initialize the ROS 2 Python client library
    rclpy.init(args=args)

    # Create an instance of the service server node
    service_server_node = ServiceServerNode()

    # Run the node until it's shut down
    try:
        rclpy.spin(service_server_node)
    except KeyboardInterrupt:
        pass

    # Clean up and shut down the node
    service_server_node.destroy_node()
    rclpy.shutdown()


def client_main(args=None):
    """
    Main function to initialize and run the service client node.
    """
    # Initialize the ROS 2 Python client library
    rclpy.init(args=args)

    # Create an instance of the service client node
    service_client_node = ServiceClientNode()

    # Send a request to the service
    try:
        response = service_client_node.send_request(42, 24)
        service_client_node.get_logger().info(
            f'Result of add_two_ints: {response.sum}'
        )
    except Exception as e:
        service_client_node.get_logger().error(f'Service call failed: {e}')

    # Clean up and shut down the node
    service_client_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    # This example can run either as a server or client depending on command line args
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'client':
        client_main()
    else:
        # Default to running as server
        server_main()