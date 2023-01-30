
# Allow the user to input the sequence.
input_sequence  = input("Enter the input sequence as words seperated by a hyphen: ")

# Make a list of the words in the input sequence.
list_sequence = input_sequence.split("-")

# Sort the words in the list.
list_sequence.sort()

# Join the words in the list with a hyphen.
output_sequence = "-".join(list_sequence)

# Print the output sequence.
print(output_sequence)
