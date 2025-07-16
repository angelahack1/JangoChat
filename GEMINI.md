# Gemini Project Context: JangoChat

## Project Overview

JangoChat is a Django-based real-time chat application. It uses Django Channels for WebSocket communication to enable instant messaging between users. The application includes user authentication and a chat interface.

## Tech Stack

*   **Backend:** Django
*   **Real-time Communication:** Django Channels, Daphne
*   **Frontend:** HTML, Bootstrap
*   **Database:** SQLite (default development database)
*   **WSGI/ASGI Server:** Daphne

## Project Structure

```
JangoChat/
├── chat/                # Main chat application
│   ├── migrations/      # Database migrations
│   ├── templates/chat/  # HTML templates for the chat app
│   │   ├── chat_page.html
│   │   ├── login.html
│   │   └── welcome.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── consumers.py     # WebSocket consumers
│   ├── models.py        # Database models
│   ├── routing.py       # Channels routing
│   ├── tests.py
│   ├── urls.py          # URL configuration
│   └── views.py         # View functions
├── JangoChat/           # Django project configuration
│   ├── __init__.py
│   ├── asgi.py          # ASGI configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # Project-level URL configuration
│   └── wsgi.py          # WSGI configuration
├── .gitignore
├── manage.py            # Django management script
├── README.md
└── requirements.txt     # Python dependencies
```

## Key Files

*   `JangoChat/settings.py`: The main Django settings file. It includes configurations for the database, installed apps, middleware, and channel layers.
*   `chat/consumers.py`: This file contains the WebSocket consumer that handles real-time chat communication.
*   `chat/routing.py`: Defines the WebSocket URL routing for the chat application.
*   `chat/templates/chat/chat_page.html`: The main chat interface where users can send and receive messages.
*   `requirements.txt`: Lists the Python packages required for the project.

## Commands

*   **Run the development server:** `python manage.py runserver`
*   **Apply database migrations:** `python manage.py migrate`
*   **Create new migrations:** `python manage.py makemigrations`
*   **Install dependencies:** `pip install -r requirements.txt`
