import readFilm
import createFilm
import updateFilm
import deleteFilm
import time

# create a function for the songs menu


def menuOptions():
    options = 0

    # concept of iteration in Python: while loop

    while options not in ["1", "2", "3", "4", "5", "6"]:
        print(
            "Film Menu Options\nEnter:\n1. Print.\n2. Create.\n3. Update.\n4. Delete.\n5.Reports\n6.Exit")

        # re-assign value, a new value to the options variable
        options = input()
        # concept of selection

        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{options} is not a valid choice! from the films menu")

    return options


def reportsMenu():
    options = 0

    while options not in ["1", "2", "3", "4", "5", "6"]:
        print(
            "Film Reports Options\nEnter:\n1. Read.\n2. printByGenre.\n3. printByYear.\n4. printByRating.\n5. printByDuration.\n6 Exit")
        options = input("Enter an option from reports:")

        if options not in ["1", "2", "3", "4", "5", "6"]:
            print(f"{options} is not a valid choice! from the reports menu")
    return options


mainProgram = True  # assign mainProgram  a boolean True variable
while mainProgram:  # same as while true
    mainMenu = menuOptions()  # assign menuOption  function to the mainMenu variable
    if mainMenu == "1":
        readFilm.read()
    elif mainMenu == "2":
        createFilm.insertFilm()
    elif mainMenu == "3":
        updateFilm.update()
    elif mainMenu == "4":
        deleteFilm.delete()

    elif mainMenu == "5":
        reportProgram = True  # assign reportProgram  a boolean True variable

        while reportProgram:  # same as while true
            reportsMenuOption = reportsMenu()
            if reportsMenuOption == "1":
                readFilm.read()

            elif reportsMenuOption == "2":
                # genre = ""
                # genre = input("Enter a genre:")
                readFilm.printByGenre()

            elif reportsMenuOption == "3":
                # year = 0
                # year = input("Enter a year:")
                readFilm.printByYear()

            elif reportsMenuOption == "4":
                # rating = ""
                # rating = input("Enter a rating:")
                readFilm.printByRating()

            elif reportsMenuOption == "5":
                # rating = ""
                # rating = input("Enter a rating:")
                readFilm.printByDuration()

            else:
                # assign reportProgram  a boolean False variable to exit the while loop
                reportProgram = False
                # sleep 2 second to allow the program to run again
                time.sleep(2)
                input("Press enter to exit")

            # press enter to exit the application
    else:
        mainProgram = False  # assign mainProgram  a boolean False variable to exit the while loop
        time.sleep(2)  # sleep 2 second to allow the program to run again
        input("Press enter to exit")

# sys = input("Press enter to exit the program")
# sys.exit()  # exit the program
