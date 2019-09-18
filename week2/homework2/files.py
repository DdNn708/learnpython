file_path = 'referat.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    text_from_file = f.read()

print(len(text_from_file))
print(len(text_from_file.split()))

with open('referat2.txt', 'w', encoding='utf-8') as f:
    for word in text_from_file.split():
        if "." in word:
            word = word.replace(".", "!")
        f.write(word + ' ')



