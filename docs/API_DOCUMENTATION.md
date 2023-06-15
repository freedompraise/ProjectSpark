# projectSpark-api API Documentation

## Authentication
Before making requests to the projectSpark-api, you need to authenticate with a valid JWT token. To obtain the token, make a `POST` request to the `/api/auth` endpoint with your credentials (username and password). The API will respond with a token that you can include in the `Authorization` header of subsequent requests as follows:
Authorization: Bearer <token>


## Endpoints

### User Registration
- URL: `/api/register/`
- Method: `POST`
- Description: Register a new user account.
- Request Body:
  - `username` (string): The username of the user.
  - `email` (string): The email address of the user.
  - `password` (string): The password of the user.
- Response: Returns the user details if registration is successful, or an error message if registration fails.

### User Login
- URL: `/api/login/`
- Method: `POST`
- Description: Authenticate and obtain a JWT token.
- Request Body:
  - `username` (string): The username of the user.
  - `password` (string): The password of the user.
- Response: Returns a JWT token if authentication is successful, or an error message if authentication fails.

### Create Idea
- URL: `/api/ideas/`
- Method: `POST`
- Description: Create a new idea.
- Request Body:
  - `title` (string): The title of the idea.
  - `description` (string): The description of the idea.
- Response: Returns the created idea details.

### Get Idea
- URL: `/api/ideas/{id}/`
- Method: `GET`
- Description: Retrieve details of a specific idea.
- Response: Returns the details of the specified idea.

### Update Idea
- URL: `/api/ideas/{id}/`
- Method: `PUT` or `PATCH`
- Description: Update the details of a specific idea.
- Request Body:
  - `title` (string): The updated title of the idea.
  - `description` (string): The updated description of the idea.
- Response: Returns the updated idea details.

### Delete Idea
- URL: `/api/ideas/{id}/`
- Method: `DELETE`
- Description: Delete a specific idea.
- Response: Returns a success message if the idea is deleted successfully.

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

