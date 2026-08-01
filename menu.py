class Menu:
    def displayMenu(self):
        print("\n" + "=" *50)
        print("  Ai Students Performnance Analyzer")
        print("="*50)
        print("1. Show all students ")
        print("2. Search student by id")
        print ("3. Search student by name")
        print ("4. Show Toper student")
        print ("5. Show Failed Student")
        print ("6. Show Passed Student")
        print("7. Show Statistics Class")
        print("8. Add the Student")
        print("9. Update the Student")
        print("10. Delete the Student")
        print ("11. exit")
        print("="*50)
        choice = int(input("Please enter your choice"))
        return choice;