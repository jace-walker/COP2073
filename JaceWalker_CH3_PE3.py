# JaceWalker_CH3_PE3
#   This program asks the user for three of their expenses from this month. The type and amount are
#       stored as a tuple but the amount is also placed into a list. The reduce function is used
#           to find the total of the expenses inside the list. The min, max, and total are displayed
#               back to the user at the end of the program.


# import reduce function
import functools

def main():

# initialize expense amount list
    expense_amount = []

    print()
    print('Please tell me three of your expenses this month.')
    print('------------------------------------------------')


# asks user for what and cost of each expense
# cost is stored in a list for later use with reduce function
# but type and cost are each stored as a tuple so we can display the item that goes with min/max cost later

    expense1 = str(input('What is your first expense?: '))
    expense1_amount = int(input("How much was your first expense?: "))
    expense_amount.append(expense1_amount)
    tuple1 = [expense1, expense1_amount]

    expense2 = str(input('What is your second expense?: '))
    expense2_amount = int(input("How much was your second expense?: "))
    expense_amount.append(expense2_amount)
    tuple2 = [expense2, expense2_amount]

    expense3 = str(input('What is your third expense?: '))
    expense3_amount = int(input("How much was your third expense?: "))
    expense_amount.append(expense3_amount)
    tuple3 = [expense3, expense3_amount]

    print('------------------------------------------------')

# min/max method used to find min and max
    min_expense = min(expense_amount)
    max_expense = max(expense_amount)
# reduce function used with lambda function
# lambda adds every value one by one until there is only one value left in expense_amount list
    total_expense = functools.reduce(lambda x, y: x + y, expense_amount)


# if statements that assign the actual min/max expense item to its tuple partner
    if expense1_amount == min_expense:
            min_expense_item = tuple1[0]

    if expense1_amount == max_expense:
            max_expense_item = tuple1[0]

    if expense2_amount == min_expense:
            min_expense_item = tuple2[0]

    if expense2_amount == max_expense:
            max_expense_item = tuple2[0]

    if expense3_amount == min_expense:
            min_expense_item = tuple3[0]

    if expense3_amount == max_expense:
            max_expense_item = tuple3[0]

# display user's expenses back to them
    print(f"Your total expenses were {total_expense} dollars.")

    print(f"Your lowest expense was {min_expense_item} and it costed you {min_expense} dollars.")

    print(f"Your highest expense was {max_expense_item} and it costed you {max_expense} dollars.")


main()
