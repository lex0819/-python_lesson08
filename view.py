def greating():
    print("Hi, gays!\nWelcome to the phonebook!")


def menu():
    print("1 - show all contacts")
    print("2 - add contact")
    print("3 - find contact")
    print("4 - remove contact")
    print("5 - exit")


def show_phonebook(data: list):
    print(f"Весь список абонентов. {len(data)}")
    print(f"Фамилия'\t'Имя'\t'Номер телефона")
    for item in data:
        print(f"{item.get('surname')}'\t'{item.get('name')}'\t'{item.get('phone')}")


def show_added(data):
    print(f"{data['surname']} {data['name']} {data['phone']} were added")


def show_found(data: list):
    count = len(data)
    print(f"Найдено {count}")
    for item in data:
        print(f"{item.get('surname')}'\t'{item.get('name')}'\t'{item.get('phone')}")
    if count == 0:
        print("нет такого абонента")
