# Honestly I feel like this is a cheat one since I'm using it in external code but meh, I think it applies anyways

from utils.Solution import Solution
from utils.Math import *

N = 200
def logic() -> list:
    digits = []

    for n in range(N):
        digits.append(sum_digits_squared(n))

    return digits    # May omit for brevity

solution = Solution(N, "Sum of squares of digits of n")
solution.logic = logic
solution.run()
