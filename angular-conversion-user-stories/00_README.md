# Angular Conversion User Stories - Agent Operations Platform

## Overview
This folder contains comprehensive user stories for converting all HTML templates in the Agent Operations Platform to Angular components. Each file corresponds to a specific page or feature module in the application.

## Document Structure

### Core Pages
1. **01_ADMIN_CONTEXT_UI.md** - Context Admin page with AI generation, CRUD operations, version history, and testing
2. **02_INDEX_DASHBOARD.md** - Main landing/dashboard page
3. **03_AGENT_MANAGEMENT.md** - Agent configuration and management
4. **04_AGENT_SOLUTION.md** - Agent solution configuration
5. **05_SESSION_USER_INTERACTION.md** - User interaction/session management
6. **06_MEMORY_MANAGEMENT.md** - Memory storage and retrieval
7. **07_AUDIT_DIAGNOSIS.md** - Audit logs and diagnosis
8. **08_COST_METRICS.md** - Cost tracking and metrics
9. **09_SENTIMENT_ANALYZER.md** - Feedback sentiment analysis
10. **10_RBAC_MANAGEMENT.md** - Role-based access control
11. **11_VIEW_AGENT_DETAILS.md** - Agent details view
12. **12_VIEW_CONFIGURATIONS.md** - Configuration viewer
13. **13_AGGREGATED_VIEW.md** - Aggregated data view

### Shared Components
14. **14_NAVBAR_COMPONENT.md** - Top navigation bar
15. **15_SIDEBAR_COMPONENT.md** - Sidebar navigation (if applicable)
16. **16_SHARED_COMPONENTS.md** - Common/reusable components

### Utility Pages
17. **17_TOKEN_MANAGEMENT.md** - Token management utility
18. **18_CALLBACK_PAGE.md** - OAuth/OKTA callback handling

## Common Themes Across All Pages

### Design System & Styling

**📁 Use Existing Style Files:**
- **`/styles/globals.css`** - Global design tokens, theme variables, dark mode support
- **`/styles/ats-utilities.css`** - Utility classes for layout, spacing, typography, gradients
- **`/guidelines/Guidelines.md`** - Design system guidelines and component specifications

**Color Palette:**
- Primary Purple: `#65336e`
- Dark Purple: `#542d6b`
- Background Purple: `#692e8b`
- Light Blue: `#80c6ff`
- Text Light: `#eee`

**Typography:** Maven Pro, Segoe UI, Arial (fallback), 14px base font size
**Icons:** Font Awesome 6.4.0 + Lucide Icons
**Branding:** Aspire Systems logo

### Common Layout Components
- Fixed toolbar (70px height)
- Sidebar navigation (200px width) where applicable
- Responsive grid layouts
- Card-based content organization
- Modal dialogs for forms and details

### Common Features
- Loading states with spinners
- Error handling with alerts/messages
- Form validation
- CRUD operations (Create, Read, Update, Delete)
- Search and filtering
- Pagination or "Load More" functionality
- Date range filtering
- Export/Import capabilities
- User authentication info display

### Common API Pattern
```javascript
// API Base from config.js
const API_BASE = window.API_BASE || '';
const AI_SEARCH_API_BASE = window.AI_SEARCH_API_BASE || '';

// Standard fetch pattern
const response = await fetch(`${API_BASE}/endpoint`, {
  method: 'POST/GET/PUT/DELETE',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data)
});
```

### State Management Needs
- User authentication state
- Current page/route state
- Form data state
- API loading states
- Error states
- Modal visibility states
- Filter/search criteria states
- Pagination states

## Angular Component Architecture Recommendations

