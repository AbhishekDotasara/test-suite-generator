# import os

# from dotenv import load_dotenv
# from openai import OpenAI
# from src.logger import logger

# load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def validate_expected_output(problem_statement: str, expected_outputs: str) -> str:
#     logger.info("Validating expected outputs...")
#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": (
#                 "You are an expert programmer. Carefully validate each expected output against the problem statement. "
#                 "Manually simulate each test case. Return only the validated test cases and expected outputs."
#             )},
#             {"role": "user", "content": f"Problem Statement:\n{problem_statement}\n\nTest Cases and Outputs:\n{expected_outputs}"}
#         ]
#     )
#     return response.choices[0].message.content


import os
from dotenv import load_dotenv
from openai import OpenAI
from src.logger import logger

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def validate_expected_output(problem_statement: str, expected_outputs: str) -> str:
    logger.info("Validating expected outputs...")
    validation_prompt = (
        "You are an expert programmer. Carefully validate each expected output against the problem statement. "
        "Manually simulate the logic and return the same format:\n"
        "Test Case 1:\n<output>\n\n"
        "No explanations. No JSON."
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": validation_prompt},
            {"role": "user", "content": f"Problem:\n{problem_statement}\nOutputs:\n{expected_outputs}"}
        ]
    )
    return response.choices[0].message.content.strip()