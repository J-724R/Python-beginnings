sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)

wordsTable = [words,word_lengths]
print("\n Table \n")
print(wordsTable)


#! Using a list comprehension, we could simplify this process to this notation:
print("")
word_lengths = [len(word) for word in words if word != "the"]
print(word_lengths)
