# A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become . Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

# Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

# Function Description

# Complete the function rotLeft in the editor below.

# rotLeft has the following parameter(s):

# int a[n]: the array to rotate
# int d: the number of rotations
# Returns

# int a'[n]: the rotated array



# solutuon
def left_rotate(a):
    if len(a) == 0:
        return a
    first_element = a[0]  # Get the first element
    for i in range(len(a) - 1):
        a[i] = a[i + 1]  # Shift each element to the left
    a[-1] = first_element  # Place the first element at the end
    return a