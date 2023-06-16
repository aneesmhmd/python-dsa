def sum(arr):
    size = len(arr)
    if size == 0:
        return 0
    else:
        return arr[0] + sum (arr[1:])
    
arr = [1, 2, 3, 4, 5]
print(sum(arr))