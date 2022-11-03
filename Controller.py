import Model
import View
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os

clear = lambda: os.system('cls')


def main_menu():
    while True:
        print('\nГлавное меню:')
        print('1. Показать все контакты')
        print('2. Открыть файл с контактами')
        print('3. Записать файл с контактами')
        print('4. Добавить контакт')
        print('5. Изменить контакт')
        print('6. Удалить контакт')
        print('7. Поиск по контактам')
        print('0. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        match (choice):
            case 1:
                clear()
                View.printPhoneBook()
            case 2:
                clear()
                what_path()
                if Model.path == '':
                    print('Не выбран файл с контактами')
                else:
                    open_file()
                    View.printPhoneBook()
            case 3:
                clear()
                save_file()
                print('\nФайл сохранен!\n')
            case 4:
                clear()
                add_contact()
                print('\nКонтакт добавлен\n')
            case 5:
                clear()
                change_contact()
            case 6:
                clear()
                remove_contact()
                print('\nКонтакт удален\n')
            case 7:
                clear()
                find_contact()
            case 0:
                break


def start():
    main_menu()


def what_path():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    Model.path = askopenfilename() # show an "Open" dialog box and return the path to the selected file


def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.phonebook)))

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};'
    Model.phonebook.append(contact)
    View.printPhoneBook()

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = Model.phonebook.pop(choice).split('; ')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, '; '.join(contact))
    View.printPhoneBook()


def find_contact():
    where_contact = []
    choice = int(input('По какому полю ищем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))
    find = input('Введите сравниваемое значение: ')
    for i in range(0, len(Model.phonebook)):
        contact = Model.phonebook[i].split('; ')
        if contact[choice] == find:
            where_contact.append(i)
    if where_contact == []:
        print('Совпадений не найдено')
    else:
        print(f'Найдено совпаление в строке {where_contact}')