import csv // Import CSV reading module

invalid = True
wordList = []
isAlphaList = []
readerList = []

with open('C:/Users/Learner Me/PycharmProjects/udemy/ascii-binary.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    for row in reader:
        readerList.append(row)

    def convert(letter):
        i= 0
        while i < len(readerList):
            row_two = readerList[i]
            i += 1
            if row_two[1] == letter:
                return row_two[0]

    # 1: needs to take a string input
    # x: read the input and check it has only supported chars (a-z, A-Z, space)
    while invalid:
        print('only use characters a-z, and space')
        userString = input("Enter characters: ")
        userString = userString.casefold()
        wordList = userString.split()
        for word in wordList:
            isAlphaList.append(word.isalpha())
        if False in isAlphaList:
            print("Invalid character string!")
        else:
            invalid = False


    for word in list(wordList):
        print(word)
        for char in word:
            # csv look up
            print(convert(char))
            print(f"exited first loop: {char}")

# 2: character by character, it needs to read through the string and add the matching binary code for each character to a list

# 3: it gets the corresponding binary - ascii from a csv file

# print binary
