# A Python program to remove "b" and 'ac' from input string
ONE = 1
TWO = 2


# Utility function to convert string to list
def toList(string):
    l = []
    for x in string:
        l.append(x)
    return l


# Utility function to convert list to string
def toString(l):
    return ''.join(l)


# The main function that removes occurrences of "a" and "bc"
# in input string
def stringFilter(string):
    # state is initially ONE (The previous character is not a)
    state = ONE

    # i and j are index variables, i is used to read next
    # character of input string, j is used for indexes of
    # output string (modified input string)
    j = 0

    # Process all characters of input string one by one
    for i in range(len(string)):

        # If state is ONE, then do NOT copy the current character
        # to output if one of the following conditions is true
        # ...a) Current character is 'b' (We need to remove 'b')
        # ...b) Current character is 'a' (Next character may be 'c')
        if state == ONE and string[i] != 'a' and string[i] != 'b':
            string[j] = string[i]
            j += 1

        # If state is TWO and current character is not 'c' (other-
        # wise we ignore both previous and current characters)
        if state == TWO and string[i] != 'c':
            # First copy the previous 'a'
            string[j] = 'a'
            j += 1

            # Then copy the current character if it is not 'a' and 'b'
            if string[i] != 'a' and string[i] != 'b':
                string[j] = string[i]
                j += 1

            # Change state according to current character
        state = TWO if string[i] == 'a' else ONE

        # If last character was 'a', copy it to output
    if state == TWO:
        string[j] = 'a'
        j += 1

    return toString(string[:j])


# Driver program
string1 = stringFilter(toList("cbacd"))
print(string1)