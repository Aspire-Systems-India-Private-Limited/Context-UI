# Sentiment Analyzer - User Stories (Content Focus)

## Overview
Feedback sentiment analysis dashboard with charts and category breakdown.

## Data Model
```typescript
interface Feedback {
  id: string;
  agent_code: string;
  context_code: string;
  feedback_type: 'good' | 'bad';
  comment: string;
  timestamp: string;
  sentiment?: {
    score: number;
    label: 'positive' | 'negative' | 'neutral';
    confidence: number;
  };
  category?: string;
}

interface SentimentSummary {
  total_count: number;
  positive_count: number;
  negative_count: number;
  neutral_count: number;
  average_score: number;
  categories: Record<string, number>;
}
```

## User Stories

### 1. Filter Feedback
- Dropdown: Select Agent Code
- Dropdown: Select Feedback Type (Good/Bad/All)
- Date range: Start Date, End Date
- Fetch button
- GET `/feedback?agent_code=&feedback_type=&start_date=&end_date=`

### 2. Display Sentiment Summary Cards
- Card 1: Total Feedback Count
- Card 2: Positive Count (%)
- Card 3: Negative Count (%)
- Card 4: Neutral Count (%)
- Card 5: Average Sentiment Score

### 3. Sentiment Distribution Chart
- Pie/Doughnut chart: Positive vs Negative vs Neutral
- Legend with percentages
- Click slice to filter table

### 4. Sentiment Score Trend
- Line chart: X-axis = Time, Y-axis = Sentiment Score
- Show trend over selected date range
- Tooltip shows date + score

### 5. Category Breakdown
- Bar chart: X-axis = Category, Y-axis = Count
- Categories auto-detected or predefined
- Show top 10 categories

### 6. Feedback Table
- Columns: ID, Agent, Context, Type, Comment, Sentiment Score, Sentiment Label, Category, Timestamp
- Sortable by score, timestamp
- Pagination
- Click row to view full details

### 7. Feedback Details Modal
- Full comment text
- Sentiment score with confidence level
- Category tags
- Timestamp
- Agent and context info

### 8. Export Data
- Export filtered feedback to CSV
- Export chart data
- Download button

## API Endpoints
```
GET /feedback                        # List feedback with filters
GET /feedback/sentiment-summary      # Summary stats
GET /feedback/{id}                   # Single feedback details
POST /feedback/analyze               # Run sentiment analysis (if needed)
```

## Key Features
- Filter by agent, type, date range
- Summary cards with statistics
- Pie chart for distribution
- Line chart for trend
- Bar chart for categories
- Feedback table with sort/pagination
- Details modal
- Export functionality
- Sentiment scoring visualization

**Estimated Effort:** 1.5 weeks
**Complexity:** Medium-High
**Priority:** Medium
**Dependencies:** Chart.js or Recharts