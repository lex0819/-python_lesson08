def greating():
    print("\nHi, gays!\nWelcome to the phonebook!")


def menu():
    print("\n1 - show all contacts")
    print("2 - add contact")
    print("3 - find contact")
    print("4 - remove contact")
    print("5 - exit")


def show_phonebook(data: list):
    count = len(data)
    print(f"\nList of abonents contains {count} rows.")
    if count > 0:
        print(f"Surname'\t'Name'\t'Phone number")
    for item in data:
        print(f"{item.get('surname')}'\t'{item.get('name')}'\t'{item.get('phone')}")


def show_added(data):
    print(f"{data['surname']} {data['name']} {data['phone']} were added")


def show_found(data: list):
    count = len(data)
    print(f"{count} rows were found\n")
    for item in data:
        print(f"{item.get('surname')}'\t'{item.get('name')}'\t'{item.get('phone')}")
    if count == 0:
        print("abonent not found")


def question_remove(data) -> str:
    count = len(data)
    if count >= 1:
        print(f"{count} rows were found\n")
        for item in data:
            print(
                f"{item.get('surname')}'\t'{item.get('name')}'\t'{item.get('phone')}")
        answer = input(
            f"\nDo you want to remove {count} rows? Y/N - ")
        return answer
    else:
        print("нет такого абонента")
        return 'n'


def show_removed(data):
    count = len(data)
    print(f"{count} rows were removed.")
    for item in data:
        print(f"{item.get('surname')}'\t'{item.get('name')}'\t'{item.get('phone')}")
