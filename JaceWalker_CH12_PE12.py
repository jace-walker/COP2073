#           Jace Walker Programming Exercise 12
#This program reads the csv file I made for PE-CSV and enters the data into a numpy array. From there, each column(exam)
#   in the array is placed into its own array. Then, using numpy, each exam has its statistics and passing rate
#       calculated. All of this data is then printed to the user.

import numpy as np

# using numpy, each statistic is calculated
def calculate_stats(array):

    print(f"Mean: {int(np.mean(array))}%")
    print(f"Median: {int(np.median(array))}%")
    print(f"Standard Deviation {int(np.std(array))}")
    print(f"Minimum: {int(np.min(array))}%")
    print(f"Maximum: {int(np.max(array))}%")


# checks if each entry in the array is above 60
#       i found flatten() online. i used it because each column when turned into an array was one-dimensional but when
#           making the array for all three exams, it was two-dimensional and would get ValueErrors.

def passing_rate(array):
    array = np.array(array).flatten()
    passing = 0
    for x in array:
        if x >= 60:
            passing += 1
        else:
            pass

    pass_rate = int(passing / len(array) * 100)
    print(f'Pass Rate: {pass_rate}%')


# main function that reads the csv file, creates each array, and calls calculation functions

def main():

# filling values returns a zero for missing values, such as the names or headers in the Excel file
# skip header let me skip the top row of irrelevant data

    exam_grades = np.genfromtxt('grades.csv', delimiter=',',filling_values=0,skip_header=1)

# created an array for each exam column
# last array is 2D but found fix online

    exam1 = exam_grades[:, 2]
    exam2 = exam_grades[:, 3]
    exam3 = exam_grades[:, 4]
    all_exams = exam_grades[:, 2:5]


# print data

    print()
    print(exam_grades)
    print()
    print('------------------------------------')
    print()

    print('Exam One:')
    calculate_stats(exam1)
    passing_rate(exam1)
    print('------------------------------------')

    print('Exam Two:')
    calculate_stats(exam2)
    passing_rate(exam2)
    print('------------------------------------')

    print('Exam Three:')
    calculate_stats(exam3)
    passing_rate(exam3)
    print('------------------------------------')

    print('All Exams:')
    calculate_stats(all_exams)
    passing_rate(all_exams)
    print('------------------------------------')

main()