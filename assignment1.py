# Name: Adrian Gustilo
# OSU Email: gustiloa@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment: Assignment 1: Python Fundamentals Review
# Due Date: 01/30/2023
# Description: A Python Review consists of 10 reviews where some of the reviews include min_max, fizz_buzz, etc.


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    """
    Function that receives an array of integers and returns a
    tuple with two values - the minimum and maximum values of the input array
    """

    array = arr.length()
    minimum_value = array[0]
    maximum_value = array[0]
    for num in range(1, array): #This will go to every num from 1 and goes up to the given parameter
        val = arr[num]
        if val > maximum_value:
            maximum_value = val
        if val < minimum_value:
            minimum_value = val
    return minimum_value, maximum_value



# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    A function that receives a StaticArray of integers and returns a new StaticArray
    If the number in the original array is divisible by 3, the corresponding element in the
    new array will be the string ‘fizz’.
    If the number in the original array is divisible by 5, the corresponding element in the
    new array will be the string ‘buzz’.
    If the number in the original array is both a multiple of 3 and a multiple of 5, the
    corresponding element in the new array will be the string ‘fizzbuzz’.
    """
    array = arr.length()
    result = StaticArray(array)

    for num in range(array):
        val = arr[num]
        if val % 3 == 0 and val % 5 == 0: #It will loop to every val to see which value will pass through each condition
            result[num] = "fizzbuzz"
        elif val % 3 == 0:
            result[num] = "fizz"
        elif val % 5 == 0:
            result[num] = "buzz"
        else:
            result[num] = val
    return result



# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
     a function that receives a StaticArray and reverses the order of the elements in the
     array.
    """
    array = arr.length()
    for num in range(array // 2): #array dividing by 2 using floor division
        val = arr[num]
        arr[num] = arr[(array - 1) - num]
        arr[(array - 1) - num] = val


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    A function that receives two parameters - a StaticArray and an integer value (called
    steps).
    """

    array = arr.length()
    result = StaticArray(array)
    move = abs(steps) % array

    for num in range(array): #Loops to the range of given parameter - array.
        val = arr[num]
        if move == 0:
            result[num] = val

        elif steps > 0:
            pos = num + move
            if pos > array - 1:
                pos = pos - array
            result[pos] = val

        elif steps < 0:
            neg = num - move
            if neg < 0:
                neg = array - abs(neg)
            result[neg] = val

    return result

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    A function that receives the two integers start and end, and returns a StaticArray that
    contains all the consecutive integers between start and end (inclusive).
    """

    array = abs(end - start) + 1
    array = StaticArray(array)

    for num in range(array):
        if start > end:
            val = array[num]
            start = val
            start = start - 1
        elif start <= end:
            val = array[num]
            start = val
            start = start + 1

    return array



# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    A function that receives a StaticArray and returns an integer that describes whether
    the array is sorted
    """

    array = arc.length()
    pos_val = 0
    neg_val = 0

    if array == 1:
        return 1

    for num in range(array - 1):
        val = arr[num]
        if val < arr[num + 1]:
            pos_val = pos_val + 1
    if pos_val == array - 1:
        return 1

    for num in range(array - 1):
        val = arr[num]
        if val > arr[num + 1]:
            neg_val = neg_val + 1
    if pos_val == array - 1:
        return -1

    return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    A function that receives a StaticArray that is sorted in order, either non-descending or
    non-ascending.
    """

    array = arr.length()
    mode = arr[0]
    ints = 1
    nums = 0
    vals = 0

    for num in range(1, array):
        val = arr[num]
        if val == mode:
            ints = ints + 1

        if val not in mode:
            value = nums
            nums = val
            if value == nums:
                vals = vals + 1
            else:
                vals = vals + 1

        if val > ints:
            mode = nums
            ints = val

    return mode, ints

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    A function that receives a StaticArray that is already in sorted order, either
    non-descending or non-ascending
    """

    array = arr.length()
    number = arr[0]
    total = 1

    for num in range(1, array):
        val = arr[num]
        if val != number:
            total = total + 1
            number = val

    for num in range(array):
        if val is not None:
            last_array[last_index] = new_array[i]
            last_index = last_index + 1
    return last_array

    pass

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    A function that receives a StaticArray and returns a new StaticArray with the same
    content sorted in non-ascending order, using the count sort algorithm.
    """

    count = minimum_maximum(arr)
    sorted_num = StaticArray(arr.length())
    nums = (count[1] - count[0]) + 1
    vals = StaticArray(nums)

    for num in range(vals.length()):
        value = vals[num]
        0 = value

    for num in range(arr.length()):
        vals[[value] - count[0]] += 1

    sum = 0
    for num in range(vals.length()):
        for val in range(sum, sum + vals[num]):
            nums[nums.length() - 1 - val] = num + count[0]
            sum = sum + 1
    return sorted_num


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    A function that receives a StaticArray where the elements are in sorted order, and
    returns a new StaticArray with squares of the values from the original array, sorted in
    non-descending order.
    """

    array = StaticArray(arr.length())
    negval = 0
    posval = arr.length() - 1

    for num in range(array.length() - 2):
        if abs(arr[negval]) >= abs(arr[posval]):
            array[num] = arr[negval] ** 2
            negval = negval + 1
        else:
            array[num] = arr[posval] ** 2
            posval = posval - 1
    return array

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
