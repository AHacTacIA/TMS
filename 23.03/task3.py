# Написать программу телефонная книга используя классы. Написать класс телефонной книги, который хранит список
# контактов. Он должен иметь возможность искать контакты по имени и по телефону (два разных метода), добавлять новые
# контакты и удалять контакты по имени или телефону. Контакты реализовать в виде объектов класса Контакт. Данные
# телефонной книги хранить в json файле.
import json


class Contact:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class PhoneBook:

    def add(self, contact: Contact):
        json_data = {
            "name": contact.name,
            "phone": contact.phone,
        }
        data = json.load(open(self.file))
        data.append(json_data)
        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)

    def find_by_name(self, name: str) -> str:
        with open(self.file, "r") as json_file:
            data = json.load(json_file)
            for contact in data:
                if contact['name'] == name:
                    return contact['phone']

    def find_by_phone(self, phone: str) -> str:
        with open(self.file, "r") as json_file:
            data = json.load(json_file)
            for contact in data:
                if contact['phone'] == phone:
                    return contact['name']

    def delete_by_phone(self, phone: str):
        with open(self.file, "r") as json_file:
            data = json.load(json_file)
            for i, contact in enumerate(data):
                if contact['phone'] == phone:
                    data.pop(i)
        with open(self.file, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def delete_by_name(self, name: str):
        with open(self.file, "r") as json_file:
            data = json.load(json_file)
            for i, contact in enumerate(data):
                if contact['name'] == name:
                    data.pop(i)
        with open(self.file, "w") as json_file:
            json.dump(data, json_file, indent=4)

    def __init__(self, contact: Contact, file_name: str ='book.json'):
        self.file = file_name
        json_data = [{
            "name": contact.name,
            "phone": contact.phone,
        }
        ]
        with open(self.file, 'w') as file:
            file.write(json.dumps(json_data, indent=4))


def get_data() -> list[Contact]:
    with open("text.txt", "r") as file:
        strings = []
        contacts = []
        for string in file:
            name, phone = string.split()
            contacts.append(Contact(name, phone))
    return contacts


contact_list = get_data()

b1 = PhoneBook(contact_list[0], "book2.json")
for i in range(1, len(contact_list)):
    b1.add(contact_list[i])

print(f"Телефон контакта по имени Tom: {b1.find_by_name('Tom')}")
print(f"Имя контакта с телефоном +375290000004: {b1.find_by_phone('+375290000004')}")
b1.delete_by_phone('+375290000004')
b1.delete_by_name('Tom')
