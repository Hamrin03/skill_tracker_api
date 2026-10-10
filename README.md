\# Skill Development Tracker API



\## Project Overview

The Skill Development Tracker API is a REST API developed using FastAPI. It allows users to register, log in securely, and manage their skills and learning progress.



\## Technologies Used

\- Python

\- FastAPI

\- SQLAlchemy

\- SQLite

\- JWT Authentication

\- Password Hashing

\- Pydantic

\- Uvicorn



\## Features

\- User registration

\- User login with JWT authentication

\- Secure password hashing

\- Create a new skill

\- View all skills

\- View a skill by ID

\- Update skill details

\- Delete a skill

\- User-specific skill access

\- Input validation and error handling



\## Project Structure

```text

skill\_tracker\_api/

├── app/

│   ├── routers/

│   │   └── skills.py

│   ├── \_\_init\_\_.py

│   ├── main.py

│   ├── database.py

│   ├── models.py

│   ├── schemas.py

│   ├── security.py

│   └── auth.py

├── .env

├── .gitignore

├── requirements.txt

└── README.md

```



\## Installation and Setup



1\. Clone or download this repository.

2\. Open the project folder in VS Code.

3\. Create and activate a virtual environment.

4\. Install the required packages:



```bash

pip install -r requirements.txt

```



5\. Create a `.env` file in the project root and add a secret key:



```text

SECRET\_KEY=your-secret-key

```



Replace the example value with a securely generated secret key. Do not upload your real `.env` file to GitHub.



6\. Start the server:



```bash

python -m uvicorn app.main:app --reload

```



\## API Documentation



After starting the server, open:



http://127.0.0.1:8000/docs



The Swagger UI allows users to test the API endpoints.



\### Authentication Endpoints

\- `POST /auth/register` — Register a user.

\- `POST /auth/login` — Log in and obtain an access token.



\### Skill Endpoints

\- `POST /skills/` — Create a skill.

\- `GET /skills/` — Retrieve the current user's skills.

\- `GET /skills/{skill\_id}` — Retrieve a skill by ID.

\- `PUT /skills/{skill\_id}` — Update a skill.

\- `DELETE /skills/{skill\_id}` — Delete a skill.



Skill endpoints require authentication.



\## Security

\- Passwords are stored as hashes rather than plain text.

\- JWT tokens are used to authenticate requests.

\- Skill records are restricted to their owner.

\- Input validation helps prevent invalid data.

\- Environment variables are used for the JWT secret key.



\## Learning Outcomes

Through this project, I learned how to build REST APIs using FastAPI, work with a SQLite database through SQLAlchemy, implement JWT authentication, hash passwords, validate input data, and test endpoints using Swagger UI.



\## Conclusion

The Skill Development Tracker API provides a foundation for managing personal learning goals and tracking skill progress through authenticated API endpoints.

