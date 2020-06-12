import math


# Add any extra import statements you may need here


# Add any helper functions you may need here

def cipherAlpha(letter, rotation_factor):
    alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alphabetarr = alphabet.split(" ")

    for i in range(len(alphabet) - 1):

        if alphabetarr[i] == letter:

            if 0 <= i <= (25 - rotation_factor):
                return alphabetarr[i + rotation_factor]
            else:
                if (i % (25 - rotation_factor)) == 0:
                    newIndex = (((i // (25 - rotation_factor)) - 1) * (25 - rotation_factor)) - 1
                else:
                    newIndex = (i - (25 - rotation_factor)) - 1
                return alphabetarr[newIndex]





def rotationalCipher(userInput, rotation_factor):
    code = []

    for i in range(len(userInput)):

        if rotation_factor >= 26:

            if rotation_factor % 25 == 0:
                newRotation = 26 - (rotation_factor // 25)
            else:
                newRotation = 26 - (rotation_factor % 25)
            return rotationalCipher(userInput, newRotation)

        else:

            if userInput[i].isnumeric():
                sumT = int(userInput[i]) + rotation_factor
                if sumT % 9 == 0:
                    code.append(userInput[i])
                elif sumT < 9:
                    code.append(str(int(userInput[i]) + rotation_factor))
                else:
                    code.append(str((sumT % 9) - 1))

            elif (userInput[i]).isupper():
                code.append(cipherAlpha(userInput[i].lower(), rotation_factor).upper())

            elif (userInput[i]).islower():
                code.append(cipherAlpha(userInput[i], rotation_factor))

            else:
                code.append(userInput[i])

    return "".join(code)


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    # input_1 = "All-convoYs-9-be:Alert1."
    # rotation_factor_1 = 4
    # expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    # output_1 = rotationalCipher(input_1, rotation_factor_1)
    # check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    # Add your own test cases here
