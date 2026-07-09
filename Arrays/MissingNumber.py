nums=[0,1,2,3,5,6,7,8]
n=len(nums)
expected=(n*(n+1))//2
actual=0
for i in range(n):
    actual+=nums[i]
missing=expected-actual
print(missing)