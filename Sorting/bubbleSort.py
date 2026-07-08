def bubbleSort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
nums=[6,4,5,2,1,9,7,8,6,2,3,0]
bubbleSort(nums)
print(nums)