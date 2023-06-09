
    k=0

    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k+=1#Bucket Sort Implementation

def insertion_sort(arr):

    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

def bucket_sort(arr):
    bucket = []
    slot_num = 10

    for i in range(slot_num):
        bucket.append([])
    
    for i in arr:
        index = int(i*slot_num)
        bucket[index].append(i)

    for i in range(slot_num):
        bucket[i] = insertion_sort(bucket[i])
    
# def bucket_int_sort(arr,num_buckets):
#     min_ele = min(arr)
#     max_ele = max(arr)

#     rnge = (max_ele-min_ele)/num_buckets

#     buckets = []

#     for i in range(num_buckets):
#         buckets.append([])
    
#     for i in range(len(arr)):
        
#         diff = ((arr[i]-min_ele)/rnge) - (int(arr[i]-min_ele)/rnge)
#         print(arr[i],int((arr[i]-min_ele)/rnge),diff)
#         if diff==0 and arr[i]!=min_ele:
#             buckets[int((arr[i]-min_ele)/rnge)].append(arr[i])
        
#         else:
#             buckets[int((arr[i]-min_ele)/rnge)-1].append(arr[i])
    
#     for i in range(len(buckets)):
#         if len(buckets[i])!=0:
#             buckets[i] = insertion_sort(buckets[i])
    
#     i=0

#     for bucket in buckets:
#         if bucket:
#             for num in bucket:
#                 arr[i] = num
#                 i+=1

arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
bucket_sort(arr)
print(arr)
arr1 = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
