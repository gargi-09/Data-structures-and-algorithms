# Print all the possible strings of length k that can be formed from a set of n character.

# Part 1: If all the characters are in a string and are to be printed in sequence.

def k_sub_it(s,k,n):
    i = 0
    j = i+k-1
    res = []
    while j!=n:
        res.append([s[i],s[j]])
        print("".join(res[0]))
        res.pop()
        i+=1
        j+=1
res = []
curr = []

def k_sub_rec(s,k,n,ind):
    if ind==n-1:
        res.append(curr[:])
        return
    
    t = ""
    for i in range(ind,n):
        t+=s[i]

        if len(t)==k:
            curr.append(t)
            k_sub_rec(s,k,n,i)
            curr.pop()


k_sub_it("abcd",2,4)
k_sub_rec("abcd",2,4,0)
print(res)

# Part 2: If k>=n

# def k_sub_it_2(s,k,n):
#     while k!=0:
#         for i in range(n):
#             prefix = ""

def k_sub_rec_2(s,k,res_2,n):
    if k==0:
        print(res_2)
        return
    
    for i in range(n):
        new = res_2+s[i]

        k_sub_rec_2(s,k-1,new,n)

s = ('a','b')
k_sub_rec_2(s,3,"",2)
