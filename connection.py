def get_numbers_from_file(file_name):

    with open(file_name, "r") as file:
        lines = file.readlines()
    numbers = [element.replace("\n", "") for element in lines]
    return numbers


def write_table_to_file(file_name, roman_numbers, arabic_numbers):

    with open(file_name, "w") as file:
        for i, record in enumerate(roman_numbers):
            file.write(record + "\n")


if __name__ == "__main__":
    print (get_numbers_from_file_for_testing('ROMAI.OUT'))
