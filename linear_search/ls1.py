def linear_search(arr, val):
    if val in arr:
        size = len(arr)
        c = [c+1 for c in range(size) if arr[c] == val]
        return c
    return None


arr = [1, 2, 3, 4, 4, 5]
pos = linear_search(arr, 4)
print(pos)
