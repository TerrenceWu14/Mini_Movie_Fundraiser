# main routine starts here

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


# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # if the response is blank, outputs the error
        if response == "":
            print("Sorry this can't be blank. Please try again")

        else:
            return response


# Checks that the user has entered an integer
def num_check(question):
    error = "Please choose an integer"

    # Checks that a number is higher or equal to 13
    while True:
        try:
            response = int(input(question))
            if response < 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)


# sets maximum number of tickets below
max_tickets = 3
tickets_sold = 0

want_instruction = yes_no("Do you want to read the instructions? ")

if want_instruction == "yes":
    print("Instructions go here")

print()

while tickets_sold < max_tickets:

    name = input("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("You are too young! You can't watch this movie")
        continue

    else:
        print("?? That looks like a typo, please try again")
        continue

    tickets_sold += 1

# output number of tickets sold
if tickets_sold == max_tickets:
    print("Congratulations you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold}. "
          f"There is {max_tickets - tickets_sold} remaining")
