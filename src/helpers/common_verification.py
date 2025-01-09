# Common Verification

# HTTP Status Code
# Headers
# Data Verification
# JSON Schema
# Time Verification


def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed to match status code"


def verify_response_key(key, expected_data):
    assert key == expected_data, "Failed, key is not matched"


def verify_json_key_not_null(key):
    assert key != 0, "Failed, key is Null"


def verify_json_key_greater_than_zero(key):
    assert key > 0, "Failed, key is not greater than 0"
