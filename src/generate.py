# import os

# from dotenv import load_dotenv
# from openai import OpenAI
# from src.logger import logger

# load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# def generate_test_cases(problem_statement: str) -> str:
#     logger.info("Generating test cases...")
#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": (
#                 "You are a test case generation expert. Generate a variety of test cases, including edge and limit cases. "
#                 "Do NOT include any explanations or expected outputs. ONLY return test cases in plain text format."
#             )},
#             {"role": "user", "content": problem_statement}
#         ]
#     )
#     return response.choices[0].message.content

### src/generate.py
import os
from dotenv import load_dotenv
from openai import OpenAI
from src.logger import logger

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_cases(problem_statement: str) -> str:
    logger.info("Generating test cases...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": (
                "You are a test case generation expert. Generate a variety of test cases for any provided problem statement including edge and limit cases. "
                "Format each as a numbered test case in plain text like this:\n"
                "Test Case 1:\n"
                "then generate and give test cases according to given problem statement"
                "Do NOT use JSON or markdown. Do NOT include any explanations."
                "each test case in next line"
            )},
            {"role": "user", "content": problem_statement}
        ]
    )
    return response.choices[0].message.content.strip()
