def isPalindrome(x):
    things = []
    if len(str(x)) % 2 == 0:
        # even number of digits

        q = True

        for i in str(x):
            things.append(i)

        n = len(things) // 2
        o = things[:-n][::-1]
        p = things[n:]

        return o == p
    else:
        # odd number of digits

        n = (len(str(x)) // 2)
        o = str(x)[n]

        y = []

        for i in str(x):
            y.append(i)

        y.pop(int(o) + 1)

        p = len(y) // 2
        q = y[:p][::-1]
        r = y[p:]

        return q == r




print(isPalindrome(input("Number: ")))