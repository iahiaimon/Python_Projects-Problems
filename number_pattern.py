def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."

    if n < 1:
        return "Argument must be an integer greater than 0."

    # numbers = []

    # for number in range(1, n + 1):
    #     numbers.append(str(number))

    # print( " ".join(numbers))

    # OR WE CAN USE THIS!!!

    print(" ".join(str(number) for number in range(1,n+1)))

number_pattern(12)