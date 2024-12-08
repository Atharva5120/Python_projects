
import numpy as np


def inp():
    # Get the input file name from the user
    input_file = input("Enter the file name: ")

    # Try and except to handle error if user enters invalid file name
    try:
        # the file is opened in read mode and stored in the variable file
        with open(input_file, 'r') as file:

            # Read the first line and get the number of students and assignment weightage
            l = file.readline()
            
            # splits the line into seperate values
            l_values = l.strip().split()

            # the value at 0th index is stored in no_of_students variable from first line
            no_of_students = int(l_values[0])

            # the value at 1st index is stored in assignment_weightage variable from first line
            assignment_weightage = int(l_values[1])

            ## created two dimensional empty array to iterate values in it from file 
            studentExamData = np.array([[0, 0.0, 0.0, 0.0]] * no_of_students)

            # this for loop reads the remaining lines and insert the values to the array
            for i in range(no_of_students):
                # Read the line from second line and further and get the registrationNum, exam_mark and course_assignment_marks
                l = file.readline()
                
                l_values = l.strip().split() # splits the line into seperate values

                registrationNum = int(l_values[0]) # the value at 0th index of a line is stored as registration number

                exam_mark = float(l_values[1]) # the value at 1st index of a line is stored as exam mark

                course_assignment_marks = float(l_values[2]) # the value at 2nd index of a line is stored as course assignment marks

                # The function total marksis called to calculate total marks and grade of a student and stored in the particular variable
                total_marks, grade = gradeCalculation(exam_mark, course_assignment_marks, assignment_weightage)

                # The function is called and all the values are stored in the array studentExamData
                studentExamData[i] = [registrationNum, exam_mark, course_assignment_marks, total_marks]
            

        # Create a variable data_type to assign the data type to the variables of the array
        data_type = np.dtype([('registrationNum', 'int'), ('exam_mark', 'float'), ('course_assignment_marks', 'float'), ('total_marks', 'int'), ('grade', 'U15')])

        # Created a one-dimensional array and assigned a data type for each index
        result_array = np.array([(0, 0.0, 0.0, 0, "")] * no_of_students, dtype=data_type)

        # This for loop extracts the values from first array and the values are inserted in the 1D result array with rounded marks and grades
        for i in range(no_of_students):

            # the values of registration number, exam mark, course assignment marks, total marks and grade are extracted from the array studentExamData
            registrationNum, exam_mark, course_assignment_marks, total_marks = studentExamData[i] 

            # The function total marksis called to calculate total marks and grade of a student and stored in the particular variable
            total_marks, grade = gradeCalculation(exam_mark, course_assignment_marks, assignment_weightage)
            
            # the calculated value of total marks and the other values present in the file are stored in result array 
            result_array[i] = (int(registrationNum), float(exam_mark), float(course_assignment_marks), float(total_marks), str(grade))

        # The array is sorted in descending order of total marks so the students with highest total marks is displayed first
        result_array = np.sort(result_array, order='total_marks')[::-1]

        # Output the sorted result_array to a file
        output_file_name = "result_ex5.txt" # name of the output file

        # The output file is opened in write mode and the new file is created named result array
        with open(output_file_name, 'w') as result:
            print(result_array, file = result) # prints the result array to the output file

        # this below block calculates the number of students in each grade and is stored in their particular variable
        first_class = sum(result_array['grade'] == 'First') # no of students passed with first class
        second_class = sum(result_array['grade'] == 'Second') # no of students passed with second class
        third_class = sum(result_array['grade'] == 'Third') # no of students passed with third class
        fail_count = sum(result_array['grade'] == 'Fail') # no of students failed

        # This variable is used to store the registration numbers of failed students
        fail_registrationNums = result_array[result_array['grade'] == 'Fail']['registrationNum']


        # This block below prints the values of the variables calculated above
        print("Number of First-class students: ",first_class)
        print("Number of Second-class students: ",second_class)
        print("Number of Third-class students: ",third_class)
        print("Number of Failed students: ",fail_count)
        print(f"Registration numbers of students who failed : {fail_registrationNums}") # list of regestration numbers of failed students

    except FileNotFoundError:
            # If the file is not found or the input is invalid, then this except block is executed
            print("File not found. Enter valid file name.")
            inp() # And the function is called back if the input or the file is invalid
             


# This function is used to calculate the total marks and grade of a student
def gradeCalculation(exam_mark, course_assignment_marks, weighting):

    # total marks is calculated by adding the exam score multiplied by exam weightage and coursework marks multiplied by coursework weightage
    total_marks = round((1 - weighting/100) * exam_mark + weighting/100 * course_assignment_marks)
 
    # grade is calculated based on the total marks
    if exam_mark < 30 or course_assignment_marks < 30:
        studentGrade = "Fail"  # if the total marks or coursework marks are less than 30 , then the student is failed
    elif total_marks >= 70:
        studentGrade = "First" # if the total marks is greater than or equal to 70, then the student is passed with first class
    elif 50 <= total_marks < 70:
        studentGrade = "Second"   # if the total marks is greater than or equal to 50 and less than 70, then the student is passed with second class
    elif 40 <= total_marks < 50:
        studentGrade = "Third" # if the total marks is greater than or equal to 40 and less than 50, then the student is passed with third class
    else:
        studentGrade = "Fail" 

    # The values of total marks and grade are returned from the function
    return total_marks, studentGrade


# This is the main function for the program above which is called below
inp()
