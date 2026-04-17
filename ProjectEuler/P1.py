s = set()

for i in range(1,1000): 
    if i % 3 == 0 or i % 5 ==0:
        s.add(i)
print(sum(s))
#233168
