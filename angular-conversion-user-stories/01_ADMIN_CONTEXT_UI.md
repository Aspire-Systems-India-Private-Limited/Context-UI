# Context Admin UI - User Stories for React Conversion

## Application Overview
A context management system for AI agents with capabilities for creating, searching, testing, and managing contexts with version control and feedback mechanisms.

---

## 1. Navigation & Layout

### User Story 1.1: Sidebar Navigation
**As a** context administrator  
**I want to** navigate between different sections using a sidebar  
**So that** I can access all features of the application

**Components:**
- Sidebar with logo/branding (Aspire Systems logo + "ContextAdmin" title)
- Navigation buttons:
  - "Create Context" (default active, plus icon)
  - "Search Contexts" (search icon)
  - "Create Reflection Context" (message-square icon)
  - "Search Reflection Context" (search-check icon)
- Active state highlighting for current section
- Icons from Lucide icon library

---

### User Story 1.2: Top Toolbar
**As a** user  
**I want to** see the current page title and my user information  
**So that** I know where I am and who I'm logged in as

**Components:**
- Page title display (dynamic based on active section)
- User information display
- Navbar component integration (from navbar.html)

---

## 2. Create Context Section

### User Story 2.1: AI-Powered Context Generation
**As a** context administrator  
**I want to** use AI to generate context content automatically  
**So that** I can quickly create contexts without manual writing

**Fields:**
- Intent for AI (text input, e.g., "customer_support, data_analysis")
- Task for AI (text input, e.g., "answer queries, process data")
- Context Type for AI (dropdown):
  - taskcontext (system)
  - domaincontext (user)
  - responsecontext (assistant)
  - parentcontext (function)
  - pastinteraction (function)
- Additional Info (optional text input)

**Actions:**
- "Generate Content with AI" button (gradient button with wand icon)
- Shows loading state during generation
- Auto-fills Content field on success
- Auto-fills Type and Intent fields based on selection
- Displays success/error messages
- API: POST /generate/context

---

### User Story 2.2: Manual Context Creation
**As a** context administrator  
**I want to** manually create a context with all required fields  
**So that** I can have full control over context configuration

**Required Fields:**
- Context Code (text input)
- Agent Code (text input)
- Type (text input)
- Intent (text input)
- Version ID (text input)
- Context Version (text input)
- Content (textarea, 6 rows)

**Optional Fields:**
- Parent Context Code (text input)

**Checkboxes:**
- Default (checkbox)
- Latest (checkbox)

**Dynamic Fields:**
- Filters (Entity key-value pairs)
  - Add/Remove filter rows dynamically
  - Each row has Key and Value fields
  - "Add Filters" button to add new rows
  - "Remove" button for each row

**Actions:**
- "Create Context" submit button
- Generates UUID for new context
- Sets CreatedBy and ModifiedBy to current user
- Displays success message with ID
- Clears form on success
- API: POST /contexts

---

## 3. Search Contexts Section

### User Story 3.1: Context Search
**As a** context administrator  
**I want to** search for contexts by agent code and version  
**So that** I can find and manage existing contexts

**Search Fields:**
- Agent Code (required, text input)
- Version ID (optional, text input)

**Actions:**
- "Search" button
- "Import" button (placeholder)
- "Export" button (placeholder)
- "Context Tree View" checkbox toggle

**API:** GET /agents/{agent_code}/contexts?version_id={version}

---

### User Story 3.2: Search Results Display
**As a** context administrator  
**I want to** view search results in a detailed card format  
**So that** I can review and edit context information

**Display Fields (per result card):**
- ID (readonly, gray background)
- Context Code (editable input)
- Parent Context Code (editable input, placeholder "None")
- Agent Code (editable input)
- Type (editable input)
- Intent (editable input)
- Version ID (editable input)
- Context Version (readonly by default, gray background)
- Content (textarea, 350px height, editable)
- Default (checkbox, editable)
- Latest (checkbox, editable)
- Filters/Entity display:
  - Show existing filters as editable key-value rows
  - "Add Filter" button to add new filter
  - "Remove" button for each filter row
  - Shows "No filters" if empty

