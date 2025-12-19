# Content Review Script for ROS 2 Humanoid Robotics Education Module

import os
import re

def review_technical_accuracy():
    """Review the content for technical accuracy."""
    
    review_results = {
        'issues_found': [],
        'recommendations': []
    }
    
    # Check chapter files for common technical issues
    chapter_files = [
        'docs/module-1/chapter-1-ros2-fundamentals.md',
        'docs/module-1/chapter-2-python-agents.md',
        'docs/module-1/chapter-3-urdf-modeling.md'
    ]
    
    for file_path in chapter_files:
        if not os.path.exists(file_path):
            review_results['issues_found'].append(f"File does not exist: {file_path}")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for common technical accuracy issues
        # Check for outdated API usage
        if 'rospy' in content and 'chapter-2' in file_path:
            review_results['issues_found'].append(
                f"Found rospy in {file_path}, but this is a rclpy-focused chapter. Consider updating to rclpy."
            )
        
        # Check for incorrect Python syntax or patterns
        if re.search(r'import roslib', content):
            review_results['issues_found'].append(
                f"Found 'import roslib' in {file_path}. roslib is deprecated for ROS 2. Use ament instead."
            )
    
    # Check example files for technical accuracy
    example_files = [
        'static/examples/ros2_nodes/publisher_node.py',
        'static/examples/ros2_nodes/subscriber_node.py',
        'static/examples/ros2_nodes/service_node.py',
        'static/examples/ros2_nodes/ai_controller_node.py'
    ]
    
    for file_path in example_files:
        if not os.path.exists(file_path):
            review_results['issues_found'].append(f"Example file does not exist: {file_path}")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for common Python/ROS 2 patterns
        if 'rclpy.init(args=args)' not in content:
            review_results['issues_found'].append(
                f"Missing proper rclpy initialization in {file_path}"
            )
        
        # Check for proper error handling
        if 'try:' not in content and 'except' not in content:
            review_results['recommendations'].append(
                f"Consider adding error handling to {file_path}"
            )
    
    # Check URDF files for technical accuracy
    urdf_files = [
        'static/examples/urdf_models/simple_humanoid.urdf',
        'static/examples/urdf_models/humanoid_with_sensors.urdf'
    ]
    
    for file_path in urdf_files:
        if not os.path.exists(file_path):
            review_results['issues_found'].append(f"URDF file does not exist: {file_path}")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for required URDF elements
        if '<robot' not in content:
            review_results['issues_found'].append(f"Invalid URDF format in {file_path}")
        
        # Check for proper inertia values
        if 'inertia ixx="0"' in content or 'inertia iyy="0"' in content:
            review_results['issues_found'].append(
                f"Zero inertia values found in {file_path} - this can cause simulation issues"
            )
    
    return review_results

def main():
    """Main function to run the content review."""
    print("Performing content review for technical accuracy...")
    
    results = review_technical_accuracy()
    
    print(f"\nReview completed. Found {len(results['issues_found'])} issues and {len(results['recommendations'])} recommendations.")
    
    if results['issues_found']:
        print("\nIssues found:")
        for issue in results['issues_found']:
            print(f"  - {issue}")
    
    if results['recommendations']:
        print("\nRecommendations:")
        for rec in results['recommendations']:
            print(f"  - {rec}")
    
    if not results['issues_found'] and not results['recommendations']:
        print("\nNo issues found. Content appears technically accurate.")
        return True
    else:
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)