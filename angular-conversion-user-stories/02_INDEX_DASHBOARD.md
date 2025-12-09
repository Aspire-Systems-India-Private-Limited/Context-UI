# Index Dashboard - User Stories for React Conversion

## Page Overview
**File:** `templates/index.html`  
**Route:** `/` or `/admin`  
**Title:** Admin Dashboard / Operations Portal  
**Purpose:** Main landing page with dashboard cards linking to all major features and optional statistics display

---

## Design System

### Colors
- Primary Purple: `#65336e`
- Dark Purple: `#542d6b`
- Background Purple: `#692e8b`
- Light Blue: `#80c6ff`
- Text Light: `#eee`

### Layout
- Full-width gradient background
- Fixed toolbar at top (70px)
- Centered content container (max-width: 1400px)
- Responsive grid layout

---

## User Stories

### User Story 1.1: Page Layout
**As a** user  
**I want to** see a welcoming dashboard page  
**So that** I can navigate to different sections of the application

**Components:**
- **Toolbar:**
  - Logo (Aspire Systems SVG logo + "Operations Portal" text)
  - Navigation menu (imported from navbar.html)
  - User info display (Administrator with user-circle icon)
  
- **Welcome Section:**
  - Large heading: "Welcome to Operations Portal"
  - Subtitle: "Manage contexts, User Interactions, memories, and diagnosis from a unified dashboard"
  - Centered and prominent

- **Background:** 
  - Gradient from background purple to primary purple (135deg angle)

---

### User Story 1.2: Statistics Cards (Optional)
**As a** system administrator  
**I want to** see key metrics at a glance  
**So that** I can monitor system health

**Note:** This feature is currently commented out in the HTML but should be included for completeness.

**Statistics Display:**
- 4 stat cards in responsive grid
- Each card shows:
  - Metric label (uppercase)
  - Large numeric value
  - Description text
  
**Metrics:**
1. **Total Contexts**
   - Shows count of contexts
   - Label: "Active contexts"
   - API: `GET /stats/contexts/count`

2. **Active Sessions**
   - Shows current session count
   - Label: "Current sessions"
   - API: `GET /stats/sessions/count`

3. **Memories Stored**
   - Shows total memory count
   - Label: "Total memories"
   - API: `GET /stats/memories/count`

4. **Inferences**
   - Shows count from last 30 minutes
   - Label: "Last 30 minutes"
   - API: `GET /stats/audit/count`

**Features:**
- Loading state (opacity 0.6, shows "-" while loading)
- Auto-refresh every 30 seconds
- Error handling (defaults to "0" on error)

---

### User Story 1.3: Feature Cards Grid
**As a** user  
**I want to** see clickable cards for each major feature  
**So that** I can quickly navigate to the section I need

**Grid Layout:**
- Responsive grid: `repeat(auto-fit, minmax(300px, 1fr))`
- 24px gap between cards
- Cards adapt to screen size

**Card Features (4 cards):**

#### Card 1: Context Management
- **Icon:** Layer group icon (fa-layer-group)
- **Title:** "Context Management"
- **Description:** "Create, search, and manage application contexts. Configure agents, types, intents, and entity mappings."
- **Link:** `/context`
- **Footer:** "Open Context Admin" with right arrow icon

#### Card 2: User Interactions  
- **Icon:** Clock icon (fa-clock)
- **Title:** "User Interactions"
- **Description:** "Monitor and manage user sessions. View session history, active connections, and session data."
- **Link:** `/session`
- **Footer:** "Open User Interaction" with right arrow icon

#### Card 3: Memory Management
- **Icon:** Memory icon (fa-memory)
- **Title:** "Memory Management"
- **Description:** "Add, search, and organize memories. Manage user-specific data with metadata tagging and retrieval."
- **Link:** `/memory`
- **Footer:** "Open Memory Portal" with right arrow icon

#### Card 4: Diagnosis
- **Icon:** File alt icon (fa-file-alt)
- **Title:** "Diagnosis"
- **Description:** "Review system inference by date. Track changes, monitor activities, and ensure compliance."
- **Link:** `/audit`
- **Footer:** "View Inferences" with right arrow icon

**Card Styling:**
- White background
- Rounded corners (12px)
- 32px padding
- Top colored border (4px gradient from primary to light blue)
- Shadow effect
- Hover effects:
  - Lifts up 8px (`translateY(-8px)`)
  - Enhanced shadow
  - Smooth transitions

**Icon Styling:**
- 60x60px square
- Gradient background (primary to dark purple, 135deg)
- Rounded corners (12px)
- White icon color
- 28px font size
- Centered

---

### User Story 1.4: Navigation Menu
**As a** user  
**I want to** access navigation options from the toolbar  
**So that** I can jump to different sections

**Navigation Items** (from navbar.html):
- Home
- Agent Solution
- Context
- User Interaction
- Memory
- Diagnosis

**Styling:**
- Semi-transparent background with glass effect
- White text
- Icons with text labels
- Hover effects (darkens, lifts, blue border)
- Responsive: text hidden on mobile, icons only

---

## Data Models

### Statistics Response
```typescript
interface StatsResponse {
  count: number;
}
```

### Navigation Item
```typescript
interface NavItem {
  label: string;
  icon: string;
  href: string;
}
```

---

## API Endpoints

### Statistics (Optional)
- `GET /stats/contexts/count` - Returns total context count
- `GET /stats/sessions/count` - Returns active session count
- `GET /stats/memories/count` - Returns total memory count
- `GET /stats/audit/count` - Returns inference count (last 30 minutes)

**Response Format:**
```json
{
  "count": 42
}
```

---

## Component Hierarchy

