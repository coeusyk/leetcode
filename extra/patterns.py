def pattern_1(n: int):
    for i in range(n):
        for j in range(i + 1):
            print(j + 1, end=" ")

        print()


def pattern_2(n: int):
    for i in range(n):
        for j in range(1, n - i + 1):
            print(j, end=" ")

        print()


def pattern_3(n: int):
    """
        *
      *   *
    * * * * *
    """

    if n < 3:
        print("invalid input: expected value greater than equal to 3")
        return

    initial_space = 2 * (n - 1)
    print(f"{' ' * initial_space}*")

    mid_space = 3

    for i in range(n - 2):
        initial_space -= 2

        print(f"{' ' * initial_space}*{' ' * mid_space}*")

        mid_space += 4

    print("* " * ((2 * n) - 1))


def pattern_4(n: int):
    if n < 3:
        print("invalid input: expected value greater than equal to 3")
        return

    print("* " * ((2 * n) - 1))

    initial_space = 2
    mid_space = 3 + (4 * (n - 3))

    for i in range(n - 2):
        print(f"{' ' * initial_space}*{' ' * mid_space}*")

        initial_space += 2
        mid_space -= 4

    print(f"{' ' * initial_space}*")


pattern_4(5)
