import nltk
from nltk.tokenize import word_tokenize

text = "Tokenization is the process of breaking down text into words or sentences. It is an important step in natural language processing."

# Tokenize the text into words
words = word_tokenize(text)

# Perform part-of-speech tagging on the words
tags = nltk.pos_tag(words)

# Print the tagged words
print(tags)
