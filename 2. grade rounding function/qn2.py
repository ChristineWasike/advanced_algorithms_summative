import math


def rounded_grading(grade):
    # base for multiples of 5
    base = 5

    # closest larger multiple of 5
    multiple = int(base * math.ceil(grade / base))

    # check if grade is greater than 37 to be a passing grade
    if grade > 37:
        # rounding up to multiple of 5 if difference is less than 3
        if multiple - grade < 3:
            return multiple, grade

        # returning the grade as is if value difference is greater than 2
        else:
            return grade, grade

    # return failing grade as is
    else:
        return grade, grade


if __name__ == '__main__':
    print(rounded_grading(84))  # 85, 84
    print(rounded_grading(29))  # 29, 29
    print(rounded_grading(57))  # 57, 57
