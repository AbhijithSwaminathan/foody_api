# User Login

**Description:** This endpoint allows a user to log in by providing their email and password. The server will verify the credentials and, if valid, return an authentication token.

**URL:** `/users/login`

**Method:** `POST`

**Auth Required:** No

**Permissions Required:** None

```tsx
loginUser(email: string, password: string): AuthToken
```

**Parameters**

- **Email** (`string`): User's email address.
- **Password** (`string`): User's password.

**Returns**

- **Auth Token** (`string`): A token that can be used to authenticate subsequent requests.

## Request

**Headers**

`Content-Type: application/json`

**Request Body**

```json
{
  "email": "john.doe@example.com",
  "password": "securepassword123"
}
```

## Response

**Success Response**

**Status:** `200 OK`

```json
{
  "auth_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTIzZTQ1NjctZTg5Yi0xMmQzLWE0NTYtNDI2NjE0MTc0MDAwIiwiaWF0IjoxNjE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```

**Error Responses**

**Status:** `400 Bad Request`

```json
{
  "error": "Invalid email or password format"
}
```

**Status:** `401 Unauthorized`

```json
{
  "error": "Invalid email or password"
}
```

## Workflow

1. **Receive Request:** The server receives the login request with the provided email and password.
2. **Validate Input:** The server validates the input data:
   - Check if the email is in the correct format.
   - Ensure the password meets the security criteria (e.g., minimum length, complexity).
3. **Retrieve User Data:** Fetch the user record from the `users` table using the provided email.
4. **Verify Password:** Compare the provided password with the stored password hash.
5. **Generate Auth Token:** If the password is correct, generate an authentication token (e.g., JWT).
6. **Send Response:** Respond to the client with the generated `auth_token`.

## Table Structure

**`users` Table**

This table contains a user's information such as name, email, password hash, and other personal details.

- `user_id` (`UUID`): Unique identifier for each user.
- `name` (`string`): User's name.
- `email` (`string`): User's email address.
- `password_hash` (`string`): Encrypted user password.
- `dob` (`date`): User's date of birth.
- `loyalty_points` (`integer`): Points accumulated through the loyalty program.
- `accessibility_preferences` (`json`): User's accessibility settings/preferences.

## Example Database Entry

```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password_hash": "$2b$12$KIXG8Z.rJGrT0TQJGYeW7e3P/Kmk5L5Hv1eC8c4s3G8GvhL9",
  "dob": "1990-01-01",
  "loyalty_points": 0,
  "accessibility_preferences": {
    "high_contrast": false,
    "screen_reader": true
  }
}
```

## Security Considerations

- **Password Storage:** Use a strong hashing algorithm like bcrypt to store passwords securely.
- **Input Validation:** Ensure all input data is validated to prevent SQL injection, cross-site scripting (XSS), and other vulnerabilities.
- **HTTPS:** Ensure that all API requests are made over HTTPS to protect data in transit.
- **Rate Limiting:** Implement rate limiting to prevent abuse of the login endpoint.
- **Auth Token Security:** Ensure that the authentication token is securely generated and signed (e.g., using JWT with a secret key).