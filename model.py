import csv
FILE_NAME = 'phonebook.csv'


def read_phonebook(file_name=FILE_NAME) -> list:
    data = []
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for line in reader:
            data.append(
                {'surname': line[0],
                 'name': line[1],
                 'phone': line[2]
                 }
            )
    return data


def add_contact(file_name=FILE_NAME) -> dict:
    surname = input("enter surname: ")
    name = input("enter name: ")
    phone = input("enter phone: ")
    with open(file_name, 'a') as file:
        writer = csv.writer(file)
        writer.writerow([surname, name, phone])
    return {'surname': surname, 'name': name, 'phone': phone}


def find_contact() -> list:
    surname = input("enter surname: ")
    name = input("enter name: ")

    data_file = read_phonebook(file_name=FILE_NAME)
    # print(data_file)
    if surname and name:
        data = list(
            filter(lambda x: x['surname'].lower() == surname.lower() and x['name'].lower() == name.lower(), data_file))
    elif surname and not name:
        data = list(
            filter(lambda x: x['surname'].lower() == surname.lower(), data_file))
    elif name and not surname:
        data = list(
            filter(lambda x: x['name'].lower() == name.lower(), data_file))

    return data
