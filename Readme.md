# Event Management API System
An Event Management API system built with FastAPI. It allows users to register for events, manage event attendance, and retrieve user and event-related data.

## Features
- User management (CRUD operations)
- Event management (CRUD operations)
- Speaker management
- Event registration and attendance tracking
- Validation and relationship management between entities

# Setup
## How to Run This Project (Step-by-Step)

### Step 1: Clone the Repository

```bash
git clone https://github.com/Paul-Skay/event-management-system
cd event-management-system
```

### Step 2: Create a Virtual Environment
```bash
python -m venv ("environment name")

(for mac/linux)
source venv/bin/activate

(for windows)
venv\Scripts\activate
```

### Step 3: Install Dependencies from requirement.txt

```bash
pip install -r requirements.txt
```
### Step 4: Running the Application
```bash
uvicorn main:app --reload
```

### Step 5: Access the API Docs
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc


# API Endpoints

## Users Endpoints
| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| POST   | `/users/`          | Create a new user   |
| GET    | `/users/`          | Get all users       |
| GET    | `/users/{user_id}` | Get a specific user |
| PUT | `/users/{user_id}` | update a specific user details |
| DELETE | `/users/{user_id}` | delete a user
| PATCH | `/users/{user_id}` | Deactivate a user |

## Events Endpoints
| Method | Endpoint             | Description          |
| ------ | -------------------- | -------------------- |
| POST   | `/events/`           | Create a new event   |
| GET    | `/events/`           | Get all events       |
| GET    | `/events/{event_id}` | Get a specific event |
| PUT | `/events/{event_id}` | update a specific event details |
| DELETE | `/events/{event_id}` | delete an event
| PATCH | `/events/{event_id}` | Close Event registration |

## Registrations Endpoints
| Method | Endpoint                         | Description                            |
| ------ | -------------------------------- | -------------------------------------- |
| POST   | `/register/`                 | Register a user for an event           |
| GET    | `/register/`                 | Get all registrations                  |
| GET    | `/register/{user_id}`        | Get registrations for a specific user  |
| PUT  | `/register/{event_id}/attendance` | Mark attendance for a user             |
| GET    | `/register/attendees/all`        | Get all attendees (users who attended) |
| GET    | `/register/attendees/{event_id}`        | Get all attendees (users who attended an event) |
| GET    | `/register/attendees/event/users`        | Get users who attended at least on event |

# MIT License

Copyright (c) 2025 Paul Mbah