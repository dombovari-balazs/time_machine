
def get_roman_number_one():
    return "MMMCCV"

def get_roman_number_two():
    return "MCMXCIV"

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


def rule_two(incoming_roman_string):
    solution = 0
    thingie = get_magic_dict()
    number_to_remember = 0
    actual_character = ""
    for i, character in enumerate(incoming_roman_string):
        actual_character = incoming_roman_string[i]
        try:
            if thingie[incoming_roman_string[i + 1]] <= thingie[incoming_roman_string[i]]:
                solution += (thingie[incoming_roman_string[i]] - number_to_remember)
                number_to_remember = 0
            else:
                number_to_remember += thingie[incoming_roman_string[i]]

        except:
            print("End of ize")
    solution += (thingie[actual_character] - number_to_remember)
    return solution




if __name__ == "__main__":
    roman_number = "MMMCCV"
    print (rule_one(roman_number))
    print (rule_two(get_roman_number_two()))





