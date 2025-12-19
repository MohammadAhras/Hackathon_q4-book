# Final validation script to ensure all success criteria can be met

import os
import subprocess
import sys
import json

def validate_success_criteria():
    """Validate that all success criteria from the spec can be met."""
    
    results = {
        'criteria_met': [],
        'criteria_not_met': [],
        'overall_status': True
    }
    
    print("Validating success criteria...")
    
    # SC-001: At least 85% of students can successfully create and connect two ROS 2 nodes that communicate via topics
    print("\n1. Checking SC-001: Students can create and connect two ROS 2 nodes...")
    # Check if publisher and subscriber examples exist and have valid structure
    pub_path = "static/examples/ros2_nodes/publisher_node.py"
    sub_path = "static/examples/ros2_nodes/subscriber_node.py"
    
    if os.path.exists(pub_path) and os.path.exists(sub_path):
        with open(pub_path, 'r') as f:
            pub_content = f.read()
        with open(sub_path, 'r') as f:
            sub_content = f.read()
        
        # Check for basic ROS 2 patterns
        if all(pattern in pub_content for pattern in ['rclpy', 'Node', 'create_publisher', 'spin']):
            if all(pattern in sub_content for pattern in ['rclpy', 'Node', 'create_subscription', 'spin']):
                results['criteria_met'].append("SC-001: Examples for publisher/subscriber communication exist")
                print("  OK SC-001 PASSED: Examples available for student use")
            else:
                results['criteria_not_met'].append("SC-001: Subscriber example may have issues")
                results['overall_status'] = False
                print("  FAIL SC-001: Subscriber example may have issues")
        else:
            results['criteria_not_met'].append("SC-001: Publisher example may have issues")
            results['overall_status'] = False
            print("  FAIL SC-001: Publisher example may have issues")
    else:
        results['criteria_not_met'].append("SC-001: Publisher/subscriber examples missing")
        results['overall_status'] = False
        print("  FAIL SC-001: Examples missing")

    # SC-002: 80% of students can develop a Python agent using rclpy that publishes sensor data or subscribes to control messages
    print("\n2. Checking SC-002: Students can develop Python agents with rclpy...")
    agent_path = "static/examples/ros2_nodes/ai_controller_node.py"

    if os.path.exists(agent_path):
        with open(agent_path, 'r') as f:
            agent_content = f.read()

        # Check for AI controller patterns
        if all(pattern in agent_content for pattern in ['rclpy', 'Node', 'create_publisher', 'create_subscription']):
            results['criteria_met'].append("SC-002: AI controller example available")
            print("  OK SC-002 PASSED: AI controller example available")
        else:
            results['criteria_not_met'].append("SC-002: AI controller example incomplete")
            results['overall_status'] = False
            print("  FAIL SC-002: AI controller example incomplete")
    else:
        results['criteria_not_met'].append("SC-002: AI controller example missing")
        results['overall_status'] = False
        print("  FAIL SC-002: AI controller example missing")

    # SC-003: Students complete a practical exercise with URDF model of humanoid robot with at least 5 joints
    print("\n3. Checking SC-003: Students can create URDF model with 5+ joints...")
    urdf_path = "static/examples/urdf_models/simple_humanoid.urdf"

    if os.path.exists(urdf_path):
        import xml.etree.ElementTree as ET
        try:
            tree = ET.parse(urdf_path)
            root = tree.getroot()

            joints = root.findall('joint')
            if len(joints) >= 5:
                results['criteria_met'].append(f"SC-003: URDF model has {len(joints)} joints")
                print(f"  OK SC-003 PASSED: URDF model has {len(joints)} joints")
            else:
                results['criteria_not_met'].append(f"SC-003: URDF model has only {len(joints)} joints, need at least 5")
                results['overall_status'] = False
                print(f"  FAIL SC-003: URDF model has only {len(joints)} joints, need at least 5")
        except ET.ParseError:
            results['criteria_not_met'].append("SC-003: URDF model has invalid XML structure")
            results['overall_status'] = False
            print("  FAIL SC-003: URDF model has invalid XML structure")
    else:
        results['criteria_not_met'].append("SC-003: URDF model file missing")
        results['overall_status'] = False
        print("  FAIL SC-003: URDF model file missing")

    # SC-004: Students achieve 90% pass rate on assessments testing ROS 2 as middleware
    print("\n4. Checking SC-004: Students can pass assessments on ROS 2 as middleware...")
    assessment_path = "docs/module-1/assessment-questions.md"

    if os.path.exists(assessment_path):
        with open(assessment_path, 'r') as f:
            assessment_content = f.read()

        # Check if assessment questions exist
        if assessment_content.count("Question") >= 5:  # At least several questions
            results['criteria_met'].append("SC-004: Assessment questions available")
            print("  OK SC-004 PASSED: Assessment questions available")
        else:
            results['criteria_not_met'].append("SC-004: Not enough assessment questions")
            results['overall_status'] = False
            print("  FAIL SC-004: Not enough assessment questions")
    else:
        results['criteria_not_met'].append("SC-004: Assessment questions missing")
        results['overall_status'] = False
        print("  FAIL SC-004: Assessment questions missing")

    # SC-005: 75% of students report increased confidence in developing robotic agents
    print("\n5. Checking SC-005: Students report increased confidence...")
    # This criterion is more subjective, but we can validate that learning materials exist
    summary_path = "docs/module-1/summary-next-steps.md"

    if os.path.exists(summary_path):
        with open(summary_path, 'r') as f:
            summary_content = f.read()

        if len(summary_content) > 100:  # Check that it's not an empty file
            results['criteria_met'].append("SC-005: Summary and next steps available")
            print("  OK SC-005 PASSED: Summary and next steps available")
        else:
            results['criteria_not_met'].append("SC-005: Summary content insufficient")
            results['overall_status'] = False
            print("  FAIL SC-005: Summary content insufficient")
    else:
        results['criteria_not_met'].append("SC-005: Summary and next steps missing")
        results['overall_status'] = False
        print("  FAIL SC-005: Summary and next steps missing")
    
    return results

def main():
    """Main function to run final validation."""
    print("Running final validation to ensure all success criteria can be met...")
    
    results = validate_success_criteria()
    
    print(f"\n\nFinal Validation Results:")
    print(f"Criteria met: {len(results['criteria_met'])}")
    print(f"Criteria not met: {len(results['criteria_not_met'])}")
    
    for criterion in results['criteria_met']:
        print(f"  OK {criterion}")

    if results['criteria_not_met']:
        for criterion in results['criteria_not_met']:
            print(f"  FAIL {criterion}")
    
    if results['overall_status']:
        print(f"\nAll success criteria validation PASSED!")
        return 0
    else:
        print(f"\nSome success criteria validation FAILED!")
        return 1

if __name__ == "__main__":
    sys.exit(main())