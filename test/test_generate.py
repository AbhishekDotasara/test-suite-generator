# test/test_generate.py
from unittest.mock import patch
from src.generate import generate_test_cases

@patch("src.generate.client.chat.completions.create")
def test_generate_mock_generic_problem(mock_create):
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
    result = generate_test_cases(problem)

    assert isinstance(result, str)
    assert "Test Case 1" in result
    assert "arr" in result
