num=list(map(int,input("Enter the values : ").split()))

has_duplicate=False
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[j]==num[i]:
            has_duplicate=True
            break
    if has_duplicate:
        break
print("Contain Duplicate: ",has_duplicate)
