# Session Management - User Stories (Content Focus)

## Overview
User Interaction page displaying collapsible sessions with messages and detailed request/response data.

## Data Model
```typescript
interface Session {
  session_id: string;
  user_name: string;
  email: string;
  start_date: string;
  end_date: string;
  messages: Message[];
}

interface Message {
  message_id: string;
  user_message: string;
  ai_response: string;
  timestamp: string;
  model: string;
  token_count: number;
  intent_code?: string;
  agent_code?: string;
}
```

## User Stories

### 1. Search Sessions
- Date range filter (start date, end date)
- Checkbox: Include ongoing sessions
- Search button to fetch filtered sessions
- POST to `/sessions/search`

### 2. Display Sessions List
- Expandable/collapsible session cards
- Show: Session ID, Username, Email, Start Date, End Date
- Click header to expand/collapse messages

### 3. View Messages in Session
- Nested messages under each session
- Click message to see full details
- Show: User Message preview, AI Response preview, Timestamp

### 4. View Message Details
- Click message to expand detailed view
- Fields: User Message, AI Response, Model, Token Count, Intent Code, Agent Code, Timestamp
- Copy button for request/response data

### 5. Save Memory from Session
- "Save Memory" button on session
- POST to `/sessions/memory` with session_id

### 6. Collapsible UI
- Sessions expand/collapse on click
- Messages expand/collapse on click
- Smooth animations for expand/collapse
- Only one section expanded at a time (optional)

### 7. Sidebar Navigation
- Fixed sidebar with navigation options
- Collapsible sidebar on mobile
- Menu toggle button

## API Endpoints
```
POST /sessions/search         # Search with date range + ongoing flag
POST /sessions/memory         # Save session as memory
```

## Key Features
- Date range search with ongoing sessions filter
- Collapsible nested structure (sessions > messages > details)
- Full request/response data view
- Save session to memory
- Responsive sidebar navigation
- Copy-to-clipboard functionality

**Estimated Effort:** 1.5 weeks
**Complexity:** Medium-High
**Priority:** High