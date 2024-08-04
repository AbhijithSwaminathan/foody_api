# Get User Profile

**Description:** This endpoint retrieves the profile information of the currently authenticated user. The user must be logged in and provide a valid authentication token.

**URL:** `/users/profile`

**Method:** `GET`

**Auth Required:** Yes

**Permissions Required:** None

```tsx
getUserProfile(): UserProfile
```

**Returns**

- **User Profile** (`UserProfile`): The profile information of the authenticated user.

## Request

**Headers**

`Authorization: Bearer {auth_token}`

**Query Parameters**

None

## Response

**Success Response**

**Status:** `200 OK`

```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "dob": "1990-01-01",
  "loyalty_points": 100,
  "accessibility_preferences": {
    "high_contrast": false,
    "screen_reader": true
  }
}
```

**Error Responses**

**Status:** `401 Unauthorized`

```json
{
  "error": "Invalid or missing authentication token"
}
```

**Status:** `404 Not Found`

```json
{
  "error": "User profile not found"
}
```

## Workflow

1. **Receive Request:** The server receives the profile request along with the authentication token.
2. **Authenticate User:** The server validates the provided authentication token.
3. **Fetch User Data:** Retrieve the user record from the `users` table using the user ID obtained from the token.
4. **Send Response:** Respond to the client with the user's profile information.

## Table Structure

**`users` Table**

This table contains a user's information such as name, email, date of birth (dob), and other personal details.

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
  "loyalty_points": 100,
  "accessibility_preferences": {
    "high_contrast": false,
    "screen_reader": true
  }
}
```

## Security Considerations

- **Authentication:** Ensure that the provided authentication token is valid and belongs to the user requesting the profile.
- **HTTPS:** Ensure that all API requests are made over HTTPS to protect data in transit.
- **Rate Limiting:** Implement rate limiting to prevent abuse of the profile endpoint.
- **Data Privacy:** Ensure that only the authenticated user's data is returned, and sensitive information is protected.