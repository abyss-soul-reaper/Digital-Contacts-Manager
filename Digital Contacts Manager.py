import os 

Consent_Terms = ('Yes', 'Ok', 'Yeah', 'Yup', 'Confirm', 'Y', 'O')

Termination_Terms = ('No', 'Nope', 'Cancel','Done', 'Exit', 'N', 'D', 'E' )

# print (os.getcwd())

# print (os.path.abspath(__file__))

# print (os.path.dirname(os.path.abspath(__file__)))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print (os.getcwd())

file_path = 'digital contacts manager.txt'

def ensure_data_file_exists() :

    if not os.path.exists(file_path) :

        print ('File Not Found. Creating New File...')

        with open (file_path, 'w', encoding= 'utf-8') as file :

            file.write('Name, Age, Country, Phone\n')

def check_file(contact_data) :

    ensure_data_file_exists()

    with open (file_path, 'r') as file :

        file_data = file.read()

        if contact_data in file_data :

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

    else :

        print ('Contact Already Exists.')

def view_contact() :

    ensure_data_file_exists()

    count = 1

    with open (file_path, 'r') as file :

        lines = file.readlines()

    contacts_lines = lines[1:]

    if not contacts_lines :

        print ('No Contacts To See.')

        return
    
    for info in contacts_lines :

        print (f'- {str(count).zfill(2)}. {info.strip()}')
        count += 1
    
def search_contacts() :

    ensure_data_file_exists()

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

        elif choice in Termination_Terms :

            print('Exiting...')

            break

        else :

            print ('Invalid choice.') 

if __name__ == '__main__' :

    main_menu()