def read_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines() # returns a list with the lines
    phone_numbers = remove_newline(lines)  # Calling remove_lines function
    return phone_numbers

def remove_newline(lines):
    result = []
    for number in lines:
        last_char = len(number) - 1
        new_number = number[0: last_char]
        result.append(new_number)

    return result




def main():
    ph_numbers = read_file("phone.txt")
    three_digits = input('Type first 3 digits: ')
    for number in ph_numbers:
        if number[3: 6] == three_digits:
            print(number)





main()