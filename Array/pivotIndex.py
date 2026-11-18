class solution():
    def povitindex(self,nums:list[int])->int:
        totalsum=sum(nums)
        left=0
        for i in range(len(nums)):
            right=totalsum-left-nums[i]
            
            if left == right:
                return i
            left=left+nums[i]
            
        return-1
    
nums=list(map(int,input("Enter the value of array : ").split()))
obj=solution()
answ=obj.povitindex(nums)
print("output : ",answ)
            