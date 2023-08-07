# Implement atoi() function both iteratively and recursively

# atoi() :  Takes a string that represents a number and returns its value.

def atoi_it(s,n):

    curr = []
    for c in s:
        curr.append(int(c))
    dig = 0
    for num in curr:
        dig+= num*10**(n-1)
        n-=1
    return dig

def atoi_rec(s,num):
    if len(s)==0:
        return 0
    if len(s)==1:
        return int(s)+num*10
    num = int(s[0:1])+num*10

    return atoi_rec(s[1:],num)

print(atoi_rec("112",0))

print(atoi_it("112",3))