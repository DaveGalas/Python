import functs as fn
import json

commands = ["new", "view", "help", "stats", "recent", "exit"]


def intro():
    print("UPC Calls Tracker")
    print("For available commands, do command help \n")
    print("Total number of calls: {}".format(fn.num))
    fn.divide()


def start():
    while fn.status != "exit":
        fn.status = input("/".format(fn.num)).lower()

        if fn.status in commands:
            if fn.status == "new":
                fn.new(fn.num)
                fn.divide()

            elif fn.status == "view":
                fn.view()
                fn.divide()

            elif fn.status == "help":
                fn.help()
                fn.divide()

            elif fn.status == "stats":
                fn.stats()
                fn.divide()

            elif fn.status == "recent":
                print("\nTotal number of entries: {}".format(fn.num))
                count = input("   Number of entries to view: ")
                fn.recent(int(count) - 1)

        else:
            print("\nInvalid command, see below list of commands. Do command help for more information.")
            print(", ".join(commands), "\n")

    confirm_exit()


def confirm_exit():
    confirm = input("\nExit the tracker? This will save the current stamp. [Y/N]: ").lower()

    if confirm == "y":
        print("\nProgress saved.")
        with open('main.txt', 'w') as convert_file:
            convert_file.write(json.dumps(fn.calls))

    elif confirm == "n":
        fn.status = ""
        start()

    else:
        print("\nInvalid character.")
        confirm_exit()


intro()
start()
