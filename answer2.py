def sort_hyphen_phrase(phrase):
    """
    This function accepts a hyphen-separated
    sequence of words as input and prints 
    the words in a hyphen-separated sequence after 
    sorting them alphabetically
    """
    splitted_phrase = phrase.split('-')      # split '-' words
    sorted_phrase = sorted(splitted_phrase)  # sort all words
    output = '-'.join(sorted_phrase)         # join words agian and seperate them by '-'
    print(output)


sort_hyphen_phrase('green-red-yellow-black-white')