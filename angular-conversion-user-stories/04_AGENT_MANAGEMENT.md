# Agent Management - React Conversion User Stories

## Overview
The Agent Management page allows users to view, create, edit, and delete agents within an agent solution. Each agent can have multiple intents, and each intent can have multiple entities with types, examples, and descriptions.

---

## Component Architecture

```
<AgentManagementPage>
├── <AppLayout>
│   ├── <Sidebar>
│   │   ├── <Logo />
│   │   ├── <AddAgentButton />
│   │   └── <BackButton />
│   ├── <Toolbar>
│   │   ├── <PageTitle />
│   │   └── <Navbar />
│   └── <PageContainer>
│       └── <AgentsTable>
│           ├── <TableHeader />
│           └── <TableBody>
│               └── <AgentRow[]>
│                   ├── <AgentData />
│                   └── <ActionButtons>
│                       ├── <EditButton />
│                       └── <DeleteButton />
└── <AgentModal>
    ├── <ModalHeader />
    ├── <AgentForm>
    │   ├── <BasicInfoSection>
    │   │   ├── <Input: ID />
    │   │   ├── <Input: Code />
    │   │   ├── <Input: Version />
    │   │   ├── <Input: Name />
    │   │   ├── <Textarea: Description />
    │   │   ├── <Select: Status />
    │   │   ├── <Input: Provider />
    │   │   ├── <Input: URL />
    │   │   ├── <Input: Type />
    │   │   ├── <Input: Environment />
    │   │   ├── <Input: Support Email />
    │   │   ├── <Input: Support Phone />
    │   │   └── <Input: Category />
    │   └── <IntentsSection>
    │       ├── <IntentsList>
    │       │   └── <IntentItem[]>
    │       │       ├── <Input: Intent Name />
    │       │       ├── <RemoveIntentButton />
    │       │       ├── <EntitiesList>
    │       │       │   └── <EntityItem[]>
    │       │       │       ├── <Input: Type />
    │       │       │       ├── <Input: Example />
    │       │       │       ├── <Textarea: Description />
    │       │       │       └── <RemoveEntityButton />
    │       │       └── <AddEntityButton />
    │       └── <AddIntentButton />
    └── <SaveButton />
```

---

## Data Models

```typescript
interface Agent {
  id: string;
  name: string;
  code: string;
  version: string;
  agent_solution_id: string;
  description: string;
  status: 'active' | 'inactive';
  provider: string;
  url: string;
  type: string;
  environment: string;
  support: {
    email: string;
    phone: string;
  };
  category: string;
  intents: Intent[];
}

interface Intent {
  name: string;
  entities: Entity[];
}

interface Entity {
  type: string;
  example: string;
  description: string;
}

interface AgentSolution {
  id: string;
  name: string;
}
```

---

## User Stories

### Story 1: View Agents Table
**As a** administrator  
**I want to** see all agents in a table format  
**So that** I can quickly browse and manage agents

#### Acceptance Criteria:
- [ ] Display table with columns: Id, Name, Code, Status, Provider, URL, Category, Actions
- [ ] Show loading indicator while fetching data
- [ ] Show "No agents found" message when list is empty
- [ ] Show error message if data fetch fails
- [ ] Table rows are clickable to navigate to agent details
- [ ] URL column has clickable links that open in new tab
- [ ] Table is responsive and scrollable
- [ ] Table has proper styling with purple headers

#### API Integration:
```typescript
GET /agent-solutions/{agentSolutionId}/agents
Response: Agent[]
```

