def super_digit(number, k):
    number = number * k
    num_list = [int(x) for x in number]
    total = 0
    for i in num_list:
        total += i
    return total


if __name__ == '__main__':
    print(super_digit('9875', 4))
