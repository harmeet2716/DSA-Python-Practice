num=list(map(int,input("Enter the values : ").split()))
target=int(input("Enter the value to find : "))

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==target:
            print(i,j)