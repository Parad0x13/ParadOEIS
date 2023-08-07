from utils.Solution import Solution

N = 100000
def logic() -> list:
    digits = [0, 1]

    for n in range(len(digits), N):
        digits.append(digits[-1] + digits[-2])

    #return digits    # Omitted for brevity

solution = Solution(N, "Fibonacci Sequence")
solution.logic = logic
solution.run()
