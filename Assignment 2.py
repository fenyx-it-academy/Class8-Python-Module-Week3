def sort_words(words):
  words_list = words.split("-")
  words_list.sort()
  sorted_words = "-".join(words_list)
  return sorted_words

input_words = input("Enter a hyphen-separated sequence of words: ")
sorted_words = sort_words(input_words)
print("Sorted sequence:", sorted_words)
