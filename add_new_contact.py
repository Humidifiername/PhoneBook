import csv
import create_book as cb

name = input('Введите имя контакта: ')
phone = int(input('Введите номер контакта: '))

def add_contact(name, phone):
    with open(cb.FILENAME, "a", newline="") as file:
        contact = [name, phone]
        writer = csv.writer(file)
        writer.writerow(contact)

add_contact(name, phone)