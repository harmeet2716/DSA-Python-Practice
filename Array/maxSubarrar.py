nums=list(map(int,input("Enter the values : ").split()))

maxsum=nums[0]
current=nums[0]
for i in range(1,len(nums)):
    current=max(nums[i],current+nums[i])
    
    maxsum=max(maxsum,current)
    
    
print(maxsum)