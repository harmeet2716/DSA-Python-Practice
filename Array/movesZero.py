nums=list(map(int,input("Enter the value with Zeros : ").split()))

nonZero=[num for num in nums if num !=0]
zero_count=nums.count(0)

nums[:]=nonZero + [0] * zero_count

print("updated Array : ",nums)
