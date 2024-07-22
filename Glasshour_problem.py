def glasshourSum(arry):
    Final_sum=0
    for i in range(4):
        for j in range(4):
            sum=(arry[i][j]+arry[i][j+1]+arry[i][j+2]+arry[i+1][j+1]+arry[i+2][j]+arry[i+2][j+1]+arry[i+2][j+2])
            if(Final_sum<sum):
                Final_sum=sum
    return Final_sum
arry=[
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
output=glasshourSum(arry)
print(output)

