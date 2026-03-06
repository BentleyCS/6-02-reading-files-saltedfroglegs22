#You must make and submit your own test file and txt file with this assignment.

def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine(fileName):
    #Given a file return the longest line from within that file
    with open(fileName) as file:
        long = -1
        for line in file:
            if len(line) > long:
                long = len(line)
                words = line
            else:
                pass
    return words

def toBinary(fileName):
    #Given a file that is only 0's and 1's return a list of the file broken into bytes.
    #An example return might be ['01101001', '00101010', '1010']
    n = 4
    with open(fileName, "r") as file:
        string = file.read().replace("\n", "")
    newlist = [string[i : i + n] for i in range(0, len(string), n)]
    return newlist

