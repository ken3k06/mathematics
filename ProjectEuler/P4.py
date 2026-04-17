def check_palindrome(n): 
    return str(n) == str(n)[::-1]

largest_num = 0 

for i in range(1000):
    for j in range(1000): 
        num = i*j 
        if check_palindrome(num) and num > largest_num: 
            largest_num = num
print(largest_num)
