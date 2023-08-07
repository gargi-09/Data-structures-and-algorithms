# Print all the subarrays from two given arrays such that it is increases and alternating
res = []
def alternate(a,b,c,ina,inb,l,flag):
    if flag:
        if l:
            print(c[:l+1])
        
        for i in range(ina,len(a)):

            if not l:
                c[l] = a[i]
                alternate(a,b,c,i+1,inb,l,False)
            else:
                if a[i]>c[l]:
                    c[l+1] = a[i]
                    alternate(a,b,c,i+1,inb,l+1,False)
        
    else:
        for j in range(inb,len(b)):

            if b[j]>c[l]:
                c[l+1] = b[j]
                alternate(a,b,c,ina,j+1,l+1,True)

a = [10,15,25]
b = [1,5,20,30]
c = [0 for _ in range(len(a)+len(b)+1)]
alternate(a,b,c,0,0,0,True)

