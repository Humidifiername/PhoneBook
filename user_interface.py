import show_record as shr
import find_record_name as frn
import find_record_phone as frp
import add_new_contact as anc
import remove_contact as rc

print('Здравствуйте, вас приветствует телефонная книга на английском языке, выберете необходимый пункт меню: ')
def print_menu():
    print('1 - Показать все записи\n 2 - Найти запись по имени\n 3 - Найти запись по номеру телефона\n 4 - Добавить запись\n 5 - Удалить запись\n 6 - Вход\n')

    number_menu = int(input("Кликни нужную цифру: "))

    if number_menu == 1:
        shr.show()
        print_menu()
    elif number_menu == 2:
        frn.find_name()
        print_menu()
    elif number_menu == 3:
        frp.find_phone()
        print_menu()
    elif number_menu == 4:
        anc.add_contact()
        print_menu()
    elif number_menu == 5:
        rc.remove()
        print_menu()
    elif number_menu == 6:
        print("До свидания!")
    else:
        print("Такого пункта меню нет")
        print_menu()
print_menu()