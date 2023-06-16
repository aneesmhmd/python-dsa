def linear_search(arr, letter):
    if letter in arr:
        size = len(arr)
        pos = [c+1 for c in range(size) if arr[c] == letter]
        return pos
    return None


word = 'aneesk'
letter = 'e'
print(linear_search(word, letter))