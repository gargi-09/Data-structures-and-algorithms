#Radix Sort Implementation

def counting_sort(arr,exp):
    mx = max(arr)
    count = [0]*(mx+1)

    for i in range(len(arr)):
        index = arr[i]//exp
        count[index%10] +=1
    
    for i in range(len(count)):
        count[i]+=count[i-1]
    
    pos = [0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        index = arr[i]//exp
        pos[count[index%10]-1] = arr[i]
        count[index%10]-=1
    
    for i in range(len(arr)):
        arr[i] = pos[i]

def radix_sort(arr):
    mx = max(arr)

    exp = 1
    while mx/exp>=1:
        counting_sort(arr,exp)
        exp = exp*10

arr = [170,45,75,90,802,24,2,66]
radix_sort(arr)
print(arr)