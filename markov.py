# import sys


def make_chains(input_text):
    """Takes input text as string; returns dictionary of markov chains."""
    # input_text is a whole text file with lines
    # input_text.read() ??
    # input_text_in_list = input_text.split(" ")
    content_list = input_text.read().split()
    # content_list = [w.rstrip("?.,\n") for w in content_list]
    bigram_dict = {}
    
    for index in range(len(content_list) - 2):
        bigram_key = (content_list[index], content_list[index + 1])
        word_after_bigram_key = content_list[index + 2]

        if bigram_key not in bigram_dict:
            bigram_dict[bigram_key] = []
      
        bigram_dict[bigram_key].append(word_after_bigram_key)
        # list.append(value)


    # the new list created from words in input_text should be stored to a new variable
    return bigram_dict

    
# def make_text(chains):
#     """Takes dictionary of markov chains; returns random text."""

#     return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

#######################################################
# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text

x = open('green-eggs.txt')

# make_chains(x)

# input_text= """Hello this is natalie and mish.
# We are in class. 
# It is super hot today.
# I want air conditioning. """

