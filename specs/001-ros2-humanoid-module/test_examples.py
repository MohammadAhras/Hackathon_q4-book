# Test script to validate ROS 2 examples

import os
import sys

def test_examples_exist():
    """Verify that the ROS 2 example files exist in the expected location."""
    
    examples_dir = "static/examples/ros2_nodes"
    
    # Check if the directory exists
    if not os.path.exists(examples_dir):
        print(f"ERROR: Directory {examples_dir} does not exist")
        return False
    
    # Check if required example files exist
    required_files = [
        "publisher_node.py",
        "subscriber_node.py",
        "service_node.py"
    ]
    
    all_found = True
    for file_name in required_files:
        file_path = os.path.join(examples_dir, file_name)
        if not os.path.exists(file_path):
            print(f"ERROR: File {file_path} does not exist")
            all_found = False
        else:
            print(f"OK: Found {file_path}")
    
    return all_found

def main():
    """Main function to run all tests."""
    print("Running tests to validate ROS 2 examples...")
    
    success = test_examples_exist()
    
    if success:
        print("\nAll tests PASSED")
        return 0
    else:
        print("\nSome tests FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())