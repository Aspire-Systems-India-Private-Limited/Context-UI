# 🎯 Figma Maker Input Prompts - Quick Start

This document provides **ready-to-use prompts** for Figma Maker to generate Angular components from the user stories.

---

## 🎨 General Design Prompt (Use for All Pages)

```
Create an Angular application using the existing design system:

**🎨 Style Files (MUST USE):**
- Import `/styles/globals.css` for design tokens and theming
- Import `/styles/ats-utilities.css` for utility classes
- Follow guidelines in `/guidelines/Guidelines.md`

**Colors:**
- Primary: #65336e (purple)
- Dark: #542d6b (dark purple)
- Background: #692e8b (gradient background)
- Accent: #80c6ff (light blue)
- Text Light: #eee

**Typography:**
- Font Family: Maven Pro, Segoe UI, Arial
- Base font-size: 14px (from globals.css)
- Headings: 24-48px, weight 500-600
- Body: 14px, line-height 1.5

**Components:**
- Use modern, clean design
- Rounded corners (4px, 8px, 12px)
- Subtle shadows
- Smooth transitions (0.3s)
- Responsive layout with utility classes from ats-utilities.css

**Icons:** Use Font Awesome 6.4.0 and Lucide icons

**Layout:** Fixed toolbar (70px), sidebar (200px), responsive content area
```

---

## 📄 Page-Specific Prompts

### 1. Dashboard (index.html)

```
Design a dashboard landing page with:

1. **Top Toolbar:**
   - Logo with "Operations Portal" text
   - Navigation menu (Home, Agent Solution, Context, User Interaction, Memory, Diagnosis)
   - User info (Administrator with user-circle icon)
   - Purple background (#65336e)

2. **Welcome Section:**
   - Large heading: "Welcome to Operations Portal"
   - Subtitle: "Manage contexts, User Interactions, memories, and diagnosis from a unified dashboard"
   - Centered, white text on gradient purple background

3. **Statistics Cards (Optional - 4 cards in grid):**
   - Total Contexts
   - Active Sessions
   - Memories Stored
   - Inferences
   - Semi-transparent cards with large numbers
   - Blur glass effect

4. **Feature Cards (4 cards in responsive grid):**
   - Context Management (layer-group icon)
   - User Interactions (clock icon)
   - Memory Management (memory icon)
   - Diagnosis (file-alt icon)
   
   Each card has:
   - Icon in gradient purple box (60x60px, rounded)
   - Title (24px, purple)
   - Description (14px, gray)
   - Footer with "Open [Name]" + arrow icon
   - White background, rounded corners
   - Top colored border stripe
   - Hover: lifts up, enhanced shadow

**Layout:** Max-width 1400px, centered, gradient background
**Grid:** repeat(auto-fit, minmax(300px, 1fr))
```

---

### 2. Admin Context UI (admin.html)

```
Design a complex context management interface with sidebar navigation:

1. **Sidebar (200px, fixed left):**
   - Logo/Title: "ContextAdmin"
   - Navigation buttons (stacked vertically):
     - Create Context (plus icon, active state)
     - Search Contexts (search icon)
     - Create Reflection Context (message-square icon)
     - Search Reflection Context (search-check icon)
   - Purple background, white text
   - Active state: darker purple, rounded

2. **Main Content Area:**
   
   **A. Create Context Panel:**
   - AI Generation Section (highlighted with gradient border):
     - Intent input
     - Task input
     - Context Type dropdown (taskcontext, domaincontext, responsecontext, parentcontext)
     - Additional Info input
     - "Generate Content with AI" button (gradient purple-to-blue, sparkles icon)
   
   - Manual Form Section:
     - Two-column grid layout
     - Fields: Context Code, Agent Code, Type, Intent, Version ID, Context Version, Parent Context Code
     - Content textarea (large, 6 rows)
     - Dynamic Filters section (add/remove key-value pairs)
     - Default and Latest checkboxes
     - "Create Context" button (purple)
   
   **B. Search Context Panel:**
   - Search form (Agent Code + Version ID)
   - Tree View toggle checkbox
   - Search results as editable cards with:
     - All context fields (inline editable)
     - Filters section (add/remove)
     - Action buttons: Save, Delete, Test, History
   - Tree View (when enabled):
     - Hierarchical structure: Agent > Intent > Type
     - Expandable nodes
     - Click to show details
   
   **C. Modals:**
   - Version History Modal (large, 900px):
     - Version list (scrollable)
     - Version details panel
     - Close button
   
   - Test Modal (very large, 1400px):
     - Basic Configuration section
     - Context List section (add items)
     - Image Input section (sample images + custom URLs)
     - Version Sets section (multiple sets, each with multiple versions)
     - Execute Tests button (gradient)
     - Results display (formatted JSON)
   
   **D. Feedback Panels:**
   - Two large selection cards (Good 👍 / Bad 👎)
   - Form with Agent Code, Intent, Reason, Filters, Content
   - Search results with feedback badge

**Toolbar:** Page title, user info
**Overall:** White cards on light gray background
```

