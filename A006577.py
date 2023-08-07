from utils.Solution import Solution

# [NOTE] This never accounts for the intended value '-1' for when the conjecture fails
# There are obvious improvements that could be made like skipping even numbers, finding cycles etc...
# But for now here is a basic implementation
def collatz(n) -> int:
    steps = 1

    while True:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n+1

        if n == 1:
            break

        steps += 1

    return steps

N = 1000
def logic() -> list:
    digits = [0]

    offset = 2    # [NOTE] To be totally honest I do not really understand OEIS' offset calculation...

    for n in range(offset, N + 1):
        steps = collatz(n)
        digits.append(steps)

    print(len(digits))
    return digits    # May omit for brevity

solution = Solution(N, "Collatz Conjecture (3x+1)")
solution.logic = logic
solution.run()
