# API Documentation: Simulation Interaction

## Overview
This document describes the API endpoints for interactive components in the ROS 2 simulation educational module. These components allow students to run simulations, configure environments, and interact with sensor models directly from the documentation.

## Endpoints

### POST /api/simulation/gazebo/run
Execute a Gazebo simulation with specified parameters.

**Request Body**:
```json
{
  "world_file": "string, path to the Gazebo world file",
  "robot_model": "string, URDF model to load",
  "physics_params": "object, physics engine parameters",
  "duration": "integer, simulation duration in seconds"
}
```

**Response**:
```json
{
  "status": "string, execution status: 'success', 'error', or 'timeout'",
  "simulation_id": "string, identifier for the running simulation",
  "gazebo_output": "string, console output from Gazebo",
  "visualization_url": "string, URL for simulation visualization if applicable",
  "duration": "integer, actual execution time in milliseconds"
}
```

### POST /api/simulation/unity/run
Load and run a Unity simulation environment.

**Request Body**:
```json
{
  "scene_file": "string, path to the Unity scene",
  "environment_params": "object, environment parameters",
  "render_quality": "string, quality setting: 'low', 'medium', 'high'"
}
```

**Response**:
```json
{
  "status": "string, execution status: 'success', 'error'",
  "session_id": "string, identifier for the session",
  "webgl_url": "string, URL to access the Unity scene in browser",
  "duration": "integer, actual loading time in milliseconds"
}
```

### POST /api/simulation/sync
Synchronize parameters between Gazebo and Unity environments.

**Request Body**:
```json
{
  "gazebo_params": "object, parameters for Gazebo simulation",
  "unity_params": "object, parameters for Unity environment",
  "sync_mode": "string, synchronization mode: 'physics', 'visual', 'full'"
}
```

**Response**:
```json
{
  "status": "string, synchronization status: 'success', 'error'",
  "sync_report": "object, details about the synchronization",
  "errors": "array of strings, any synchronization errors"
}
```

### POST /api/sensor/configure
Configure sensor simulation parameters.

**Request Body**:
```json
{
  "sensor_type": "string, type of sensor: 'lidar', 'depth_camera', 'imu'",
  "sensor_params": "object, specific parameters for the sensor model",
  "robot_position": "object, position and orientation of the sensor on the robot",
  "environment": "string, environment context for the sensor simulation"
}
```

**Response**:
```json
{
  "status": "string, configuration status: 'success', 'error'",
  "sensor_config_id": "string, identifier for the configuration",
  "expected_output": "object, example of the expected sensor output",
  "validation": "object, validation results for the configuration"
}
```

## Error Responses
All endpoints follow this error response format:
```json
{
  "error": {
    "code": "string, error code",
    "message": "string, human-readable error message",
    "details": "object, additional error details if applicable"
  }
}
```

## Authentication
For student tracking and personalized feedback:
- Header: `Authorization: Bearer {token}`
- Tokens are issued through the learning management system