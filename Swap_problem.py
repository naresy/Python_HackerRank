def minimumSwaps(arr):
    count=0
    for i in range(len(arr)-1):
        for j in range (len(arr)-1):

            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                count+=1
        print(arr)
    return count
arry=[4,3,1,2]
output=minimumSwaps(arry)
print(output)