nums1=list(map(int,input("Enter nums1 elements : ").split()))
m=int(input("Enter number of valid element of nums 1"))
nums2=list(map(int,input("Enter nums2 elements : ").split()))
n=int(input("Enter number of valid element of nums 2"))

nums1[m:]=nums2[:n]
nums1.sort()
unique=sorted(set(nums1))

print("Merge sorted array ", nums1)
print ("unique array : ",unique)