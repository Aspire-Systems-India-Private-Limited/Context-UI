# 🅰️ Angular Setup Guide - Quick Start

## 📋 Project Initialization

### Step 1: Create Angular Project
```bash
# Navigate to your workspace
cd c:\Users\soundarya.shanmugam\Downloads\agent-ops 1\agent-ops

# Create new Angular application
ng new agent-ops-angular --routing --style=scss

# Navigate to project
cd agent-ops-angular
```

**Angular CLI Options:**
- `--routing`: Generates routing module
- `--style=scss`: Uses SCSS for styling (better for variables)

---

## 📦 Install Dependencies

```bash
# Angular Material (optional UI components)
ng add @angular/material

# State Management (NgRx)
npm install @ngrx/store @ngrx/effects @ngrx/store-devtools

# HTTP & Forms (already included with Angular)
# @angular/common/http
# @angular/forms

# Utilities
npm install ngx-toastr                    # Toast notifications
npm install @fortawesome/fontawesome-free # Icons
npm install date-fns                      # Date formatting
npm install class-validator               # Validation
npm install class-transformer             # Object transformation

# Charts (choose one)
npm install ngx-charts                    # Angular-native charts
# OR
npm install chart.js ng2-charts           # Chart.js for Angular
```

---

## 🎨 Import Existing Styles

### Option 1: angular.json (Recommended)
```json
{
  "projects": {
    "agent-ops-angular": {
      "architect": {
        "build": {
          "options": {
            "styles": [
              "src/styles.scss",
              "src/assets/styles/globals.css",
              "src/assets/styles/ats-utilities.css",
              "node_modules/@fortawesome/fontawesome-free/css/all.min.css"
            ]
          }
        }
      }
    }
  }
}
```

### Option 2: styles.scss
```scss
/* src/styles.scss */
@import 'assets/styles/globals.css';
@import 'assets/styles/ats-utilities.css';
@import '@fortawesome/fontawesome-free/css/all.min.css';
```

### Step 2: Copy Existing Style Files
```bash
# Create assets/styles directory
mkdir -p src/assets/styles

# Copy existing styles
cp ../styles/globals.css src/assets/styles/
cp ../styles/ats-utilities.css src/assets/styles/
```

---

## 🏗️ Project Structure

```
agent-ops-angular/
├── src/
│   ├── app/
│   │   ├── core/                    # Core module (singleton services)
│   │   │   ├── layout/
│   │   │   │   ├── navbar/
│   │   │   │   ├── sidebar/
│   │   │   │   └── toolbar/
│   │   │   ├── guards/
│   │   │   │   └── auth.guard.ts
│   │   │   ├── interceptors/
│   │   │   │   └── api.interceptor.ts
│   │   │   ├── services/
│   │   │   │   ├── api.service.ts
│   │   │   │   ├── auth.service.ts
│   │   │   │   └── context.service.ts
│   │   │   └── core.module.ts
│   │   ├── shared/                  # Shared module (reusable components)
│   │   │   ├── components/
│   │   │   │   ├── button/
│   │   │   │   ├── card/
│   │   │   │   ├── modal/
│   │   │   │   └── loader/
│   │   │   ├── pipes/
│   │   │   ├── directives/
│   │   │   └── shared.module.ts
│   │   ├── features/                # Feature modules (lazy-loaded)
│   │   │   ├── admin/
│   │   │   │   ├── components/
│   │   │   │   ├── admin-routing.module.ts
│   │   │   │   └── admin.module.ts
│   │   │   ├── agent/
│   │   │   ├── session/
│   │   │   └── memory/
│   │   ├── pages/
│   │   │   └── dashboard/
│   │   ├── app-routing.module.ts
│   │   ├── app.component.ts
│   │   └── app.module.ts
│   ├── assets/
│   │   ├── styles/
│   │   │   ├── globals.css
│   │   │   └── ats-utilities.css
│   │   └── images/
│   ├── environments/
│   │   ├── environment.ts
│   │   └── environment.prod.ts
│   └── styles.scss
├── angular.json
├── package.json
└── tsconfig.json
```

---

## 🚀 Generate Components

Use Angular CLI to generate components, services, modules:

