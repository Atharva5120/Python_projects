
#Function to check pallindrome
def fun1(str):
    lower_string = str.lower() # Conversion of input string to lower case
    str_reverse = '' # variable to store reversed string
    
    # Below for loop is for reversing the input string
    for str in lower_string:
        str_reverse = str + str_reverse  # Storing reversed string in str_reverse variable

    # IF condition below checks both the string for pallindrome and if the input is pallindrome it will return true else will return false     
    if lower_string == str_reverse : return True
    else : return False

#########################################################################################################################################################################

# Function to check the most frequent element entered in a string ignoring special characters
def fun2(str):
    main_string = str.lower() #Converting string to lower case

    txt_inStr = any(c.isalpha() for c in main_string)  # Returns true if string has alphabets
    dig_indig = any(c.isdigit() for c in main_string)  # Returns true if string has Digits

    lowerCase_string = [] # Creating a string to store the string without special characters as we have to ignore it
    symbols = ['$','%','~','#','@','&','*',' ','.',','] # all special symbol list
    
    #This loop will store all the alphabets and number excluding the speciial symbols
    for i in main_string:      
        if i not in symbols:    
            lowerCase_string.append(i)
                     
    count_dct = {} ## Dictionary to store element aand their Frequency
    count = 0      

    if txt_inStr or dig_indig: ## This condition checks if the string entered has digit and alphabets or else return none
        # For loop to iterate over lower case string 
        for element in lowerCase_string: # This loop will iterate element bt element
            if element in count_dct: ## this condition will increment the counter if element is repeated 
                count = count + 1 
                count_dct.update({element: count})
            else: ## the element appears to be single time this condition will assign count as 1
                count = 1    
                count_dct.update({element: count})

        most_frequent = max(count_dct,key=count_dct.get) ## this command line will return most frequent element excluding special symbols and spaces
        return print("Most Frequent is: ",most_frequent)   
    else:
        return None ## if string has no alphabet or digit code will return 'None' 



##########################################################################################################################################################################        

# Function to calculate number of letters, spaces and digits in a string
def fun3(str):
    # Creating variable and assigning them value as ZERO
    letter_count= 0 ; spaces_count= 0 ;digit_count = 0
    
    # For loop to split the elements and check them one by one 
    for i in str:

        # Below if Condition calculates number of letters in a string using isalpha() function
        if i.isalpha():
            letter_count = letter_count + 1 # When the element is a character this will increment by 1

        # Below if Condition calculates number of spaces in a string using isspace() function
        elif i == ' ': 
            spaces_count = spaces_count + 1 # When the element in a string is a empty space this will increment by 1

        # Below if Condition calculates number of digit in a string using isdigit() function
        elif i.isdigit(): 
            digit_count = digit_count + 1 # When the element in a string is a digit this will increment by 1

    # storing all the calculated values in a tuple
    return(letter_count,spaces_count,digit_count) ## Returning dictionary 'count' calculating letters, spaces and digit

#########################################################################################################################################################################        
