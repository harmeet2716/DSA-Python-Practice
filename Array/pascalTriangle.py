numrows=int(input("enter the no of rows : "))

new =[]

for i in range(numrows):
    curr=[1]
    
    if i >0:
        prev=new[i-1]
        
        for j in range(len(prev)-1):
            curr.append(prev[j]+prev[j+1])
            
        curr.append(1)
        
    new.append(curr)
print("\n Parscal Triangle ")
for row in new:
    print(row) 