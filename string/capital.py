def sent_capitalise(sentence:str):
    capitalised = ''
    for i in range(len(sentence)):
        if i == 0 or sentence[i-1] == ' ':
            capitalised += sentence[i].upper()
        else:
            capitalised += sentence[i]
    return capitalised


sent = " hello my name is anees"
res = sent_capitalise(sent)
print(res)