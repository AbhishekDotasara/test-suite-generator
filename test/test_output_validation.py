# test/test_output_validation.py
from unittest.mock import patch
from src.output_validation import validate_expected_output

@patch("src.output_validation.client.chat.completions.create")
def test_output_validation_mock_generic_problem(mock_create):
    mock_create.return_value.choices = [
        type("obj", (object,), {
            "message": type("msg", (object,), {
                "content": """Test Case 1:\n9"""
            })
        })
    ]

    problem = "Given an array of integers, find the maximum subarray sum."
    outputs = "Test Case 1:\n9"
    validated = validate_expected_output(problem, outputs)
    assert isinstance(validated, str)
    assert "Test Case 1" in validated
