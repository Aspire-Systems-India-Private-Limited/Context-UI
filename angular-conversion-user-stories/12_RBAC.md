# RBAC (Role-Based Access Control) - User Stories (Content Focus)

## Overview
Role and permission management interface with CRUD operations.

## Data Model
```typescript
interface RBACRole {
  id: string;
  role_name: string;
  description: string;
  permissions: string[];
  users: string[];
  created_at: string;
  updated_at: string;
}

interface Permission {
  id: string;
  name: string;
  resource: string;
  action: string; // 'create' | 'read' | 'update' | 'delete'
}
```

## User Stories

### 1. View Roles Table
- Display table with columns: Role Name, Description, Permissions Count, Users Count, Actions
- Show all roles
- GET `/rbac/roles`

### 2. Add New Role
- Click "Add Role" button
- Modal with fields: Role Name, Description, Permissions (multi-select)
- POST to `/rbac/roles`

### 3. Edit Role
- Click edit icon on row
- Pre-fill modal with existing data
- Update role name, description, permissions
- PUT to `/rbac/roles/{id}`

### 4. Delete Role
- Click delete icon
- Confirmation dialog
- DELETE to `/rbac/roles/{id}`

### 5. Assign Permissions
- Multi-select dropdown or checkbox list
- Available permissions loaded from API
- Select multiple permissions for role
- GET `/rbac/permissions` to list all

### 6. Assign Users to Role
- Search users by email/name
- Multi-select users for role
- Save user assignments
- PUT to `/rbac/roles/{id}/users`

### 7. View Role Details
- Click row to see full details
- Show: Role name, description, full permissions list, assigned users
- Side panel or modal view

### 8. Permissions Management (Optional)
- Separate tab/page for managing permissions
- CRUD for permissions
- Define resource + action combinations

## API Endpoints
```
GET    /rbac/roles                # List all roles
POST   /rbac/roles                # Create role
GET    /rbac/roles/{id}           # Get role details
PUT    /rbac/roles/{id}           # Update role
DELETE /rbac/roles/{id}           # Delete role
GET    /rbac/permissions          # List all permissions
PUT    /rbac/roles/{id}/users     # Assign users to role
```

## Key Features
- Roles table with CRUD
- Permissions assignment (multi-select)
- User assignment to roles
- Role details view
- Confirmation dialogs
- Form validation
- Search/filter roles (optional)

**Estimated Effort:** 1 week
**Complexity:** Medium
**Priority:** High