**Actions per Card:**
- "Save" button - updates the context
- "Delete" button (red) - deletes the context
- "Test" button - opens test modal
- "History" button (small, with history icon) - opens version history modal
- "Update Context Version" checkbox:
  - When checked, enables Context Version field for editing
  - Shows warning message about creating new version
  - Validates version is different before saving

---

### User Story 3.3: Context Tree View
**As a** context administrator  
**I want to** view contexts in a hierarchical tree structure  
**So that** I can understand relationships between contexts

**Features:**
- Toggle checkbox to show/hide tree view
- Requires agent code and existing search results
- Shows alongside search results (not replacing them)
- Tree Structure:
  - Agent Code (root, with server icon)
  - Intent level (expandable, with target icon, shows count of types)
  - Type level (clickable, with file-text icon, shows count of contexts)
- Expand/collapse functionality for intent nodes
- Click on Type to show details in panel below

**Tree Detail Panel:**
- Shows all contexts for selected Intent + Type
- Displays in card format similar to search results
- Includes metadata: ID, Context Code, Parent, Version ID, Context Version
- Shows Default/Latest flags
- Shows Modified On timestamp
- Content display in code block
- Filters list
- "History" button for each context
- Latest version highlighted with badge
- Sorted by Context Version (descending)

---

### User Story 3.4: Update Context
**As a** context administrator  
**I want to** update existing context fields  
**So that** I can modify context information

**Editable Fields:**
- Context Code
- Parent Context Code
- Agent Code
- Type
- Intent
- Version ID
- Content
- Default checkbox
- Latest checkbox
- Filters (add/edit/remove)

**Update Context Version:**
- Checkbox to enable version update mode
- When enabled:
  - Context Version field becomes editable
  - Shows warning message
  - Validates new version is different from current
  - Confirms before creating new version
- When disabled:
  - Context Version remains readonly
  - Updates existing context in-place

**API:** PUT /contexts/{id}?doc_id={id}&update_context_version={boolean}

---

### User Story 3.5: Delete Context
**As a** context administrator  
**I want to** delete a context  
**So that** I can remove outdated or incorrect contexts

**Actions:**
- "Delete" button (red)
- Shows confirmation dialog
- Shows loader during deletion
- Refreshes search results on success
- API: DELETE /contexts/{id}?doc_id={id}

---

## 4. Version History Modal

### User Story 4.1: View Context Version History
**As a** context administrator  
**I want to** view the complete version history of a context  
**So that** I can track changes over time

**Trigger:** Click "History" button on any context card

**Modal Header:**
- Title: "Version History" with history icon
- Close button (X)
- Shows Context Code
- Shows total version count

**Version List:**
- Shows all unique Context Versions
- Each version item displays:
  - Context Version number
  - Modified On timestamp
  - Modified By user
  - Count of contexts with this version
  - "Latest" badge for newest version
- Sorted by version (descending, newest first)
- Clickable to view details

**API:** GET /context-code/{context_code}/contexts

---

### User Story 4.2: View Version Details
**As a** context administrator  
**I want to** view detailed information for a specific version  
**So that** I can see all contexts with that version

**Features:**
- Click on version in list to expand details
- Highlights selected version
- Shows close button to collapse details
- Displays all contexts with that version
- Each context shows:
  - ID, Context Code, Parent Context Code
  - Agent Code, Type, Intent
  - Version ID, Context Version
  - Default/Latest flags
  - Created On/By, Modified On/By
  - Content (in scrollable code block, max 200px height)
  - Filters list
- Smooth scroll to details panel
- Can close details to return to version list

---

## 5. Context Testing Modal

### User Story 5.1: Open Context Test Modal
**As a** context administrator  
**I want to** test a context with different configurations  
**So that** I can validate it works correctly

