def slambook():
    contacts = []

    while True:
        print("******** SLAMBOOK MENU ********")
        print("1. Add new contact")
        print("2. View all contacts")
        print("3. Search contact by name")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Add new contact
            name = input("Name: ")
            number = input("Phone number: ")
            about = input("Something about your friend: ")
            dob = input("Date of birth (dd/mm/yy): ")
            category = input("Category (Family/Friends/Work/Others): ")

            contact = {
                "Name": name,
                "Number": number,
                "About": about,
                "DOB": dob,
                "Category": category
            }
            contacts.append(contact)
            print("Contact added successfully!")

        elif choice == "2":
            # View all contacts
            if not contacts:
                print("No contacts found.")
            else:
                print("--- Slambook Contacts ---")
                for i, c in enumerate(contacts, start=1):
                    print(f"\nContact {i}:")
                    for key, value in c.items():
                        print(f"{key}: {value}")

        elif choice == "3":
            # Search contact by name
            search_name = input("Enter name to search: ")
            found = False
            for c in contacts:
                if c["Name"].lower() == search_name.lower():
                    print("Contact found:")
                    for key, value in c.items():
                        print(f"{key}: {value}")
                    found = True
                    break
            if not found:
                print("No contact found with that name.")

        elif choice == "4":
            print("Exiting Slambook. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

slambook()
