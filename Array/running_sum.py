nums =list(map(int,input("Enter array elements : ").split()))

for i in range(1,len(nums)):
    nums[i]=nums[i-1]+nums[i]

print("running sum: ", nums)
