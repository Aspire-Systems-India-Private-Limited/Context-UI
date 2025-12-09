# OAuth Callback Handler - User Stories (Content Focus)

## Overview
OAuth/Okta callback handler page that processes authentication redirects.

## Data Model
```typescript
interface OAuthCallback {
  code?: string;
  state?: string;
  error?: string;
  error_description?: string;
}

interface OktaTokenResponse {
  access_token: string;
  id_token: string;
  refresh_token?: string;
  expires_in: number;
  token_type: string;
}
```

## User Stories

### 1. Display Loading State
- Show "Signing you in..." message
- Loading spinner/animation
- Prevent user interaction during processing

### 2. Handle OAuth Redirect
- Extract code and state from URL query parameters
- Validate state parameter matches original request
- Handle error parameters if present

### 3. Exchange Code for Tokens
- Call Okta token endpoint with authorization code
- Receive access token, ID token, refresh token
- Store tokens securely (localStorage or httpOnly cookie)

### 4. Redirect on Success
- After successful token exchange, redirect to home/dashboard
- Preserve original destination URL if stored in state
- Clear URL parameters

### 5. Handle Errors
- Display error message if authentication fails
- Show specific error description from OAuth provider
- Provide "Try Again" button to restart auth flow
- Log error details for debugging

### 6. Timeout Handling
- Set timeout for callback processing (e.g., 10 seconds)
- Show error if callback takes too long
- Provide manual retry option

## Implementation Notes
- Uses OktaClient module from static/okta-client.js
- Minimal UI - primarily background processing
- Error handling crucial
- Redirect URLs must be pre-configured in Okta

## API/Client Methods
```typescript
// From okta-client.js
OktaClient.handleRedirect()  // Process callback
OktaClient.getTokens()       // Get stored tokens
OktaClient.logout()          // Clear session (if error)
```

## Features
- OAuth callback processing
- Loading state display
- Error handling with messages
- Automatic redirect on success
- Token storage
- State validation
- Timeout handling

**Estimated Effort:** 2-3 hours
**Complexity:** Low
**Priority:** Medium (if using OAuth)
**Dependencies:** Okta SDK or custom OAuth client