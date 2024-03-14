# functions

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


# calculate the ticket price based on the age
def calc_ticket_price(var_age):
    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket price is $6.5 for seniors (65+)
    else:
        price = 6.5

    return price


# checks that users enter a valid response (e.g. yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = f"Please choose from {valid_responses[0]} or {valid_responses[1]}"

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item
            elif response == "c":
                item = input("Cash or credit? ")
                return item

        print(error)


# main routine goes here

# sets maximum number of tickets below
max_tickets = 3
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

want_instruction = string_checker("Do you want to read the "
                                  "instructions (y/n)? "
                                  , 1, yes_no_list)

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

    # calculate the tickets cost
    ticket_cost = calc_ticket_price(age)

    # gets payment method
    pay_method = string_checker("Choose a payment method "
                                "(cash / credit): ",
                                2, payment_list)

    tickets_sold += 1

# output number of tickets sold
if tickets_sold == max_tickets:
    print("Congratulations you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold}. "
          f"There is {max_tickets - tickets_sold} remaining")
