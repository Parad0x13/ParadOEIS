# 2023.08.07.1008.EST
# (Hey, gotta start with something fun and simple right?)

from utils.Solution import Solution

N = 5000000
def logicA() -> list:
    digits = []

    for n in range(1, N + 1):
        digits.append(n)

    #return digits    # Omitted for brevity

solution = Solution(N, "The positive integers")
solution.logic = logicA
solution.run()

# [NOTE] Interesting that this seems to run slower on my machine. Guess python optimizes loops or something?
def logicB() -> list:
    digits = [1]

    n = 1
    while n < N:
        n += 1
        digits.append(n)

    #return digits    # Omitted for brevity

solution = Solution(N, "The positive integers")
solution.logic = logicB
solution.run()

# Obviously this runs slower, but hey why not try it out!
def logicC() -> list:
    digits = [1]

    n = 1
    while n < N:
        n += 1
        digits.append(str(n))

    #return digits    # Omitted for brevity

solution = Solution(N, "The positive integers")
solution.logic = logicC
solution.run()
