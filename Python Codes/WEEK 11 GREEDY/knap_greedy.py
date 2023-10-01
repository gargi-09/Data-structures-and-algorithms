#Implementation of Greedy method on knapsack problem
def frac_knap(values,w):
    
    result = 0
    for i in range(1,len(values)):
        val = values[i]
        key = values[i][0]/values[i][1]
        j = i-1
        
        while j>=0 and key>values[j][0]/values[j][1]:
            values[j+1] = values[j]
            j = j-1
        values[j+1] = val
    
    for val in values:

        if val[1]<=w:
            w-=val[1]
            result+=val[0]
        else:
            result += val[0]*(w/val[1])
            w = 0
    return int(result)

values = [(100,40),(60,10),(120,60)]
print(frac_knap(values,50))
