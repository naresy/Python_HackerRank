def left_rotate(a):
    if len(a) == 0:
        return a
    first_element = a[0]  # Get the first element
    for i in range(len(a) - 1):
        a[i] = a[i + 1]  # Shift each element to the left
    a[-1] = first_element  # Place the first element at the end
    return a