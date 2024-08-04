# Delete User Profile

**Description:** This endpoint allows an authenticated user to delete their profile from the system. The user must be logged in and provide a valid authentication token. Deleting the profile will remove all associated data.

**URL:** `/users/profile`

**Method:** `DELETE`

**Auth Required:** Yes

**Permissions Required:** None

```tsx
deleteUserProfile(): void
```

**Returns**

- No content

## Request

**Headers**

`Authorization: Bearer {auth_token}`

**Request Body**

None

## Response

**Success Response**

**Status:** `204 No Content`

No content

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

1. **Receive Request:** The server receives the profile deletion request along with the authentication token.
2. **Authenticate User:** The server validates the provided authentication token.
3. **Fetch User Data:** Retrieve the user record from the `users` table using the user ID obtained from the token.
4. **Delete User Data:** Remove the user record and all associated data from the database.
5. **Send Response:** Respond to the client with a `204 No Content` status indicating successful deletion.

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

## Security Considerations

- **Authentication:** Ensure that the provided authentication token is valid and belongs to the user requesting the profile deletion.
- **Authorization:** Verify that the user has the appropriate permissions to delete their profile.
- **HTTPS:** Ensure that all API requests are made over HTTPS to protect data in transit.
- **Data Privacy:** Ensure that all user data is securely deleted from the database and that no sensitive information is left behind.
- **Rate Limiting:** Implement rate limiting to prevent abuse of the profile deletion endpoint.
- **Backup:** Ensure that recent backups are available in case the profile deletion needs to be reversed due to an error or malicious activity.