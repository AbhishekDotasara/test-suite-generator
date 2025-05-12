# import os

# from dotenv import load_dotenv
# from openai import OpenAI
# from src.logger import logger

# load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_expected_output(problem_statement: str, validated_test_cases: str) -> str:
#     logger.info("Generating expected outputs...")
#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": (
#                 "You are an expert in generating expected outputs for algorithm problems. "
#                 "Given the test cases and problem statement, return ONLY the expected outputs in plain text format."
#             )},
#             {"role": "user", "content": f"Problem Statement:\n{problem_statement}\n\nTest Cases:\n{validated_test_cases}"}
#         ]
#     )
#     return response.choices[0].message.content


import os
from dotenv import load_dotenv
from openai import OpenAI
from src.logger import logger

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_expected_output(problem_statement: str, validated_test_cases: str) -> str:
    logger.info("Generating expected outputs...")
    system_prompt = (
        "You are an expert in generating expected outputs based upon give problem statement . "
        "For each test case, return the output in this format:\n"
        "Test Case 1:\n<output>\n\n"
        "No explanations. No JSON."
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Problem:\n{problem_statement}\nTest Cases:\n{validated_test_cases}"}
        ]
    )
    return response.choices[0].message.content.strip()