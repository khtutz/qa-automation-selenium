# QA Automation Framework with Selenium

## Overview
A modular test automation framework project built with Selenium WebDriver and Python, designed for testing multiple web applications from different domains. The framework implements the Page Object Model pattern and provides core utilities for robust test automation.

## Project Structure
```
qa-automation-selenium/
├── src/
│   ├── core/                      # Core framework components
│   │   ├── factories/             # Factory classes
│   │   │   ├── browser_factory.py # WebDriver initialization
│   │   │   └── page_factory.py    # Page object initialization
│   │   ├── page_objects/          # Base page components
│   │   │   ├── base_locators.py   # Common web element locators
│   │   │   ├── base_page.py       # Base page functionalities
│   │   │   └── popups_handler.py  # Common popup handling
│   │   └── securities/            # Security utilities
│   │       └── cookies_helper.py  # Cookie management
│   └── travel_airbnb/             # Airbnb testing implementation
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Prerequisites
- Python 3.8+
- pip (Python package installer)
- Chrome/Firefox browser
- MacOS/Linux/Windows

## Installation and Setup

1. Clone the repository:
```bash
git clone <your-repository-url>
cd qa-automation-selenium
```

2. Create and activate a virtual environment:
```bash
# For macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# For Windows
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Framework Architecture

### Core Components

#### 1. Factory Classes
- **browser_factory.py**: Manages WebDriver initialization and configuration
- **page_factory.py**: Handles dynamic page object creation and initialization

#### 2. Base Page Objects
- **base_page.py**: Implements common web element interactions
- **base_locators.py**: Defines shared element locators
- **popups_handler.py**: Manages common popup interactions

#### 3. Security Utils
- **cookies_helper.py**: Handles cookie management and session handling

### Test Implementation Structure
Each website testing suite follows a consistent structure:
- **configs/**: Environment-specific configurations
- **data/**: Test data and data models
- **page_objects/**: Website-specific page objects and locators
- **tests/**: Test implementations
- **utils/**: Helper utilities

## Running Tests

### Run all tests:
```bash
pytest src/travel_airbnb/tests/
```

### Run specific test module:
```bash
pytest src/travel_airbnb/tests/<test_file_name>.py
```

#### For example:
```bash
pytest src/travel_airbnb/tests/test_login.py
```

### Run with HTML report:
```bash
pytest --html=reports/report.html
```

## Key Features
- Page Object Model implementation
- Factory pattern for WebDriver and page objects
- YAML-based configuration management
- Structured test data handling
- Detailed HTML test reports
- Common popup and cookie management
- Extensible base page functionality

## Currently Implemented Test Suites
- Automated tests for Airbnb's core functionalities
  - Account login
  - End-to-end booking flow
  - For details, see travel_airbnb/README.md

## Work-In-Progress Functionalities
- Automated tests for Airbnb's core functionalities
  - Account registration
  - Reservation, and payment handling processes
  - Load testing

## Best Practices
- Use of Page Object Model
- Separation of test data from test logic
- Centralized configuration management
- Structured element locator organization
- Comprehensive test documentation
- Modular and reusable components

## Documentation
Each test suite includes:
- Detailed test cases in Markdown format
- Configuration guidelines
- Test data documentation
- Page object documentation

## Author
Kaung Htut Zaw

## License
This project is licensed under the MIT License - see the LICENSE file for details