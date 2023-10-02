def hex_to_bin(hex_num):
    try:
        decimal_num = int(hex_num,16)
        binary_num = bin(decimal_num)

        print(f"The binary number of 0x{hex_num} is {binary_num}")
    except ValueError:
        print("Invalid hexadecimal number input!!")

if __name__ == "__main__":
    user_input = input("Enter hexadecimal number: ")
    hex_to_bin(user_input)