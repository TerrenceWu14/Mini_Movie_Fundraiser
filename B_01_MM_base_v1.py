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


# sets maximum number of tickets below
max_tickets = 3
tickets_sold = 0

want_instruction = yes_no("Do you want to read the instructions? ")

if want_instruction == "yes":
    print("Instructions go here")

print()

# loops to sell all tickets
while tickets_sold < max_tickets:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    tickets_sold += 1

# output number of tickets sold
if tickets_sold == max_tickets:
    print("Congratulations you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold}. "
          f"There is {max_tickets - tickets_sold} remaining")
