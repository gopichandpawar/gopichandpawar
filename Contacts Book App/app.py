#Contact Book Management App

Contacts = {}
while True:
    print("\nContact book App")
    print("1, Add contact")
    print("2, Update contact")
    print("3, View all Contact")
    print("4, Remove contact")
    print("5, Search contact")
    print("6, Count contact")
    print("7, Exit")

    choice = input("enter you choice =")

    if(choice == '1'):
        name = input("enter you name =")
        if(name in Contacts):
            print(f"contact name {name} already exists")
        else:
            age = int(input('enter age ='))
            mobile = input('enter mobile =')
            email = input('enter email =')
            Contacts[name] = {"age":age, "mobile":mobile, "email":email}
            print(f"contact name {name} has been created successfully")
        
    elif(choice == '2'):
        name = input("enter contact name to Update =")
        if(name in Contacts):
            age = int(input("enter update age ="))
            mobile = input("enter update mobile =")
            email = input("enter update email =")
            Contacts[name] = {"age":age, "mobile":mobile, "email":email}
            print(f"contact name {name} has been updated successfully")
        else:
            print("contact not found")
    
    elif(choice == '3'):
        name = input("enter contact name to view =")
        if(name in Contacts):
            contact = Contacts[name]
            print(f"age:{age}, mobile:{mobile}, email:{email}")
        else:
            print("contact not found")
    
    elif(choice == '4'):
        name = input("enter contact name to delete =")
        if(name in Contacts):
            del Contacts[name]
            print(f"contact name {name} has been delete successfully")
        else:
            print("contact not found")

    elif(choice == '5'):
        search_name = input("enter contact name to search contact =")
        found = False 
        for name, contact in Contacts.items():
            if(search_name.lower() in name.lower()):
                print(f"found = name:{name}, age:{age}, mobile:{mobile}, email:{email}")
                found = True
        if(not found):
            print("not contact found with that name")
    
    elif(choice == '6'):
        print(f"Tatal contact you book: {len(Contacts)}")
    
    elif(choice == '7'):
        print("good by, closing progrm..!")
        break
    
    else:
        print("invalid input")