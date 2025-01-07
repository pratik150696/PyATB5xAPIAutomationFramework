### Python API Automation Framework

Hybrid custom API Automation Framework include the proper folder structure

[API Automation Framework.png](../../Downloads/API%20Automation%20Framework.png)

Tech Stack
- Python - 3.13
- Requests - HTTP Requests
- PyTest - Testing Framework
- Reporting - Allure Report, PyTest HTML
- Test Data - cvs, excel
- Parallel Execution - x Distribute (xdist)
- Advance API Testcase - jsonschema


How to Install Packages
''' pip install requests pytest pytest-html faker allure-pytest jsonschema
'''


How to Run Test Cases Parallel
''' pip install pytest-xdist '''

How to Run Basic Test Cases with Allure Report
''' pytest filepath --allure=allure_result -s '''
