import copy
import csv
FILE_NAME = 'phonebook.csv'


def read_phonebook(file_name=FILE_NAME) -> list:
    data = list()
    with open(file_name, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in list(reader):
            data.append(
                {'surname': row['surname'], 'name': row['name'], 'phone': row['phone']})
    return data


def rewrite_phonebook(data_file: list, file_name=FILE_NAME):
    with open(file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data_file[0])
        writer.writeheader()
        writer.writerows(data_file)


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
    data = []
    data_file = read_phonebook()
    if len(data_file) > 0:
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


def remove_contact(data: list):
    for item in data:
        data_file = read_phonebook()
        if len(data_file):
            data_res = list(filter(lambda x: x['surname'].lower() != item['surname'].lower(
            ) and x['name'].lower() != item['name'].lower(), data_file))
            rewrite_phonebook(data_res)
