#SairajPulaparthi
#10/03/2023
#Numberic Conversion



#define the hex_char_decode and pass the digit through the function.
def hex_char_decode(digit):


    digit = digit.lower()
    if digit == "a" or digit =="A":
        return 10
    elif digit == "b"or digit == "B":
        return 11
    elif digit == "c" or digit == "C":
        return 12
    elif digit == "d" or digit == "D":
        return 13
    elif digit == "e" or digit == "E":
        return 14
    elif digit == "f" or digit =="F":
        return 15
    else:
        return int(digit)


#define hex string decode and pass the hex string through the function.

def hex_string_decode(hex_string):
    hex_string = hex_string.lower()
    deci_num = 0

    power = len(hex_string) - 1

    for digit in hex_string:
        deci_num += hex_char_decode(digit) * (16 ** power)
        power -= 1
    return deci_num

#define the binary string decode and pass the binarystr through the function.
def binary_string_decode(binary_str):
    deci_num = 0
    power = len(binary_str) - 1

    for bit in binary_str:
        if bit == '1':
            deci_num += 2 ** power
        power -= 1

    return deci_num

#define the binary to hex and pass the binary str through the function.
def binary_to_hex(binary_str):
    deci_num = binary_string_decode(binary_str)
    hex_chars = "0123456789abcdef"
    hex_string = ""
#start the while loop
    while deci_num > 0:
        remainder = deci_num % 16
        hex_string = hex_chars[remainder] + hex_string
        deci_num //= 16

    return  hex_string
#define the main
def main():
#have the while statement to repeat the menu
    while True:
        print("Decoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit")

        menu = input("Please enter an option: ")
#start the if statements
        if menu == '1':
            hexInput = input("Please enter the numeric string to convert: ")
            spliced = hexInput[2:]
            output = hex_string_decode(spliced)
            print(f"Result: {output}")

        elif menu == '2':
            binaryInput = input("Please enter the numeric string to convert: ")
            spliced = binaryInput[2:]
            output = binary_string_decode(spliced)
            print(f"Result: {output}")

        elif menu == '3':
            binaryInput = input("Please enter the numeric string to convert: ")
            spliced = output[2:]
            output = binary_to_hex(spliced)
            print(f"Result: {output}")

        elif menu == '4':
            print("Goodbye!")
            break
        else:
            print("Goodbye!")


if __name__ == "__main__":
    main()


##

    # keep = 1
    # data = []
    #
    # for i in range(1, len(flat_data)):
    #
    #     if flat_data[i] == flat_data[i-1]:
    #         keep +=1
    #         if keep >= 15:
    #             data.append(keep)
    #             data.append(flat_data[i-1])
    #             keep = 0
    #     else:
    #         data.append(keep)
    #         data.append(flat_data[i-1])
    #         keep = 1
    #
    # data.append(flat_data[-1])
    # data.append(keep)
    # return data
    # counter = 0
    # runs = 1
    # num = flat_data[0]
    # for i in flat_data[1:]:
    #     if i == num:
    #         counter += 1
    #     else:
    #         counter = 1
    #         runs += 1
    #         num = i
    #     if counter >= 15:
    #         runs += 1
    #         counter = 1
    # return runs