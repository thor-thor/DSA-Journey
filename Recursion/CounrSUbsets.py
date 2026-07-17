nums=[1,2,3,4,5]
result=[]
k=5
exist=False
count=0
def solve(index,total,subset):
    if total==k:
        result.append(subset[:])
        global exist,count
        exist=True
        count+=1
        return 
    elif total>k or index==len(nums):
        return 
    subset.append(nums[index])
    sum=total+nums[index]
    solve(index+1,sum,subset)
    e=subset.pop()
    sum-=e
    solve(index+1,sum,subset)
solve(0,0,[])
print(result)
print(count)
print(exist)