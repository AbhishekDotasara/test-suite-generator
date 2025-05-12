# test/test_output.py
from unittest.mock import patch
from src.output import generate_expected_output

@patch("src.output.client.chat.completions.create")
def test_output_mock_generic_problem(mock_create):
    mock_create.return_value.choices = [
        type("obj", (object,), {
            "message": type("msg", (object,), {
                "content": """Test Case 1:\n9"""
            })
        })
    ]

    problem = "Given an array of integers, find the maximum subarray sum."
    validated_cases = "Test Case 1:\nn = 5\narr = [1, 2, 3, -2, 5]"
    outputs = generate_expected_output(problem, validated_cases)
    assert isinstance(outputs, str)
    assert "Test Case 1" in outputs
