nums=[5,6,9,8,1,5,4,7,6,3,0,1,-1,-2,-3,-4,10,15]
largest=nums[0]
smallest=nums[0]
for num in nums:
    if num>largest:
        smallest=largest
        largest=num
    elif num>smallest and num<largest:
        smallest=num
print('Second Largest: ',smallest)
