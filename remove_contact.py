def remove():
    number_str = int(input("Введите номер строки, контакт которой вы хотите удалить, отсчет начинайте с нуля: "))
    with open("PhoneBook.txt", "r") as file:
        lines = file.readlines()
        del lines[number_str]
    with open("PhoneBook.txt", "w") as file:
        file.writelines(lines)