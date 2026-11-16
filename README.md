SQA Automation Project

This project contains sample Selenium tests for login scenarios using pytest and Allure reporting.

Folder Structure

C:\sqa_automation_project
│
├─ drivers\                # ChromeDriver
├─ reports\                # Allure reports
├─ screenshots\            # Test screenshots
│   ├─ report_dashboard.png
│   ├─ test_details.png
│   ├─ report_dashboard_valid_user.png
│   ├─ test_details_valid_user.png
│   ├─ report_dashboard_invalid_password.png
│   └─ test_details_invalid_password.png
├─ tests\                  # Test scripts
│   ├─ test_login_locked_user.py
│   ├─ test_login_valid_user.py
│   └─ test_login_invalid_password.py
├─ pytest_cache\           # Automatically created by pytest (ignore)
└─ README.md               # Project documentation

How to Run Tests

1. Open CMD in the project folder:

cd C:\sqa_automation_project

2. Run the test with pytest and generate Allure report:

pytest --alluredir=reports

3. Serve the Allure report:

allure serve reports

Test Results Screenshots
Task 1: Locked User Login

Allure Report Dashboard: report_dashboard.png

Test Details: test_details.png

Notes:

drivers folder contains ChromeDriver required for Selenium.

pytest_cache folder is automatically created by pytest (ignore it).

There is 1 test case in test_login_locked_user.py which passed successfully.

The test uses @pytest.mark.sanity. You may see a warning about it, but it can be safely ignored.

Task 2: Valid User Login

Allure Report Dashboard: report_dashboard_valid_user.png

Test Details: test_details_valid_user.png

Notes:

There is 1 test case in test_login_valid_user.py which passed successfully.

Screenshots were taken manually using Lightshot.

The test uses @pytest.mark.sanity. You may see a warning about it, but it can be safely ignored.

Task 3: Invalid Password Login

Allure Report Dashboard: report_dashboard_invalid_password.png

Test Details: test_details_invalid_password.png

Notes:

There is 1 test case in test_login_invalid_password.py which passed successfully.

Screenshots were taken manually using Lightshot.

The test uses @pytest.mark.sanity. You may see a warning about it, but it can be safely ignored.

