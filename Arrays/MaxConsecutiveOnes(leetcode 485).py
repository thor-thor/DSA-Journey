nums=[0,1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0]
count=0
maxCount=0
for i in range(len(nums)):
    if nums[i]==1:
        count+=1
        if count>maxCount:
            maxCount=count
    else:
        count=0
print(maxCount)