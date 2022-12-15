def romanToInt(s):

    t = s.lower()

    roman_numerals = {
        "m": 1000,
        "d": 500,
        "c": 100,
        "l": 50,
        "x": 10,
        "v": 5,
        "i": 1
    }

    numbers = []
    numbers_proper = []

    for letter in t:
        numbers.append(roman_numerals[letter])
    i = 0

    while i < len(numbers) - 1:
        cur_num = numbers[i]
        aft_num = numbers[i+1]

        if cur_num >= aft_num:
            numbers_proper.append(cur_num)

        else:
            numbers_proper.append(cur_num * -1)

        i += 1

    numbers_proper.append(numbers[len(numbers) - 1])

    count = 0

    for number in numbers_proper:
        count += number

    return count


print(romanToInt(input("Roman Numeral: ").lower()))