#### Component:
```tsx
const AgentsTable: React.FC<{ agentSolutionId: string }> = ({ agentSolutionId }) => {
  const [agents, setAgents] = useState<Agent[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  
  useEffect(() => {
    loadAgents();
  }, [agentSolutionId]);
  
  const loadAgents = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${apiBase}/agent-solutions/${agentSolutionId}/agents`);
      if (!response.ok) throw new Error('Failed to load agents');
      const data = await response.json();
      setAgents(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };
  
  if (loading) return <LoadingState />;
  if (error) return <ErrorState message={error} />;
  if (agents.length === 0) return <EmptyState />;
  
  return <Table data={agents} columns={columns} onRowClick={handleRowClick} />;
};
```

---

### Story 2: Navigate to Agent Details
**As a** user  
**I want to** click on an agent row to view its details  
**So that** I can see complete information about the agent

#### Acceptance Criteria:
- [ ] Clicking anywhere on table row navigates to agent details page
- [ ] Row shows hover effect to indicate clickability
- [ ] Cursor changes to pointer on hover
- [ ] Clicks on action buttons (Edit/Delete) do NOT trigger row navigation
- [ ] Clicks on URL link do NOT trigger row navigation
- [ ] Navigation URL format: `/agent-sol/{agentSolutionId}/agent/{agentId}`

#### Implementation:
```tsx
const AgentRow: React.FC<{ agent: Agent; onClick: () => void }> = ({ agent, onClick }) => {
  const handleClick = (e: React.MouseEvent) => {
    // Ignore clicks on action buttons or links
    if ((e.target as HTMLElement).closest('.no-row-click')) {
      return;
    }
    onClick();
  };
  
  return (
    <tr onClick={handleClick} style={{ cursor: 'pointer' }}>
      <td>{agent.id}</td>
      <td>{agent.name}</td>
      <td>{agent.code}</td>
      <td>{agent.status}</td>
      <td>{agent.provider}</td>
      <td className="no-row-click">
        <a href={agent.url} target="_blank" rel="noopener noreferrer">Click Here</a>
      </td>
      <td>{agent.category}</td>
      <td className="action-cell no-row-click">
        <ActionButtons agent={agent} />
      </td>
    </tr>
  );
};
```

---

### Story 3: Add New Agent
**As a** administrator  
**I want to** click "Add Agent" button in sidebar  
**So that** I can create a new agent

#### Acceptance Criteria:
- [ ] "Add Agent" button visible in sidebar with plus icon
- [ ] Button is highlighted as active
- [ ] Clicking button opens modal dialog
- [ ] Modal title shows "Add Agent"
- [ ] All form fields are empty
- [ ] Agent ID field is editable
- [ ] Save button shows "Save" text
- [ ] Modal can be closed with X button or backdrop click
- [ ] Form is cleared when modal closes

#### Component:
```tsx
const AddAgentButton: React.FC<{ onClick: () => void }> = ({ onClick }) => {
  return (
    <button className="is-active" onClick={onClick}>
      <i className="fas fa-plus icon"></i> Add Agent
    </button>
  );
};

