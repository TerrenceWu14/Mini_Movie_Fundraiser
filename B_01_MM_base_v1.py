import pandas


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

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item
            elif response == "c":
                item = input("Cash or credit? ")
                return item

        print(error)

# currency formatting function
def currency(x):
    return f"${x:.2f}"


# main routine goes here

# initializes variables
max_tickets = 5
tickets_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# dictionaries to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# dictionary used to create data frame ie: column_name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge,
}

# asks the user if they want to see the instructions
want_instruction = string_checker("Do you want to read the "
                                  "instructions (y/n)? "
                                  , 1, yes_no_list)

# if they wanted to view the instructions it displays itself
if want_instruction == "yes":
    print("Instructions go here")

print()

# loops as long as tickets sold is less than max tickets
while tickets_sold < max_tickets:

    # asks for the users name
    name = input("Please enter your name or 'xxx' to quit: ")

    # exits if the users wants to quit
    if name == 'xxx':
        break

    # asks for the users age
    age = num_check("Age: ")

    # passes if they are within this accepted range
    if 12 <= age <= 120:
        pass

    # sends back to the top of the while loops, user is too young
    elif age < 12:
        print("You are too young! You can't watch this movie")
        continue

    # sends back to the top of the while loops, user may be faking their age
    else:
        print("?? That looks like a typo, please try again")
        continue

    # calculate the tickets cost
    ticket_cost = calc_ticket_price(age)

    # gets payment method
    pay_method = string_checker("Choose a payment method "
                                "(cash / credit): ",
                                2, payment_list)

    if pay_method == "cash":
        surcharge = 0
    else:
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index('Name')

# calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# calculates the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# currency formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print("----- Ticket Data -----")
print()

print(mini_movie_frame)

print()
print("----- Ticket Cost / Profit -----")

# output total ticket sales and profit
print(f"Total Ticket Sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")

# output number of tickets sold
if tickets_sold == max_tickets:
    print("Congratulations you have sold all the tickets")
else:
    print(f"You have sold {tickets_sold}. "
          f"There is {max_tickets - tickets_sold} remaining")
