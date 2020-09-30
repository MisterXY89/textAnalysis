
def prepareText(sentences, forSentiment=True):
    preped_sentences = []
    preped_sentences_append = preped_sentences.append
    for i, sentence in enumerate(sentences):
        sentence = sentence.replace("\n", " ")
        if sentence.startswith(" "):
            sentence = sentence[1:]
        if forSentiment:
            sentence = sentence.replace("ß", "ss")
        if sentence != "" or sentence != " " or sentence != "\n" and sentence != None:
            preped_sentences_append(sentence)
        # printProgressBar(i + 1, len(sentences), prefix = 'Progress:', suffix = 'Complete', length = 50)
    return preped_sentences
