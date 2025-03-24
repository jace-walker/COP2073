# this program reads the "grades.csv" file and outputs the data into a table

# import csv
import csv

def read_file():
# open the file in READ mode to not clear the information
    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)

# stores each value in header in list to then display it piece by piece
        file_header = next(reader)

# displays header
# the numbers define how much space before next value is displayed
        print(f"{file_header[0]:<14}{file_header[1]:<14}{file_header[2]:<9}"
              f"{file_header[3]:<9}{file_header[4]:<9}")


# for every student (row) in file, display with same distance as header
        for student in reader:
            student_first, student_last, student_exam1, student_exam2, student_exam3 = student
            print("----------------------------------------------------")
            print(f"{student_first:<14}{student_last:<14}{student_exam1:<9}{student_exam2:<9}{student_exam3:<9}")


read_file()