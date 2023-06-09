#Quick Sort Implementation
import random
def partition(arr,low,high):
    pivot = arr[high]
    i = low-1

    for j in range(low,high):

        if arr[j]<=pivot:
            i=i+1

            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]

    return i+1

def quick_sort(arr,low,high):
    if low<high:
        p = partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)

def partitionr(arr,low,high):
    ind = random.randint(low,high)
    arr[high],arr[ind] = arr[ind],arr[high]

    return partition(arr,low,high)

def randomized_quick_sort(arr,low,high):
    if low<high:
        p = partitionr(arr,low,high)

        randomized_quick_sort(arr,low,p-1)
        randomized_quick_sort(arr,p+1,high)

arr = [8,4,30,10,2,1,9]
low = 0
high = len(arr)-1

quick_sort(arr,low,high)
print(f"final : {arr}")
randomized_quick_sort(arr,low,high)
print(f"Random quick sort:{arr}")
