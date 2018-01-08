# put your code here.
# open file (don't forget close)
# iteratre by line
# strip, split
# iterate over that list
# do the .get method demonstrated in lecture

def word_counter(file_path):
    # text_file = open(file_path)

    with open(file_path) as text_file:  # this is a context manager, this implementation is auto-close

        counted_words = {}
        for line in text_file:
            line = line.rstrip()
            # line = line.translate(None, string.punctuation)  # https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
            line = line.lower()
            word_list = line.split()

            for word in word_list:
                counted_words[word] = counted_words.get(word, 0) + 1

    return counted_words

    # text_file.close()

result = word_counter("test.txt")
for word, count in result.iteritems():
    print "{} {}" .format(word, count)
