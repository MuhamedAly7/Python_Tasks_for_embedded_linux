def count_vowl(input_string):
    # Set of vowl letter
    vowl_set = ("AEIOUaeiou")

    # vowl counter
    vowl_count = 0

    # iterate through the string letter to count the number of vowls
    for char in input_string:
        # check if character is vowl or not
        if char in vowl_set:
            vowl_count += 1

    return vowl_count


# Recieve string from the user
my_str = str(input("Enter your string letter please : "))
result = count_vowl(my_str)
print(f"Your string letter has {result} vowl characters")
    

    

