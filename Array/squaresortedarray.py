class solution:
    def calculateSquare(self,nums:list[int])->list[int]:
        result=[num**2 for num in nums]
        return sorted(result)
    
    
nums=list(map(int,input("Enter the value : ").split()))
square =solution()

ans=square.calculateSquare(nums)

print("output ",ans)
