import math

def reversePart(array, start_index):
    newArray = []
    index = start_index

    if index == 0:
        newArray.append(array[0])
    else:
        for i in range(index):
            newArray.append(array[i])

    for j in range(len(array) - 1, start_index, -1):
        newArray.append(array[j])

    return newArray


def are_they_equal(array_a, array_b):
    flag = False
    for i in range(len(array_b)):
        reversedArray = reversePart(array_b, i)
        if reversedArray == array_a:
            flag = True
            return True

    if flag == False:
        return False


# Tests
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
    n_1 = 4
    a_1 = [1, 2, 3, 4]
    b_1 = [1, 4, 3, 2]
    expected_1 = True
    output_1 = are_they_equal(a_1, b_1)
    check(expected_1, output_1)

    n_2 = 4
    a_2 = [1, 2, 3, 4]
    b_2 = [1, 2, 3, 5]
    expected_2 = False
    output_2 = are_they_equal(a_2, b_2)
    check(expected_2, output_2)

