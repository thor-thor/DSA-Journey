def solve(n,sum,last,nums,k,ans):
    if sum==n and len(nums)==k:
        ans.append(list(nums))
        return
    if sum>n or len(nums)>k:
        return
    for i in range(last,10):
        nums.append(i)
        solve(n,sum+i,i+1,nums,k,ans)
        nums.pop()
def combinationSum(k,n):
    ans=[]
    nums=[]
    solve(n,0,1,nums,k,ans)
    return ans
print(combinationSum(3,8))