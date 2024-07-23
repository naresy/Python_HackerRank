def minimumSwaps(arr):
    n=len(arr)
    arrpos=list(enumerate(arr))
    arrpos.sort(key=lambda it: it[1])
    visited={k:False for k in range(n) }
    count=0
    for i in range(n):
        if visited[i]or arrpos[i][0]==i:
            continue
        cyclic_size=0
        j=i
        while not visited[j]:
            visited[j]=True
            j=arrpos[j][0]
            cyclic_size+=1
        if cyclic_size>0:
            count+=cyclic_size-1
    return count
arr=[4,3,1,2]
output=minimumSwaps(arr)
print(output)    