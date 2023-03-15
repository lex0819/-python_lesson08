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
