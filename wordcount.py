# put your code here.
# open file (don't forget close)
# iteratre by line
# strip, split
# iterate over that list
# do the .get method demonstrated in lecture

def word_counter(file_path):
    file = open(file_path)

    counted_words = {}
    for line in file:
        line = line.rstrip()
        word_list = line.split()

        for word in word_list:
            counted_words[word] = counted_words.get(word, 0) + 1
    return counted_words

    file.close()

result = word_counter("twain.txt")
for word, count in result.items():
    print "{} {}".format(word, count)
