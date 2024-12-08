from datetime import date  # imports date from datetime
from datetime import datetime # imports datetime from datetime

def age():

    # Try Catch block used to handle errors
    try:
        # Get user input for date of birth
        birth_date_inp = input("Enter your date of birth in the format MM/DD/YYYY: ")

        dateOfBirth = birth_date_inp.split('/') # Split the date of birth by '/'
        day = int(dateOfBirth[0]) # Convert the first element of the list to integer
        month = int(dateOfBirth[1]) # Convert the second element of the list to integer
        year = int(dateOfBirth[2]) # Convert the third element of the list to integer

        # Get today's date
        today = date.today()

        # Check if it's the user's birthday today
        birthday = (month, day) == (today.month, today.day)

        # Age calculation
        age = today.year - year - ((today.month, today.day) < (month,day))

        # Age output
        print("Your age is: ",age)

        if birthday: print("Happy birthday to you!") # If its user birthday, print happy birthday

    except ValueError:
        ## If the input is invalid then error message is printed and the function is called again
        print("Invalid date of birth or input. Please try again.")  
        invalid_inp()

## If input is invalid then this function is called to run our main function again
def invalid_inp():
    age()

# This function is called to run our main function
age() 
