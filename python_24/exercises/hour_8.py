name_list = ["Ada", "Becky", "Celia", "Diana"]


def main():
    print("Welcome to the student check!")
    while True:
        name = raw_input(
            "Please give me the name of a student(enter 'q' to quit): ")
        if name == 'q':
            print("Good bye!")
            break

        check_name(name)


def check_name(name):
    if name in name_list:
        print("Yes, that student is enrolled in the class!")
    else:
        print("No, that student is not in the class.")


if __name__ == "__main__":
    main()
