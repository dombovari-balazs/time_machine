def arabic_to_roman_9_dict(number):
    roman_numbers = {
        0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
        6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
    return roman_numbers[number]



def arabic_to_roman_90_dict(number):
    roman_numbers = {
        10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L",
        60: "LX", 70: "LXX", 80: "LXXX", 90: "XC"}
    return roman_numbers[number]


def arabic_to_roman_900_dict(number):
    roman_numbers = {
        100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D",
        600: "DC", 700: "DCC", 800: "DCCC", 900: "CM"}
    return roman_numbers[number]



def arabic_to_roman_3000_dict(number):
    roman_numbers = {
        1000: "M", 2000: "MM", 3000: "MMM"}
    return roman_numbers[number]



def get_result_under_4000(number):
    arabic = ""
    if number >= 1000:
        number_1000 = number // 1000
        arabic += arabic_to_roman_3000_dict(number_1000 * 1000)
        number -= number_1000 * 1000
    if number >= 100:
        number_100 = number // 100
        arabic += arabic_to_roman_900_dict(number_100 * 100)
        number -= number_100 * 100
    if number >= 10:
        number_10 = number // 10
        arabic += arabic_to_roman_90_dict(number_10 * 10)
        number -= number_10 * 10

    arabic += arabic_to_roman_9_dict(number)
    return arabic
