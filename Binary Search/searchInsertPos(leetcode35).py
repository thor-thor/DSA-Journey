def insertPosition(nums,target):
    n=len(nums)
    low=0
    high=len(nums)-1
    ub=n
    lb=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return ub
nums=[0,2,4,6,8,10,12]
target=5
print(insertPosition(nums,target))