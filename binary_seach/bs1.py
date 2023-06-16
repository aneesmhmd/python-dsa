def binary_search(data, arr):
    start = 0
    end = len(arr) - 1
    if arr[0] == data:
            return 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == data:
            return mid
        if arr[mid] > data:
            end = mid - 1
        elif arr[mid] < data:
            start = mid + 1
    return None

nums = [1,2,3,4,5,6,7,8]
data = 1
res = binary_search(data, nums)

if res:
    print(f'{data} found in {res}th index')
else:
    print(data, ' not found')