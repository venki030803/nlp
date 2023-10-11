import nltk
from nltk.tree import Tree
from nltk import word_tokenize, pos_tag

def generate_parse_tree(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)

    # Perform part-of-speech tagging on the words
    tagged_words = pos_tag(words)

    # Generate the parse tree
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(tagged_words)

    # Print the parse tree
    result.pretty_print()

# Example usage
generate_parse_tree("The quick brown fox jumps over the lazy dog.")
