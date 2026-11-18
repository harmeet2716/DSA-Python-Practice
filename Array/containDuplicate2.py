class solution():
    def containduplicate(self,nums:list[int],k:int)-> bool:
        
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen:
                if i-seen[nums[i]]<=k:
                    return True
            seen[nums[i]]=i
            
        return False
    

nums=list(map(int,input("Enter the value of array : ").split()))
k=int(input("Enter the value : "))
obj=solution()
answ=obj.containduplicate(nums,k)
print("output : ",answ)
