import math

print("Welcome to compute area of circle program")
while True:
    try:
        radious = input("Enter the radious of circle (or 'q' if you want to close the program): ")

        if radious == 'q':
            break

        radious = float(radious)
        print("The area of circle with {} m = {} m^2".format(radious, ((math.pi) * (radious**2))))
    except:
        print("Invlid radious please enter valid number or 'q' to quit the program")