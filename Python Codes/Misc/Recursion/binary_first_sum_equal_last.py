# Given an integer N return all binary number sequences such that the sum of first half of that number is equal to the second half and its length is 2N.

binary = []

def equal_sum(val):
    mid = len(val)//2
    left = val[:mid]
    right = val[mid:]

    sum_1,sum_2 = 0,0
    for l in left:
        sum_1+=int(l)
    for r in right:
        sum_2+=int(r)
    if sum_1==sum_2:
        return True
    return False

def bin_seq(s,n,prefix,l):
    if n==0:
        if equal_sum(prefix):
            binary.append(prefix)
        return
    
    for i in range(l):
        new = prefix+s[i]
        bin_seq(s,n-1,new,l)

N = 4
out = [0 for _ in range(N)]
def bin_seq_2(diff,start,end):
    if diff>(end-start+1)//2:
        return
    if start>end:
        if diff==0:
            return "".join(out)
        return
    out[start] = '0'
    out[end] = '1'
    bin_seq_2(diff+1,start+1,end-1)

    out[start]=out[end]='1'
    bin_seq_2(diff,start+1,end-1)
    
    out[start]=out[end]='0'
    bin_seq_2(diff,start+1,end-1)

    out[start]='1'
    out[end] = '1'
    bin_seq_2(diff-1,start+1,end-1)

bin_seq(('0','1'),4,"",2)
# i=0
# while i<len(binary):
#     if not equal_sum(binary[i]):
#         binary.pop(i)
#         continue
#     i+=1
print(binary)
bin_seq_2(0,0,N-1)



