#xndir6 (Write a function that counts the number of words in a sentence)
def counts_the_number_of_words_in_a_sentence(m):
    x = m.split()
    return len(x)
y = counts_the_number_of_words_in_a_sentence("do you speak english?")
print(y)