const openAddModal = () => {
  setIsEditMode(false);
  setCurrentAgent(null);
  setModalOpen(true);
};
```

---

### Story 4: Agent Basic Information Form
**As a** administrator  
**I want to** fill in agent basic information  
**So that** I can create or update an agent

#### Acceptance Criteria:
- [ ] Form has 13 input fields for basic information
- [ ] ID field: text input, required
- [ ] Code field: text input, required
- [ ] Version field: text input
- [ ] Name field: text input, required
- [ ] Description field: textarea, multi-line
- [ ] Status field: dropdown with Active/Inactive options
- [ ] Provider field: text input
- [ ] URL field: text input, validates URL format
- [ ] Type field: text input
- [ ] Environment field: text input
- [ ] Support Email field: email input, validates email format
- [ ] Support Phone field: text input
- [ ] Category field: text input
- [ ] All fields show validation errors
- [ ] Focus styles on active field

#### Form Fields:
```tsx
interface AgentFormData {
  id: string;               // Required
  code: string;             // Required
  version: string;
  name: string;             // Required
  description: string;
  status: 'active' | 'inactive';
  provider: string;
  url: string;              // URL validation
  type: string;
  environment: string;
  supportEmail: string;     // Email validation
  supportPhone: string;
  category: string;
}
```

#### Validation Rules:
```typescript
const validationSchema = z.object({
  id: z.string().min(1, 'ID is required'),
  code: z.string().min(1, 'Code is required'),
  name: z.string().min(1, 'Name is required'),
  url: z.string().url('Must be a valid URL').optional(),
  supportEmail: z.string().email('Must be a valid email').optional(),
  // ... other fields
});
```

---

### Story 5: Dynamic Intents Management
**As a** administrator  
**I want to** add, edit, and remove intents for an agent  
**So that** I can define what the agent can handle

#### Acceptance Criteria:
- [ ] "Add Intent" button visible below intents list
- [ ] Clicking "Add Intent" creates new intent section
- [ ] Each intent has: Name input field and Remove button
- [ ] Intent name field is required
- [ ] Remove intent button deletes the intent section
- [ ] Confirm dialog before removing intent
- [ ] Intents can be reordered (drag and drop - enhancement)
- [ ] At least one intent can be added
- [ ] Intent sections have distinct visual separation
- [ ] Intent removal immediately updates UI

#### Component:
```tsx
const IntentsSection: React.FC<{
  intents: Intent[];
  onChange: (intents: Intent[]) => void;
}> = ({ intents, onChange }) => {
  const addIntent = () => {
    onChange([...intents, { name: '', entities: [] }]);
  };
  
  const removeIntent = (index: number) => {
    if (confirm('Remove this intent?')) {
      onChange(intents.filter((_, i) => i !== index));
    }
  };
  
  const updateIntent = (index: number, updates: Partial<Intent>) => {
    const updated = intents.map((intent, i) =>
      i === index ? { ...intent, ...updates } : intent
    );
    onChange(updated);
  };
  
  return (
    <div className="intents-section">
      <label>Intents</label>
      {intents.map((intent, idx) => (
        <IntentItem
          key={idx}
          intent={intent}
          onUpdate={(updates) => updateIntent(idx, updates)}
          onRemove={() => removeIntent(idx)}
        />
      ))}
      <button className="btn-icon intent-btn" onClick={addIntent}>
        <i className="fa fa-plus"></i> Intent
      </button>
    </div>
  );
};
```

---

### Story 6: Dynamic Entities Management Within Intent
**As a** administrator  
**I want to** add, edit, and remove entities within each intent  
**So that** I can define the parameters the intent accepts

#### Acceptance Criteria:
- [ ] Each intent has "Add Entity" button
- [ ] Clicking "Add Entity" creates new entity section within that intent
- [ ] Each entity has 3 fields: Type, Example, Description
- [ ] Type field: text input, required
- [ ] Example field: text input, required
- [ ] Description field: large textarea (min 180px height)
- [ ] Remove entity button on each entity
- [ ] Remove button aligned to right with proper styling
- [ ] Entity removal immediately updates UI
- [ ] Entities visually nested under their intent
- [ ] Multiple entities can be added per intent
- [ ] Entity fields are full width

#### Data Structure:
```typescript
interface Entity {
  type: string;        // e.g., "date", "location", "person"
  example: string;     // e.g., "tomorrow", "New York", "John Doe"
  description: string; // Detailed description of entity
}
```

#### Component:
```tsx
const EntityItem: React.FC<{
  entity: Entity;
  onUpdate: (entity: Entity) => void;
  onRemove: () => void;
}> = ({ entity, onUpdate, onRemove }) => {
  return (
    <div className="entity-item">
      <input
        type="text"
        placeholder="Type"
        className="entity-type"
        value={entity.type}
        onChange={(e) => onUpdate({ ...entity, type: e.target.value })}
      />
      <input
        type="text"
        placeholder="Example"
        className="entity-example"
        value={entity.example}
        onChange={(e) => onUpdate({ ...entity, example: e.target.value })}
      />
      <textarea
        placeholder="Description"
        className="entity-description"
        value={entity.description}
        onChange={(e) => onUpdate({ ...entity, description: e.target.value })}
        style={{ minHeight: '180px', width: '100%' }}
      />
      <button
        type="button"
        className="btn-icon"
        onClick={onRemove}
      >
        <i className="fa fa-minus-circle"></i> Entity
      </button>
    </div>
  );
};
```

---

### Story 7: Save New Agent
**As a** administrator  
**I want to** save a new agent with all its data  
**So that** the agent is created in the system

#### Acceptance Criteria:
- [ ] "Save" button at bottom of modal
- [ ] Button disabled while saving
- [ ] Button shows loading indicator during save
- [ ] Validate all required fields before submission
- [ ] Show validation errors if any field is invalid
- [ ] Submit data via POST API call
- [ ] Show success message on successful save
- [ ] Close modal after successful save
- [ ] Refresh agents table after save
- [ ] Show error message if save fails
- [ ] Keep modal open if save fails (allow retry)

#### API Integration:
```typescript
POST /agents
Body: Agent
Response: Agent

