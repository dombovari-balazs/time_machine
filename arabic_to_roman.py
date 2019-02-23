def get_arabic():
    return 3974

def arabic_to_roman_9(number):
    if number == 0:
        return ""
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

def arabic_to_roman_900(number):
    if number == 100:
        return "C"
    if number == 200:
        return "CC"
    if number == 300:
        return "CCC"
    if number == 400:
        return "CD"
    if number == 500:
        return "D"
    if number == 600:
        return "DC"
    if number == 700:
        return "DCC"
    if number == 800:
        return "DCCC"
    if number == 900:
        return "CM"

def arabic_to_roman_3000(number):
    if number == 1000:
        return "M"
    if number == 2000:
        return "MM"
    if number == 3000:
        return "MMM"

def get_result_under_4000(number):
    arabic = ""
    if number >= 1000:
        number_1000 = number // 1000
        arabic += arabic_to_roman_3000(number_1000 * 1000)
        number -= number_1000 * 1000
    if number >= 100:
        number_100 = number // 100
        arabic += arabic_to_roman_900(number_100 * 100)
        number -= number_100 * 100
    if number >= 10:
        number_10 = number // 10
        arabic += arabic_to_roman_90(number_10 * 10)
        number -= number_10 * 10

    arabic += arabic_to_roman_9(number)
    return arabic


if __name__ == "__main__":
    print (get_result_under_4000(get_arabic()))