**Trigger:** Click "Test" button on any context card

**Auto-populated Fields:**
- Agent Code (readonly, from clicked context)
- Intent (dropdown, populated from agent's contexts)
- Version ID (hidden, from clicked context)
- Model (hidden, from backend data, default: gpt-4o-mini)
- Session ID (hidden, auto-generated: admin_YYYYMMDD_HHMMSS)

**User Configurable Fields:**
- User ID (default: "user_001")
- Request ID (default: "req_" + timestamp)
- User Message (optional textarea)
- Top Results (number input, default: 5)
- Default checkbox (checked by default)
- Latest checkbox (checked by default)

---

### User Story 5.2: Context List Configuration
**As a** context administrator  
**I want to** add context items for placeholder replacement  
**So that** I can test with dynamic values

**Features:**
- Section: "Context List"
- Description: "Add context items that will be used for placeholder replacement in parent contexts"
- Add multiple context items
- Each item has:
  - Context Type (e.g., "perception")
  - Context Name (e.g., "user_input")
  - Context Value (text or URL)
  - "Remove" button
- "Add Context Item" button to add new rows

---

### User Story 5.3: Image Input Configuration
**As a** context administrator  
**I want to** select or add images for testing  
**So that** I can test vision-enabled contexts

**Sample Images:**
- Grid of predefined sample images (4 images):
  - Shoes (Unsplash)
  - Shirt (Unsplash)
  - Jacket (Unsplash)
  - Bag (Unsplash)
- Click to select/deselect (checkbox overlay)
- Multiple selection allowed

**Custom Image URLs:**
- Add custom image URLs
- Each row has:
  - Image URL input field
  - "Remove" button
- "Add Custom Image URL" button

---

### User Story 5.4: Context Version Sets
**As a** context administrator  
**I want to** test multiple version combinations  
**So that** I can compare results across different versions

**Features:**
- Add multiple version sets
- Each set has:
  - Set number (auto-numbered)
  - Model dropdown (gpt-4o-mini, gpt-4o)
  - "Remove" button for the set
  - Multiple version items within set

**Version Item Fields:**
- Type dropdown (taskcontext, domaincontext, responsecontext, parentcontext)
- Version (text input, e.g., "v1", "v2")
- TypeName/Prompt Code (text input)
- "Remove" button for item

**Actions:**
- "Add Version Set" button
- "Add Context Version" button (per set)
- Auto-prefills first set from current context

---

### User Story 5.5: Execute Tests
**As a** context administrator  
**I want to** execute tests and view results  
**So that** I can validate context behavior

**Actions:**
- "Execute Tests" button (gradient, with play icon)
- "Cancel" button to close modal

**Test Execution:**
- Shows loader during execution
- API: POST /validate_multiple_output
- Payload includes:
  - All basic configuration
  - Context list items
  - Image inputs (sample + custom)
  - Context version sets
  - Entity from current context

**Results Display:**
- Shows results per version set
- Each set shows:
  - Set number
  - Model used (badge)
  - Multiple results per set
  - Each result contains:
    - Request context versions used
    - Refined output (formatted with structure)
- Output formatting:
  - Parses JSON if possible
  - Shows key-value pairs in styled boxes
  - Handles nested objects/arrays
  - Color-codes values (booleans, numbers, strings)
  - Shows "N/A" for null/undefined

---

## 6. Reflection Context (Feedback)

### User Story 6.1: Create Reflection Context
**As a** context administrator  
**I want to** create good or bad feedback contexts  
**So that** I can store examples for learning

**Feedback Type Selection:**
- Two large clickable cards:
  - Good Example (👍, green theme when selected)
  - Bad Example (👎, red theme when selected)
- Stores selection in hidden field

**Fields:**
- Agent Code (required)
- Intent (required)
- Reason (required, text input)
- Filters (dynamic key-value pairs, add/remove)
- Content (required, textarea, 8 rows)

**Actions:**
- "Create Reflection Context" button
- Generates UUID
- Sets CreatedBy/ModifiedBy
- Shows success with feedback type badge
- API: POST /good-feedback/contexts OR /bad-feedback/contexts

---

### User Story 6.2: Search Reflection Contexts
**As a** context administrator  
**I want to** search for feedback contexts by type  
**So that** I can review and manage feedback

**Feedback Type Selection:**
- Same two-card selection as create (Good/Bad)

**Search Fields:**
- Agent Code (required)

**Actions:**
- "Search Feedback" button
- API: GET /agent-code/{agent_code}/feedback-type/{type}/feedback-contexts

---

### User Story 6.3: Display Feedback Search Results
**As a** context administrator  
**I want to** view feedback search results  
**So that** I can review feedback details

**Display per Result:**
- Feedback badge (👍 Good or 👎 Bad) with color coding
- Metadata grid:
  - ID
  - Agent Code
  - Intent
  - Reason
  - Created By/On
  - Modified By/On
- Filters list
- Content section:
  - Textarea (editable, initially 100px height)
  - "Expand/Collapse" button to toggle height
  - Smooth height transition

**Actions per Result:**
- "Save" button - updates feedback
- "Delete" button (red) - deletes feedback
- API Update: PUT /contexts/feedback/{id}/feedback-type/{type}
- API Delete: DELETE /contexts/feedback/{id}/feedback-type/{type}

---

## 7. Global Features

### User Story 7.1: Global Loader
**As a** user  
**I want to** see a loading indicator during operations  
**So that** I know the system is processing

**Features:**
- Full-screen overlay with blur effect
- Circular spinner animation
- Customizable loading text (default: "Processing...")
- Blocks interaction during loading
- Used for:
  - AI generation
  - Creating contexts
  - Updating contexts
  - Deleting contexts
  - Building tree view
  - Executing tests

---

### User Story 7.2: Form Validation
**As a** user  
**I want to** see validation errors  
**So that** I can correct input mistakes

**Features:**
- Required field validation
- Alert messages for missing fields
- Context version uniqueness validation
- Confirmation dialogs for destructive actions
- Success/error messages after operations

---

### User Story 7.3: Icon System
**As a** user  
**I want to** see intuitive icons throughout the interface  
**So that** I can quickly understand functionality

**Icon Library:** Lucide Icons
- Navigation: plus, search, message-square, search-check
- Actions: wand-2, play, history, sparkles, layers, check-circle, info, alert-circle
- Structure: server, target, file-text, git-branch
- General: loader (spinning), flask-conical

---

## 8. Data Models

### Context Object
```json
{
  "id": "uuid",
  "PromptCode": "string",
  "ParentPromptCode": "string | null",
  "AgentCode": "string",
  "Type": "string",
  "Intent": "string",
  "VersionId": "string",
  "ContextVersion": "string",
  "Content": "string",
  "Default": "boolean",
  "Latest": "boolean",
  "CreatedBy": "string",
  "ModifiedBy": "string",
  "CreatedOn": "timestamp",
  "ModifiedOn": "timestamp",
  "Entity": [
    {
      "Key": "string",
      "Value": "string"
    }
  ]
}
```

### Feedback Context Object
```json
{
  "id": "uuid",
  "Reason": "string",
  "AgentCode": "string",
  "Intent": "string",
  "Entity": [
    {
      "Key": "string",
      "Value": "string"
    }
  ],
  "Content": "string | null",
  "CreatedBy": "string",
  "ModifiedBy": "string",
  "CreatedOn": "timestamp",
  "ModifiedOn": "timestamp"
}
```

### Test Request Object
```json
{
  "user_msg": "string",
  "user_id": "string",
  "intent": "string",
  "session_id": "string",
  "version_id": "string",
  "default": "boolean",
  "latest": "boolean",
  "entity": {
    "key": "value"
  },
  "image_input": [
    {
      "type": "image_url",
      "url": "string",
      "name": "string (optional)"
    }
  ],
  "agent_code": "string",
  "context_list": [
    {
      "context_type": "string",
      "context_name": "string",
      "context_value": "string"
    }
  ],
  "top": "number",
  "validation_clue": "string | null",
  "model": "string",
  "context_code": "string",
  "request_id": "string",
  "context_version_sets": [
    {
      "model": "string",
      "contexts": [
        {
          "type": "string",
          "version": "string",
          "typename": "string"
        }
      ]
    }
  ]
}
```

---

## 9. API Endpoints

### Context Management
- `POST /generate/context` - AI generate context content
- `POST /contexts` - Create new context
- `GET /agents/{agent_code}/contexts?version_id={version}` - Search contexts
- `GET /contexts/{id}?doc_id={id}` - Get single context
- `PUT /contexts/{id}?doc_id={id}&update_context_version={boolean}` - Update context
- `DELETE /contexts/{id}?doc_id={id}` - Delete context
- `GET /context-code/{context_code}/contexts` - Get version history

### Feedback Management
- `POST /good-feedback/contexts` - Create good feedback
- `POST /bad-feedback/contexts` - Create bad feedback
- `GET /agent-code/{agent_code}/feedback-type/{type}/feedback-contexts` - Search feedback
- `GET /contexts/feedback/{id}/feedback-type/{type}` - Get feedback
- `PUT /contexts/feedback/{id}/feedback-type/{type}` - Update feedback
- `DELETE /contexts/feedback/{id}/feedback-type/{type}` - Delete feedback

### Testing
- `POST /validate_multiple_output` - Execute context tests

---

## 10. Configuration

### API Configuration
- Primary API: `API_BASE` (from config.js)
- AI Search API: `AI_SEARCH_API_BASE` (from config.js)

### Default Values
- User ID: "admin" or "user_001"
- Session ID format: `admin_YYYYMMDD_HHMMSS`
- Request ID format: `req_{timestamp}`
- Model: "gpt-4o-mini"
- Top results: 5
- Default checkbox: checked
- Latest checkbox: checked

### Sample Images URLs
- Shoes: `https://images.unsplash.com/photo-1549298916-b41d501d3772?w=400`
- Shirt: `https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=400`
- Jacket: `https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400`
- Bag: `https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=400`

---

## 11. Component Hierarchy for React

```
App
├── Layout
│   ├── Sidebar
│   │   ├── Logo
│   │   └── NavigationButtons (4)
│   └── MainContent
│       ├── Toolbar
│       │   ├── PageTitle
│       │   └── UserInfo
│       └── PageContainer
│           ├── CreateContextPanel
│           │   ├── AIGenerationSection
│           │   └── ManualContextForm
│           ├── SearchContextPanel
│           │   ├── SearchForm
│           │   ├── TreeViewToggle
│           │   ├── SearchResults
│           │   │   └── ContextCard[] (with inline edit)
│           │   └── TreeView
│           │       ├── TreeNode[]
│           │       └── TreeDetailPanel
│           ├── CreateFeedbackPanel
│           │   ├── FeedbackTypeSelector
│           │   └── FeedbackForm
│           └── SearchFeedbackPanel
│               ├── FeedbackTypeSelector
│               ├── SearchForm
│               └── FeedbackResults
│                   └── FeedbackCard[] (with inline edit)
├── Modals
│   ├── TestModal
│   │   ├── BasicConfiguration
│   │   ├── ContextListSection
│   │   ├── ImageInputSection
│   │   │   ├── SampleImagesGrid
│   │   │   └── CustomImageURLs
│   │   ├── VersionSetsSection
│   │   │   └── VersionSet[]
│   │   │       └── VersionItem[]
│   │   ├── TestActions
│   │   └── TestResults
│   │       └── ResultSet[]
│   │           └── ResultItem[]
│   └── HistoryModal
│       ├── VersionList
│       │   └── VersionItem[]
│       └── VersionDetailsPanel
│           └── ContextCard[]
└── GlobalLoader
```

---

## 12. State Management Needs

### Global State
- Current user info
- Active navigation section
- API base URLs
- Loading states

### Create Context State
- AI generation form data
- Manual form data
- Entity filters array
- AI generation results

### Search Context State
- Search filters (agent code, version ID)
- Search results array
- Tree view enabled flag
- Tree data structure
- Expanded nodes set
- Selected tree node

### Feedback State
- Selected feedback type (create)
- Selected feedback type (search)
- Feedback form data
- Feedback search results
- Expanded content items

### Test Modal State
- Current test context
- All agent contexts
- Form data (basic config, context list, images, version sets)
- Test results
- Selected sample images

### History Modal State
- History data array
- Selected version index
- Version details visibility

---

## 13. Key Interactions & Behaviors

### Dynamic Form Behaviors
- Add/remove entity filter rows
- Add/remove context list items
- Add/remove image URLs
- Add/remove version sets and items
- Expand/collapse content sections
- Enable/disable context version editing

### Modal Behaviors
- Open on button click
- Close on X button, Cancel, outside click, or Escape key
- Smooth animations (fade in, slide in)
- Scroll to relevant sections
- Lucide icons re-initialization after DOM updates

### Tree View Behaviors
- Toggle visibility with checkbox
- Requires existing search results
- Expand/collapse intent nodes
- Click type to show details
- Highlight active node
- Smooth scroll to details

### Data Refresh
- Refresh search after update/delete
- Clear form after successful create
- Maintain expanded states in tree
- Re-fetch version history on modal open

---

## 14. Validation Rules

### Required Fields (Create Context)
- Context Code
- Agent Code
- Type
- Intent
- Version ID
- Context Version

### Required Fields (Test Modal)
- Agent Code
- Intent
- At least one version set with valid versions

### Required Fields (Feedback)
- Agent Code
- Intent
- Reason
- Content

### Business Rules
- Context Version must be unique when updating with new version
- Cannot update to same version number
- Confirmation required for delete operations
- Confirmation required for version updates

---

## 15. Error Handling

### User Feedback
- Alert dialogs for validation errors
- Success messages for operations
- Error messages in styled boxes
- Loading states during async operations

### API Error Handling
- Parse error.detail from response
- Display user-friendly messages
- Graceful degradation
- Retry capability where appropriate

---

## 16. Performance Considerations

### Optimization Needs
- Debounce search inputs
- Lazy load tree nodes
- Virtualize long lists (if needed)
- Cache search results for tree view
- Batch icon initialization calls
- Optimize re-renders with React.memo

### Data Handling
- Sort versions numerically when possible
- Filter and map efficiently
- Clean up event listeners
- Manage modal state lifecycle

---

## 17. Accessibility Requirements

### Keyboard Navigation
- Tab through form fields
- Enter to submit forms
- Escape to close modals
- Arrow keys in tree (optional enhancement)

### Screen Reader Support
- Proper label associations
- ARIA labels for icon buttons
- Status announcements for operations
- Semantic HTML structure

### Visual Indicators
- Focus states on inputs
- Hover states on clickable items
- Disabled states
- Loading states

---

## 18. Responsive Behavior Notes

### Layout Adaptations
- Grid layouts convert to single column on mobile
- Sidebar behavior (could be hamburger menu)
- Modal sizes adjust to viewport
- Tree view horizontal scroll if needed
- Button groups wrap on small screens

---

## End of User Stories Document

**Total Features:** 18 major feature areas with 50+ user stories
**Total Components:** 40+ React components needed
**Total API Endpoints:** 13 endpoints
**Modals:** 2 major modals (Test, History)
**Forms:** 4 main forms (Create Context, Search, Create Feedback, Search Feedback)

This document provides complete functional specifications for converting the HTML template to React using Figma Maker or any other tool.