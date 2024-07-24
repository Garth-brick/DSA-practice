memo = {}

def knapsack(capacity: int, weights: list[int], values: list[int], n: int) -> int:
    
    # think of the smallest valid input while writing your base case
    # we could have a bag with 0 capacity or an array with 0 length, both of which would have 0 value 
    if capacity == 0 or n == 0:
        return 0
    
    if (capacity, n) in memo:
        return memo[(capacity, n)]
    
    # if this weight is too much to be added then just move on without it
    if weights[n - 1] > capacity:
        return knapsack(capacity, weights, values, n - 1)
        
    # otherwise do one function for picking this weight and one without picking it
    result = max(
        values[n - 1] + knapsack(
            capacity - weights[n - 1], 
            weights, 
            values, 
            n - 1
        ),
        knapsack(capacity, weights, values, n - 1)
    )
    memo[(capacity, n)] = result
    return result


capacity = int(input())
n = int(input())
weights = list(map(int, input().strip().split()))
values = list(map(int, input().strip().split()))
result = knapsack(capacity, weights, values, n)
print(result)


"""input
7
4
1 3 4 5
1 4 7 5
"""