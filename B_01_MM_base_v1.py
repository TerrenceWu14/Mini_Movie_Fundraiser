import pandas
import random
from datetime import date


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


# Displays instructions
def instructions():
    print('''

***** Instructions *****

For each ticket, enter ...
- The person's name (can't be blank)
- Age (between 12 and 120)
- Payment method (cash or credit)

When you have entered all the users, press 'xxx' to quit.

The program will then display the ticket details
including the cost of each ticket, the total cost
and the total profit.

This information will also be automatically written to 
a text file.
************************************************************
    ''')


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
    instructions()

print()
# loops as long as tickets sold is less than max tickets

while tickets_sold < max_tickets:

    # asks for the users name
    name = not_blank("Please enter your name or 'xxx' to quit: ")

    # exits if the users wants to quit
    if name == 'xxx' and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must sell at least ONE ticket before quitting")
        continue

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

# calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# calculates the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# chooses a winner and looks up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# currency formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# get current date for heading and filename
# get today's date
today = date.today()

# get day, month and year as individual string
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

print()
heading = f"----- Mini Movie Fundraiser Ticket Data {day}/{month}/{year} ----- \n"
filename = f"MMF_{year}_{month}_{day}"

# change frame to a string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create string for printing
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = f"Total Ticket Sales ${total:.2f}"
total_profit = f"Total Profit: ${profit:.2f}"

# edit text below!! It needs to work if we have unsold ticket
if tickets_sold == max_tickets:
    sales_status = "\n*** All tickets have been sold ***"
else:
    sales_status = f"\n*** {tickets_sold} out of {max_tickets} sold ***"

winner_heading = "\n----- Raffle Winner -----"
winner_text = (f"Congratulations to {winner_name}. You have won ${total_won:.2f} ie: "
               f"your ticket is free!")

# list holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# print output
for item in to_write:
    print(item)

# write output to file
# create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
