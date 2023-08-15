"""
[NOTE] For some reason my understanding of how to calculate this is effed up
I'm going to move onto a different sequence and leave this one to solve later
Honestly it really SHOULD be simple
"""

from utils.Solution import Solution

N = 20
def logic() -> list:
    digits = [0]

    for n in range(1, N):
        tmp = digits[-1] - n
        print(digits)
        print("{} - {} = {}".format(digits[-1], n, tmp))
        if tmp > 0 and tmp not in digits:
            digits.append(n)
        else:
            digits.append(digits[-1] + n)

    return digits    # May omit for brevity

solution = Solution(N, "Recaman's Sequence")
solution.logic = logic
solution.run()
