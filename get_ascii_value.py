def get_ascii_value(char):
    if len(char) == 1:
        ascii_value = ord(char)
        print(f"The ASCII value of '{char}' is {ascii_value}")
    else:
        print("Please enter a single character.")

if __name__ == "__main__":
    user_input = input("Enter a character: ")
    get_ascii_value(user_input)