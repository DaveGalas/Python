def isPalindrome(x):
    things = []
    # for numbers with even digits
    if len(str(x)) % 2 == 0:

        # turn every digit into an element in the list things
        for i in str(x):
            things.append(i)

        # get the number of digits of the number / 2
        n = len(things) // 2

        # get the first half of the list things then reverse
        o = things[:-n][::-1]

        # get the second half of the list things
        p = things[n:]

        # if the reverse of the half is equal to the other half, it is a palindrome and will return True
        return o == p

    # for numbers with odd digits
    else:

        # get the number of the digits - 1 / 2
        n = len(str(x)) // 2

        # get the middle number
        o = str(x)[n]

        # append every digit of x to the list things except the middle number
        for i in str(x):
            if i != o:
                things.append(i)

        # get the first half of the list things then reverse
        p = things[:n][::-1]

        # get the second half of the list things
        q = things[n:]

        # if the reverse of the half is equal to the other half, it is a palindrome and will return True
        return p == q


print(isPalindrome(int(input("Number: "))))
