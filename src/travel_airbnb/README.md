# Airbnb Test Automation Suite

## Overview
Automated testing implementation for Airbnb's core functionalities using the qa-automation-selenium framework.

## Directory Structure
```
travel_airbnb/
├── configs/                     # Configuration files
│   └── env_config.yaml          # Environment configurations
├── data/                        # Test data management
│   ├── models/                  # Data models
│   │   ├── account_models.py    # User account models
│   │   └── booking_models.py    # Booking data models
│   └── test_data/               # Test data files
│       └── development/
│           └── booking_test_data.yaml
├── documents/                   # Test documentation
│   └── test_cases/              # Detailed test cases
│       ├── login_with_email_test.md
│       ├── properties_booking_test.md
│       └── signup_with_email_test.md
├── page_objects/                # Page Object Model implementation
│   ├── locators/                # Web element locators for each page object
│   │   ├── base_locators.py
│   │   ├── home_page_locators.py
│   │   ├── payment_page_locators.py
│   │   ├── properties_result_page_locators.py
│   │   ├── reservation_page_locators.py
│   │   └── signup_login_page_locators.py
│   ├── base_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── payment_page.py
│   ├── properties_result_page.py
│   ├── reservation_page.py
│   └── signup_page.py
├── reports/                    # Test execution reports
├── tests/                      # Test implementations
│   ├── base_test.py            # Base test class
│   ├── conftest.py             # pytest configurations
│   ├── test_endtoend_booking.py
│   ├── test_login.py
│   └── test_signup.py
└── utils/                      # Utility functions
    ├── config_reader.py        # Configuration management
    ├── data_loader.py          # Test data loading
    ├── enums.py                # Enumerations
    └── logging_helper.py       # Logging utilities
```

## Test Modules

### Login Tests (test_login.py)
- Email login validation
- Session management

### Signup Tests (test_signup.py)
- New user registration

### End-to-End Booking Tests (test_endtoend_booking.py)
- Property search
- Filtering
- Reservation

## Configuration
- Environment configurations in `configs/env_config.yaml`
- Test data in `data/test_data/development/`
- Logging configuration in `utils/logging_helper.py`

## Test Data Management
- Data models defined in `data/models/`
- YAML-based test data files
- Environment-specific test data

## Running Tests
```bash
# Run all tests
pytest tests/

# Run specific test module
pytest tests/test_login.py
pytest tests/test_signup.py
pytest tests/test_endtoend_booking.py

# Run with HTML report
pytest --html=reports/report.html
```

## Test Documentation
Detailed test cases are available in `documents/test_cases/`:
- login_with_email_test.md
- properties_booking_test.md
- signup_with_email_test.md

## Utilities
- **config_reader.py**: YAML configuration parser
- **data_loader.py**: Test data loading utility
- **logging_helper.py**: Custom logging implementation
- **enums.py**: Common enumerations

## Reports
Test execution reports are generated in the `reports/` directory

For framework-level documentation and setup instructions, please refer to the main README in the root directory.