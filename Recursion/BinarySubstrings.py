def solve(index,flag,numbers,result,count):
    if index==len(numbers):
        result.append("".join(numbers))
        count[0]+=1
        return
    numbers[index]="0"
    solve(index+1,True,numbers,result,count)
    if flag==True:
        numbers[index]='1'
        solve(index+1,False,numbers,result,count)
        numbers[index]='0'
def BinaryNumbers(n):
    numbers=['0']*n
    result=[]
    count=[0]
    solve(0,True,numbers,result,count)
    return result,count[0]
n=int(input("Enter: "))
print(BinaryNumbers(n))