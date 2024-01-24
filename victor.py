import sys

# Define the options that the user can select.
options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Exit"]

# Get the user's selection.
while True:
    print("Please select an option:")
    for i, option in enumerate(options):
        print(f"{i + 1}: {option}")

    # Get the user's input.
    selection = input("Enter your selection: ")

    # Check if the user's selection is valid.
    if selection not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid selection. Please try again.")
        continue

    # Print the message corresponding to the user's selection.
    if selection == "1":
        print("You selected Option 1.")
    elif selection == "2":
        print("You selected Option 2.")
    elif selection == "3":
        print("You selected Option 3.")
    elif selection == "4":
        print("You selected Option 4.")
    elif selection == "5":
        print("You selected Option 5.")
    elif selection == "6":
        print("You selected Exit. Goodbye.")
        sys.exit()

    # Ask the user to select again.
    print("Would you like to select another option? (Y/N)")
    if input() == "Y":
        continue
    else:
        print("Goodbye.")
        sys.exit()