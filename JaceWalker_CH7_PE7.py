# Jace Walker     Programming Exercise 7
#   This program asks the user to enter a paragraph. The program then calls a function to count every sentence.
#       The program then displays each individual sentence and amount of sentences.

import re

# defines pattern to search for and then searches through input
# prints each sentence and amount of sentences
def sentence_split(paragraph):

    pattern = r'[A-Z0-9].*?[.!?] (?=[A-Z0-9]|$)'           # pattern from textbook

    sentences = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)

    for i in sentences:
        print('->', i)

    print(f'you have {len(sentences)} sentences')

# asks user for input and then calls regular expression function
def main():

    user_paragraph = input('enter a paragraph: ')
    user_paragraph += ' '                                # realized that the input would be missing a whitespace after
                                                         #     last sentence and therefore would not count so manually
    sentence_split(user_paragraph)                       #        add whitespace after user's string

main()