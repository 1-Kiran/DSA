#   A Pronic number is the product of two consecutive integers.
#   P=n(n+1)

numbers=100
for i in range(1,numbers):
    n=i
    if n<=1:
        print(0)
    elif numbers<(n*(n-1)):
        break
    else:
        print((n)*(n-1))