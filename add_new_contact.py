import create_book as cb

name = input("Введите имя контакта: ")
phone = input("Введите телефон: ")

new_contact = {name : phone}

with open(cb.FILENAME, 'a') as file:
    for key, value in new_contact.items():
        file.write(f'{key} - {value}\n')
