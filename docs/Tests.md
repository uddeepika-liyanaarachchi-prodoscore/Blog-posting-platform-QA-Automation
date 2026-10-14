# Blog Poster Frontend (FE) QA Automation - Test Cases Specification

## 1. Traceability Matrix

| Module            | Test Case ID  | Test Case Title                                       | Automation Status | Priority |
| :---------------- | :------------ | :---------------------------------------------------- | :---------------- | :------- |
| **Navigation**    | `TC_NAV_01`   | Default Page Load & Initial UI State                  | Automated         | Critical |
| **Navigation**    | `TC_NAV_02`   | Navigate to Login View via Navbar                     | Automated         | High     |
| **Navigation**    | `TC_NAV_03`   | Navigate Back to Home / Explore View                  | Automated         | High     |
| **Navigation**    | `TC_NAV_04`   | Toggle Between Sign-In & Sign-Up Views                | Automated         | Critical |
| **Login UI**      | `TC_LOGIN_01` | Login Form Elements & Attributes Validation           | Automated         | High     |
| **Login UI**      | `TC_LOGIN_02` | Client-Side Required Field Validation on Empty Submit | Automated         | Medium   |
| **Login UI**      | `TC_LOGIN_03` | Browser Validation Error on Malformed Email           | Automated         | Medium   |
| **Login UI**      | `TC_LOGIN_04` | Credential Input Field Interaction                    | Automated         | High     |
| **Register UI**   | `TC_REG_01`   | Registration Form Elements & Placeholders             | Automated         | High     |
| **Register UI**   | `TC_REG_02`   | Registration Input Field Interaction                  | Automated         | High     |
| **Register UI**   | `TC_REG_03`   | Return to Login View from Registration View           | Automated         | Medium   |
| **Dashboard UI**  | `TC_DASH_01`  | Authenticated Session UI State & Greeting             | Automated         | Critical |
| **Dashboard UI**  | `TC_DASH_02`  | Logout Session Cleanup & State Reset                  | Automated         | Critical |
| **Post Modal UI** | `TC_MODAL_01` | Open Blog Post Details Modal & Verify Content         | Automated         | High     |
| **Post Modal UI** | `TC_MODAL_02` | Close Modal via Close ('×') Button                    | Automated         | High     |
| **Post Modal UI** | `TC_MODAL_03` | Close Modal via Backdrop Click                        | Automated         | Medium   |
| **Post Modal UI** | `TC_MODAL_04` | Close Modal via Keyboard 'Escape' Key                 | Automated         | Medium   |

---

## 2. Detailed Test Specifications

### 2.1 Navigation & View Toggling

#### `TC_NAV_01`: Default Page Load & Initial UI State

- **Objective**: Verify that upon initial landing without active session:
- Page title contains `Blog Poster Project`
- `#main-view` (Explore) is visible
- `#login-view`, `#sign-up-view`, and `#my-view` are hidden
- Navbar `#navlogin-btn` is visible and `#navdashboard-btn` is hidden
- **Expected Result**: Standard unauthenticated UI renders correctly.

#### `TC_NAV_02`: Navigate to Login View

- **Objective**: Verify clicking the login button in navbar switches views.
- **Steps**:

1.  Click `#navlogin-btn`.

- **Expected Result**: `#login-view` becomes visible; `#main-view` becomes hidden.

#### `TC_NAV_03`: Navigate Back to Home View

- **Objective**: Verify clicking Home button in navbar returns to Explore feed.
- **Steps**:

1.  Navigate to login view.
2.  Click `#navhome-btn`.

- **Expected Result**: `#main-view` becomes visible; `#login-view` becomes hidden.

#### `TC_NAV_04`: Toggle Between Sign-In & Sign-Up Views

- **Objective**: Verify seamless switching between registration and login forms.
- **Steps**:

1.  In Login view, click `#sign-up-btn` ("Don't have an account? Sign up").
2.  Verify `#sign-up-view` is displayed.
3.  In Registration view, click `#sign-in-btn` ("Need to login in ? Sign In").

- **Expected Result**: Views toggle reciprocally without page reload.

---

### 2.2 Login UI & Form Validation

#### `TC_LOGIN_01`: Elements & Attributes Validation

- **Objective**: Verify `#login_email` has `type="email"` & `required="true"`, `#password` has `type="password"` & `required="true"`.
- **Expected Result**: Form inputs enforce required constraints.

#### `TC_LOGIN_02`: Empty Submission Validation

- **Objective**: Verify browser triggers HTML5 native validation popup when submitting empty form.
- **Expected Result**: Validation message is raised on `#login_email`.

#### `TC_LOGIN_03`: Malformed Email Validation

- **Objective**: Verify browser catches invalid email format without `@`.
- **Expected Result**: HTML5 type-mismatch validation message triggered.

#### `TC_LOGIN_04`: Credential Input Fields

- **Objective**: Verify entering email and password correctly reflects in input values.
- **Expected Result**: Value attributes match entered test data.

---

### 2.3 Registration UI

#### `TC_REG_01`: Elements & Placeholders

- **Objective**: Verify `#signup_mail` and `#register_password` are present with appropriate placeholders.
- **Expected Result**: Registration form structure is verified.

#### `TC_REG_02`: Input Field Interaction

- **Objective**: Verify typing test values into registration inputs updates field values.
- **Expected Result**: Input values match typed text.

#### `TC_REG_03`: Return to Login

- **Objective**: Verify user can easily navigate back to sign in view.
- **Expected Result**: `#login-view` becomes visible.

---

### 2.4 Dashboard & Session Management

#### `TC_DASH_01`: Authenticated Session UI State

- **Objective**: Verify authenticated session behavior:
- Simulate `accessToken` in `localStorage`.
- Reload page.
- **Expected Result**:
- Navbar `#navdashboard-btn` is visible.
- Navbar `#navlogin-btn` is hidden.
- `#my-view` is displayed with greeting header `#HI` ("Welcome to Blog Poster").

#### `TC_DASH_02`: Logout Session Cleanup

- **Objective**: Verify clicking `#logout-btn` clears `localStorage` and resets UI.
- **Steps**:

1.  Click `#logout-btn`.

- **Expected Result**:
- `localStorage.getItem("accessToken")` is `None`.
- UI switches to `#login-view`.
- `#navdashboard-btn` is hidden, `#navlogin-btn` is restored.

---

### 2.5 Blog Post Details Modal

#### `TC_MODAL_01`: Open Blog Post Modal

- **Objective**: Verify post details modal opens with title and content.
- **Expected Result**: `#post-modal` removes `.hidden`, `#modal-post-title` and `#modal-post-desc` display post data.

#### `TC_MODAL_02`: Close Modal via Close Button

- **Objective**: Verify clicking `#modal-close-btn` closes the modal.
- **Expected Result**: `#post-modal` gains `.hidden` class and body scrolling is restored.

#### `TC_MODAL_03`: Close Modal via Backdrop Click

- **Objective**: Verify clicking dark backdrop outside modal content closes the modal.
- **Expected Result**: Modal closes smoothly.

#### `TC_MODAL_04`: Close Modal via Escape Key

- **Objective**: Verify pressing keyboard `Escape` closes the modal.
- **Expected Result**: Modal closes immediately.
