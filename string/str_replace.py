def replace_vowels(word):
    res = []
    vowels = 'aeiouAEIOU'
    for i in range(len(word)):
        if word[i] in vowels:
            res.append('1')
        else:
            res.append(word[i])
    return ''.join(res)

word = 'abcdefghijkmno'
print(replace_vowels(word))