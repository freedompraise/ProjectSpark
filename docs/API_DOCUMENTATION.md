# projectSpark-api API Documentation

## Authentication
The ProjectSpark API uses JSON Web Token (JWT) for authentication. To access the authenticated endpoints, you need to include the access token in the `Authorization` header of your requests as follows:
Authorization: Bearer <token>


### User Registration
- URL: `/api/register/`
- Method: `POST`
- Description: Register a new user account.
- Request Body:
  - `username` (string): The username of the user.
  - `email` (string): The email address of the user.
  - `password` (string): The password of the user.
  - Example Request:
  ```http
  POST /api/users/register/
  Content-Type: application/json

  {
    "email": "user@example.com",
    "password": "password123"
  }
  ```
  - Example Response:
  ```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "access": "<access_token>",
  "refresh": "<refresh_token>",
  "user": {
    "email": "user@example.com"
  }
}
  ```

### User Login
- URL: `/api/login/`
- Method: `POST`
- Description: Log in an existing user.
- Request Body:
  - `email` (string): The email of the user.
  - `password` (string): The password of the user.
- Example Response: 
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
  "message": "Login successful"
}
```

## Ideas
The following endpoints are available for performing CRUD operations on ideas.

### Create Idea
- URL: `/api/ideas/`
- Method: `POST`
- Description: Create a new idea.
- Request Body:
  - `title` (string): The title of the idea.
  - `description` (string): The description of the idea.
  - `tags` (optional): List of tags associated with the idea.

-Example Request: 
```http
POST /api/ideas/
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "title": "My Idea",
  "description": "This is my idea",
  "tags": ["tag1", "tag2"]
}
```
- Example Response:
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "title": "My Idea",
  "description": "This is my idea",
  "tags": ["tag1", "tag2"]
  "created_by": "user_id>",
  "created_at": "2021-01-01T00:00:00.000000Z",
  "updated_at": "2021-01-01T00:00:00.000000Z"
}
```

### List Ideas
- URL: `/api/ideas/`
- Method: GET
- Description: Get a list of all ideas.
- Authentication: Required
- Example Request:
```http
GET /api/ideas/
Authorization: Bearer <access_token>
```
- Example Response:
```http
HTTP/1.1 200 OK
Content-Type:application/json

[
  {
    "id": 1,
    "title": "My Idea 1",
    "description": "This is my idea 1",
    "tags": ["tag1", "tag2"]
    "created_by": "user_id>",
    "created_at": "2021-01-01T00:00:00.000000Z",
    "updated_at": "2021-01-01T00:00:00.000000Z"
  },
  {
    "id": 2,
    "title": "My Idea 2",
    "description": "This is my idea 2",
    "tags": ["tag1", "tag2"]
    "created_by": "user_id>",
    "created_at": "2021-01-01T00:00:00.000000Z",
    "updated_at": "2021-01-01T00:00:00.000000Z"
  }
]
```

### Update Idea
- URL: `/api/ideas/{id}/`
- Method: `PUT` or `PATCH`
- Description: Update the details of a specific idea.
- Request Body:
  - `title` (string): The updated title of the idea.
  - `description` (string): The updated description of the idea.
  - `tags` (optional): List of updated tags associated with the idea.
- Response: Returns the updated idea details.

### Delete Idea
- URL: `/api/ideas/{id}/`
- Method: `DELETE`
- Description: Delete a specific idea.
- Response: Returns a success message if the idea is deleted successfully.

## Comments
The following endpoints are available for performing CRUD operations on comments.

### Create Comment
- URL: `/api/ideas/{idea_id}/comments/`
- Method: `POST`
- Description: Add a comment to a specific idea.
- Request Body:
  - `content` (string): The content of the comment.
- Response: Returns the created comment details.

### Get Comments
- URL: `/api/ideas/{idea_id}/comments/`
- Method: `GET`
- Description: Retrieve all comments for a specific idea.
- Response: Returns a list of comments for the specified idea.

### Update Comment
- URL: `/api/comments/{id}/`
- Method: `PUT` or `PATCH`
- Description: Update the content of a specific comment.
- Request Body:
  - `content` (string): The updated content of the comment.
- Response: Returns the updated comment details.

### Delete Comment
- URL: `/api/comments/{id}/`
- Method: `DELETE`
- Description: Delete a specific comment.
- Response: Returns a success message if the comment is deleted successfully.

## Tags

### Create a Tag
- URL: `/api/tags/`
- Method: `POST`
- Description: Create a new tag.
- Request Body:
  - `name` (string): The name of the tag.

-Example Request:
```http
POST /api/tags/
Content-Type: application/json
Authorization: Bearer <access_token>

{
  "name": "tag1"
}
```
- Example Response:
```http
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": 1,
  "name": "tag1",
  "created_at": "2021-01-01T00:00:00.000000Z",
  "updated_at": "2021-01-01T00:00:00.000000Z"
}
```

### List Tags
- URL: `/api/tags/`
- Method: `GET`
- Description: Get a list of all tags.
- Authentication: Required
- Example Request:
```http
GET /api/tags/
Authorization: Bearer <access_token>
```