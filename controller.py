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
            view.show_found(data)
        elif int(answer) == 4:
            data = model.find_contact()
            ok = view.question_remove(data)
            if ok.lower() == 'y':
                model.remove_contact(data)
                view.show_removed(data)
        elif int(answer) == 5:
            break
