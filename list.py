class Contact:
    def execute(self):
        self.name
        self.age

gustavo = Contact()
gustavo.name = "Gustavo"
gustavo.age = 18

joao = Contact()
joao.name = "Joao"
joao.age = 17

contacts = [gustavo, joao]

for contact in contacts:
    print("-------------------------------")
    print("First list! Contact with name:", contact.name, "and age:", contact.age)


maria = Contact()
maria.name = "Maria"
maria.age = 30

contacts.append(maria)
contacts.remove(joao)

for contact in contacts:
    print("-------------------------------")
    print("Second list! Contact with name:", contact.name, "and age:", contact.age)