def word_sorting(words):
    """a function that accepts a hyphen separated sequence of words 
    and return a sorted hyphen separated sequence of words"""
    words=words.split("-")
    words.sort()
    return "-".join(words)
words =input('Enter a hyphen separated sequence of words \n')
print(word_sorting(words))

# the program below I wrote at first, which works perfectly but not efficient.
# input_words = input('Enter words seperated by - \n')
# input_words=list(input_words.split('-'))
# sorted_words = sorted(list(input_words))
# for index, i in enumerate(sorted_words):
#     if index < len(sorted_words)-1:
#      print (i, end="-")
#     else:
#         print(i)