const saveAgent = async (agent: Agent) => {
  try {
    const response = await fetch(`${apiBase}/agents`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(agent)
    });
    
    if (!response.ok) throw new Error('Failed to save agent');
    
    const data = await response.json();
    toast.success('Agent created successfully');
    closeModal();
    loadAgents();
  } catch (err) {
    toast.error('Error saving agent');
    console.error(err);
  }
};
```

---

### Story 8: Edit Existing Agent
**As a** administrator  
**I want to** edit an existing agent  
**So that** I can update agent information

#### Acceptance Criteria:
- [ ] Click edit icon button on agent row
- [ ] Modal opens with title "Edit Agent"
- [ ] All form fields pre-filled with current agent data
- [ ] Agent ID field is read-only (cannot be changed)
- [ ] All intents and entities loaded and editable
- [ ] Fetch latest intent/entity data from API
- [ ] Save button updates existing agent
- [ ] PUT request sent to API with updated data
- [ ] Table refreshes after successful update
- [ ] Show success/error messages

#### API Integration:
```typescript
GET /agents/{id}        // Fetch full agent details including intents
Response: Agent

PUT /agents/{id}        // Update agent
Body: Agent
Response: Agent

const loadAgentForEdit = async (agentId: string) => {
  const response = await fetch(`${apiBase}/agents/${agentId}`);
  const agent = await response.json();
  setFormData(agent);
  setModalOpen(true);
};

