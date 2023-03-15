def greating():
    print("Hi, gays!")


def menu():
    print("1 - show all contacts")
    print("2 - add contact")
    print("3 - find contact")
    print("4 - exit")


def show_phonebook(data: list):
    print(f"Фамилия'\t'Имя'\t'Номер телефона")
    for item in data:
        print(f"{item.get('surname')}'\t'{item.get('name')}'\t'{item.get('phone')}")


def show_added(data):
    print(f"{data['surname']} {data['name']} {data['phone']} were added")
