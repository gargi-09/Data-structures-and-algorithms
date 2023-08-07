# Find if player 1 wins (players are not playing optimally)

res = []

def win(a,b,nums,flag):
            
    if len(nums)==0:
        res.append([a,b])
        return
            
    ind,m = 0,0
    if nums[0]>nums[-1]:
        ind = 0
        m = nums[0]
    else:
        ind = len(nums)-1
        m = nums[-1]
    nums.pop(ind)

    if flag:
        print(a,b)
        win(a+m,b,nums,False)

    else:
        print(a,b)
        win(a,b+m,nums,True)
        
win(0,0,[1,5,2],True)
print(res[0][0]>res[0][1])