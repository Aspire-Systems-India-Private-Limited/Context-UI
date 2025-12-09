# View Agent Details - User Stories (Content Focus)

## Overview
Detailed view page for a single agent displaying all properties, intents, and entities with RBAC permissions.

## Data Model
```typescript
interface AgentDetails {
  id: string;
  name: string;
  code: string;
  version: string;
  description: string;
  status: 'active' | 'inactive';
  provider: string;
  url: string;
  type: string;
  environment: string;
  support: {
    email: string;
    phone: string;
  };
  category: string;
  intents: Intent[];
  rbac_permissions?: Permission[];
}

interface Intent {
  name: string;
  entities: Entity[];
}

interface Entity {
  type: string;
  example: string;
  description: string;
}
```

## User Stories

### 1. Display Agent Basic Info
- Page header with agent name
- Cards/sections for: 
  - Basic Info (ID, Code, Version, Status)
  - Contact Info (Support Email, Phone)
  - Technical Info (Provider, URL, Type, Environment, Category)
- Description field with full text

### 2. Display Intents Section
- Expandable/collapsible section for intents
- List all intents with entity count
- Click intent to expand and show entities

### 3. Display Entities Within Intent
- Nested under each intent
- Show: Entity Type, Example, Description
- Formatted display for readability

### 4. RBAC Permissions Display
- Section showing role-based permissions for this agent
- Show: Allowed roles, Restricted actions, User access levels
- Read-only view

### 5. Back Navigation
- Back button to return to agents list
- Breadcrumb: Agent Solutions > Agents > {Agent Name}

### 6. Edit Agent
- Edit button redirects to agent edit modal/page
- Only visible if user has edit permission

### 7. Export Agent Data
- Export agent details as JSON
- Download button

## API Endpoints
```
GET /agents/{id}                    # Get agent full details
GET /agents/{id}/permissions        # Get RBAC permissions for agent (optional)
```

## Key Features
- Full agent details display
- Collapsible intents/entities sections
- RBAC permissions view
- Back navigation
- Edit redirect button
- Export to JSON
- Read-only interface

**Estimated Effort:** 3-4 days
**Complexity:** Low-Medium
**Priority:** Medium