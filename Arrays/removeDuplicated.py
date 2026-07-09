nums=[0,1,2,3,4,5,6,7,8,9,8,7,5,6,4,1,2,0,0,2,4,2,1,5,6,3,8,7,9,3,3,0,1,4,5,9,8,7,7,1,5]
n=len(nums)
freq={}
for i in range(n):
    freq[nums[i]]=0
j=0
for k in freq:
    nums[j]=k
    j+=1
print(nums[:j])