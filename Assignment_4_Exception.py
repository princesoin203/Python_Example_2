# Assignment 4 - Exception Handling
# Author - Prince Soin
# Student ID - u3229940
# Description - Comparing Airplanes using a shell based menu with exception handling.


# Functions
def fuel_1(l1):
    fuel1 = l1 * 0.6
    return fuel1


def fuel_2(l2):
    fuel2 = l2 * 0.8
    return fuel2


heading = "Airplane comparison menu"
option_a = "A: Choose option A to input values"
option_r = "R: Refresh the menu options"
option_b = "B: Choose to Exit"
enter = "Enter your choice:"


def printmenu():
    print()
    print(f"{heading.center(175)} \n")
    print(f"{option_a.center(135)} \n")
    print(f"{option_r.center(130)} \n")
    print(f"{option_b.center(120)} \n")
    print(f"{enter.center(120)} \n")


# Menu
printmenu()
choice = input()
while choice != "B":
    choice = input().upper()
    if choice == "R":
        printmenu()
    elif choice == "B":
        print("You chose to exit")
    elif choice == "A":
        print("Please enter your input values:")
        # User Inputs
        try:
            speed_1 = float(input("Enter the speed of Airplane 1"))
            speed_2 = float(input("Enter the speed of Airplane 2"))
            acceleration_1 = float(input("Enter the acceleration of Airplane 1"))
            acceleration_2 = float(input("Enter the acceleration of Airplane 2"))
        except ValueError:  # "ValueError", exception used to aviod the user typing an inapropriate value of the correct type. Ensures the user enters an appropriate value.
            print("Error: Did not enter a value. Please only enter a number.")
            print("Press R to refresh the menu, press B to exit or A to input values.")
        else:
            try:
                # Formulas
                length1 = (speed_1 * speed_1) / (2 * acceleration_1)
                length2 = (speed_2 * speed_2) / (2 * acceleration_2)
                seconds_Before_Takeoff_1 = 3 * length1
                seconds_Before_Takeoff_2 = 3 * length2
                # Read only files, stored within tuples
                my_file = open("airplane_price_2.txt", "r")
                content2 = my_file.read()
                my_file = open("airplane_price_1.txt", "r")
                content1 = my_file.read()
                # List of Specs
                AIRPLANE_1_SPECIFICATIONS = ["5669 kg (Weight), 12 meters (Length), 7 meters (Width)"]
                AIRPLANE_2_SPECIFICATIONS = ["5655 kg (Weight), 11 meters (Length), 9 meters (Width)"]
                # Tuple of airplane prices, read from files
                AIRPLANE_price = (content1, content2)
                # Main Code
            except ZeroDivisionError:  # "ZeroDivisionError", used to stop the user from entering 0 as a value as dividing by 0 will cause the program to raise an error.
                print("Do not enter 0 as an input")
                printmenu()
            except FileNotFoundError:  # ""ZeroDivisionError", used to inform the user that one of the required txt files have been deleted or removed from the root folder so the program cannot work.
                print("Could not find airplane price files. Please retry the program after adding in the price files.")
                printmenu()
            else:
                if length1 > length2:
                    for elements in AIRPLANE_2_SPECIFICATIONS:
                        print("Airplane 2 Specifications =", elements, AIRPLANE_price[1])
                        print("Airplane 2 requires the least amount of runway length, requiring", round(length2, 2),
                              "meters before the plane can take-off.")
                        print("Whereas Airplane 1 requires", round(length1, 2), "meters")
                        print("Airplane 2 will use,", round(fuel_2(l2=length2), 2), "liters of fuel during take-off")
                        print("And will take", round(seconds_Before_Takeoff_2, 2), "seconds to take-off \n")
                        print("Press R to return to the menu, or press B to exit.")


                        def main():
                            outfile = open("Airplane_2_Specifications_Fuel_Editable.txt", 'w')
                            CreateWithWritelines(outfile)


                        def CreateWithWritelines(outfile):
                            SPECIFICATIONS_Fuel = ["5655 kg (Weight)", "11 meters (Length)", "9 meters (Width)",
                                                   "Fuel Consumption:", str(round(fuel_2(l2=length2), 2))]
                            for i in range(len(SPECIFICATIONS_Fuel)):
                                SPECIFICATIONS_Fuel[i] = SPECIFICATIONS_Fuel[i] + "\n"
                            outfile.writelines(SPECIFICATIONS_Fuel)
                            outfile.close()


                        main()

                        break

                if length2 > length1:
                    for elements in AIRPLANE_1_SPECIFICATIONS:
                        print("Airplane 1 Specifications =", elements, AIRPLANE_price[0])
                        print("Airplane 1 requires the least amount of runway length, requiring", round(length1, 2),
                              "meters before the plane can take-off.")
                        print("Whereas Airplane 2 requires ", round(length2, 2), "meters")
                        print("Airplane 1 will use", round(fuel_1(l1=length1), 2), "liters of fuel during take-off")
                        print("And will take ", round(seconds_Before_Takeoff_1, 2), "seconds to take-off \n")
                        print("Press R to return to the menu, or press B to exit.")


                        def main():
                            outfile = open("Airplane_1_Specifications_Fuel_Editable.txt", 'w')
                            CreateWithWritelines(outfile)


                        def CreateWithWritelines(outfile):
                            SPECIFICATIONS_Fuel = ["5669 kg (Weight)", "12 meters (Length)", "7 meters (Width)",
                                                   "Fuel Consumption:", str(round(fuel_1(l1=length1), 2))]
                            for i in range(len(SPECIFICATIONS_Fuel)):
                                SPECIFICATIONS_Fuel[i] = SPECIFICATIONS_Fuel[i] + "\n"
                            outfile.writelines(SPECIFICATIONS_Fuel)
                            outfile.close()


                        main()

                        break

                if length1 == length2: # Used in case the user enters the same values for both planes. Avoids errors.
                    print("Airplane 1 length required =", length1)
                    print("Airplane 2 length required =", length2)
                    print("Both planes are the same")
                    printmenu()

    else:
        print("Invalid input")  # Used as invalid input control form the menu.
        printmenu()
