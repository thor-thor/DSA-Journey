def missingNumber(nums):
    res=len(nums)
    for i,x in enumerate(nums):
        res^=i^x
    return res
print(missingNumber([3,1,0,2,4,5,7]))