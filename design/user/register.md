# Register User

**Description:** This endpoint registers a new user by collecting their name, email, password, and date of birth. The password will be hashed before storing it in the database for security.

**URL:** `/users/register`

**Method:** `POST`

**Auth Required:** No

**Permissions Required:** None

```tsx
registerUser(name: string, email: string, password: string, dob: string): UUID
```

**Parameters**

- **Name** (`string`): User's name.
- **Email** (`string`): User's email address.
- **Password** (`string`): User's password.
- **DOB** (`string`): User's date of birth.

**Returns**

- **User ID** (`UUID`): The ID of the newly registered user.

## Request

**Headers**

`Content-Type: application/json`

**Request Body**

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "securepassword123",
  "dob": "1990-01-01"
}
```

## Response

**Success Response**

**Status:** `201 Created`

```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000"
}
```

**Error Responses**

**Status:** `400 Bad Request`

```json
{
  "error": "Invalid email format"
}
```

**Status:** `409 Conflict`

```json
{
  "error": "Email already exists"
}
```

## Workflow

1. **Receive Request:** The server receives the user registration request with the provided details.
2. **Validate Input:** The server validates the input data:
   - Check if the email is in the correct format.
   - Ensure the password meets the security criteria (e.g., minimum length, complexity).
   - Ensure the date of birth is a valid date.
3. **Check Email Uniqueness:** Verify that the provided email does not already exist in the database.
4. **Hash Password:** Use a secure hashing algorithm to hash the user's password.
5. **Store User Data:** Insert the new user record into the `users` table with the following data:
   - `user_id`: A newly generated UUID.
   - `name`: The provided name.
   - `email`: The provided email.
   - `password_hash`: The hashed password.
   - `dob`: The provided date of birth.
   - `loyalty_points`: Initialize to 0.
   - `accessibility_preferences`: Initialize to default settings.
6. **Send Confirmation:** Respond to the client with the `user_id` of the newly created user.

## Table Structure

**`users` Table**

This table will contain a user's information such as name, email, date of birth (dob), and other personal details.

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
- **Rate Limiting:** Implement rate limiting to prevent abuse of the registration endpoint.