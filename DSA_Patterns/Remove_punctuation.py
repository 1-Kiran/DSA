# Example

# Input:
# Hello!!!, he said ---and went.

# Output:
# Hello he said and went

import string

sentence = input("Enter a sentence: ")

result = sentence.translate(
    str.maketrans("", "", string.punctuation)
)

print("String without punctuation:", result)