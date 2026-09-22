# A Happy number is a number that eventually becomes 1 when we repeatedly replace it with the sum of the squares of its digits.

# Example: 19
# 19 → 1² + 9² = 82
# 82 → 8² + 2² = 68
# 68 → 6² + 8² = 100
# 100 → 1² + 0² + 0² = 1

# Therefore, 19 is a Happy number.

n=19
seen=set()
while n!=1 and n not in seen:
    seen.add(n)
    n=sum(int(num)**2 for num in str(n))
    if n==1:
        print("Happy number")
print(seen)


#Print All Happy Numbers from 1 to 100
# for i in range(1,101):
#     n=i
#     seen=set()
#     while n!=1 and n not in seen:
#         seen.add(n)
#         n=sum(int(num)**2 for num in str(n))
#         if n==1:
#             print("Happy number")