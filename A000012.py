# 2023.08.13.0616.EST One of the more complicated patterns studied to date
# However with a much more improved understanding of mathematics and computer science
# I've been able to replicate OEIS' A000012 sequence "The Simply all 1's Sequence"
# I've also kept the N value rather low to accomidate the time-complexity of solving this sequence

from utils.Solution import Solution

N = 100
def logic() -> list:
    digits = []

    for n in range(N):
        digits.append(1)

    return digits    # May omit for brevity

solution = Solution(N, "A sequence of simply the value 1 continued forever")
solution.logic = logic
solution.run()
