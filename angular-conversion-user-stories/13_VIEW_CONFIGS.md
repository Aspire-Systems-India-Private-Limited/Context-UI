# View Configurations - User Stories (Content Focus)

## Overview
Configuration viewer displaying system and agent configurations in JSON format.

## Data Model
```typescript
interface Configuration {
  id: string;
  name: string;
  type: 'system' | 'agent' | 'database' | 'api';
  config_data: Record<string, any>; // JSON object
  agent_code?: string;
  last_updated: string;
  updated_by?: string;
}
```

## User Stories

### 1. List Configurations
- Display configurations as cards or table
- Show: Config Name, Type, Agent Code (if applicable), Last Updated
- Click to view details
- GET `/configs`

### 2. Filter by Type
- Dropdown to filter: All, System, Agent, Database, API
- Refresh list based on selection

### 3. Filter by Agent Code
- Input field for agent code
- Show only configs for specific agent
- GET `/configs?agent_code={code}`

### 4. View Configuration Details
- Click config to expand/open modal
- Display JSON data in formatted viewer
- Syntax highlighting
- Collapsible JSON tree view

### 5. Copy Configuration
- Copy button to copy JSON to clipboard
- Success notification

### 6. Download Configuration
- Download as JSON file
- Button to export config

### 7. Search Configurations
- Search bar to filter by name/key
- Real-time search as user types

### 8. Read-Only View
- All configs are view-only (no edit)
- Edit button links to admin config page (if exists)

## API Endpoints
```
GET /configs                    # List all configurations
GET /configs?type={type}        # Filter by type
GET /configs?agent_code={code}  # Filter by agent
GET /configs/{id}               # Get single config
```

## Key Features
- Configuration list (cards or table)
- Filter by type and agent code
- JSON viewer with syntax highlighting
- Collapsible JSON tree
- Copy to clipboard
- Download JSON
- Search functionality
- Read-only interface

**Estimated Effort:** 3-4 days
**Complexity:** Low-Medium
**Priority:** Low
**Dependencies:** JSON viewer library (react-json-view)