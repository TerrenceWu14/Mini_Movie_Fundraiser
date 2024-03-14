# Checks whether the user entered yes or no
def cash_credit(question):

    while True:

        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"

        elif response == "credit" or response == "cr":
            return "credit"

        else:
            print("Please choose a valid payment method")


# Main routine
while True:
    payment_method = cash_credit("Do you want to read the instructions? ")
    print(f"you chose {payment_method}")
