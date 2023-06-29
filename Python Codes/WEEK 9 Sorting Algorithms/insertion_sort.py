#Insertion Sorting Implementation

def insertion_sort(arr):
    
    for i in range(1,len(arr)):

        key = arr[i]

        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        
        arr[j+1] = key

arr=[8,3,10,2,5,0]

insertion_sort(arr)

print(arr)