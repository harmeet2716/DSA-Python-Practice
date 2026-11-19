class solution:
    def findmax(self,nums:list[int],k:int)->float:
        current =sum(nums[:k])
        maxsum=current
        
        for i in range(len(nums)):
            current += nums[i]-nums[i-k]
            maxsum=max(maxsum,current)
            
        return maxsum / k
    
    
nums=list(map(int,input("Enter the value with  : ").split()))
k =int(input("Enter the value of sub array: "))
obj=solution()

num=obj.findmax(nums,k)

print("updated Array : ",num)

