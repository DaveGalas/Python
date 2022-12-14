import pyperclip


def convert_256_to_ratio(n):

    list = []

    for character in n:
        if character != ",":
            list.append(character)
            
    o = "".join(list)

    p = o.split()

    list2 = []

    for number in p:
        q = int(number) / 256
        list2.append("{:.5f}".format(q))

    r = "(" + ", ".join(list2) + ")"

    pyperclip.copy(r)

    print(f"Copied {r}")

m = input("RGB: ")

convert_256_to_ratio(m)