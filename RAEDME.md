### Python API Automation Framework

Hybrid custom API Automation Framework include the proper folder structure

https://private-user-images.githubusercontent.com/1409610/354955159-3c7d5fe5-207a-42e7-84fe-f4d53354d987.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzYyNjAzODksIm5iZiI6MTczNjI2MDA4OSwicGF0aCI6Ii8xNDA5NjEwLzM1NDk1NTE1OS0zYzdkNWZlNS0yMDdhLTQyZTctODRmZS1mNGQ1MzM1NGQ5ODcucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDEwNyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAxMDdUMTQyODA5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MWJlNWNhNjcxODA3NmRlNjI2MzIxNGMzZGI4N2M5NzAyYWY4OWJiNmZlNTk2OTJhZTFlNWFlOTI3MTg4ZWViMiZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.Op_5nJmeiY8ZeFDsssVYyl3bJt84htovnyxEMuWwH1E

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
