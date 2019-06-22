def merge(l1,h1,l2,h2,n,arr):
    i = l1
    j = l2
    A=[0]*(h2-l1+1)
    for k in range(h2-l1):
        if(arr[i] <= arr[j]):
            A[k] = arr[i]
            i = i+1
        elif(arr[j]<arr[i]):
            A[k] = arr[j]
            j = j+1
    arr=A
    
def mergeSort(low,high,n,arr):
    if(low<high):
        m= (low+high)/2
        mergeSort(low,m,n,arr)
        mergeSort(m+1,high,n,arr)
        merge(low,m,m+1,high,n,arr)
        

##n=int(input("Enter size of array: "))
##arr=[0]*n
##print("Enter elements: ")
##for i in range(n):
##    arr[i] = int(input())
arr=[1,2,3,4,5]
mergeSort(0,4,5,arr)
print(arr)
        
