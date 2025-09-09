# API Documentation

## Users API

### 1. List All Users

**Endpoint:** `GET /core/users/`

**Description:** Retrieves a list of all users.

**How to Access:**

- No authentication required.
- Use any HTTP client (e.g., `curl`, Postman, or a browser).

**Response Example:**

```json
[
    {
        "id": 1,
        "username": "user1",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "date_of_birth": "1990-01-01",
        "phone_number": "+1234567890",
        "roles": [
            {
                "id": 1,
                "name": "Student",
                "description": "A student in the school."
            }
        ]
    }
]
```

---

### 2. Retrieve a Single User

**Endpoint:** `GET /core/users/{id}/`

**Description:** Retrieves details of a specific user by ID, including their roles.

**How to Access:**

- No authentication required.
- Replace `{id}` with the user ID.
- Use any HTTP client (e.g., `curl`, Postman, or a browser).

**Response Example:**

```json
{
    "id": 1,
    "username": "user1",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "date_of_birth": "1990-01-01",
    "phone_number": "+1234567890",
    "roles": [
        {
            "id": 1,
            "name": "Student",
            "description": "A student in the school."
        }
    ]
}
```

---

### 3. Create a User

**Endpoint:** `POST /core/users/`

**Description:** Creates a new user. Admin-only access.

**How to Access:**

- Authenticate as an admin user.
- Use the `Authorization: Token <your-admin-auth-token>` header.
- Send a JSON payload with the required user details.

**Request Example:**

```json
{
    "username": "newuser",
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@example.com",
    "date_of_birth": "1995-05-15",
    "phone_number": "+9876543210"
}
```

**Response Example:**

```json
{
    "id": 2,
    "username": "newuser",
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jane.smith@example.com",
    "date_of_birth": "1995-05-15",
    "phone_number": "+9876543210",
    "roles": []
}
```

---

### 4. Update User Info

**Endpoint:** `PUT /core/users/{id}/`

**Description:** Updates the information of a specific user. Admin-only access.

**How to Access:**

- Authenticate as an admin user.
- Use the `Authorization: Token <your-admin-auth-token>` header.
- Replace `{id}` with the user ID.
- Send a JSON payload with the updated user details.

**Request Example:**

```json
{
    "first_name": "Jane",
    "last_name": "Doe"
}
```

**Response Example:**

```json
{
    "id": 2,
    "username": "newuser",
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane.smith@example.com",
    "date_of_birth": "1995-05-15",
    "phone_number": "+9876543210",
    "roles": []
}
```

---

### 5. Remove User

**Endpoint:** `DELETE /core/users/{id}/`

**Description:** Deletes a specific user. Admin-only access.

**How to Access:**

- Authenticate as an admin user.
- Use the `Authorization: Token <your-admin-auth-token>` header.
- Replace `{id}` with the user ID.

**Response Example:**

```json
{
    "message": "User deleted successfully."
}
```

---

## Roles API

### 1. List All Roles

**Endpoint:** `GET /api/roles/`

**Description:** Retrieves a list of all roles.

**How to Access:**

- No authentication required.
- Use any HTTP client (e.g., `curl`, Postman, or a browser).

**Response Example:**

```json
[
    {
        "id": 1,
        "name": "Student",
        "description": "A student in the school."
    },
    {
        "id": 2,
        "name": "Teacher",
        "description": "A teacher in the school."
    }
]
```

---

### 2. Create a Role

**Endpoint:** `POST /api/roles/`

**Description:** Creates a new role.

**How to Access:**

- Authenticate as an admin user.
- Use the `Authorization: Token <your-admin-auth-token>` header.
- Send a JSON payload with the role details.

**Request Example:**

```json
{
    "name": "Coordinator",
    "description": "A coordinator in the school."
}
```

**Response Example:**

```json
{
    "id": 3,
    "name": "Coordinator",
    "description": "A coordinator in the school."
}
```

---

## User-Role API

### 1. Assign Role to User

**Endpoint:** `POST /api/users/{id}/roles/`

**Description:** Assigns a role to a specific user.

**How to Access:**

- Authenticate as an admin user.
- Use the `Authorization: Token <your-admin-auth-token>` header.
- Replace `{id}` with the user ID.
- Send a JSON payload with the `role_id`.

**Request Example:**

```json
{
    "role_id": 1
}
```

**Response Example:**

```json
{
    "message": "Role Student assigned to user user1."
}
```

---

### 2. Remove Role from User

**Endpoint:** `DELETE /api/users/{id}/roles/{role_id}/`

**Description:** Removes a role from a specific user.

**How to Access:**

- Authenticate as an admin user.
- Use the `Authorization: Token <your-admin-auth-token>` header.
- Replace `{id}` with the user ID and `{role_id}` with the role ID.

**Response Example:**

```json
{
    "message": "Role Student removed from user user1."
}
```