```
DashboardPage
├── Toolbar
│   ├── Logo
│   ├── NavigationMenu (from Navbar component)
│   └── UserInfo
├── Container
│   ├── WelcomeSection
│   │   ├── Heading
│   │   └── Subtitle
│   ├── StatsSection (optional)
│   │   └── StatCard[] (4 cards)
│   │       ├── Label
│   │       ├── Value
│   │       └── Description
│   └── FeatureCardsGrid
│       └── DashboardCard[] (4 cards)
│           ├── CardIcon
│           ├── Title
│           ├── Description
│           └── CardFooter
```

---

## State Management

### Page State
```typescript
interface DashboardState {
  stats: {
    contextCount: number | null;
    sessionCount: number | null;
    memoryCount: number | null;
    auditCount: number | null;
    loading: boolean;
    error: string | null;
  };
}
```

### Actions
- `fetchStats()` - Fetch all statistics
- `refreshStats()` - Refresh statistics (auto-trigger every 30s)

---

## Behavior & Interactions

### Page Load
1. Render layout immediately
2. Show loading state for stats ("-" placeholders)
3. Fetch statistics in parallel
4. Update each stat as it loads
5. Remove loading class on completion
6. Handle errors gracefully (show "0" instead of crashing)

### Auto-Refresh
- Set interval for 30 seconds
- Silently refresh stats in background
- Update UI without flickering
- Clear interval on component unmount

### Card Interactions
- Hover: Lift card, enhance shadow
- Click: Navigate to feature page
- Smooth transitions (0.3s)
- No page reload (use React Router)

### Responsive Behavior
- **Desktop:** 
  - Full navigation with icons and text
  - Cards in multi-column grid
  - Large headings

- **Mobile (< 768px):**
  - Navigation shows icons only (text hidden)
  - Cards in single column
  - Smaller heading (32px vs 48px)
  - Navigation wraps if needed

---

## Accessibility

### Keyboard Navigation
- All cards are keyboard-focusable
- Tab through navigation and cards
- Enter to activate cards
- Focus indicators visible

### Screen Readers
- Semantic HTML (header, main, nav)
- Card links have descriptive text
- Icon aria-labels where needed
- Stats have proper labels

### ARIA Labels
- Logo: "Company Logo"
- Navigation: aria-label="Main navigation"
- Stats section: role="region" aria-label="System statistics"
- Cards: aria-label with full description

---

## Error Handling

### Statistics Loading Errors
- Catch fetch errors
- Log to console
- Display "0" instead of crashing
- Remove loading state
- Optionally show error toast/message

### Navigation Errors
- Handle 404s gracefully
- Fallback to dashboard if route not found

---

## Performance Considerations

### Optimization
- Lazy load stat cards if not immediately visible
- Memoize card components (React.memo)
- Debounce stat refresh if user returns to page quickly
- Cancel pending requests on unmount

### Loading Strategy
- Show page skeleton immediately
- Load stats asynchronously
- Progressive enhancement (page works even if stats fail)

---

## Testing Scenarios

### Functional Tests
1. Page loads with correct title and welcome message
2. All 4 feature cards are displayed
3. Cards link to correct routes
4. Stats load and display correctly
5. Auto-refresh works every 30 seconds
6. Error handling works when API fails
7. Navigation menu includes all items
8. User info displays correctly

### Interaction Tests
1. Clicking card navigates to correct page
2. Hover effects work on cards
3. Keyboard navigation works
4. Focus states are visible

### Responsive Tests
1. Layout adapts to mobile screens
2. Cards stack in single column on mobile
3. Navigation icons display properly on mobile
4. Text sizes adjust appropriately

---

## Configuration

### Environment Variables
```javascript
// From config.js
window.API_BASE = 'http://api.example.com';
```

### Constants
```javascript
const STATS_REFRESH_INTERVAL = 30000; // 30 seconds
const MAX_WIDTH = '1400px';
const TOOLBAR_HEIGHT = '70px';
```

---

## Sample Data

### Feature Cards Data
```javascript
const featureCards = [
  {
    id: 'context',
    icon: 'fa-layer-group',
    title: 'Context Management',
    description: 'Create, search, and manage application contexts. Configure agents, types, intents, and entity mappings.',
    link: '/context',
    linkText: 'Open Context Admin'
  },
  {
    id: 'session',
    icon: 'fa-clock',
    title: 'User Interactions',
    description: 'Monitor and manage user sessions. View session history, active connections, and session data.',
    link: '/session',
    linkText: 'Open User Interaction'
  },
  {
    id: 'memory',
    icon: 'fa-memory',
    title: 'Memory Management',
    description: 'Add, search, and organize memories. Manage user-specific data with metadata tagging and retrieval.',
    link: '/memory',
    linkText: 'Open Memory Portal'
  },
  {
    id: 'audit',
    icon: 'fa-file-alt',
    title: 'Diagnosis',
    description: 'Review system inference by date. Track changes, monitor activities, and ensure compliance.',
    link: '/audit',
    linkText: 'View Inferences'
  }
];
```

---

## Future Enhancements

1. **User Personalization:** Remember user's preferred landing card
2. **Quick Actions:** Add quick action buttons to cards (e.g., "Create New Context")
3. **Recent Activity:** Show recent user activity feed
4. **Notifications:** Display system notifications or alerts
5. **Search:** Global search bar in toolbar
6. **Dark Mode:** Theme toggle
7. **Customizable Dashboard:** Drag-and-drop card organization
8. **More Stats:** Additional metrics based on user role
9. **Charts:** Visualize trends in statistics
10. **Shortcuts:** Keyboard shortcuts for quick navigation

---

**Total User Stories:** 4 main stories  
**Components:** 10+ components  
**API Endpoints:** 4 (statistics)  
**Routes:** 1 main dashboard route + links to 4 features
