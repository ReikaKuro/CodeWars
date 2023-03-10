"""
Problem Context

The Fibonacci sequence is traditionally used to explain tree recursion.

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

This algorithm serves welll its educative purpose but it's tremendously inefficient, not only because of recursion, but because we invoke the fibonacci function twice, and the right branch of recursion (i.e. fibonacci(n-2)) recalculates all the Fibonacci numbers already calculated by the left branch (i.e. fibonacci(n-1)).

This algorithm is so inefficient that the time to calculate any Fibonacci number over 50 is simply too much. You may go for a cup of coffee or go take a nap while you wait for the answer. But if you try it here in Code Wars you will most likely get a code timeout before any answers.

For this particular Kata we want to implement the memoization solution. This will be cool because it will let us keep using the tree recursion algorithm while still keeping it sufficiently optimized to get an answer very rapidly.

The trick of the memoized version is that we will keep a cache data structure (most likely an associative array) where we will store the Fibonacci numbers as we calculate them. When a Fibonacci number is calculated, we first look it up in the cache, if it's not there, we calculate it and put it in the cache, otherwise we returned the cached number.

Refactor the function into a recursive Fibonacci function that using a memoized data structure avoids the deficiencies of tree recursion. Can you make it so the memoization cache is private to this function?
"""
cache = {}


def fibonacci(n):
    print(cache)
    if n in [0, 1]:
        return n
    result = cache
    if n in cache:
        return cache[n]
    result = fibonacci(n - 1) + fibonacci(n - 2)
    cache[n] = result
    return result


# def fibonacci(n):
#     if n in [0, 1]:
#         return n
#     nums = [0, 1]
#     for x in range(n):
#         nums = [nums[1], nums[0]+nums[1]]
#     return nums[0]


print(fibonacci(70))
print(fibonacci(60))
print(fibonacci(50))
print(fibonacci(100000))
print(fibonacci(1000000))
