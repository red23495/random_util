def mod_pow(base, power, mod=None):
    """
    Implements divide and conquere binary exponetiation algorithm
    Complexity: O(log power) 
    source: https://cp-algorithms.com/algebra/binary-exp.html
    Params:
    @base: base number which needs to be multiplied
    @power: power to which base should be raised
    @mod: modulas with which number should be mod'ed
    returns: (base^power)%mod
    """
    if mod:
        base %= mod
    result = 1
    while power > 0:
        if power & 1:
            result *= base
            if mod:
                result %= mod
        base *= base
        if mod:
            base %= mod
        power //= 2
    return result