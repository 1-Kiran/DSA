num=135
val=num
l=len(str(num))
sum=0
while val>0:
    one=val%10
    sum+=one**(l)
    l-=1
    val=val//10
if sum==num:
    print("Disarium number")


# A Disarium number is a number equal to the sum of its digits raised to their respective positions.

# Positions start from 1.

# Example
# 89 = 8¹ + 9²
#    = 8 + 81
#    = 89

#Print All Disarium Numbers from 1 to 100
# n=100
# for i in range(1,n+1):
#     num=i
#     val=num
#     l=len(str(num))
#     sum=0
#     while val>0:
#         one=val%10
#         sum+=one**(l)
#         l-=1
#         val=val//10
#     if sum==num:
#         print("Disarium number",sum)