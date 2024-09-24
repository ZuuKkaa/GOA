def stray(arr):
    unique_elements = set(arr)
    if len(unique_elements) != 2:
        raise ValueError("Input array.")
    unique_list = list(unique_elements)
    if arr.count(unique_list[0]) == 1:
        return unique_list[0]
    else:
        return unique_list[1]
    