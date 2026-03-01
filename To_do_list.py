while True:
    user_input = input("do you want to add a new To-Do item? answer by \"y\" for yes and \"n\" for no. type 'exit' to quit: ").lower()

    if user_input == "exit":
        print("Thank you for using the To-Do program, come back again soon.")
        break

    elif user_input == "y":
        input_user_yes = input("Enter your new To-Do item: ")
        file = open("to_do.txt", "a", encoding="utf-8")
        file.write(input_user_yes + "\n")
        file.close()
        print("To-Do item added successfully!\n")

    elif user_input == "n":
        user_input_no = input("do you want to list your To-Do items ? answer \"y\" for yes and \"n\" for no: ").lower()

        if user_input_no == "y":
            try:
                file = open("to_do.txt", "r", encoding="utf-8")
                items = file.readlines() 
                file.close()

                if items:
                    print("\nYour To-Do List:")
                    for item in items:
                        print(item.strip())
                else:
                    print("Your To-Do list is empty.")

            except FileNotFoundError:
                print("No To-Do list found yet. Add some items first!")

        elif user_input_no == "n":
            print("Returning to main menu...\n")

        else:
            print("Invalid choice.\n")

    else:
        print("Invalid input.\n")