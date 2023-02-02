text = input("Enter a text: ")

# creating an empty dictionary to store letter counts
letter_counts = {}

# For loop and iterate through each letter in the text
for letter in text:
    # ignore spaces and convert letter to lowercase
    if letter != ' ':
        letter = letter.lower()
        # if the letter is already in the dictionary, increase the counting
        if letter in letter_counts:
            letter_counts[letter] += 1
        # or else, add the letter to the dictionary with a count of 1
        else:
            letter_counts[letter] = 1

# items() for getting the elemnets as pairs, sort() for getting the alphabetic order
letter_counts_list = list(letter_counts.items())
letter_counts_list.sort()
print(letter_counts_list)
