def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers a and b
    using the Euclidean algorithm (recursive, no loops).
    """
    # validate input types
    if not isinstance(a, int) or not isinstance(b, int):
        print("Error: gcd(a, b) requires both inputs to be integers.")
        return None

    # gcd(0, 0) is undefined
    if a == 0 and b == 0:
        print("Error: gcd(0, 0) is undefined.")
        return None

    # make non-negative
    a = abs(a)
    b = abs(b)

    # base case
    if b == 0:
        return a

    # recursive step
    return gcd(b, a % b)


# basic tests
print(gcd(54, 24))   # 6
print(gcd(48, 18))   # 6
print(gcd(101, 10))  # 1

# edge cases
print(gcd(-54, 24))  # 6
print(gcd(0, 5))     # 5
print(gcd(5, 0))     # 5
print(gcd(0, 0))     # None (prints error)