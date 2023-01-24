def runLengthEncoding(string):

    encodedStringCharacters = []
    currentRunLength = 0

    for i in range(1, len(string)):
        currentChar = string[i]
        previousChar = string[i - 1]

        if currentChar != previousChar or currentRunLength == 9:
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(previousChar)
            currentRunLength = 0 
        currentRunLength += 1 

        # Handle the last run
        encodedStringCharacters.append(str(currentRunLength))
        encodedStringCharacters.append(string[(len(string)) - 1])

        return "".join(encodedStringCharacters)
        