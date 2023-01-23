def find_phone():
    phone = input("Введите номер телефона, имя, которого вы хотите найти: ")
    with open("PhoneBook.txt") as file:
        for line in file:
            if phone in line:
                print(line)