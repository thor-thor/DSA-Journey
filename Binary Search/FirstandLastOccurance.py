nums=[0,1,2,3,4,5,6,7,7,7,8,9]
target=7
def firstOccurance(nums,target):
    low=0
    n=len(nums)
    high=n-1
    first=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            first=mid
            high=mid-1
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return first
def lastOccurance(nums,target):
    low=0
    n=len(nums)
    high=n-1
    last=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            last=mid
            low=mid+1
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return last
print(firstOccurance(nums,target))
print(lastOccurance(nums,target))