---

### 3. Agent Management (agent.html)

```
Design an agent management dashboard with:

1. **Sidebar + Toolbar** (same as Admin Context UI)

2. **Main Content:**
   - Grid of agent cards (3 columns, responsive)
   - Each card shows:
     - Agent icon (robot)
     - Agent name (heading)
     - Agent code
     - Description (truncated)
     - Edit/View/Delete buttons
   - Hover: lift card, show shadow
   - Click card: navigate to details

3. **Create Agent Button:** 
   - Floating action button (bottom-right)
   - OR top-right with plus icon
   - Purple gradient

**Color:** White cards, purple accents
**Layout:** Grid with gap 24px
```

---

### 4. Session/User Interaction (session.html)

```
Design a session management interface:

1. **Top Section:**
   - Search form:
     - Start Date input (date picker)
     - End Date input (date picker)
     - "Include filters" checkbox
     - Search button
   
2. **Main Layout (2 columns):**
   
   **Left Side (Sessions List):**
   - Session cards (stacked, scrollable)
   - Each card shows:
     - Session ID
     - User ID
     - Timestamp
     - Message count badge
     - Click to view details
   - "Load More Sessions" button at bottom
   
   **Right Side (Collapsible Sidebar):**
   - Toggle button to show/hide
   - Message Details panel:
     - User message
     - AI response
     - Metadata (JSON display)
     - Timestamp
   - Memory Feedback Form:
     - Content textarea
     - Add Metadata Fields (key-value pairs, dynamic)
     - Submit button

**Responsive:** On mobile, sidebar becomes full-screen overlay
**Colors:** White cards, purple buttons
```

---

### 5. Memory Management (memory.html)

```
Design a memory management interface:

1. **Tab Switcher:**
   - "Add Memory" tab
   - "Search Memory" tab
   - Active tab highlighted (purple underline)

2. **Add Memory Panel:**
   - User ID input
   - Agent Code input
   - Memory Content textarea (large)
   - Metadata section (dynamic key-value pairs)
   - "Add Metadata Field" button
   - Submit button (purple)

3. **Search Memory Panel:**
   - User ID input (required)
   - Agent Code input (optional)
   - Search button
   - Results displayed as cards:
     - Memory content
     - User ID, Agent Code
     - Metadata display
     - Created timestamp
     - Edit/Delete buttons

**Layout:** Single column, max-width 1000px, centered
**Cards:** White background, subtle shadow
```

---

### 6. Sentiment Analyzer (sentiment-analyzer.html)

