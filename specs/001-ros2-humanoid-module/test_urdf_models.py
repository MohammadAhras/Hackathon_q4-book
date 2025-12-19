# Test script to validate URDF models

import os
import xml.etree.ElementTree as ET
import sys

def test_urdf_models_exist():
    """Verify that the URDF model files exist in the expected location."""
    
    models_dir = "static/examples/urdf_models"
    
    # Check if the directory exists
    if not os.path.exists(models_dir):
        print(f"ERROR: Directory {models_dir} does not exist")
        return False
    
    # Check if required URDF model files exist
    required_files = [
        "simple_humanoid.urdf",
        "humanoid_with_sensors.urdf"
    ]
    
    all_found = True
    for file_name in required_files:
        file_path = os.path.join(models_dir, file_name)
        if not os.path.exists(file_path):
            print(f"ERROR: File {file_path} does not exist")
            all_found = False
        else:
            print(f"OK: Found {file_path}")
    
    return all_found

def test_urdf_models_structure():
    """Verify that the URDF model files have valid XML structure."""
    
    models_dir = "static/examples/urdf_models"
    
    required_files = [
        "simple_humanoid.urdf",
        "humanoid_with_sensors.urdf"
    ]
    
    all_valid = True
    for file_name in required_files:
        file_path = os.path.join(models_dir, file_name)
        
        try:
            # Parse the XML to check for basic validity
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            # Check if it's a robot description
            if root.tag != 'robot':
                print(f"ERROR: {file_path} does not contain a robot element")
                all_valid = False
                continue
            
            # Check for basic robot properties
            robot_name = root.get('name')
            if not robot_name:
                print(f"ERROR: {file_path} does not have a robot name")
                all_valid = False
                continue
            
            # Count links and joints
            links = root.findall('link')
            joints = root.findall('joint')
            
            print(f"OK: {file_path} is valid - name: {robot_name}, links: {len(links)}, joints: {len(joints)}")
            
        except ET.ParseError as e:
            print(f"ERROR: {file_path} has invalid XML structure - {e}")
            all_valid = False
        except Exception as e:
            print(f"ERROR: {file_path} could not be parsed - {e}")
            all_valid = False
    
    return all_valid

def main():
    """Main function to run all tests."""
    print("Running tests to validate URDF models...")
    
    exists_ok = test_urdf_models_exist()
    structure_ok = test_urdf_models_structure()
    
    if exists_ok and structure_ok:
        print("\nAll tests PASSED")
        return 0
    else:
        print("\nSome tests FAILED")
        return 1

if __name__ == "__main__":
    sys.exit(main())