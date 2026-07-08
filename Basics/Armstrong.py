n=153
num=n
total=0
nod=len(str(n))
while num>0:
    id=num%10
    total=total+(id**nod)
    num//=10
if total==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")