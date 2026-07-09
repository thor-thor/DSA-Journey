nums=[0,1,2,3,4,5,6]
n=len(nums)
isSorted=True
for i in range(0,n-1):
    if nums[i]>nums[i+1]:
        isSorted=False
print('Is Sorted: ',isSorted)