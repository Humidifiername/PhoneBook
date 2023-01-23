def show():
    with open("PhoneBook.txt", "r") as file:
        for line in file:
            print(f'{line}')