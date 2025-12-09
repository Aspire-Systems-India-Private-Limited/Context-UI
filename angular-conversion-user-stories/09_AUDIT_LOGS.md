# Audit Logs / Diagnosis - User Stories (Content Focus)

## Overview
Audit log viewer with multiple filtering options and detailed log display.

## Data Model
```typescript
interface AuditLog {
  id: string;
  content: string;
  createdOn: string;
  modifiedOn: string;
  source?: string;
  session_id?: string;
  user_id?: string;
  request_id?: string;
}
```

## User Stories

### 1. Sidebar Navigation
- Options: By Date, By DateTime Range, By Session ID, By Request ID
- Click option to show relevant form
- Active state on selected option

### 2. Filter by Date
- Single date input
- Fetch logs for specific UTC date
- GET `/audit?date={YYYY-MM-DD}`

### 3. Filter by DateTime Range  
- Start datetime and end datetime inputs
- Optional: Context/Source filter
- POST or GET with query params
- API: Custom endpoint for range + source

### 4. Filter by Last N Minutes
- Input for number of minutes
- Fetch logs from last N minutes
- GET `/audit?minutes={N}`

### 5. Filter by Session ID
- Input session ID
- Fetch all logs for that session
- Custom API endpoint

### 6. Filter by Request ID
- Input request ID
- Fetch all logs for that request
- Custom API endpoint

### 7. Display Audit Logs
- Table or card list format
- Columns: ID, Content, Created On, Modified On, Source, Session ID, User ID, Request ID
- Expandable rows for full content
- Sortable by date

### 8. Export Logs (Optional)
- Export filtered logs to CSV/JSON
- Download button

## API Endpoints
```
GET /audit?date={date}                       # By date
GET /audit?minutes={N}                       # Last N minutes
GET /audit/datetime-range?start=&end=&source= # DateTime range + source
GET /audit/session/{session_id}              # By session
GET /audit/request/{request_id}              # By request
```

## Key Features
- Multiple filter modes via sidebar
- Date, datetime range, session, request filters
- Audit log table/card display
- Expandable log content
- Real-time filtering
- Optional export

**Estimated Effort:** 1 week
**Complexity:** Medium
**Priority:** Medium