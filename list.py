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
    print("Contact with name:", contact.name)
    print("Contact with age:", contact.age)