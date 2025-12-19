# Validation script for ROS 2 examples

import os
import subprocess
import sys
import ast

def validate_python_examples():
    """Validate that Python examples have correct syntax and structure."""
    
    examples_dir = "static/examples/ros2_nodes"
    python_files = [
        "publisher_node.py",
        "subscriber_node.py",
        "service_node.py",
        "ai_controller_node.py"
    ]
    
    all_valid = True
    
    for file_name in python_files:
        file_path = os.path.join(examples_dir, file_name)
        
        if not os.path.exists(file_path):
            print(f"ERROR: File {file_path} does not exist")
            all_valid = False
            continue
        
        # Check Python syntax
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse the Python syntax
            ast.parse(content)
            print(f"OK: {file_name} has valid Python syntax")
            
            # Check for required ROS 2 patterns
            if "rclpy.init(args=args)" not in content:
                print(f"WARNING: {file_name} may be missing proper rclpy initialization")
            
            if "Node" not in content:
                print(f"WARNING: {file_name} may not inherit from rclpy.Node")
            
            if "if __name__ == '__main__':" not in content:
                print(f"WARNING: {file_name} may not have proper main guard")
                
        except SyntaxError as e:
            print(f"ERROR: {file_name} has syntax error at line {e.lineno}: {e.msg}")
            all_valid = False
        except Exception as e:
            print(f"ERROR: Could not validate {file_name}: {e}")
            all_valid = False
    
    return all_valid

def validate_urdf_models():
    """Validate that URDF models have correct XML structure."""
    
    models_dir = "static/examples/urdf_models"
    urdf_files = [
        "simple_humanoid.urdf",
        "humanoid_with_sensors.urdf"
    ]
    
    all_valid = True
    import xml.etree.ElementTree as ET
    
    for file_name in urdf_files:
        file_path = os.path.join(models_dir, file_name)
        
        if not os.path.exists(file_path):
            print(f"ERROR: File {file_path} does not exist")
            all_valid = False
            continue
        
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            if root.tag != 'robot':
                print(f"ERROR: {file_name} does not contain a robot element")
                all_valid = False
                continue
            
            # Check for required elements
            links = root.findall('link')
            joints = root.findall('joint')
            
            if len(links) == 0:
                print(f"WARNING: {file_name} contains no links")
            
            if len(joints) == 0:
                print(f"WARNING: {file_name} contains no joints")
            
            print(f"OK: {file_name} is valid - {len(links)} links, {len(joints)} joints")
            
        except ET.ParseError as e:
            print(f"ERROR: {file_name} has invalid XML structure - {e}")
            all_valid = False
        except Exception as e:
            print(f"ERROR: Could not validate {file_name}: {e}")
            all_valid = False
    
    return all_valid

def main():
    """Main function to run all validations."""
    print("Validating code examples...")
    
    python_ok = validate_python_examples()
    urdf_ok = validate_urdf_models()
    
    print(f"\nPython examples validation: {'PASS' if python_ok else 'FAIL'}")
    print(f"URDF models validation: {'PASS' if urdf_ok else 'FAIL'}")
    
    if python_ok and urdf_ok:
        print("\nAll validations PASSED")
        return 0
    else:
        print("\nSome validations FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())