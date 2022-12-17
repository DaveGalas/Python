def longestCommonSubsequence(text1, text2):

    a = [x for x in text1 if x in text2]
    b = [x for x in text2 if x in text1]

    i = 0

    c = []

    for x in a:
        if a.index(x) <= b.index(x):
            c.append(x)

    d = {}

    for x in c:
        if d.keys().count(x) == 0:
            d[x] += 1

    return print(a, b)


r = input("Text 1: ")
s = input("Text 2: ")

longestCommonSubsequence(r, s)
