def add_contact():
    name = input("Введите имя контакта: ")
    phone = input("Введите телефон: ")

    new_contact = {name : phone}

    with open("PhoneBook.txt", 'a') as file:
        for key, value in new_contact.items():
            file.write(f'{key} - {value}\n')