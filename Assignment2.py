
# Assignment 2
''' this program accepts a hyphen-separated sequence of words as input and prints them
 after sorting them alphabetically '''

words = input(("Enter the words separated by a hyphen as a list: "))# asking to give the words in the sequence
words_list = words.split('-')                                        # put the words in a list
words_list.sort()                                                   # Sorting the words
result = '-'.join(words_list)                                       # Joining the words with a hyphen
print("the words after sorting them alphabetically: " + result)     # Printing the output
