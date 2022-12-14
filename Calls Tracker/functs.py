import datetime


status = ""

calls = {1: ["test1", "test1", "test1", "test1"],
         2: ["test2", "test2", "test2", "test1"],
         3: ["test3", "test3", "test3", "test1"],
         4: ["test4", "test4", "test4", "test1"],
         5: ["test5", "test5", "test5", "test1"],
         6: ["test6", "test6", "test6", "test1"],
         }

num = len(calls)


def divide():
    print("-------------------------------------------------- ")

def new(num):
    count = num + 1
    time = datetime.datetime.today()

    print("Entry #: {}".format(count))
    print("Time: {}\n".format(time.strftime("%a, %b %d, %Y [%I:%M:%S]")))

    pol = input("Policy Number: \t")
    cal = input("Caller: \t\t")
    res = input("Resolution: \t")

    calls[count] = [pol, cal, res, time.strftime("%a, %b %d, %Y [%I:%M:%S]")]

    action = "\n" \
             "  Inserted # {}: \n" \
             "\t{}\n" \
             "\tPolicy number: \t{}\n" \
             "\tCaller: \t\t{}\n" \
             "\tResolution: \t{}\n" \
             "".format(count, time.strftime("%a, %b %d, %Y [%I:%M:%S]"), pol, cal, res)

    print(action)


def view():
    req = input("What entry? : ")

    count = int(req)
    pol = calls[count][0]
    cal = calls[count][1]
    res = calls[count][2]
    time = calls[count][3]

    view = "\n" \
           "  Entry # {}: \n" \
           "\t{}\n" \
           "\tPolicy number: \t{}\n" \
           "\tCaller: \t\t{}\n" \
           "\tResolution: \t{}\n" \
           "".format(count, time, pol, cal, res)

    print(view)

def help():
    instance = ""
    print("--------------------------------------------------")
    print(f"Available commands: ")
    print(f"new {instance}\t\t\t: Adds a new entry.")
    print(f"view {instance}\t\t\t: Views a new entry.")
    print(f"help {instance}\t\t\t: Display available commands.")
    print(f"stats {instance}\t\t\t: Views current statistics.")
    print(f"recent<number> {instance}\t: Views number of recent entries.")
    print(f"exit {instance}\t\t\t: Exits the tracker.")
    print("--------------------------------------------------")


def stats():
    print("--------------------------------------------------")
    print("Total calls: {}".format(num))
    print("--------------------------------------------------")


def recent(n):
    i = 0
    if n + 1 > len(calls):
        print("\nMaximum is {}.\n".format(len(calls)))
        count = input("Number: ")
        recent(int(count) - 1)
    else:
        print("\n--------------------------------------------------")
        while i <= n:
            count = len(calls)
            pol = calls[count - i][0]
            cal = calls[count - i][1]
            res = calls[count - i][2]
            time = calls[count - i][3]

            print("| {}\t| {} |{}\t{}\t{}\t".format(count - i, time, pol, cal, res))
            i += 1
        print("--------------------------------------------------")
