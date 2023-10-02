# Implementation of Travelling Salesman Problem's Solution or Job Sequencing

def job_seq(jobs,t):
    
    for i in range(1,len(jobs)):
        key = jobs[i]
        j = i-1
        while j>=0 and key[2]>jobs[j][2]:
            jobs[j+1] = jobs[j]
            j = j-1
        jobs[j+1] = key
    
    res = [False]*t
    ans = []
    for i in range(len(jobs)):
        for j in range(min(t,jobs[i][1]-1),-1,-1):
            if res[j]==False:
                res[j] = True
                ans.append(jobs[i][0])
                break
    return ans

arr = [['a', 2, 100],  # Job Array
              ['b', 1, 19],
              ['c', 2, 27],
              ['d', 1, 25],
              ['e', 3, 15]]
print(job_seq(arr,3))