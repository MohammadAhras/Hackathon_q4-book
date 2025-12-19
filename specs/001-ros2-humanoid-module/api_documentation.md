# API Documentation for Interactive Learning Components

This document describes the API endpoints for interactive components in the ROS 2 educational module. These components allow students to run simulations or interact with ROS 2 examples directly from the documentation.

## Endpoints

### POST /api/simulation/run
Execute a ROS 2 simulation example

**Request Body**:
```json
{
  "example_id": "string, identifier for the specific example",
  "parameters": "object, configuration parameters for the simulation",
  "timeout": "integer, maximum execution time in seconds"
}
```

**Response**:
```json
{
  "status": "string, execution status: 'success', 'error', or 'timeout'",
  "output": "string, console output from the simulation",
  "results": "object, simulation results if applicable",
  "duration": "integer, actual execution time in milliseconds"
}
```

### GET /api/examples/{example_id}
Retrieve information about a specific example

**Path Parameters**:
- example_id: string, identifier of the example

**Response**:
```json
{
  "id": "string, example identifier",
  "title": "string, example title",
  "description": "string, what the example demonstrates",
  "files": "array of objects, containing file paths and content",
  "dependencies": "array of strings, required ROS 2 packages",
  "execution_instructions": "string, how to run the example"
}
```

### POST /api/validate-submission
Validate a student's exercise submission

**Request Body**:
```json
{
  "exercise_id": "string, identifier for the exercise",
  "solution": "string or object, the student's solution",
  "student_id": "string, identifier for the student"
}
```

**Response**:
```json
{
  "status": "string, 'correct', 'incorrect', or 'partial'",
  "feedback": "string, feedback for the student",
  "score": "number, score between 0 and 1",
  "analysis": "object, detailed analysis of the submission"
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

## Authentication Implementation

The authentication system uses JWT (JSON Web Tokens) to identify and track students as they interact with the educational content:

### Token Generation
- Students receive a JWT token upon registration in the learning system
- Tokens contain student identifier and expiration time
- Tokens are signed with a server-side secret key

### Token Validation
- Each API request includes the token in the Authorization header
- The server validates the token signature and expiration
- Student ID from the token is used to personalize responses

### Implementation Example
```python
import jwt
from datetime import datetime, timedelta

def generate_student_token(student_id: str, secret_key: str) -> str:
    """Generate a JWT token for a student."""
    payload = {
        'student_id': student_id,
        'exp': datetime.utcnow() + timedelta(days=30)  # Token expires in 30 days
    }
    return jwt.encode(payload, secret_key, algorithm='HS256')

def validate_student_token(token: str, secret_key: str) -> dict:
    """Validate a JWT token and return student info."""
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return {
            'valid': True,
            'student_id': payload.get('student_id'),
            'exp': payload.get('exp')
        }
    except jwt.ExpiredSignatureError:
        return {'valid': False, 'error': 'Token has expired'}
    except jwt.InvalidTokenError:
        return {'valid': False, 'error': 'Invalid token'}
```