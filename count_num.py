#!/usr/bin/python3

def count_num(num, list):
    record = list.count(num)
    print("Number {} is existed in {} times.".format(num, record))
    return record

my_list = []

print(10*" ",10 * "-", "welcome to COUNT NUMBER IN LIST program", 10 * "-")
print("<-Start creating the list of numbers->")

while True:
    try:
        # recieve inputs from user
        num = input("Enter number wanted to be in the list (or 'q' to make it enough): ")

        # check if user wants to quit 
        if num.lower() == 'q':
            break
        
        # convert input into integer
        num = int(num)

        # append number to the list 
        my_list.append(num)

    except:
        print("Invalid input!! , Please enter a valid number or 'q' to quit.")

my_num = input("Enter the number that you want to count it's occurance in the list : ")
my_num = int(my_num)
record = count_num(my_num, my_list)
