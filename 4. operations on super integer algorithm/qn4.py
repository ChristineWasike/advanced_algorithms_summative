import time


def super_digit(n, k):
    # if n has one digit return n
    if len(n) == 1:
        return int(n)

    # concatenate the n string k times
    p = n * k
    # call the recursive function and supply p as in integer to it
    return helper_fun(int(p))


# The recursive function that adds up digits in a number
def helper_fun(value):
    # base case when the number of digits in the summed number is one
    if len(str(value)) == 1:
        # return the super digit
        return value

    # create a list of the digits in value
    num_list = [int(x) for x in str(value)]

    # stores the sum of digits in value
    total = 0

    # adds up digits in number list
    for i in num_list:
        total += i

    # recursive call and supplying total as the argument
    return helper_fun(total)


if __name__ == '__main__':
    # Confirmation of return type
    print(type(super_digit('9875', 1)))  # <class 'int'>

    print(super_digit('148', 3))  # 3

    print(super_digit('9875', 4))  # 8

    print(super_digit('9875', 1))  # 2

    print(super_digit('8', 1000))  # 1

    start = time.process_time()
    # Time estimate: 2.689699999999795e-05
    print("Growth Test 1: ", super_digit('1234', 10), ". Process time: ", time.process_time() - start)  # 1

    start = time.process_time()
    # Time estimate: 0.0002168409999999954
    print("Growth Test 2: ", super_digit('12345', 100), ". Process time: ", time.process_time() - start)  # 6

    start = time.process_time()
    # Time estimate: 0.0036098560000000016
    print("Growth Test 3: ", super_digit('123456', 1000), ". Process time: ", time.process_time() - start)  # 3

    start = time.process_time()
    # Time estimate: 0.19087736900000002
    print("Growth Test 4: ", super_digit('1234567', 10000), ". Process time: ", time.process_time() - start)  # 1

    start = time.process_time()
    # Time estimate: 21.206148272
    print("Growth Test 5: ", super_digit('12345678', 100000), ". Process time: ", time.process_time() - start)  # 1
