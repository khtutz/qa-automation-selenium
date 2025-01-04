# Test Case: Airbnb User Sign Up with Email

## General Information
- **Module Name:** Account Registration with Email
- **Test Case ID:** ACCOUNT_SIGNUP_EMAIL_001
- **Tester Name:** 
- **Created Date:** 
- **Modified Date:** 
- **Priority:** High
- **Severity:** High

## Test Case Description
Verify that a new user can successfully create an account on Airbnb using email registration method.

## Prerequisites
1. Active internet connection
2. Valid email address
3. No existing Airbnb account with the test email
4. Web browser installed

## Environmental Information
- **Operating System:** macOS Sonoma 14.2
- **Browser:** Chrome 120.0.6099.129
- **Screen Resolution:** 1920x1080
- **Device:** MacBook Pro 2023

## Test Data
- **First Name:**
- **Last Name:**
- **Email:**
- **Password:**
- **Date of Birth:**

## Test Scenarios
Verification of account registration using email, and other relevant information

## Testing

### Pre-conditions
1. Browser is opened and ready to be used.
2. Home page www.airbnb.com is browsed.

### Steps
| Step # | Action Description | Expected Result | Actual Result | Status | Date | Comments |
|--------|-------------------|-----------------|---------------|---------|------|-----------|
| 1 | Click on "Sign up" button in the top-right corner | Sign up modal window appears |  |  |  |  |
| 2 | Click "Continue with email" option | Email input field appears |  |  |  |  |
| 3 | Enter (unregistered) email address | Email is accepted in the field |  |  |  |  |
| 4 | Click "Continue" button | Registration form expands to show additional fields |  |  |  |  |
| 5 | Enter First Name | First name is accepted |  |  |  |  |
| 6 | Enter Last Name | Last name is accepted |  |  |  |  |
| 7 | Enter Date of Birth | DOB is accepted |  |  |  |  |
| 8 | Enter Password | Password is accepted and strength indicator updates |  |  |  | Password meets complexity requirements |
| 9 | Click “Agree and continue” button | Account is created, and confirmation email is sent |  |  |  | Email confirmation required |


## Post-conditions
1. User account is created successfully (after email confirmation)
2. User is logged into the account
3. User profile is accessible

## Test Execution Summary
- **Test Result:** 
- **Execution Date:** 
- **Executed By:** 
- **Defects Found:** 
- **Bugs Ids (If applicable):**
- **Test Duration:** 

## Additional Notes
- Password rules:
  - It can't contain user's name or email address
  - It must have at least 8 characters
  - It can contain a number or symbol
- Email verification link is sent to the provided email address
- Test case should be executed on different browsers and devices for complete coverage
- Mobile responsiveness should be tested separately

## Document History
| Version | Date | Modified By | Description of Changes |
|---------|------|-------------|----------------------|
| 1.0 |  |  | Initial test case creation |
