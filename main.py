import random


def hula():
    x = int(input("Ilang items huhulaan mo: "))

    for i in range(x):
        n = random.randint(1, 4)
        print()
        cat = {1: "a", 2: "b", 3: "c", 4: "d"}

        print(f"{i + 1}.)", cat[n], end="")

    print("\n\nChances na tama ka sa lahat: 1 in {:,}".format(4 ** x))


hula()