nums=list(map(int ,input("Enter the value : ").split()))

n=len(nums)
exepted=n*(n+1)//2
actual=sum(nums)
print(exepted-actual)