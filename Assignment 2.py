words = input('Please enter words: ')
def sorted_words(words):
     
    words_list = sorted(words.split('-'))
    words_list = '-'.join(words_list)
    print(words_list)
     
sorted_words(words)