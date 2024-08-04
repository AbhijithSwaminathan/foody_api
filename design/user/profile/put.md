# Update User Profile

**Description:** This endpoint allows an authenticated user to update their profile information, such as name, date of birth, and accessibility preferences. The user must be logged in and provide a valid authentication token.

**URL:** `/users/profile`

**Method:** `PUT`

**Auth Required:** Yes

**Permissions Required:** None

```tsx
updateUserProfile(name?: string, dob?: string, accessibility_preferences?: AccessibilityPreferences): UserProfile
```

**Parameters**

- **Name** (`string`, optional): User's name.
- **DOB** (`string`, optional): User's date of birth.
- **Accessibility Preferences** (`AccessibilityPreferences`, optional): User's accessibility settings/preferences.

**Returns**

- **User Profile** (`UserProfile`): The updated profile information of the authenticated user.

## Request

**Headers**

`Content-Type: application/json`
`Authorization: Bearer {auth_token}`

**Request Body**

```json
{
  "name": "John Doe",
  "dob": "1990-01-01",
  "accessibility_preferences": {
    "high_contrast": false,
    "screen_reader": true
  }
}
```

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

**Status:** `400 Bad Request`

```json
{
  "error": "Invalid input data"
}
```

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

1. **Receive Request:** The server receives the profile update request along with the authentication token and new profile data.
2. **Authenticate User:** The server validates the provided authentication token.
3. **Validate Input:** The server validates the input data:
   - Check if the name and date of birth (if provided) are in the correct format.
   - Ensure the accessibility preferences (if provided) are valid.
4. **Fetch User Data:** Retrieve the user record from the `users` table using the user ID obtained from the token.
5. **Update User Data:** Update the user record with the new profile data.
6. **Send Response:** Respond to the client with the updated user's profile information.

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

- **Authentication:** Ensure that the provided authentication token is valid and belongs to the user requesting the profile update.
- **Input Validation:** Validate all input data to prevent SQL injection, cross-site scripting (XSS), and other vulnerabilities.
- **HTTPS:** Ensure that all API requests are made over HTTPS to protect data in transit.
- **Rate Limiting:** Implement rate limiting to prevent abuse of the profile update endpoint.
- **Data Privacy:** Ensure that only the authenticated user's data is updated, and sensitive information is protected.