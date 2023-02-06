# Создать телефонный справочник
# Функции справочника:
# - Показать все записи
# - Найти запись по вхождению частей имени
# - Найти запись по телефону
# - Добавить новый контакт
# - Удалить контакт
# - Изменить номер телефона у контакта

#==========================================================================================================
import os
import time

fileName = 'Phonebook.txt'

def cls():
    os.system('cls')
cls()    


def rewrite_data(result, answer, line, contact_id, file_name):
    new_data = input("Введите новое значение: ")
    result[answer - 1] = new_data
    result[len(result) - 1] += '\n'
    line[contact_id - 1] = ' '.join(result)
    with open (file_name, 'w', encoding = 'utf-8') as data:
        for i in line:
            data.write(i)

def writeFile (file_name):
    cls()
    print('*****Добавление нового контакта*****')

    while True:
        with open (file_name, 'a+', encoding = 'utf-8') as data:
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            patronymic = input('Отчество: ')
            phone_number = input('Номер телефона: ')

            data.writelines(f'\n{last_name} {first_name} {patronymic} {phone_number}')
            choice = input('Нажмите Enter чтобы добавить новый контакт\nВведите 0 для выхода\n')
            if choice == '0': 
                return 
        
def readFile (file_name):
    cls()
    print('*****Список контактов*****')
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
            
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')
        choice = input('\nНажмите 0 для выхода\n')
        if choice == '0': 
            return
    
def findContactByKeyWord (file_name):
    cls()
    print('*****Поиск контакта*****')
    while True:
        key_word = input('Введите ФИО или номер телефона для поиска: ').casefold()
        
        with open(file_name, 'r', encoding = 'utf-8') as data:
            count = 0
            for line in data:
                if key_word in line.casefold(): 
                    print(line)
                    count += 1
            if count == 0: print('Контакт не найден.')
            else: print(f'Найдено контактов: {count}')    
        choice = input('\nНажмите Enter для продолжения или 0 для выхода\n')
        if choice == '0': 
            return
        

def DeleteContact(file_name):
    cls()
    print('*****Удаление контакта*****\n')             
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
        
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')
        
        deleted_str = int(input('Введите номер контакта, который хотите удалить: '))
        del line[deleted_str - 1]
        
        with open (file_name, 'w', encoding = 'utf-8') as data:
            for i in line:
                data.write(i)
        choice = input('\nНажмите Enter, чтобы продолжить удаление контактов\nВведите 0 для выхода\n')
        if choice == '0': 
            return   
        
def ReplaceData(file_name):
    cls()
    print('*****Изменение данных*****')             
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
            
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')

        contact_id = int(input('Введите порядковый номер контакта: '))
        result = line[contact_id - 1].split()

        answer = int(input('Какие данные хотите изменить?\n'
                        '1 - Фамиля\n'
                        '2 - Имя\n'
                        '3 - Отчество\n'
                        '4 - Номер телефона\n'
                        '0 - для выхода\n'))
        
        
        if (answer == 1) or (answer == 2) or (answer == 3) or (answer == 4):
            rewrite_data(result, answer, line, contact_id, fileName)
                    
        choice = input('\nНажмите Enter, чтобы продолжить изменение контактов\nВведите 0 для выхода\n')
        if choice == '0': 
            return


def main_menu():
    cls()
    print('*****Главное меню*****')
 
    print('1 - Показать все записи\n'
          '2 - Найти запись по ФИО или номеру телефона\n'
          '3 - Добавить новый контакт\n'
          '4 - Удалить контакт\n'
          '5 - Изменить данные контакта\n'
          '0 - Выход')

def Phonebook():
    while True:
        main_menu()
        user_choice = input('Выберете необходимый пункт меню: ')

        match user_choice:
            case '1':
                  if os.path.exists(fileName): readFile(fileName)
                  else: 
                    print('Контакты отсутствуют. Создайте хотя бы один контакт. Выход в главное меню через 3 секунды...')
                    time.sleep(3)      
            case '2': findContactByKeyWord(fileName)
            case '3': writeFile(fileName)
            case '4': DeleteContact(fileName)
            case '5': ReplaceData(fileName)
            case '0': 
                print('До новых встреч!')
                break
            case _: 
                print('Будьте внимательнее!')
                time.sleep(1)   
            
Phonebook() 