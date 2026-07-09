import sys

def initialize_phone_book():
    rows, cols = int(input("Enter the Initial Number of contacts:")), 5

    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter the details for contact", i + 1)
        print("Note: Please enter the details in the following order: Name,Phone Number, Email, Address, Birthday, Category")
        print("........................................................................................")

        temp = []
        for j in range(cols):
            if j == 0:
                temp.append(input("Enter Name: "))
                if temp[j] == "" or temp[j] == " ":
                    sys.exit("Name cannot be empty. Please enter a valid name.")

                    if j == 1:
                        temp.append(input("Enter Phone Number: "))
                        if temp[j] == "" or temp[j] == " ":
                            sys.exit("Phone Number cannot be empty. Please enter a valid phone number.")

                    if j == 2:
                        temp.append(input("Enter Email: "))
                        if temp[j] == "" or temp[j] == " ":
                            temp[j] = "N/A"

                    if j == 3:
                        temp.append(input("Enter Birthday: "))
                        if temp[j] == "" or temp[j] == " ":
                            temp[j] = "N/A"

                    if j == 4:
                        temp.append(input("Enter Category: (Family, Friends, Work, Other): "))
                        if temp[j] == "" or temp[j] == " ":
                            temp[j] = "N/A"

        phone_book.append(temp)

        print(phone_book)
        return phone_book
    

def menu():
    print("*********************************************************************")
    print("Welcome to the Phone Book Application")
    print("*********************************************************************")
    print("You Can now perform the following operations on your Phone Book!")
    print("1. Add a new contact")
    print("2. Remove Existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit the application")

    choice = int(input("Please enter your choice: "))
    return choice  


def add_contact(phone_book):
    dip = []
    for i in range(len(phone_book[0])):
        if i == 0:
            dip.append(input("Enter Name: "))
            

        if i == 1:
            dip.append(input("Enter Phone Number: "))
                

        if i == 2:
            dip.append(input("Enter Email: "))
           

        if i == 3:
            dip.append(input("Enter Birthday: "))

        if i == 4:
            dip.append(input("Enter Category: (Family, Friends, Work, Other): "))
                
            phone_book.append(dip)

            return phone_book
def remove_contact(phone_book):
    query = input("Enter the name of the contact you want to remove: ")
    temp = 0

    for i in range(len(phone_book)):
        if query == phone_book[i][0]:
            temp += 1
            print(phone_book.pop(i))
            print("Contact removed successfully.")

            return phone_book
        if temp == 0:
            print("Contact not found.")
            return phone_book
        
        def delete_all_contacts(phone_book):
            return phone_book.clear()
        
        query = int(input("Please enter the the email of the contact you want to search for: "))
        for i in range(len(phone_book)):
            if query == phone_book[i][2]:
                print("Contact found: ", phone_book[i])
                return phone_book
            
        query = input("Please enter the name of the contact you want to search for: ")
        for i in range(len(phone_book)):
            if query == phone_book[i][0]:
                print("Contact found: ", phone_book[i])
                return phone_book
            
            elif choice==3:

             for i in range(len(phone_book)):
              if query == phone_book[i][3]:
                  check = i
                  temp.append(phone_book[i])

            elif choice==4:
             query = input("Please enter the category of the contact you want to search for: ")
        for i in range(len(phone_book)):
               if query == phone_book[i][4]:
                  print("Contact found: ", phone_book[i])
                  return phone_book

               elif choice==5:
                query = input("Please enter the phone number of the contact you want to search for: ")
        for i in range(len(phone_book)):
                if query == phone_book[i][1]:
                    print("Contact found: ", phone_book[i])
                    return phone_book
                
                else:
                    print("Invaild choice. Please enter a valid choice (1-6).")
                    return -1
                
                if check == -1:
                    return -1
                
                else:
                    display_all(temp)
                    return check
                
                def display_all(phone_book):
                    if not phone_book:
                        print("No contacts found.")
                    else:
                        for i in range(len(phone_book)):
                            print(phone_book[i])

def thanks ():
        
    print("*********************************************************************")
    print("Thank you for using the Phone Book Application. Have a great day!")
    print("Please come back again!")

print("*********************************************************************")
print("...........................................................................................")
print
("Hello user, Welcome to the Phone Book Application.!")
print
("...........................................................................................")

ch = 1
phone_book = initialize_phone_book()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        phone_book = add_contact(phone_book)
    elif ch == 2:
        phone_book = remove_contact(phone_book)
    elif ch == 3:
        phone_book = delete_all_contacts(phone_book)
    elif ch == 4:
        d = search_contact(phone_book)
        if d == -1:
            print("Contact not found.")
    elif ch == 5:
        display_all(phone_book)
    else:
        thanks()



                


        
        
    




                    