```
Design a feedback sentiment analysis dashboard:

1. **Filter Section:**
   - Feedback Type dropdown (User/Agent)
   - Agent Code input
   - Date Range picker (start/end)
   - Sentiment filter (Positive/Negative/Neutral/All)
   - "Load Feedback" button (primary)
   - "Reset Filters" button (secondary)

2. **Statistics Cards (4 cards in row):**
   - Total Feedback (count)
   - Positive (count + percentage, green)
   - Negative (count + percentage, red)
   - Neutral (count + percentage, yellow)
   - Large numbers, color-coded

3. **Feedback Cards (list):**
   - User name
   - Agent code
   - Large sentiment badge (Positive/Negative/Neutral, color-coded)
   - Sentiment scores (3 bars: positive, negative, neutral)
   - Summary section (expandable)
   - Two columns:
     - Positive sentiments list (green checkmarks)
     - Negative sentiments list (red X marks)
   - Categories section (grouped by category)
   - Request/Response section (two columns, code blocks)
   - Expand/Collapse buttons
   - Created timestamp

**Colors:** 
- Positive: #28a745 (green)
- Negative: #dc3545 (red)
- Neutral: #ffc107 (yellow)
- Purple accents for non-sentiment elements

**Layout:** Full-width cards, stacked vertically
```

---

### 7. Cost Metrics (cost_metrics.html)

```
Design a cost metrics dashboard:

1. **Filters (top section):**
   - Date Range picker
   - Agent Code filter (dropdown)
   - Model filter (dropdown)
   - User ID filter (input)
   - Apply Filters button

2. **KPI Cards (4 cards in grid):**
   - Total Cost (large currency display)
   - Total Tokens (number with K/M suffix)
   - Total Requests (count)
   - Average Cost per Request (currency)
   - Color-coded icons

3. **Charts Section (2x2 grid):**
   - Cost over Time (line chart)
   - Cost by Agent (bar chart)
   - Cost by Model (pie chart)
   - Tokens Usage Trend (area chart)

4. **Data Table:**
   - Columns: Date, Agent, Model, Requests, Tokens, Cost
   - Sortable headers
   - Pagination controls
   - Export to CSV button (top-right)

**Colors:** Use purple for charts, varying shades for data series
**Layout:** Full-width, responsive grid
```

---

### 8. RBAC Management (rbac.html)

```
Design an RBAC management interface:

1. **Top Section:**
   - Page title: "RBAC Dashboard"
   - "Add RBAC" button (top-right, purple)
   - "Home" button

2. **RBAC Table:**
   - Columns:
     - User ID
     - Role
     - Permissions (truncated with "View" button)
     - Created Date
     - Actions (View, Edit, Delete buttons)
   - Striped rows
   - Hover highlight

3. **Add RBAC Modal:**
   - User ID input
   - Role dropdown (Admin, User, Viewer, etc.)
   - Permissions section:
     - Checkboxes for common permissions
     - OR JSON editor for advanced permissions
   - Save/Cancel buttons

4. **View Permissions Modal:**
   - JSON display with syntax highlighting
   - Copy button
   - Close button

**Colors:** Purple theme, white background
**Layout:** Full-width table, modals 600px wide
```

---

## 🎯 Component-Specific Prompts

### Navbar Component

```
Create a navigation bar component:

- Dark purple background (#65336e)
- 6 navigation links:
  1. Home (fa-home icon)
  2. Agent Solution (fa-robot icon)
  3. Context (fa-cog icon)
  4. User Interaction (fa-user icon)
  5. Memory (fa-clock icon)
  6. Diagnosis (fa-file-alt icon)

- Each link:
  - Icon + text label
  - Semi-transparent button style
  - White text
  - Hover: darker background, light blue border
  - Active: highlighted

- User info section (right side):
  - User-circle icon
  - "Administrator" text
  - Italic style

- Responsive: Hide text labels on mobile, show icons only
```

---

### Modal Component

```
Create a reusable modal dialog:

- Overlay: Dark semi-transparent background (rgba(0,0,0,0.5))
- Content box:
  - White background
  - Rounded corners (8px)
  - Max-width: 900px (configurable)
  - Max-height: 85vh
  - Scrollable content
  - Shadow: 0 4px 20px rgba(0,0,0,0.3)

- Header:
  - Title (left, purple color)
  - Close button (right, X icon, hover turns red)
  - Bottom border

- Content area: Padding 30px
- Animations: Fade in (0.3s), slide in from top

- Backdrop click: Close modal
- Escape key: Close modal
```

