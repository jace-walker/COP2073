# this function accepts input and writes it into the "grades.csv" file.

import csv

def write_grades():
#open the file in writing mode to clear file and start editing
    with open('grades.csv', mode='w', newline='') as file:

        writer = csv.writer(file)

# create header
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

# get quantity of students
        student_amount = int(input("How many student grades are you checking?: "))

# get information for each student
        for x in range(student_amount):
            student_first = input("Enter their first name: ")
            student_last = input("Enter their last name: ")
            student_exam1 = int(input("Enter grade for Exam 1: "))
            student_exam2 = int(input("Enter grade for Exam 2: "))
            student_exam3 = int(input("Enter grade for Exam 3: "))
            print('---------------------------')

# write the info into file below header
            writer.writerow([student_first, student_last, student_exam1,
                             student_exam2, student_exam3])

    print('Grades have been recorded.')

# call write function
write_grades()
