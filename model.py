def most_frequent_word(word_dict):
    most_freq_word = ""
    freq = 0
    for word in word_dict:
        if word_dict[word] > freq:
            most_freq_word = word
            freq = word_dict[word]
    return most_freq_word


def create_dictionary(lemmatized_sentences, sentences):
    # Dumb model 2 -> use the most frequent word for lemma translation
    lemma_to_word = {}
    for lemma_sentence, word_sentence in zip(lemmatized_sentences, sentences):
        for lemma, word in zip(lemma_sentence.split(), word_sentence.split()):
            if lemma not in lemma_to_word:
                lemma_to_word[lemma] = {word: 1} # add lemma
            elif word not in lemma_to_word[lemma]:
                lemma_to_word[lemma][word] = 1 # add word
            else:
                lemma_to_word[lemma][word] += 1 # add frequency
    for lemma in lemma_to_word:
        lemma_to_word[lemma] = most_frequent_word(lemma_to_word[lemma])
    return lemma_to_word


def dictionary_model(lemmatized_sentences, sentences):
    lemma_to_word = create_dictionary(lemmatized_sentences, sentences)
    y = []
    for sentence in lemmatized_sentences:
        result_sentence = ""
        for lemma_word in sentence.split():
            result_word = ""
            if lemma_word in lemma_to_word:
                result_word = lemma_to_word[lemma_word]
            else:
                result_word = lemma_word
            result_sentence = result_sentence + result_word + " "
        # print(result_sentence)
        y.append(result_sentence.strip())
    return y

