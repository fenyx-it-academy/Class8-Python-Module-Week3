
def hyphen_sort (words) :


    list = words.split ("-") # split by the hyphen
    list =sorted(list) 

    final = '-'.join(list) #making sorted string
    return (final)


words =  input('enter the words: ')
words = hyphen_sort (words)

print (words)