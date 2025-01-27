running_total = 0
buyer_total = 0
ticket_limit = 20
tickets_sold = 0

print("Welcome to the cinema. We have 20 tickets available")
print("-----------------------------------------------------------")

def sell(purchased_tickets):
    global buyer_total
    global tickets_sold
    global ticket_limit

    if purchased_tickets == 0:
        pass

    if purchased_tickets == 1:
        tickets_sold += 1
        ticket_limit -= 1
        buyer_total += 1
        return buyer_total, tickets_sold, ticket_limit

    if purchased_tickets == 2:
        tickets_sold += 2
        ticket_limit -= 2
        buyer_total += 1
        return buyer_total, tickets_sold, ticket_limit

    if purchased_tickets == 3:
        tickets_sold += 3
        ticket_limit -= 3
        buyer_total += 1
        return buyer_total, tickets_sold, ticket_limit

    if purchased_tickets == 4:
        tickets_sold += 4
        ticket_limit -= 4
        buyer_total += 1
        return buyer_total, tickets_sold, ticket_limit

    if purchased_tickets > 4:
        print("There is a max of 4 tickets per person. Try again.")


def main():

    global ticket_limit


    while ticket_limit > 0:
        user_input = int(input("How many tickets (up to four), would you like to purchase?: "))
        if user_input > ticket_limit:
            print(f"We only have {ticket_limit} tickets remaining. Please adjust your ordered quantity.")
            print("-----------------------------------------------------------")
            continue
        sell(user_input)
        print(f"You purchased {user_input} tickets.")
        print(f"There are now {ticket_limit} tickets remaining.")
        print("-----------------------------------------------------------")

    print("There are no more tickets available for sale.")
    print(f"We had {buyer_total} ticket buyers.")


main()
