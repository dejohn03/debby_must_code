def reverse_words(sentence):
    return " ".join([word[::-1] for word in sentence.split()])def reverse_words(sentence):


def reverse_words(sentence):
    reverse_words_list = []
    words = sentence.split()
    for word in words:
        reverse_words_list.append(word[::-1])
    rev_sentence = " ".join(reverse_words_list)
    return rev_sentence

print(reverse_words("Divine is a girl"))