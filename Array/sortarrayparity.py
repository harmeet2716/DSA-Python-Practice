nums=list(map(int,input("Enter the the values of array : ").split()))

array=[]
even=[x for x in nums if x %2==0]
odd= [x for x in nums if x %2!=0]

array=even+odd
print(array)