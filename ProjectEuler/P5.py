def gcd(a:int, b : int) -> int: 
    while b: 
        a, b = b, a % b 
    return a 
def lcm(a:int, b: int) -> int:
    return abs(a * b) // gcd(a, b)
def lcmm(*args): 
    return reduce(lcm, args)
b = list(range(1, 21))
print(lcmm(*b))
