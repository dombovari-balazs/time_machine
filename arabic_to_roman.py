def get_arabic():
    return 79

def arabic_to_roman_9(number):
    if number == 1:
        return "I"
    if number == 2:
        return "II"
    if number == 3:
        return "III"
    if number == 4:
        return "IV"
    if number == 5:
        return "V"
    if number == 6:
        return "VI"
    if number == 7:
        return "VII"
    if number == 8:
        return "VIII"
    if number == 9:
        return "IX"

def arabic_to_roman_90(number):
    if number == 10:
        return "X"
    if number == 20:
        return "XX"
    if number == 30:
        return "XXX"
    if number == 40:
        return "XL"
    if number == 50:
        return "L"
    if number == 60:
        return "LX"
    if number == 70:
        return "LXX"
    if number == 80:
        return "LXXX"
    if number == 90:
        return "XC"


def get_result_under_100(number):
    arabic = ""
    number_10 = number // 10
    arabic += arabic_to_roman_90(number_10 *10)
    number -= number_10 *10
    arabic += arabic_to_roman_9(number)
    return arabic


if __name__ == "__main__":
    print (get_result_under_100(get_arabic()))
