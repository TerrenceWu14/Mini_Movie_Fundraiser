# Checks whether the user entered yes or no
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("you didn't choose a valid option (yes/no)")


# Main routine
while True:
    want_instruction = yes_no("Do you want to read the instructions? ")
    print(f"you chose {want_instruction}")