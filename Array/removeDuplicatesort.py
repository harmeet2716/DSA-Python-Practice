nums=list(map(int,input("Enter the numbers : ").split()))
unique=sorted(set(nums))

nums[:]=unique
print("Updated arry : ",nums)
print("Number of the unique elements :  ",len(nums))
