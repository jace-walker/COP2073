# Programming Exercise 2 , Jace Walker

# This program asks for the user to enter a message. This message is then checked for possible spam
#       keywords against a list of typical spam words. A 'spam score' is calculated by counting the
#           number of spam words used. At the end, the program will print out the spam score, the likelihood
#              this is a spam message, and the spam words that were found.


# create list of usual spam words , I made this up
spam_words = [
    'free', 'act', 'must', 'money', 'access', 'spam',
    'boss', 'password', 'username', 'job', 'million', 'offer',
    'billion', 'thousand', 'cash', 'only', 'urgent', 'quotes',
    'fee', 'cure', 'debt', 'junk', 'scam', 'credit', 'tax',
    'new', 'claim', 'cheap', 'insurance', 'discount', 'loans',
    'interest', 'unlimited', 'warranty', 'lifetime', 'income'
]


# initialize empty list of spam words found in the user's message for later
words_in_email = []


# this function checks for spam words in the message
# for loop : python checks if inputted string is contained in spam word list
# if a word is found, that word is added to the already created 'words_in_email' list
def spam_checker(email, spam_list):

    for word in email:
        if word in spam_list:
            words_in_email.append(word)



# this function calculates the input's 'spam score' or just number of spam words found
# assign variable to length of found spam words list
# if statements checking length of list against 0, <=3, or >3
def spam_score(email_spam_words):

    total = len(email_spam_words)
    if total == 0:
        return 'This was not a spam email.'
    if 0 < total <= 3:
        return 'This might be a spam email.'
    if total > 3:
        return 'This is likely a spam email'



# main function where we display everything and call the two functions
def main():

    print()
    print('Spam Email Detector')       # cosmetic

    user_message = input('Please write an email: ')
    user_message = user_message.lower()         # make input lowercase
    user_message = user_message.split()         # makes anything separated by a space in input
    print('------------------------------------')    #                     into its own string
    
# run spam_checker function with parameters of user's input and the likely spam word list
    spam_checker(user_message, spam_words)

# print user's spam score
    print(f'Your spam score was: {len(words_in_email)}.')
    print(spam_score(words_in_email))

# if statements to ensure grammar is correct regardless of spam score

    if len(words_in_email) == 0:
        print('There were no spam words to display.')
    if len(words_in_email) == 1:
        print(f'The word that appears to be spam is: {", ".join(words_in_email)}.')     # join method so list
    if len(words_in_email) > 1:                                                         #    displays pretty
        print(f'The words that appear to be spam are: {", ".join(words_in_email)}.')


# call main function
main()