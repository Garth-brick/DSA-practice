# 0, 1, 1, 2, 3, 5, 8, ...
# 0  1  2  3  4  5  6

def fib(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
    
print(fib(50))