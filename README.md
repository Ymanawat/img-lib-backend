Guide to set up and run the project locally.

## Setup Instructions

### 1. Clone the Repository

First, create a folder and clone the repository:

```bash
mkdir project-folder
cd project-folder
git clone https://github.com/Ymanawat/img-lib-backend
```

### 2. Create a Virtual Environment

Create a virtual environment for the project:

```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

Activate the virtual environment. On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.\.venv\Scripts\activate
```

### 4. Install Requirements

Install project dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Environment Variables

Create a `.env` file based on `env.template` and set correct values for environment variables.

### 6. Run Migrations

Apply database migrations:

```bash
python manage.py migrate
```

### 7. Start the Development Server

Navigate to the backend directory in the project view:

```bash
cd backend
```

Run the development server:

```bash
python manage.py runserver
```

## API Endpoints

### 1. User Signup

**Endpoint:** `POST /users/signup`

**Description:** Create a new user account.

**Request:**
```
POST http://127.0.0.1:8000/users/signup
Content-Type: application/json

{
  "username": "email@gmail.com",
  "password": "your_password",
}
```

**Response:**
```json
{
  "token": "asegwaesg",
  "user": {
    "id": 1,
    "username": "email@gmail.com",
  }
}
```

### 2. User Login

**Endpoint:** `POST /users/login`

**Description:** Authenticate a user and return an authentication token.

**Request:**
```
POST http://127.0.0.1:8000/users/login
Content-Type: application/json

{
  "username": "email@gmail.com",
  "password": "your_password"
}
```

**Response:**
```json
{
  "token": "your_token_here",
  "user": {
    "id": 1,
    "username": "your_username",
  }
}
```

### 3. Get User Info

**Endpoint:** `GET /users/me`

**Description:** Retrieve details of the authenticated user.

**Request:**
```
GET http://127.0.0.1:8000/users/me
Content-Type: application/json
Authorization: Token your_token_here
```

**Response:**
```json
{
  "success" : true,
  "user": {
    "id": 1,
    "username": "your_username",
  }
}
```

### 4. Retrieve Images by Tags

**Endpoint:** `GET /images/retrieve`

**Description:** Retrieve images based on tags.

**Request:**
```
GET http://127.0.0.1:8000/images/retrieve?tags=tag1,tag2&page=1&offset=20
Content-Type: application/json
Authorization: token your_token_here
```

**Response:**
```json
{
  "pagination": {
    "page": 1,
    "offset": 20,
    "nextPageExists": true,
    "start": 1,
    "end": 20
  }
  "images": [
    {
      "id": 1,
      "unique_id" : 'asdfwegwg2',
      "image": "http://example.com/image1.jpg",
      "image_url": "http://example.com/image1.jpg",
      "tags": ["tag1", "tag2"]
    },
  ]
}
```

