nums=[-1,0,1,2,3,4,5,6]
n=len(nums)
low=0
high=n-1
target=5
lb=-1
while low<=high:
    mid=(low+high)//2
    if nums[mid]>=target:
        lb=mid
        high=mid-1
    else:
        low=mid+1
print(lb)