# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print("-------------------")

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count("a"))
print("-------------------")


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
for letter in word.lower():
    if letter in ['а', 'е']:
        count += 1
print(count)
print("-------------------")


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split()))
print("-------------------")


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split():
    print(word[0])
print("-------------------")



# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'  #FIXME нужно поделить длину слова на количество слов
for word in sentence.split():
    print(len(word)/len(sentence.split()))