const updateAgent = async (id: string, agent: Agent) => {
  const response = await fetch(`${apiBase}/agents/${id}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(agent)
  });
  
  if (!response.ok) throw new Error('Failed to update agent');
  toast.success('Agent updated successfully');
};
```

---

### Story 9: Delete Agent
**As a** administrator  
**I want to** delete an agent  
**So that** I can remove agents that are no longer needed

#### Acceptance Criteria:
- [ ] Delete button (trash icon) visible on each agent row
- [ ] Clicking delete shows confirmation dialog
- [ ] Confirmation dialog shows agent name/ID
- [ ] Confirm button sends DELETE request to API
- [ ] Show loading indicator during deletion
- [ ] Remove agent from table on successful deletion
- [ ] Show success message after deletion
- [ ] Show error message if deletion fails
- [ ] Cancel button closes dialog without deleting

#### API Integration:
```typescript
DELETE /agents/{id}
Response: { message: string }

const deleteAgent = async (agentId: string) => {
  const confirmed = confirm(`Are you sure you want to delete agent "${agentId}"?`);
  if (!confirmed) return;
  
  try {
    const response = await fetch(`${apiBase}/agents/${agentId}`, {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json' }
    });
    
    if (!response.ok) throw new Error('Failed to delete agent');
    
    toast.success('Agent deleted successfully');
    loadAgents();
  } catch (err) {
    toast.error('Error deleting agent');
    console.error(err);
  }
};
```

---

### Story 10: Back Navigation
**As a** user  
**I want to** navigate back to Agent Solution page  
**So that** I can return to the parent view

#### Acceptance Criteria:
- [ ] "Back to Agent Solution" button in sidebar
- [ ] Button navigates to previous page in browser history
- [ ] Button uses browser's back() function
- [ ] Button has consistent styling with sidebar
- [ ] Button is always visible below "Add Agent" button

#### Implementation:
```tsx
const BackButton: React.FC = () => {
  return (
    <button className="btn" onClick={() => history.back()}>
      Back to Agent Solution
    </button>
  );
};
```

---

### Story 11: Form Validation
**As a** user  
**I want to** see validation errors on form fields  
**So that** I know what needs to be corrected

#### Acceptance Criteria:
- [ ] Required fields show error if left empty
- [ ] Email field validates email format
- [ ] URL field validates URL format
- [ ] Errors appear below the field or as red border
- [ ] Errors clear when field is corrected
- [ ] Submit button disabled if form has errors
- [ ] Show all errors at once (not one at a time)
- [ ] Error messages are clear and actionable

#### Validation:
```typescript
const validate = (agent: Agent): ValidationErrors => {
  const errors: ValidationErrors = {};
  
  if (!agent.id) errors.id = 'ID is required';
  if (!agent.code) errors.code = 'Code is required';
  if (!agent.name) errors.name = 'Name is required';
  
  if (agent.url && !isValidUrl(agent.url)) {
    errors.url = 'Must be a valid URL';
  }
  
  if (agent.support.email && !isValidEmail(agent.support.email)) {
    errors.supportEmail = 'Must be a valid email';
  }
  
  agent.intents.forEach((intent, idx) => {
    if (!intent.name) {
      errors[`intent_${idx}_name`] = 'Intent name is required';
    }
    
    intent.entities.forEach((entity, entityIdx) => {
      if (!entity.type) {
        errors[`intent_${idx}_entity_${entityIdx}_type`] = 'Entity type is required';
      }
    });
  });
  
  return errors;
};
```

---

### Story 12: Modal Styling and Behavior
**As a** user  
**I want to** have a well-designed modal experience  
**So that** I can efficiently create/edit agents

#### Acceptance Criteria:
- [ ] Modal appears centered on screen
- [ ] Modal has semi-transparent backdrop (50% opacity)
- [ ] Clicking backdrop closes modal
- [ ] Escape key closes modal
- [ ] Modal header has title and X close button
- [ ] Modal content is scrollable if too tall (max 80vh)
- [ ] Modal width is 90% with max-width 700px
- [ ] Modal has rounded corners and white background
- [ ] Modal has proper padding (30px)
- [ ] Smooth fade-in animation when opening

#### CSS:
```css
.modal {
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 30px;
  border-radius: 8px;
  width: 90%;
  max-width: 700px;
  max-height: 80vh;
  overflow-y: auto;
}
```

---

### Story 13: Intent/Entity Layout and Styling
**As a** user  
**I want to** see a clear visual hierarchy for intents and entities  
**So that** I can easily understand the structure

#### Acceptance Criteria:
- [ ] Intent sections have light gray background (#f9f9f9)
- [ ] Intent sections have border and rounded corners
- [ ] Intent name input and remove button on same row
- [ ] Intent name takes most of row width
- [ ] Remove intent button aligned to right
- [ ] Entities section indented or visually nested
- [ ] Entity items have lighter background
- [ ] Entity description textarea is large (180px min height)
- [ ] Add entity button aligned to right within intent
- [ ] Proper spacing between all elements

#### CSS Structure:
```css
.intent-item {
  display: grid;
  grid-template-columns: 1fr auto;
  gap: 10px;
  border: 1px solid #ddd;
  padding: 12px;
  border-radius: 8px;
  background: #f9f9f9;
  margin-bottom: 12px;
}

.intent-name {
  flex-grow: 1;
  min-width: 300px;
}

.entitiesContainer {
  grid-column: 1 / span 2;
  margin-top: 8px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.entity-item {
  background: #fff;
  padding: 12px;
  border: 1px solid #eee;
  border-radius: 4px;
}

.entity-description {
  min-height: 180px !important;
  width: 100% !important;
}
```

---

### Story 14: Button Styling Consistency
**As a** user  
**I want to** see consistent button styling throughout the form  
**So that** the interface feels cohesive

#### Acceptance Criteria:
- [ ] All primary buttons use purple background (#65336e)
- [ ] Buttons have white text color (#fff)
- [ ] Buttons are 130px wide and 40px tall (standard size)
- [ ] Buttons have rounded corners (6px radius)
- [ ] Buttons have subtle shadow
- [ ] Hover effect darkens background (#542d6b)
- [ ] Delete/remove buttons are red (#dc3545)
- [ ] Delete buttons hover to darker red (#dc2626)
- [ ] Icon buttons have icons with proper spacing
- [ ] Add buttons have plus icon, remove have minus icon

#### Button Variants:
```tsx
// Primary button
<button className="btn-icon">
  <i className="fa fa-plus"></i> Add
</button>

// Delete button
<button className="btn-icon delete-btn">
  <i className="fa fa-minus-circle"></i> Remove
</button>

// Save button
<button className="btn-icon" onClick={saveAgent}>
  Save
</button>
```

---

### Story 15: Loading States
**As a** user  
**I want to** see loading indicators during data operations  
**So that** I know the system is processing

#### Acceptance Criteria:
- [ ] Show "Loading..." in table while fetching agents
- [ ] Loading text has blinking animation
- [ ] Loading spans all table columns
- [ ] Save button shows spinner icon while saving
- [ ] Save button text changes to "Saving..." while saving
- [ ] Save button disabled while saving
- [ ] Delete button shows confirmation spinner
- [ ] Modal shows loading overlay if fetching intent data

#### Implementation:
```tsx
const LoadingState: React.FC = () => (
  <tr>
    <td colSpan={8} style={{ textAlign: 'center' }}>
      <div className="loading">Loading...</div>
    </td>
  </tr>
);

const SaveButton: React.FC<{ loading: boolean; onClick: () => void }> = ({ loading, onClick }) => (
  <button
    className="btn-icon"
    onClick={onClick}
    disabled={loading}
  >
    {loading ? (
      <>
        <i className="fa fa-spinner fa-spin"></i> Saving...
      </>
    ) : (
      'Save'
    )}
  </button>
);
```

---

### Story 16: Empty States
**As a** user  
**I want to** see helpful messages when there's no data  
**So that** I understand what to do next

#### Acceptance Criteria:
- [ ] Show "No agents found" when agents list is empty
- [ ] Empty message spans all table columns
- [ ] Empty message has helpful styling
- [ ] Suggest action: "Click Add Agent to create your first agent"
- [ ] Empty state has icon (optional)

#### Component:
```tsx
const EmptyState: React.FC = () => (
  <tr>
    <td colSpan={8} style={{ textAlign: 'center', padding: '40px' }}>
      <i className="fas fa-robot" style={{ fontSize: '48px', color: '#ccc' }}></i>
      <p style={{ marginTop: '16px', color: '#666' }}>No agents found</p>
      <p style={{ fontSize: '14px', color: '#999' }}>
        Click "Add Agent" to create your first agent
      </p>
    </td>
  </tr>
);
```

---

### Story 17: Error Handling
**As a** user  
**I want to** see clear error messages when something goes wrong  
**So that** I can understand and resolve the issue

#### Acceptance Criteria:
- [ ] Show error message in table if fetch fails
- [ ] Error message is red and prominent
- [ ] Show toast notification for save/delete errors
- [ ] Toast appears at top-right of screen
- [ ] Toast auto-dismisses after 5 seconds
- [ ] Toast has close button
- [ ] Console logs detailed error for debugging
- [ ] Network errors show specific message

#### Error Component:
```tsx
const ErrorState: React.FC<{ message: string; onRetry?: () => void }> = ({ message, onRetry }) => (
  <tr>
    <td colSpan={8} style={{ textAlign: 'center', padding: '40px' }}>
      <i className="fas fa-exclamation-circle" style={{ fontSize: '48px', color: '#dc3545' }}></i>
      <p style={{ marginTop: '16px', color: '#dc3545', fontWeight: 600 }}>
        {message}
      </p>
      {onRetry && (
        <button onClick={onRetry} style={{ marginTop: '12px' }}>
          Try Again
        </button>
      )}
    </td>
  </tr>
);
```

---

### Story 18: Responsive Design
**As a** user on different devices  
**I want to** use the agent management page on any screen size  
**So that** I can work from desktop, tablet, or mobile

#### Acceptance Criteria:
- [ ] Table is horizontally scrollable on small screens
- [ ] Modal is full-width on mobile with small padding
- [ ] Form fields stack vertically on mobile
- [ ] Buttons stack vertically on mobile
- [ ] Sidebar collapses to hamburger menu on mobile
- [ ] Touch-friendly button sizes (min 44x44px)
- [ ] Proper spacing on all screen sizes

#### Responsive Breakpoints:
```css
/* Mobile */
@media (max-width: 768px) {
  .modal-content {
    width: 95%;
    padding: 20px;
  }
  
  .intent-item {
    grid-template-columns: 1fr;
  }
  
  .intent-name {
    min-width: 100%;
  }
  
  .button-row {
    flex-direction: column;
  }
  
  table {
    display: block;
    overflow-x: auto;
  }
}
```

---

## API Endpoints Summary

```typescript
// Agents
GET    /agent-solutions/{agentSolutionId}/agents  // List all agents
GET    /agents/{id}                                // Get agent details with intents
POST   /agents                                     // Create new agent
PUT    /agents/{id}                                // Update agent
DELETE /agents/{id}                                // Delete agent
```

---

## State Management

```typescript
interface AgentManagementState {
  // Data
  agents: Agent[];
  currentAgent: Agent | null;
  
  // UI State
  isModalOpen: boolean;
  isEditMode: boolean;
  loading: boolean;
  saving: boolean;
  
  // Errors
  error: string | null;
  validationErrors: ValidationErrors;
  
  // Actions
  loadAgents: () => Promise<void>;
  createAgent: (agent: Agent) => Promise<void>;
  updateAgent: (id: string, agent: Agent) => Promise<void>;
  deleteAgent: (id: string) => Promise<void>;
  openAddModal: () => void;
  openEditModal: (agent: Agent) => void;
  closeModal: () => void;
}
```

---

## Component File Structure

```
src/
├── pages/
│   └── AgentManagement/
│       ├── index.tsx
│       ├── AgentManagementPage.tsx
│       ├── components/
│       │   ├── AgentsTable.tsx
│       │   ├── AgentRow.tsx
│       │   ├── AgentModal.tsx
│       │   ├── AgentForm.tsx
│       │   ├── IntentsSection.tsx
│       │   ├── IntentItem.tsx
│       │   ├── EntitiesList.tsx
│       │   ├── EntityItem.tsx
│       │   ├── LoadingState.tsx
│       │   ├── EmptyState.tsx
│       │   └── ErrorState.tsx
│       ├── hooks/
│       │   ├── useAgents.ts
│       │   ├── useAgentForm.ts
│       │   └── useAgentValidation.ts
│       ├── types.ts
│       ├── api.ts
│       ├── validation.ts
│       └── styles.module.css
```

---

## Testing Checklist

### Unit Tests:
- [ ] Agent form validation
- [ ] Intent add/remove logic
- [ ] Entity add/remove logic
- [ ] Form submit handler
- [ ] Modal open/close logic
- [ ] Delete confirmation

### Integration Tests:
- [ ] Fetch agents on page load
- [ ] Create new agent flow
- [ ] Edit existing agent flow
- [ ] Delete agent flow
- [ ] Form validation with API
- [ ] Error handling scenarios

### E2E Tests:
- [ ] Complete create agent workflow
- [ ] Complete edit agent workflow
- [ ] Complete delete agent workflow
- [ ] Navigation flows
- [ ] Multi-intent/entity creation

### Accessibility Tests:
- [ ] Keyboard navigation
- [ ] Screen reader compatibility
- [ ] Focus management in modal
- [ ] ARIA labels
- [ ] Color contrast

---

## Implementation Priority

**Phase 1 - Core Functionality** (Week 1-2)
- [ ] Agents table display
- [ ] Basic modal structure
- [ ] Agent form (basic fields only)
- [ ] Create agent API integration
- [ ] Edit agent API integration
- [ ] Delete agent API integration

**Phase 2 - Advanced Features** (Week 3)
- [ ] Intents management
- [ ] Entities management
- [ ] Dynamic add/remove functionality
- [ ] Form validation
- [ ] Loading/error states

**Phase 3 - Polish** (Week 4)
- [ ] Responsive design
- [ ] Animations and transitions
- [ ] Accessibility improvements
- [ ] Error handling refinements
- [ ] Performance optimizations

---

## Performance Considerations

- [ ] Memoize agent rows to prevent unnecessary re-renders
- [ ] Debounce form input validation
- [ ] Lazy load modal content
- [ ] Optimize re-renders with React.memo
- [ ] Use virtual scrolling for large agent lists
- [ ] Cache agent data with React Query

---

## Accessibility Requirements

- [ ] WCAG 2.1 AA compliance
- [ ] Keyboard navigation throughout
- [ ] Focus trap in modal
- [ ] Screen reader announcements for actions
- [ ] Proper heading hierarchy
- [ ] Form labels associated with inputs
- [ ] Error messages announced to screen readers
- [ ] High contrast mode support

---

**Estimated Effort:** 2-3 weeks (2 developers)  
**Complexity:** High  
**Priority:** High  
**Dependencies:** React Router, React Hook Form, Zod, Axios, React Toastify

---

## Notes

- Agent solution ID is extracted from URL path: `/agent-sol/{agentSolutionId}/agent`
- Intents and entities have dynamic add/remove, requiring careful state management
- Entity description textarea needs special attention for proper sizing (180px min-height)
- Grid layout for intent items ensures proper alignment of name/button
- API base URL should be configurable via environment variable
- Consider adding drag-and-drop for reordering intents (future enhancement)
- Consider adding search/filter for large agent lists (future enhancement)
- Consider adding bulk actions (future enhancement)