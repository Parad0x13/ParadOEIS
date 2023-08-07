# This is used for mathematic functions that are not solutions themselves, but may aid in several solutions

# I would rather not use a python optimization and stick with a pure mathematical one
# Reference from: https://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def sum_digits_squared(n):
    s = 0
    while n:
        s += (n % 10)*(n % 10)
        n //= 10
    return s
