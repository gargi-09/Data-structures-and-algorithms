#Dutch National Flag Sorting Implementation

def dnf_sort(arr):
    low,mid,high = 0,0,len(arr)-1

    while mid<=high:

        if arr[mid] == 0:
            arr[low],arr[mid] = arr[mid],arr[low]
            low+=1
            mid+=1
        
        elif arr[mid] == 1:
            mid+=1
        
        else:
            arr[high],arr[mid] = arr[mid],arr[high]
            high-=1
            
    
arr = [0,1,1,2,2,0,0,1,2]
dnf_sort(arr)
print(arr)