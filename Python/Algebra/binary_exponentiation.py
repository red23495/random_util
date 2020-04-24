
def bin_pow(base, power):
    """
    Complexity: O(log n)
    Note: This function is only used to calculate exponetiation of
    integer base to positive integer power and will always return an integer value.
    """
    result = 1
    while power > 0:
        if power & 1:
            result *= base
        base *= base
        power //= 2
    return result