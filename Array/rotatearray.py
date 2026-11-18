class solution:
    def rotate(self,nums:list[int],k:int)->None:
        
        n=len(nums)
        k=k%n
        nums[:]=nums[-k:]+nums[:-k]
        

nums = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter rotation steps: "))

obj = solution()
obj.rotate(nums, k)

print("Rotated array:", nums)
