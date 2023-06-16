def binary_search(arr, data):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end) // 2)
        if arr[mid] == data:
            return mid
        elif data < arr[mid]:
            end = mid - 1
        elif data > arr[mid]:
            start = mid + 1
        else:
            return -1
        
arr = ['a','b','c','','e']
data = 'a'
print(f'The string {data} is at position {binary_search(arr, data)}')

