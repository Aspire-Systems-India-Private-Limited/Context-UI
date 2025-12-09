# Agent Solution Management - User Stories (Content Focus)

## Overview
Agent Solution dashboard for viewing, creating, editing, and deleting agent solutions with thumbnail upload support.

## Data Model
```typescript
interface AgentSolution {
  id: string;
  name: string;
  description: string;
  thumbnail: string;
  thumbnail_url: string;
  support: {
    email: string;
    phone: string;
  };
  url: string;
  permission_scopes: string[];
}
```

## User Stories

### 1. View Agent Solutions Table
- Display table with columns: Thumbnail, Name, Support Email, Support Phone, Scopes/Role, URL, Actions
- Click row to navigate to `/agent-sol/{id}/agent`
- Clickable URL opens in new tab

### 2. Add Agent Solution
- Click "Add Agent Solution" button in sidebar
- Modal with fields: Name, Description, Support Email, Support Phone, URL, Thumbnail (file upload), Permission Scopes
- Upload thumbnail image (preview shown)
- Add multiple permission scopes dynamically
- POST to `/agent-solutions`

### 3. Edit Agent Solution  
- Click edit icon on row
- Pre-fill form with existing data
- Thumbnail upload hidden in edit mode
- PUT to `/agent-solutions/{id}`

### 4. Update Thumbnail
- Click on thumbnail image
- Separate modal for thumbnail update
- Upload new image, preview before save
- PUT to `/agent-solutions/{id}/image`

### 5. Delete Agent Solution
- Click delete icon
- Confirmation dialog
- DELETE to `/agent-solutions/{id}`

### 6. Dynamic Permission Scopes
- Add permission scope button
- Each scope has input field and remove button
- Stored as array in permission_scopes

## API Endpoints
```
GET    /agent-solutions              # List all
POST   /agent-solutions              # Create with FormData (includes file)
PUT    /agent-solutions/{id}         # Update
PUT    /agent-solutions/{id}/image   # Update thumbnail only
DELETE /agent-solutions/{id}         # Delete
```

## Key Features
- Table with agent solutions
- Modal form for add/edit
- Separate thumbnail update modal
- Dynamic permission scopes management
- File upload with preview
- Row click navigation
- CRUD operations

**Estimated Effort:** 1.5 weeks
**Complexity:** Medium
**Priority:** High