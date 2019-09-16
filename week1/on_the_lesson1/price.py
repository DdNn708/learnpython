def get_summ(one, two, delimiter='&'):
    # string_to_return = str(one + delimiter + two).upper()
    string_to_return = delimeter.join([str(one), str(two)]).upper()
    return string_to_return


def format_price(price):
    price = int(price)
    string_to_return = f"Цена: {price} руб."
    return string_to_return


string1 = "Learn"
string2 = "python"
delimeter = "-*-"


string3 = get_summ(string1, string2, delimiter=delimeter)
print(string3)

print(format_price(56.24))

