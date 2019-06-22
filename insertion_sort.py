'''Insertion Sort'''
arr=[]
n=int(input("Enter size of array: "))
print("Enter Elements:")
for i in range(n):
    ele=int(input())
    arr.append(ele)

for i in range(1,n):
    key=arr[i]
    j=i-1
    while(j>=0 and arr[j]>key):
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key

print("Sorted array: ",arr)
