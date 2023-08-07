from utils.Solution import Solution

N = 3000
def logic() -> list:
    digits = []

    for n in range(N):
        total = 1
        for x in range(1, n + 1):
            total *= x
        digits.append(total)

    #return digits    # Omitted for brevity

solution = Solution(N, "Factorial Numbers")
solution.logic = logic
solution.run()
