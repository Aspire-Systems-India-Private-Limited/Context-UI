# 🎨 Style Reference - Quick Guide

## 📁 Existing Style Files

Your project already has a complete design system. **Use these files** instead of recreating styles:

### 1. `/styles/globals.css`
**Purpose:** Global design tokens, CSS variables, theme colors, dark mode support

**Key Features:**
- CSS custom properties (variables) for colors, spacing, fonts
- Dark mode theme with `.dark` class
- Base font-size: 14px
- Responsive design tokens
- Chart color schemes
- Sidebar theming

**Usage in React:**
```javascript
// Import in your main App.jsx or index.js
import '../styles/globals.css';
```

---

### 2. `/styles/ats-utilities.css`
**Purpose:** Utility classes for rapid UI development

**Key Features:**
- Layout utilities (`.container-fluid`, `.section-padding`)
- Spacing utilities (`.space-y-8`, `.space-y-12`)
- Typography utilities (`.text-balance`, `.text-pretty`, `.gradient-text`)
- Gradient backgrounds
- Custom scrollbars
- Animation utilities
- Responsive helpers

**Usage in React:**
```javascript
// Import after globals.css
import '../styles/ats-utilities.css';

// Use utility classes in components
<div className="container-fluid section-padding">
  <h1 className="gradient-text">Hello World</h1>
</div>
```

---

### 3. `/guidelines/Guidelines.md`
**Purpose:** Design system guidelines, component specifications, usage rules

**Key Topics:**
- General guidelines for positioning, code structure
- Design system guidelines (fonts, dates, toolbars)
- Component specifications (Button, etc.)
- Usage examples

**When to Use:**
- Before designing new components
- When unsure about styling patterns
- To maintain consistency across the app

---

## 🎨 Color Palette

From `globals.css`:

```css
:root {
  /* Primary Colors */
  --primary: #030213;
  --secondary: oklch(0.95 0.0058 264.53);
  
  /* Background */
  --background: #ffffff;
  --card: #ffffff;
  
  /* Text */
  --foreground: oklch(0.145 0 0);
  
  /* Accent */
  --accent: #e9ebef;
  --destructive: #d4183d;
  
  /* Borders & Inputs */
  --border: rgba(0, 0, 0, 0.1);
  --input-background: #f3f3f5;
}
```

**Purple Theme (from HTML templates):**
- `--primary-purple: #65336e`
- `--dark-purple: #542d6b`
- `--bg-purple: #692e8b`
- `--light-blue: #80c6ff`

---

## 📝 Typography

**Base Settings:**
- Font size: `14px` (from `globals.css`)
- Font family: Maven Pro, Segoe UI, Arial, sans-serif
- Font weights: 400 (normal), 500 (medium)

**Headings:**
- Large: 48px
- Medium: 36px
- Small: 24px
- Sub: 18px

---

## 🧩 Common Utility Classes

### Layout
```html
<div className="container-fluid">...</div>
<div className="section-padding">...</div>
```

### Spacing
```html
<div className="space-y-8">...</div>   <!-- 2rem vertical spacing -->
<div className="space-y-12">...</div>  <!-- 3rem vertical spacing -->
```

### Typography
```html
<h1 className="text-balance">...</h1>       <!-- Balanced text wrap -->
<p className="text-pretty">...</p>          <!-- Pretty text wrap -->
<h2 className="gradient-text">...</h2>      <!-- Purple-teal gradient -->
```

---

## 🎯 Quick Start for Angular

### Step 1: Import Styles
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

### Step 2: Use CSS Variables
```scss
/* In component.scss */
.button {
  background-color: var(--primary);
  color: var(--primary-foreground);
  border-radius: var(--radius);
}
```

```typescript
// Or use ngStyle in component.html
<button [ngStyle]="{ 'background': 'var(--primary)' }">Click</button>
```

### Step 3: Use Utility Classes
```html
<!-- In component.html -->
<div class="container-fluid section-padding">
  <h1 class="gradient-text">Welcome</h1>
  <div class="space-y-8">
    <p>Content 1</p>
    <p>Content 2</p>
  </div>
</div>
```

---

## 🔧 Customization

If you need to extend the styles:

1. **Add new CSS variables** in `globals.css`:
```css
:root {
  --custom-color: #your-color;
}
```

2. **Add new utility classes** in `ats-utilities.css`:
```css
.my-custom-class {
  /* your styles */
}
```

3. **Follow guidelines** in `/guidelines/Guidelines.md`

---

## ✅ Best Practices

1. ✅ **Always import** `globals.css` first, then `ats-utilities.css`
2. ✅ **Use CSS variables** from `globals.css` for colors, spacing, fonts
3. ✅ **Use utility classes** from `ats-utilities.css` for common patterns
4. ✅ **Follow** design guidelines in `Guidelines.md`
5. ✅ **Maintain consistency** with existing patterns
6. ❌ **Don't** create duplicate styles
7. ❌ **Don't** hardcode colors - use variables
8. ❌ **Don't** ignore the guidelines

---

## 📚 Related Files

- **User Stories:** All files in `react-conversion-user-stories/` folder
- **Figma Prompts:** `FIGMA_PROMPTS.md` (already references style files)
- **README:** `00_README.md` (architecture overview)
- **Index:** `INDEX.md` (navigation guide)

---

**Quick Tip:** When using Figma Maker, always mention in your prompts:
```
"Use the existing design system from /styles/globals.css and /styles/ats-utilities.css"
```

This ensures generated React code is consistent with your existing styles! 🎨