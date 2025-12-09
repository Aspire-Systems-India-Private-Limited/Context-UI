# Cost Metrics Dashboard - User Stories (Content Focus)

## Overview
Cost and metrics visualization dashboard with multiple chart types and data filtering.

## Data Model
```typescript
interface AgentMetric {
  id: string;
  AgentCode: string;
  IntentCode?: string;
  DateTime: string;
  MetricCode: string;
  MetricValue: number;
  TokenCount?: number;
  SessionId?: string;
  Model?: string;
  UserId?: string;
  RequestId?: string;
}

interface MonthlyCost {
  agent_code: string;
  month: string;
  total_cost: number;
  total_tokens: number;
}

interface AgentViolation {
  Agent: string;
  Status: string;
  ViolationType: string;
  Timestamp: string;
}
```

## User Stories

### 1. Sidebar Navigation
- Options: Metrics, Monthly Cost, Aggregated Cost, Violations
- Click to switch views
- Active state on selected view

### 2. Agent Metrics View
- Form: Agent Code, Intent Code, Metric Code, Start DateTime, End DateTime
- Fetch metrics button
- Display results in chart (line/bar chart)
- Table view below chart
- POST `/metrics/agent` with filters

### 3. Monthly Cost View
- Display monthly cost by agent
- Bar chart: X-axis = Month, Y-axis = Cost
- Table: Agent Code, Month, Total Cost, Total Tokens
- GET `/cost/monthly`

### 4. Aggregated Cost View
- Summary of total costs across all agents
- Pie chart: Cost breakdown by agent
- Summary cards: Total Cost, Total Tokens, Avg Cost per Agent
- GET `/cost/aggregated`

### 5. Violations View
- Table of agent violations
- Columns: Agent, Violation Type, Status, Timestamp
- Filter by agent code
- Resolve violation button
- GET `/violations`
- POST `/violations/resolve/{agent_code}`

### 6. Chart Visualization
- Line chart for metrics over time
- Bar chart for monthly costs
- Pie chart for cost distribution
- Interactive tooltips
- Legend display

### 7. Data Table
- Show chart data in tabular format
- Sortable columns
- Pagination for large datasets
- Export to CSV (optional)

### 8. Filter Form
- Dynamic form based on selected view
- Date/datetime pickers
- Agent/Intent/Metric dropdowns
- Submit button to refresh data

## API Endpoints
```
POST /metrics/agent                        # Agent metrics by filters
GET  /cost/monthly                         # Monthly cost data
GET  /cost/aggregated                      # Aggregated cost summary
GET  /violations                           # Agent violations
POST /violations/resolve/{agent_code}      # Resolve violations
```

## Key Features
- Multi-view dashboard (metrics, cost, violations)
- Multiple chart types (line, bar, pie)
- Date range filtering
- Agent/Intent/Metric filters
- Violations management
- Data table with sort/pagination
- Chart + table combined view
- Resolve violations action

**Estimated Effort:** 2 weeks
**Complexity:** High
**Priority:** High
**Dependencies:** Chart.js or Recharts