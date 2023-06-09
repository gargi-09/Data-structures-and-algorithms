#Count Sort Implementation

def count_sort(arr):
    mx = max(arr)
    count = [0]*(mx+1)

    for i in range(len(arr)):
        count[arr[i]] += 1
    
    for i in range(1,len(count)):
        count[i] = count[i]+count[i-1]
    
    
    print(count)
    i=len(arr)-1
    pos = [0]*(i+1)
    while i>=0:
        print(pos)
        pos[count[arr[i]]-1] = arr[i]
        count[arr[i]] -=1
        i-=1
    for i in range(len(pos)):
        arr[i] = pos[i]

arr = [1,4,1,2,7,5,2]
count_sort(arr)
print(arr)