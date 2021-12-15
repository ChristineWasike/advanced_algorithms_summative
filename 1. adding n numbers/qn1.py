def adding_numbers(number):
    # declaring a variable to store the total sum
    total = 0

    # looping through numbers from one to the given upper-bound inclusive
    for i in range(1, number + 1):
        # adding the current number to the total
        total += i

    # function returns the total
    return total


if __name__ == '__main__':
    # test 1
    # print(adding_numbers(8))  # 36

    # test 2
    print(adding_numbers(10))  # 55

    # test 3
    print(adding_numbers(10000))  # 50005000

    # test 4
    print(adding_numbers(1000000))  # 500000500000

    # test 5
    print(adding_numbers(1000000000))  # 500000000500000000
