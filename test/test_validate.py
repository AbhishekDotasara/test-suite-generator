# test/test_validate.py
from unittest.mock import patch
from src.validate import validate_test_cases

@patch("src.validate.client.chat.completions.create")
def test_validate_mock_generic_problem(mock_create):
    mock_create.return_value.choices = [
        type("obj", (object,), {
            "message": type("msg", (object,), {
                "content": """Test Case 1:
n = 5
arr = [1, 2, 3, 4, 5]"""
            })
        })
    ]

    problem = "Given an array of integers, find the maximum subarray sum."
    raw_cases = "Test Case 1:\nn = 5\narr = [1, 2, 3, 4, 5]"
    validated = validate_test_cases(problem, raw_cases)
    assert isinstance(validated, str)
    assert "Test Case 1" in validated
