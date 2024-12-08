
def students_by_department(student_list , department):
    # a list of tuples is passed in the function args that contains the name and id of the students in the department
    filtered_students = [] # empty list to store the filtered students

    # this loop is used to iterate over the student list to check whether the department of the student is the same as the department entered by the user entered 
    for s in student_list:

        # If department is same as entered department the those are appended to the empty list filtered students
        if s[2] == department:
            name = s[1]
            id = s[0]
            filtered_students.append((name,id)) # this line of code appends value by value to the list

    # this loop is used to print the name and id of the students in the department entered by user
    print("Sorted students by department:",department)
    for s in filtered_students:
        print(s[1],"-",s[0]) 


def file_list():
    # Get the input file name from the user
    input_file = input("Enter file name: ")

    # Try and except to handle error if user enters invalid file name
    try:
        # the file is opened in read mode and stored in the variable file
        with open(input_file,'r') as file:
            students = [] # empty list to store values from the file

            # this loop is created to take values from each line of the file and store it in a list and split it by comma
            for line in file:
                s = line.strip().split(',') 
                students.append(tuple(s)) ## this line of code appends the value by value to the list

            students = sorted(students,key=lambda x: x[1]) # sorted the values in the list by id

    except FileNotFoundError:
        # If the file is not found or the input is invalid, then this except block is executed
        print("File not found. Enter valid file name.")
        file_list() # the function is called back if the input or the file is invalid
        return

    print('list of students:', students) # prints list of student

    while True:
        # Get the department name from the user and the loop is executed until user enters 'quit'
        department_name = input("Enter the department name or 'quit' to exit: ")
        if department_name.lower() == 'quit':
            break

        students_by_department(students, department_name) # this function is called to print the students by department


## This is the main function for the program above which is called below
file_list() 














