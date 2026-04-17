from itertools import combinations
n = 100 
arr = range(1,n+1)
ans = 2*sum(a*b for a,b in combinations(arr,2)) 
print(ans)