### Folder Structure
```
src/
├── app/
│   ├── core/
│   │   ├── layout/
│   │   │   ├── navbar/
│   │   │   │   ├── navbar.component.ts
│   │   │   │   ├── navbar.component.html
│   │   │   │   └── navbar.component.scss
│   │   │   ├── sidebar/
│   │   │   ├── toolbar/
│   │   │   └── page-container/
│   │   ├── guards/
│   │   ├── interceptors/
│   │   └── services/
│   │       ├── api.service.ts
│   │       ├── auth.service.ts
│   │       └── context.service.ts
│   ├── shared/
│   │   ├── components/
│   │   │   ├── button/
│   │   │   ├── card/
│   │   │   ├── modal/
│   │   │   ├── loader/
│   │   │   ├── form-input/
│   │   │   └── icon/
│   │   ├── pipes/
│   │   ├── directives/
│   │   └── models/
│   ├── features/
│   │   ├── admin/
│   │   │   ├── components/
│   │   │   │   ├── context-admin/
│   │   │   │   ├── ai-generation/
│   │   │   │   ├── context-form/
│   │   │   │   ├── search-results/
│   │   │   │   ├── tree-view/
│   │   │   │   ├── test-modal/
│   │   │   │   └── history-modal/
│   │   │   └── admin.module.ts
│   │   ├── agent/
│   │   ├── session/
│   │   ├── memory/
│   │   └── ...
│   ├── pages/
│   │   ├── dashboard/
│   │   ├── context-admin/
│   │   ├── agent-management/
│   │   └── ...
│   └── app-routing.module.ts
├── assets/
│   └── styles/
│       ├── globals.css (imported from /styles/)
│       └── ats-utilities.css (imported from /styles/)
└── environments/
```

### Recommended Angular Libraries & Tools
- **Angular Router** - Client-side routing (built-in)
- **RxJS** - Reactive programming (built-in)
- **HttpClient** - HTTP requests (built-in)
- **Angular Forms** - Template-driven or Reactive forms (built-in)
- **@ngrx/store** - State management (optional)
- **Angular Material** or **PrimeNG** - UI component library (optional)
- **@angular/common** - Date pipes, currency pipes (built-in)
- **ngx-toastr** - Toast notifications
- **class-validator** - Validation

**⚠️ Important:** Import existing stylesheets in your Angular app:
```scss
/* In src/styles.scss */
@import 'styles/globals.css';
@import 'styles/ats-utilities.css';
```

Or in `angular.json`:
```json
{
  "styles": [
    "src/styles.scss",
    "src/styles/globals.css",
    "src/styles/ats-utilities.css"
  ]
}
```

## How to Use These Documents

### For Figma Design
1. Read each user story document
2. Create wireframes/mockups in Figma for each page
3. Use the component hierarchy as guide for design modules
4. Follow the color palette and typography specs
5. Design mobile and desktop versions
6. Use Figma Maker to generate initial Angular code

### For Angular Development
1. Create Angular project: `ng new agent-ops-app`
2. Set up routing module with all page routes
3. Create shared module with common components (Navbar, Sidebar, Button, Card, Modal)
4. Implement core services (API, Auth, Context, Agent, etc.)
5. Create feature modules for each major section
6. Build page components one at a time
7. Implement reactive forms with validation
8. Add RxJS observables for state management
9. Implement error handling with interceptors
10. Add loading states and spinners
11. Test responsiveness
12. Optimize with lazy loading and OnPush change detection

### For Testing
- Reference user stories as acceptance criteria
- Ensure all fields, buttons, and actions work as documented
- Validate API integrations
- Test responsive behavior
- Test accessibility features

## Next Steps
1. Review all user story documents
2. Prioritize pages based on business value
3. Create design system in Figma
4. Set up React project structure
5. Implement core components
6. Build pages iteratively
7. Integrate with backend APIs
8. Test and refine

## Notes
- All API endpoints are documented in each user story file
- Data models/schemas are included where applicable
- Validation rules are specified for forms
- Each component's props and state needs are outlined
- Accessibility requirements are noted

---

**Document Version:** 1.0  
**Last Updated:** December 9, 2025  
**Total Pages:** 18 user story documents  
**Total Features:** 150+ user stories across all pages
