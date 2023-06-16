def linear_search(arr, num1, num2):
    sum = num1 + num2
    if sum in arr:
        pos = [c+1 for c in range(len(arr)) if arr[c] == sum]
        return pos
    return None


arr = [5, 3, 7, 4, 19, 43, 10]
print(linear_search(arr, 10, 9))
