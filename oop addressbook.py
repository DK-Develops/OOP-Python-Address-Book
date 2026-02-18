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
    def deletecontact(self, name):
        #for contacts in self.contacts:
            # if self.contacts == name:
               # self.contacts.remove(name)
              #  print("Contact deleted successfully.")
                # for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' has been deleted.")
                return
            print(f"Contact '{name}' not found in the address book.")

    def lookupcontact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
            else:
                print(f"Contact '{name}' not found in the address book.")



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

userInput = input("do you want to delete a contact? (y/n) ")

if userInput.lower() == "y":
    name = input("Enter the name of the contact you want to delete: ")
    myaddressbook.deletecontact(name)
   
else:
    print("No contacts will be deleted.")

     
lookup = input("do you want to look up a contact? (y/n) ")

if lookup.lower() == "y":

    name = input("Enter the name of the contact you want to look up: ")
    myaddressbook.lookupcontact(name)
else:
    print("No contacts will be looked up.")




  







myaddressbook.displaycontacts()

  

