def binary_search(arr, num1, num2):
    data = num1 + num2
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = int((start + end) // 2)
        if arr[mid] == data:
            return mid
        elif data > arr[mid]:
            start = mid + 1
        elif data < arr[mid]:
            end = mid - 1
        else:
            return None
        

