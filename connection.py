def read_input(filename):
    with open(filename, 'r') as file:
        file.read('Hi there!')


def get_table_from_file(file_name):
    """
    Reads csv file and returns it as a list of lists.
    Lines are rows columns are separated by ";"

    Args:
        file_name (str): name of file to read

    Returns:
         list: List of lists read from a file.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
    numbers = [element.replace("\n", "") for element in lines]
    return numbers


def write_table_to_file(file_name, roman_numbers, arabic_numbers):

    with open(file_name, "w") as file:
        for i, record in enumerate(roman_numbers):
            file.write(record + " " + str(arabic_numbers[i]) + "\n")
