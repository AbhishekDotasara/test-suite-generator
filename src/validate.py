# import os
# from dotenv import load_dotenv
# from openai import OpenAI
# from src.logger import logger

# load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def validate_test_cases(problem_statement: str, test_cases: str) -> str:
#     logger.info("Validating test cases...")
#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": (
#                 "You are a validation expert. Validate the following test cases for correctness and diversity. "
#                 "Return only the valid test cases in plain text format. Do not add explanations."
#             )},
#             {"role": "user", "content": f"Problem Statement:\n{problem_statement}\n\nTest Cases:\n{test_cases}"}
#         ]
#     )
#     return response.choices[0].message.content


import os
from dotenv import load_dotenv
from openai import OpenAI
from src.logger import logger

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def validate_test_cases(problem_statement: str, test_cases: str) -> str:
    logger.info("Validating test cases...")
    validation_prompt = (
        "You are a validation expert. Validate the following test cases based upon give contraints present in problem statement and return only the valid ones in plain text. "
        "Maintain the same formatting as the input (Test Case 1: ...). Do NOT include any explanations or JSON."
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a validation expert. Return only valid test cases, in plain text."},
            {"role": "user", "content": f"Problem:\n{problem_statement}\nTest Cases:\n{test_cases}"},
            {"role": "user", "content": validation_prompt}
        ]
    )
    return response.choices[0].message.content.strip()
