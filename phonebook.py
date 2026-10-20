import json

def save_contacts(contacts,filename):
    with open(filename,"w",encoding="utf-8") as f:
        json.dump(contacts,f, ensure_ascii=False,indent=2)

def load_contacts(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def find_phones(contacts, name):
    matches = []
    for contact in contacts:
        if contact["name"] == name:
            matches.append(contact["phone"])
    return matches

def add_contact(contacts, name, phone):
    contacts.append({"name": name, "phone": phone})

contacts = load_contacts("contacts.json")

while True:
    print("1 - Поиск")
    print("2 - Добавить")
    print("3 - Показать все")
    print("4 - Удалить")
    print("0 - Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        name = input("Введите имя: ")
        phones = find_phones(contacts, name)
        if len(phones) == 0:
            print("Контакт не найден")
        else:
            print("Найдено:", phones)

    elif choice == "2":
        name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        if name == "" or phone == "":
            print("Имя и телефон не могут быть пустыми")
        elif phone in find_phones(contacts, name):
            print("Такой контакт уже есть")
        else:
            add_contact(contacts, name, phone)
            save_contacts(contacts, "contacts.json")
            print("Контакт добавлен")

    elif choice == "3":
        number = 1
        if len(contacts) == 0:
            print("Список пуст")
        else:
            for contact in contacts:
                print(f"{number}. {contact['name']} {contact['phone']}")
                number = number + 1

    elif choice == "4":
        name = input("Введите имя: ")
        phone = input("Введите телефон: ")
        found = False
        for contact in contacts:
            if contact["name"] == name and contact["phone"] == phone:
                contacts.remove(contact)
                save_contacts(contacts, "contacts.json")
                print("Контакт удалён")
                found = True
                break
        if not found:
            print("Контакт не найден")
    
    elif choice == "0":
        break
    else:
        print("Неизвестная команда")