class Contact:
   
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phonenumber = phone_number
        self.email = email
    def displayinfo(self):
       print("Name: ", self.name)
       print("Phone Number:", self.phonenumber)
       print("Email:", self.email)
class AddressBook:
    def __init__(self):
        self.contacts = []
    
    def contact(self):
        return self.contacts
    def addcontacts(self, contact):
        self.contacts.append(contact)
    
    def displaycontacts(self):
        if not self.contacts:
            print("No contacts in the address book.")
        for contact in self.contacts:
            contact.displayinfo()





contactnumber = int(input("What is the the number of the contacts you want ? "))



myaddressbook = AddressBook()






for i in range(int(contactnumber)):
   name = input("Name of contact: ")
   phonenumber = input("Phone number: ")
   email = input("Email: ")
   contact = Contact(name, phonenumber, email)
   myaddressbook.addcontacts(contact)
   
contact = Contact(name, phonenumber, email)

print("Here are the contacts in the address book:") 
myaddressbook.displaycontacts()