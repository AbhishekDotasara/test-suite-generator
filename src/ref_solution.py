# src/ref_solution.py

def max_income(n, edges, bob, amount):
    from collections import defaultdict

    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    parent = [-1] * n

    def dfs_build(u, p):
        parent[u] = p
        for v in tree[u]:
            if v != p:
                dfs_build(v, u)

    dfs_build(0, -1)

    # Track bob's time to reach each node
    time = [-1] * n

    def dfs_time(u, t):
        time[u] = t
        if u == 0:
            return True
        return dfs_time(parent[u], t + 1)

    dfs_time(bob, 0)

    ans = float('-inf')
    visited = [False] * n

    def dfs_gain(u, depth):
        nonlocal ans
        visited[u] = True

        if time[u] == -1:
            gain = amount[u]
        elif depth < time[u]:
            gain = amount[u]
        elif depth == time[u]:
            gain = amount[u] // 2
        else:
            gain = 0

        is_leaf = True
        total = float('-inf')

        for v in tree[u]:
            if not visited[v]:
                is_leaf = False
                total = max(total, dfs_gain(v, depth + 1))

        result = gain if is_leaf else gain + total
        ans = max(ans, result)
        return result

    dfs_gain(0, 0)
    return ans


def max_subarray_sum(n, arr):
    max_ending_here = max_so_far = arr[0]
    for i in range(1, n):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


def solve_reference(problem_description: str, case: dict):
    """
    Dispatch reference logic based on the problem type inferred from the description.
    """
    if "subarray sum" in problem_description.lower():
        return max_subarray_sum(case["n"], case["arr"])
    elif "tree" in problem_description.lower() and "bob" in case:
        return max_income(case["n"], case["edges"], case["bob"], case["amount"])
    else:
        raise NotImplementedError("No reference solution for this problem type.")
