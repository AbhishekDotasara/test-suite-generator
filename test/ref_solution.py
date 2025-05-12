# test/test_ref_solution.py
from src.ref_solution import max_income, max_subarray_sum, solve_reference

def test_max_subarray_sum():
    assert max_subarray_sum(5, [1, 2, -1, 3, -2]) == 5
    assert max_subarray_sum(6, [-2, -3, 4, -1, -2, 1]) == 4

def test_max_income():
    n = 4
    edges = [[0, 1], [1, 2], [1, 3]]
    bob = 3
    amount = [4, 4, -8, 6]
    assert isinstance(max_income(n, edges, bob, amount), int)

def test_solve_reference_subarray():
    problem = "Given an array of integers, find the maximum subarray sum."
    case = {"n": 5, "arr": [1, 2, -1, 3, -2]}
    assert solve_reference(problem, case) == 5

def test_solve_reference_tree():
    problem = "Tree problem with Bob and Alice gates"
    case = {
        "n": 4,
        "edges": [[0, 1], [1, 2], [1, 3]],
        "bob": 3,
        "amount": [4, 4, -8, 6]
    }
    assert isinstance(solve_reference(problem, case), int)
