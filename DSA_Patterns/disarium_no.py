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
    print("OK")