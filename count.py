sentence = input("Enter a sentence: ")
char_count = len(sentence)
word_count = len(sentence.split())
line_count = sentence.count('\n') + 1
print("Number of characters:", char_count)
print("Number of words:", word_count)
print("Number of lines:", line_count)