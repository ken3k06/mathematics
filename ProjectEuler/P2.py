from functools import lru_cache 
@lru_cache(None) 
def even_fibo(n): 
    if n == 0: 
        return 2
    if n == 1: 
        return 8 
    return 4 * even_fibo(n-1) + even_fibo(n-2)
even_sum = 0 
i = 0 
while True:
    even = even_fibo(i)
    if even > 4000000: 
        break
    even_sum += even
    i += 1
print(even_sum)
