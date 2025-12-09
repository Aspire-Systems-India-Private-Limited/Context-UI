# Aggregated Cost Data - User Stories (Content Focus)

## Overview
View aggregated cost data across agents with summary tables and total calculations.

## Data Model
```typescript
interface AggregatedCost {
  agent_code: string;
  agent_name?: string;
  total_cost: number;
  total_tokens: number;
  request_count: number;
  avg_cost_per_request: number;
  period: string; // e.g., "2025-01" or "Q1 2025"
}

interface CostSummary {
  grand_total_cost: number;
  grand_total_tokens: number;
  total_requests: number;
  agent_count: number;
  period_range: string;
}
```

## User Stories

### 1. Display Summary Cards
- Card 1: Grand Total Cost
- Card 2: Total Tokens Used
- Card 3: Total Requests
- Card 4: Number of Agents

### 2. Display Aggregated Table
- Columns: Agent Code, Agent Name, Total Cost, Total Tokens, Request Count, Avg Cost/Request
- Sortable by any column
- Pagination for large datasets

### 3. Filter by Period
- Dropdown or date picker for period selection
- Options: Last Month, Last Quarter, Last Year, Custom Range
- Refresh data on period change

### 4. Filter by Agent
- Search/filter by agent code or name
- Show data for specific agent(s)

### 5. Cost Breakdown Chart
- Bar chart: X-axis = Agent, Y-axis = Total Cost
- Show top 10 agents by cost
- Click bar to filter table

### 6. Export Data
- Export aggregated data to CSV/Excel
- Download button

### 7. Drill-Down to Details
- Click agent row to see monthly breakdown
- Navigate to detailed cost metrics page

## API Endpoints
```
GET /cost/aggregated                      # All aggregated data
GET /cost/aggregated?period={period}      # Filter by period
GET /cost/aggregated?agent={code}         # Filter by agent
GET /cost/summary                         # Summary statistics
```

## Key Features
- Summary cards with totals
- Aggregated data table
- Period filter
- Agent filter
- Bar chart visualization
- Export to CSV
- Drill-down navigation
- Sortable table

**Estimated Effort:** 4-5 days
**Complexity:** Medium
**Priority:** Medium
**Dependencies:** Chart.js or Recharts