# Find Minimum and maximum value in the array

def min_ele(arr,num):
    if len(arr)==0:
        print(num)
        return
    if arr[0]<num:
        num = arr[0]
    min_ele(arr[1:],num)

def max_ele(arr,num):
    if len(arr)==0:
        print(num)
        return
    if arr[0]>num:
        num = arr[0]
    max_ele(arr[1:],num)

arr = [20]
num = arr[0]
min_ele(arr,num)
max_ele(arr,num)