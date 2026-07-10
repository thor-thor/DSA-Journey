nums=[[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]
n=len(nums)
m=len(nums[0])
for i in range(n-1):
    for j in range(i+1,n):
        nums[i][j],nums[j][i]=nums[j][i],nums[i][j]
for i in range(n):
    nums[i].reverse()
print(nums)
