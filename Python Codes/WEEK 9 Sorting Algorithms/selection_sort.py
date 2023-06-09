#Selection Sort Implementation

def selection_sort(arr):
    
    n = len(arr)

    for i in range(n):
        min_ind = i

        for j in range(i+1,n):

            if arr[j]<arr[min_ind]:
                min_ind = j

        arr[min_ind], arr[i] = arr[i], arr[min_ind]
    
arr=[10,7,8,1,0]
selection_sort(arr)
print(arr)