```bash
# Generate core layout components
ng generate component core/layout/navbar --module=core
ng generate component core/layout/sidebar --module=core
ng generate component core/layout/toolbar --module=core

# Generate shared components
ng generate component shared/components/button --module=shared --export
ng generate component shared/components/card --module=shared --export
ng generate component shared/components/modal --module=shared --export

# Generate services
ng generate service core/services/api
ng generate service core/services/auth
ng generate service core/services/context

# Generate feature module (lazy-loaded)
ng generate module features/admin --routing
ng generate component features/admin/context-admin --module=features/admin

# Generate guard
ng generate guard core/guards/auth

# Generate interceptor
ng generate interceptor core/interceptors/api
```

---

## 🔧 Configure Environment

```typescript
// src/environments/environment.ts
export const environment = {
  production: false,
  apiBase: 'http://localhost:8009',
  aiSearchApiBase: 'http://localhost:8010'
};

// src/environments/environment.prod.ts
export const environment = {
  production: true,
  apiBase: 'http://agent-ops-public.westus2.azurecontainer.io:8009',
  aiSearchApiBase: 'http://ai-search-api.azurecontainer.io:8010'
};
```

---

## 🛣️ Setup Routing

```typescript
// src/app/app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AuthGuard } from './core/guards/auth.guard';

const routes: Routes = [
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  {
    path: 'dashboard',
    loadChildren: () => import('./pages/dashboard/dashboard.module').then(m => m.DashboardModule)
  },
  {
    path: 'admin',
    loadChildren: () => import('./features/admin/admin.module').then(m => m.AdminModule),
    canActivate: [AuthGuard]
  },
  {
    path: 'agent',
    loadChildren: () => import('./features/agent/agent.module').then(m => m.AgentModule),
    canActivate: [AuthGuard]
  },
  { path: '**', redirectTo: '/dashboard' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

---

## 📡 Setup API Service

```typescript
// src/app/core/services/api.service.ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiBase = environment.apiBase;

  constructor(private http: HttpClient) {}

  get<T>(endpoint: string): Observable<T> {
    return this.http.get<T>(`${this.apiBase}${endpoint}`);
  }

  post<T>(endpoint: string, data: any): Observable<T> {
    return this.http.post<T>(`${this.apiBase}${endpoint}`, data);
  }

  put<T>(endpoint: string, data: any): Observable<T> {
    return this.http.put<T>(`${this.apiBase}${endpoint}`, data);
  }

  delete<T>(endpoint: string): Observable<T> {
    return this.http.delete<T>(`${this.apiBase}${endpoint}`);
  }
}
```

---

## 🎯 Development Commands

```bash
# Start development server
ng serve
# Navigate to http://localhost:4200

# Build for production
ng build --prod

# Run tests
ng test

# Run linter
ng lint

# Generate component
ng generate component <name>

# Generate service
ng generate service <name>

# Generate module
ng generate module <name>
```

---

## 📚 Next Steps

1. ✅ Review user stories in `/angular-conversion-user-stories/`
2. ✅ Follow folder structure above
3. ✅ Generate components using Angular CLI
4. ✅ Implement services for each API endpoint
5. ✅ Create reactive forms with validators
6. ✅ Add RxJS observables for state
7. ✅ Implement routing with guards
8. ✅ Add interceptors for error handling
9. ✅ Test components and services
10. ✅ Build and deploy

---

## 🔗 Useful Resources

- **Angular Docs**: https://angular.io/docs
- **Angular Material**: https://material.angular.io/
- **NgRx**: https://ngrx.io/
- **RxJS**: https://rxjs.dev/
- **Angular CLI**: https://angular.io/cli

---

## 💡 Pro Tips

1. ✅ Use **lazy loading** for feature modules to improve performance
2. ✅ Use **OnPush change detection** for better performance
3. ✅ Use **RxJS operators** (map, filter, switchMap) for reactive data flow
4. ✅ Use **async pipe** in templates to auto-unsubscribe
5. ✅ Use **track by** in *ngFor for better list rendering
6. ✅ Follow **Angular style guide**: https://angular.io/guide/styleguide
7. ✅ Use **Angular DevTools** for debugging

---

**Ready to start building! 🎉**