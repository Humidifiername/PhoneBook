def find_name():
    name = input("Введите имя которое вы хотите найти: ")
    with open("PhoneBook.txt","r") as myfile:
        for line in myfile:
            if name in line:
                print(line)