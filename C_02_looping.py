# main routine starts here


# sets maximum number of tickets below
max_tickets = 3

# loops to sell all tickets
tickets_sold = 0
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
