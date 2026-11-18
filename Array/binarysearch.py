import bisect

class solution:
    def search(self,nums:list[int],target:int)->int:
        
        i=bisect.bisect_left(nums,target)
        
        if i <len(nums)and nums[i]==target:
            return i
        return -1
    
nums = list(map(int,input("enter the sorted array: ").split()))

target =int(input("enter the target value : "))
obj =solution()

answer=obj.search(nums,target)
print("Target in which index " , answer)