---

### Button Component

```
Create button variants:

1. **Primary Button (.btn):**
   - Purple background (#65336e)
   - White text
   - Padding: 10px 24px
   - Border-radius: 4px
   - Hover: darker purple (#542d6b)
   - Disabled: opacity 0.6

2. **AI Button (.btn-ai):**
   - Gradient background (purple to blue)
   - White text
   - Icon + text
   - Hover: lift up 2px, enhanced shadow
   - Disabled: no transform

3. **History Button (.btn-history):**
   - Smaller size (padding: 6px 12px)
   - Gradient purple
   - Icon + text
   - Hover: lift up

4. **Secondary Button:**
   - Transparent with purple border
   - Purple text
   - Hover: fill purple, white text

All buttons: Smooth transitions (0.3s)
```

---

### Card Component

```
Create a card component:

- White background
- Border-radius: 8px
- Padding: 20-32px (configurable)
- Shadow: 0 2px 8px rgba(0,0,0,0.1)
- Border: 1px solid #e0e0e0

- Hover effects:
  - Lift up 2-4px (translateY)
  - Enhanced shadow
  - Optional: purple border

- Variants:
  - Default: White background
  - Highlighted: Light purple background
  - Featured: Top colored border stripe

- Responsive: Full-width on mobile
```

---

### Form Input Component

```
Create form input fields:

- Label:
  - Font-weight: 600
  - Margin-bottom: 8px
  - Color: #333
  - Font-size: 14px

- Input:
  - Width: 100%
  - Padding: 10px 12px
  - Border: 1px solid #ddd
  - Border-radius: 4px
  - Background: white
  - Font-size: 14px

- Focus state:
  - Border-color: purple
  - Box-shadow: 0 0 0 2px rgba(101, 51, 110, 0.1)
  - No outline

- Error state:
  - Border-color: #ff6b6b
  - Background: #fff5f5

- Variants: text, textarea, select, date picker
```

---

### Tree View Component

```
Create a hierarchical tree view:

- Tree nodes:
  - Toggle arrow (right: collapsed, down: expanded)
  - Icon (changes by level: server, target, file-text)
  - Label text
  - Badge (count of children)
  - Hover: light purple background, border-left purple
  - Active: purple background, bold text

- Indentation: 32px per level
- Expand/collapse animation: slideDown (0.3s)
- Colors:
  - Default: #f8f9fa background
  - Hover: rgba(101, 51, 110, 0.1)
  - Active: rgba(101, 51, 110, 0.15)

- Detail panel (when node clicked):
  - Appears below tree
  - Shows full information for selected item
  - Close button
```

---

## 🚀 Usage Instructions

### For Figma Maker:

1. **Start with General Design Prompt** - Apply to all pages
2. **Pick a Page-Specific Prompt** - Copy to Figma Maker
3. **Generate Design** - Let Figma Maker create the layout
4. **Refine Components** - Use Component-Specific Prompts for details
5. **Export React Code** - Generate React components from Figma
6. **Integrate** - Combine with user stories for full implementation

### Tips:
- Use prompts as **starting points**, refine based on user story details
- Reference **01_ADMIN_CONTEXT_UI.md** and **02_INDEX_DASHBOARD.md** for complete specifications
- Check **SUMMARY_ALL_PAGES.md** for quick feature lists
- Combine multiple component prompts for complex pages

---

## ✅ Checklist After Using Prompts

- [ ] All colors match design system
- [ ] All icons included (Font Awesome + Lucide)
- [ ] Typography follows Maven Pro specification
- [ ] Layouts are responsive
- [ ] Hover states defined
- [ ] Loading states included
- [ ] Error states included
- [ ] All buttons have proper variants
- [ ] Forms have validation styling
- [ ] Modals have close functionality
- [ ] Component hierarchy matches user stories

---

**Ready to generate!** Pick a prompt, paste into Figma Maker, and start building! 🎨