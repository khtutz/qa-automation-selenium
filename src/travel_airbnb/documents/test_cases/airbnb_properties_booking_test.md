# Test Case: Airbnb Property Booking

## General Information
- **Module Name:** Property Booking
- **Test Case ID:** PROPERTY_BOOKING_001
- **Tester Name:** 
- **Created Date:** 
- **Modified Date:** 
- **Priority:** High
- **Severity:** High

## Test Case Description
Verify that a registered user can successfully book a property.

## Prerequisites
1. Web browser installed
2. Active internet connection
3. Valid account
4. Valid credit card or other payment method

## Environmental Information
- **Operating System:** macOS Sonoma 14.2
- **Browser:** Chrome 120.0.6099.129
- **Screen Resolution:** 1920x1080
- **Device:** MacBook Pro 2023

## Test Data
- **Email:**
- **Password:**
- **Date of Birth:**
- **Destination**
- **Check in date**
- **Check out date**
- **Guests**
- **Payment Information**

## Test Scenarios
Verification of steps invovled in property booking

## Testing

### Pre-conditions
1. Browser is opened and ready to be used
2. Home page www.airbnb.com is browsed
3. At least one of the login test cases must be passed (for a successful account logged in)
4. Account is logged

### 1. Steps - Home Page
| Step # | Action Description | Expected Result | Actual Result | Status | Date | Comments |
|--------|-------------------|-----------------|---------------|---------|------|-----------|
| 1.1 | Enter destination | Auto suggestion comes out |  |  |  |  |
| 1.2 | Choose suggested destination | Destination is accepted |  |  |  |  |
| 1.3 | Click check in date | Calendar comes out |  |  |  |  |
| 1.4 | Choose check in date from calendar | Check in date is selected at calendar |  |  |  |  |
| 1.5 | Choose check out date from calendar | Check out date is selected at calendar |  |  |  |  |
| 1.6 | Press '+' button for Adults, Children, Infants, and/or Pets to add guests | Guest number is increased and accepted |  |  |  |  |
| 1.7 | Press '-' button for Adults, Children, Infants, and/or Pets to reduce guests | Guest number is modified and accepted |  |  |  |  |
| 1.8 | Press 'Search' button | Page is browsed to 'Properties Result' page, and results based on choosen destination name, dates, and guests are displayed |  |  |  |  |

### 2. Steps - Properties Result Page
| Step # | Action Description | Expected Result | Actual Result | Status | Date | Comments |
|--------|-------------------|-----------------|---------------|---------|------|-----------|
| 2.1 | Press 'Filters' button | Filters pop up comes out |  |  |  |  |
| 2.2 | Choose 'Type of place' | Type of place is selected |  |  |  |  |
| 2.3 | Enter minimum price | Entered price is accepted |  |  |  |  |
| 2.4 | Enter maximum price | Entered price is accepted |  |  |  |  |
| 2.5 | Press '+' to choose numbers of Bedrooms, Beds, and Bathrooms | Rooms numbers are modified and accepted |  |  |  |  |
| 2.6 | Press '-' to subtract the numbers of Bedrooms, Beds, and Bathrooms | Rooms numbers are modified and accepted |  |  |  |  |
| 2.7 | Choose one or more 'Amenities' | Amenity options are selected |  |  |  |  |
| 2.8 | Choose one or more 'Bookings' | booking options are selected |  |  |  |  |
| 2.9 | Choose 'Property type' | Property type is selected |  |  |  |  |
| 2.10 | Press 'Show <number> places' button | Button is clicked, results are filtered according to criteria selected, and properties result page is displayed with filtered properties |  |  |  |  |
| 2.11 | Select the desire property by clicking on photos, captions, or other descriptions | Page is browsed to individual property reservation page |  |  |  |  |

### 3. Steps - Reservation
| Step # | Action Description | Expected Result | Actual Result | Status | Date | Comments |
|--------|-------------------|-----------------|---------------|---------|------|-----------|
| 3.1 | Press 'Reserve' button | Page is browsed to Payment page |  |  |  |  |

### 4. Steps - Payment Page
| Step # | Action Description | Expected Result | Actual Result | Status | Date | Comments |
|--------|-------------------|-----------------|---------------|---------|------|-----------|
| 4.1 | Choose payment option: Credit or debit card from drop down menu | Payment options is selected |  |  |  |  |
| 4.2 | Enter 16 digits as card number | All card numbers are accepted |  |  |  |  |
| 4.3 | Enter expiration date in MM/YYYY | Date in MM/YYYY format is accepted |  |  |  |  |
| 4.4 | Enter 'ZIP code' | Zip code is accepted |  |  |  |  |
| 4.5 | Choose 'Country/region' from drop down menu | Country/region is selected |  |  |  |  |
| 4.6 | Press 'Request to book' button | Property booking request is sent |  |  |  |  |

## Post-conditions
1. Property is booked successfully
2. Booking information can be viewed from the profile
3. Reservation won't be confirmed until the host accepts the booking request
4. User/client won't be charged until the host accepts the booking request

## Test Execution Summary
- **Test Result:** 
- **Execution Date:** 
- **Executed By:** 
- **Defects Found:** 
- **Bugs Ids (If applicable):**
- **Test Duration:** 

## Additional Notes
- Test case should be executed on different browsers and devices for complete coverage
- Mobile responsiveness should be tested separately

## Document History
| Version | Date | Modified By | Description of Changes |
|---------|------|-------------|----------------------|
| 1.0 |  |  | Initial test case creation |
