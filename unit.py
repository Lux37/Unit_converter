print("Hy! This is the program that converts kilometers into miles.")

while True:
    print("Please enter a number of kilometers that you'd like to convert into miles.")
    km = input("Kilometers: ")

    km = float(km.replace(",", "."))  # replace comma with dot, if user entered a comma

    # 1 Kilometre = 0.621371 Mile
    ratio = 0.621371

    # Converting km to mi.
    mi = km * ratio

    print("The entered value in Miles: ", mi)

    choice = input("Would you like to do another conversion (y/n): ")

    if choice.lower() != "y" and choice.lower() != "yes":
        break