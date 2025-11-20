import os 

# print (os.getcwd())

# print (os.path.abspath(__file__))

# print (os.path.dirname(os.path.abspath(__file__)))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print (os.getcwd())

file_path = 'address book.txt'

def check_file(contact_data) :

    with open (file_path, 'r') as file :

        file_data = file.read()

        if contact_data in file_data :

            print ('Contact Already Exists.')

            return True 
        
        else :
            
            return False
        
def add_contact() :

    name = input ('Enter Name: ').strip().capitalize()
    age = int (input ('Enter Your Age: '))
    country = input ('Enter Your Country: ').strip().capitalize()
    phone = input ('Enter Phone Number: ')

    contact_data = f"{name}, {age}, {country}, {phone}\n"

    result = check_file(contact_data)

    if not result:

        with open (file_path, 'a') as file :

            file.write(contact_data)

        print (f'Contact For {name} Saved Successfully.')

def view_contact() :

    count = 1

    with open (file_path, 'r') as file :

        for info in file :

            print (f'- {count} {info.strip()}')

            count += 1

def search_contacts() :

    search_term = input ('Enter Name: ').strip().lower()

    with open (file_path, 'r') as file :

        all_contacts = file.readlines()

    found = False

    for contact_line in all_contacts :

        if search_term in contact_line.lower() :

            print (contact_line.strip())

            found = True

    if not found :

        print ('No Matching Contacts Found.')

def main_menu() :

    while True :

        print ('What Do You Want To Choose?\nAdd\nView\nContact\nExit')

        choice = input ().strip().capitalize()

        if choice == 'Add' or choice == 'A' :

            add_contact()

        elif choice == 'View' or choice == 'V' :

            view_contact()

        elif choice == 'Contact' or choice == 'C' :

            search_contacts()

        elif choice == 'Exit' or choice == 'E' :

            print('Exiting...')

            break

        else :

            print ('Invalid choice.') 

if __name__ == '__main__' :

    main_menu()