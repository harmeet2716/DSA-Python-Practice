nums=list(map(int,input("Enter the value : ").split()))

for num in nums: 
    if nums.count(num)>len(nums)//2:
        print(num)
        break
    