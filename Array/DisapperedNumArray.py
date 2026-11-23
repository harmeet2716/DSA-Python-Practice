nums=list(map(int , input("enter the values in array").split()))

n=len(nums)
seen=set(nums)

for i in range(1,n+1):
    if i not in seen:
        print(i)