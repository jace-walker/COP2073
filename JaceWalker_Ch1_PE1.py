# JaceWalker_Ch1_PE1
# Jace Walker / Programming Exercise 1

# This program replicates selling movie tickets at a cinema.
# Each buyer can buy up to 4 tickets. No more than 20 tickets can be sold total.

# initialize these variables for use later
# 'buyer_total' is running total of buyers / 'ticket_limit' is max tickets that can be sold (20)

buyer_total = 0
ticket_limit = 20


print("Welcome to the cinema. We have 20 tickets available")
print("-----------------------------------------------------------")


# this function will check user's input and put it through if statements to determine how many tickets to sell
# we add a buyer for every one sale and subtract our ticket limit (20) by tickets sold
# 'buyer_total' and 'ticket_limit' are global so they can be used inside and outside the function
# at end of each if statement, we return 'buyer_total' and 'ticket_limit'

def sell(purchased_tickets):
    global buyer_total
    global ticket_limit

    if purchased_tickets == 0:
        pass

    if purchased_tickets == 1:
        ticket_limit -= 1
        buyer_total += 1
        return buyer_total, ticket_limit

    if purchased_tickets == 2:
        ticket_limit -= 2
        buyer_total += 1
        return buyer_total, ticket_limit

    if purchased_tickets == 3:
        ticket_limit -= 3
        buyer_total += 1
        return buyer_total, ticket_limit

    if purchased_tickets == 4:
        ticket_limit -= 4
        buyer_total += 1
        return buyer_total, ticket_limit



def main():

# while loop will continue until ticket limit reaches zero
# if user wants to purchase more tickets than available, they will be prompted to retry

    while ticket_limit > 0:
        user_input = int(input("How many tickets (up to four), would you like to purchase?: "))
        if user_input > ticket_limit:
            print(f"We only have {ticket_limit} tickets remaining. Try again.")
            print("-----------------------------------------------------------")
            continue
        if user_input > 4:
            print(f"You can only purchase a max of four tickets. Try again.")
            print("-----------------------------------------------------------")
            continue

# call sell(user_input) / user_input is used as parameter

        sell(user_input)
        print(f"You purchased {user_input} tickets.")
        print(f"There are now {ticket_limit} tickets remaining.")
        print("-----------------------------------------------------------")

    print("There are no more tickets available for sale.")
    print(f"We had {buyer_total} ticket buyers.")


main()
