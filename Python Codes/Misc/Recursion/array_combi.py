# Print all the possible combinations of r elements from the given array of size n

res = []
curr = []
def combine(arr,r,ind):
    if r==0:
        res.append(curr[:])
        return
    
    for i in range(ind,len(arr)):
        curr.append(arr[i])
        combine(arr,r-1,i+1)
        curr.pop()

arr=[1,2,3,4]
r=2
combine(arr,r,0)
print(res)
while res:
    res.pop()
n = 3
k = 2
arr_1 = [i for i in range(1,n+1)]
combine(arr_1,k,0)
print(res)

# res_1 = curr_1 = []
# def combine_1(n,k,ind):
#     if k==0:
#         res_1.append(curr[:])
#         return
    
#     for i in range(ind,n):
#         curr_1.append(i)
#         print(curr_1)
#         combine_1(n,k-1,i+1)
#         curr_1.pop()
#         print(-1,curr_1)
# k = 2
# n = 3
# combine_1(n+1,k,1)
# print(res_1)