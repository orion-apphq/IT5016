import csv #Import CSV reading module

# Global Variable Declaration
Loop = True
invalid = True
wordList = []
isAlphaList = []
readerList = []

with open('C:/Users/Learner Me/PycharmProjects/udemy/ascii-binary.csv') as csv_file: # Specifies the location of the CSV file and saves it into the variable
                                                                                     # csv_file
    reader = csv.reader(csv_file, delimiter=",") # Creates a variable called reader and assigns the data contained at the location of csv_file into it
    # It reads the data using the reader method in the csv module - It takes two parameters, the location of the file to be read, and the character used
    # as a delimiter ( the character used to seperate the values the file contains )
    
    for row in reader: # This goes through each row ( seperated by \n character ) and adds that row to the end of a list. We do this because the reader has a
                       # custom object type, and it has funny behaviour after looping through it more than once
        readerList.append(row)

    # Here we define the function that converts a letter to its ascii binary equivalent - the parameter letter is the character to be converted
    def convert(letter):
        i= 0 # Set counter to 0 after function is called
        while i <= len(readerList): # Initialize a while loop that will loop the same amount of times as the length ( no. of items ) in the list
            row_two = readerList[i] # Creates the variable row_two and assigns it to it the row that matches the iteration of the loop
            i += 1 # Increase loop counter by 1
            if row_two[1] == letter: # Each row looks like this: [01010101, x] so this if statement checks if the item at the second index - the character -
                                     # matches the one the was passed into the function and, if it does, returns its binary equivalent located at the first
                                     # index
                return row_two[0]
            
    while Loop: # Just keeps looping through over and over until "exit" is input
        
        # This while loop here checks the user is inputting compatible strings and sanitizing the inputted data
        while invalid:
            isAlphaList.clear() # Clears the list that is used to store the values of if the input only contains characters from the alphabet 
            print('only use characters a-z, and space') # Prints a message to the user, telling them which characters are valid
            userString = input("Enter characters: ") # Creates a variable userString and asks the user to input the characters which are saved into it
            userString = userString.casefold() # .casefold turns all the characters in a string to lowercase - we then save that back into userString
            if userString == "exit":
              Loop = False
              break;
            wordList = userString.split() # This splits the string on " " (space) and saves each word as a string item in a list
            for word in wordList: # This loops through each word in the list of words the user inputted
                isAlphaList.append(word.isalpha()) # .isalpha checks if the string only contains characters from the alphabet and returns True or False
                # We take that boolean it returns and save it into the isalpha list
            if False in isAlphaList: # After looping the list of input, this statement checks if the words are all valid - if a invalid character was entered
                # anywhere in the words from the user isAlphaList will contain a False value and my program will through an error if i tried to
                # convert that character
                print("Invalid character string!") # If here was an invalid character, let the user know and go back to the top of the loop
            else: # Here else will be hit if the isAlphaList only contains True values
                invalid = False # Sets invalid to false, meaning the user input has been sanitised and only contains valid characters, breaking the loop so we
                # move onto the next section

        # Starts looping through each word in the list of words
        for word in list(wordList):
            print(word) # prints that word to the screen
            for char in word: # starts looping through each character in the word
                print(convert(char)) # passes the character into the converting function which returns its ascii binary equivalent and we print that to the screen
        invalid = True # after looping through the entire list of words sets invalid back to true


