
def get_magic_dict():
    magic_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return magic_dict

def rule_one(incoming_roman_string):
    solution = 0
    thingie = get_magic_dict()
    mode = 'basic'
    for i, character in enumerate(incoming_roman_string):
        if mode == 'basic':
            solution += thingie[incoming_roman_string[i]]
            try:
                if incoming_roman_string[i + 1] <= incoming_roman_string[i]:
                    mode = 'basic'
            except:
                print("End of ize")
    return solution


if __name__ == "__main__":
    roman_number = "MMMCCV"
    print (rule_one(roman_number))





