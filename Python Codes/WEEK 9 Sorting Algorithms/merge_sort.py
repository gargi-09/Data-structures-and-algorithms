#Merge Sort Implementation

def merge(arr,low,mid,high):
    
    l = arr[low:mid+1]
    r = arr[mid+1:high+1]

    m = len(l)
    n = len(r)
    i,j,k = 0,0,low

    while i<m and j<n:
        if l[i]<=r[j]:
            arr[k] = l[i]
            i+=1
            k+=1
        elif l[i]>r[j]:
            arr[k] = r[j]
            j+=1
            k+=1
    while i<m:
        arr[k] = l[i]
        i+=1
        k+=1
    while j<n:
        arr[k] = r[j]
        j+=1
        k+=1



def merge_sort(arr,low,high):
    
    if low<high:

        mid = (low+high)//2
        print(arr)
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)

arr = [4,9,0,1,12,5]
low = 0
high = len(arr)-1
merge_sort(arr,low,high)
print(arr)
