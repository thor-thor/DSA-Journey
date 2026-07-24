nums=[1,2,3,1]
n=len(nums)
left=0
right=n-1
while left<right:
    mid=(left+right)//2
    if nums[mid]<nums[mid+1]:
        left=mid+1
    else:
        right=mid
print(left)