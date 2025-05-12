# from fastapi import FastAPI, HTTPException
# from fastapi.responses import HTMLResponse
# from pydantic import BaseModel
# from src.generate import generate_test_cases
# from src.validate import validate_test_cases
# from src.output import generate_expected_output
# from src.output_validation import validate_expected_output

# app = FastAPI()

# # Define the problem statement
# PROBLEM_STATEMENT = """
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Constraints:

# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# """

# class ProblemInput(BaseModel):
#     problem_statement: str = PROBLEM_STATEMENT

# @app.post("/generate", response_class=HTMLResponse)
# async def generate_test_suite(input_data: ProblemInput):
#     try:
#         raw_test_cases = generate_test_cases(input_data.problem_statement)
#         validated_cases = validate_test_cases(input_data.problem_statement, raw_test_cases)
#         outputs = generate_expected_output(input_data.problem_statement, validated_cases)
#         validated_outputs = validate_expected_output(input_data.problem_statement, outputs)

#         html_result = (
#             f"<h2>Test Cases:</h2><pre>{raw_test_cases}</pre>"
#             f"<h2>Valid Test Cases:</h2><pre>{validated_cases}</pre>"
#             f"<h2>Expected Outputs:</h2><pre>{outputs}</pre>"
#             f"<h2>Validated Outputs:</h2><pre>{validated_outputs}</pre>"
#         )
#         return html_result

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/", response_class=HTMLResponse)
# async def test_endpoint():
#     try:
#         return await generate_test_suite(ProblemInput())
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.generate import generate_test_cases
from src.validate import validate_test_cases
from src.output import generate_expected_output
from src.output_validation import validate_expected_output
import os

app = FastAPI()

# Mount the frontend static files under /ui
app.mount("/ui", StaticFiles(directory="public", html=True), name="static")

# Define the problem statement
PROBLEM_STATEMENT = """
There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:

the price needed to open the gate at node i, if amount[i] is negative, or,
the cash reward obtained on opening the gate at node i, otherwise.
The game goes on as follows:

Initially, Alice is at node 0 and Bob is at node bob.
At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
If the gate is already open, no price will be required, nor will there be any cash reward.
If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.
Return the maximum net income Alice can have if she travels towards the optimal leaf node.

Constraints:

2 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.
1 <= bob < n
amount.length == n
amount[i] is an even integer in the range [-10^4, 10^4].
"""

class ProblemInput(BaseModel):
    problem_statement: str = PROBLEM_STATEMENT

@app.post("/generate", response_class=HTMLResponse)
async def generate_test_suite(input_data: ProblemInput):
    try:
        raw_test_cases = generate_test_cases(input_data.problem_statement)
        validated_cases = validate_test_cases(input_data.problem_statement, raw_test_cases)
        outputs = generate_expected_output(input_data.problem_statement, validated_cases)
        validated_outputs = validate_expected_output(input_data.problem_statement, outputs)

        html_result = (
            f"<h2>Test Cases:</h2><pre>{raw_test_cases}</pre>"
            f"<h2>Valid Test Cases:</h2><pre>{validated_cases}</pre>"
            f"<h2>Expected Outputs:</h2><pre>{outputs}</pre>"
            f"<h2>Validated Outputs:</h2><pre>{validated_outputs}</pre>"
        )
        return html_result

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

