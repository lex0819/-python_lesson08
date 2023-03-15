import view
import model


def run():
    view.greating()
    while True:
        view.menu()
        answer = input("Enter your chois: ")
        if int(answer) == 1:
            data = model.read_phonebook()
            view.show_phonebook(data)
        elif int(answer) == 2:
            data = model.add_contact()
            view.show_added(data)
        elif int(answer) == 3:
            data = model.find_contact()
        elif int(answer) == 4:
            break
