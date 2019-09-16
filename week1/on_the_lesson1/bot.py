# dictionary = {}
#
# dictionary['first_name'] = "Sasha"
# dictionary['last_name'] = 'Ozerov'
# dictionary['age'] = 12
# dictionary['city'] = 'Moscow'
#
# for key, value in dictionary.items():
#     print(f'{key} : {value}')



# dictionary = {}
#
# dictionary['Kat'] = 12
# dictionary['Vova'] = 14
# dictionary['Sara'] = 23
# dictionary['Karolina'] = 44
#
# for name, num in dictionary.items():
#     print(name.lower() + ' likes number ' + str(num))

#
# dictionary = {}
#
# dictionary['Тикет'] = "Это такая штука, в которой пишем задание"
# dictionary['Дескрипшн'] = "Это описание к задаче"
#
# for k, v in dictionary.items():
#     print(k + "\n" + v + "\n")


favorite_languages = {
    'jen': 'python',
    'paul': 'c',
    'komi': 'php',
    'ki': 'haskel',
    'noi': '',
}

for name, language in favorite_languages.items():
    if language:
        print("Thx for your answer " + name.title() +
              " Now we know that your favorite language is " + language.title())
    else:
        favorite_languages[name] = input("What's your favorite language " + name.title() + "? ")
print(favorite_languages)


