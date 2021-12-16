def super_digit(n, k):
    p = n * k
    return helper_fun(int(p))


def helper_fun(value):
    if len(str(value)) == 1:
        return value

    num_list = [int(x) for x in str(value)]

    total = 0
    for i in num_list:
        total += i

    str_total = str(total)
    print(str_total)
    return helper_fun(str_total)


if __name__ == '__main__':
    print(super_digit('148', 3))  # 3
