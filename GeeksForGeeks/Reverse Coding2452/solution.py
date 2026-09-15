n = int(input())

# Recursion Approach
# def sum_of_number(n):
    
#     if n == 0:
#         return 0
        
#     return n + sum_of_number(n-1)

# print(sum_of_number(n))
        
def sum_of_number(n):
    total = 0
    
    for i in range(n+1):
        total += i
        
    return total
    
print(sum_of_number(n))