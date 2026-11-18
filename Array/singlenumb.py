nums=list(map(int ,input("enter the value : ").split()))
for num in nums:
    if nums.count(num)==1:
        print(num)