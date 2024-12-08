## Function to check whether the number is prime
def prime(number):
        if number < 2: ## This condtion returns false the number is less than 2 because 1 is not a prime number 
            return False
        ## this for loop below retuns prime number 
        for i in range(2, number): 
            if number % i == 0:
                return False
        return number

def inp():
    # try and except is used for exception handeling in input
    try: 
        ## Taking input from user
        number1 = int(input("Enter a positive number: ")) 
        number2 = int(input("Enter another positive number: "))

        ## checking the input 
        if number1 < 0 or number2 < 0 : 
            print("invalid input please enter a positive number")
            invalid_inp() ## calling this function if the input is invalid

    except ValueError: 
        ## if the input is anything other than a number or empty value code will run this line of 
        ## command and call a function asking to enter a correct value
        print("Invalid Input") 
        invalid_inp()


    # this statement extract lowest input as start of range and highest input as end of range
    if number2 > number1:
        start = number1
        end = number2
    else:
        start = number2
        end = number1

    prime_list =[] # Creating list to store prime numbers between defined range
    ## this loop iterate over each number to check whether the number is prime by iretating all numbers defined in a 
    ## range by calling prime function starting from given range to end 
    for number in range(start , end + 1):
        if prime(number): 
            prime_list.append(number) ## if the number is prime append it to the list

    count = 0 ## initialised counter to zero

    # this loop is used to print max 10 numbers in a row
    for pr in prime_list:
        print(pr, end = " ") # Print element and then space
        count += 1 # counter increment by 1 when element is printed
        if count % 10 == 0: ## when counter is 10 it will break the line
            print()
    
def invalid_inp(): ## This function will get called if the user input is invalid 
    inp()

inp()
