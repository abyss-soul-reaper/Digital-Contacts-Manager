import os 

from datetime import datetime

from uuid import uuid4

Consent_Terms = ('Yes', 'Ok', 'Yeah', 'Yup', 'Confirm', 'Y', 'O')

Termination_Terms = ('No', 'Nope', 'Cancel','Done', 'Exit', 'N', 'D', 'E' )

Available_features = ('Add', 'Delete', 'View', 'Search contacts', 'Update Info', 'Feedback', 'Contact Us',)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# print (os.getcwd())

file_path = 'digital contacts manager.txt'

def ensure_data_file_exists() :

    if not os.path.exists(file_path) :

        print ('File Not Found. Creating New File...')

        with open (file_path, 'w', encoding= 'utf-8') as file :

            file.write('Date,Name,Age,Address,Phone,ID\n')

def check_file(phone, exclude_id=None):

    ensure_data_file_exists()

    with open(file_path, 'r') as file:

        next(file, None)

        for line in file:
            parts = line.strip().split(',')

            if len(parts) >= 6 and parts[4] == phone:

                if exclude_id and parts[5] == exclude_id:
                    continue
                return True
    return False

def add_contact() :

    name = input ('Enter Name: ').strip().title()
    while True :
        age_str = (input ('Enter Your Age: '))
        if age_str.isdigit() :
            age = int(age_str)
            break
        else :
            print("❌ Age Can't Be Empty or Non-numeric. Enter Age:")
    Address = input ('Enter Your Address: ').strip().title()
    phone = input ('Enter Phone Number: ')

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    contact_id = str(uuid4())

    contact_data = f"{timestamp},{name},{age},{Address},{phone},{contact_id}\n"

    result = check_file(phone)

    if not result:

        with open (file_path, 'a') as file :

            file.write(contact_data)

        print (f'Contact For {name} Saved Successfully.')

    else :

        print ('Contact Already Exists.')
    
def delete_contact(contact_id) :

    ensure_data_file_exists()
    found = False
    kept_lines = []

    try:

        with open(file_path, 'r', encoding= 'utf-8') as file :
            header = next(file)
            kept_lines.append(header)

            for line in file :

                parts = line.strip().split(',')

                if len(parts) >= 6 and parts[5] == contact_id :
                    found = True
                    continue

                kept_lines.append(line)

    except FileNotFoundError:
        print(f"❌ Error: User data file not found: {file_path}")
        return

    if not found :
        print(f"❌ No contact found with ID: {contact_id}")
        return
    
    try:

        with open(file_path, 'w', encoding='utf-8') as file :

            file.writelines(kept_lines)

        print("=" * 60)
        print(f"🗑️ Contact with ID {contact_id} has been successfully deleted.")
        print("=" * 60)

    except Exception as e:
        print(f"❌ An error occurred while updating the file: {e}")

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

    found = False

    count = 1

    try :

        with open (file_path, 'r', encoding= 'utf-8') as file :
            next(file, None)
            header_printed = False

            for line in file : 

                original_parts = line.strip().split(',')

                searchable_line = line.lower()

                if search_term in searchable_line :

                    if len(original_parts) >= 6 :

                        if not header_printed :

                            print("=" * 80)
                            print(f"{'Name':<25}{'Age':<10}{'Address':<30}{'Phone':<15}{'ID':<70}")
                            print("=" * 80)
                            header_printed = True

                        contact = {
                            "Timestamp" : original_parts[0],
                            'Name' : original_parts[1].title(),
                            'Age' : int(original_parts[2]),
                            'Address' : original_parts[3].title(),
                            'Phone' : original_parts[4],
                            'ID' : original_parts[5]
                        }

                        print(
                            f"- {str(count).zfill(2)}. {contact['Name']:<20}"
                            f"{contact['Age']:<10}"
                            f"{contact['Address']:<30}"
                            f"{contact['Phone']:<15}"
                            f"{contact['ID']:<70}"
                        )

                        count += 1

                        found = True

            if header_printed :
                print("=" * 80) 
            
    except FileNotFoundError :

        print(f"❌ Error: User data file not found: {file_path}")
        return

    if not found :

        print ('No Matching Contacts Found.')

def get_info(current_data, termination_terms) :

    current_name = current_data['Name']
    current_age = current_data['Age']
    current_address = current_data['Address']
    current_phone = current_data['Phone']
    current_id = current_data['ID']

    print("User Data Update Options:")
    print("1. Partial Update (Change one or more fields).")
    print("2. Full Re-entry (Fill all fields again).")
    print("3. Cancel Update.")

    choice = input().strip()

    if choice == '3' or choice in termination_terms :

        print("🚫 Update operation cancelled.")
        return None,None,None,None,None # Return None for all fields
    
    elif choice == '1' :

        print("📝 Partial Update Mode (Leave blank to keep current value):")

        # --- Name ---
        new_name = input(f"   Name (Current: {current_name}): ").strip().title()
        new_name = new_name if new_name else current_name

        # --- Age ---
        new_age_str = input(f"   Age (Current: {current_age}): ").strip()

        if not new_age_str:
            new_age = current_age
        elif new_age_str.isdigit():
            new_age = int(new_age_str)
        else:
            print("⚠️ Invalid age. Keeping previous value.")
            new_age = current_age


        # --- Address ---
        new_address = input(f"   Address (Current: {current_address}): ").strip().title()
        new_address = new_address if new_address else current_address

        # --- Phone ---
        new_phone_input = input(f"   Phone (Current: {current_phone}): ")

        if not new_phone_input:
            new_phone = current_phone

        elif new_phone_input == current_phone:
            new_phone = current_phone

        else:
            if check_file(new_phone_input, current_id):
                print("❌ This phone number already exists in another contact. Keeping old number.")
                new_phone = current_phone
            else:
                new_phone = new_phone_input


        return new_name, new_age, new_address, new_phone,current_id
    
    elif choice == '2' :

        print("📝 Full Re-entry Mode (All fields must be filled):")

        # --- New Name ---
        new_name = input("   New Name: ").strip().title()
        while not new_name :
            new_name = input("   Name Can\'t Be Empty. Enter Name: ")

        # --- New Age ---
        while True:
            new_age_str = input("   New Age: ").strip()
            if  new_age_str.isdigit():
                new_age = int(new_age_str)
                break
            else :
                print("❌ Age Can't Be Empty or Non-numeric. Enter Age:")

        # --- New Address ---
        new_address = input("   New Address: ").strip().title()
        while not new_address :
            new_address = input("   Address Can\'t Be Empty. Enter Address: ").strip().title()

        # --- New Phone ---
        new_phone = input("   New Phone: ")
        while not new_phone :
            new_phone = input("   Phone Can\'t Be Empty. Enter Phone: ")

        return new_name, new_age, new_address, new_phone,current_id
    
    else :
        print("⚠️ Invalid option. Update cancelled.")
        return None, None, None, None, None

def update_info(contact_id) :

    lines = []
    found_and_updated = False

    try :

        with open (file_path, 'r', encoding= 'utf-8') as file :
            lines = file.readlines()

    except FileNotFoundError :

        print(f"❌ Error: User data file not found: {file_path}")
        return
    
    header_line = lines[0] if lines else ''
    data_lines = lines[1:]
    
    for i, line in enumerate(data_lines) :

        parts = line.strip().split(',')

        if len(parts) >= 6 and parts[5] == contact_id :

            current_data = {
                "Timestamp" : parts[0],
                'Name' : parts[1].capitalize(),
                'Age' : int(parts[2]),
                'Address' : parts[3].title(),
                'Phone' : parts[4],
                'ID' : parts[5]
            }

            results = get_info(current_data, Termination_Terms)

            if results[0] == None :
                return None
            
            new_name,new_age,new_address,new_phone,current_id = results

            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            updated_line = f'{timestamp},{new_name},{new_age},{new_address},{new_phone},{current_id}\n'

            data_lines[i] = updated_line
            found_and_updated = True

            break

    if not found_and_updated :
        print(f"❌ User with id '{contact_id}' not found.")
        return None
    
    try :

        with open (file_path, 'w', encoding= 'utf-8') as file :

            if header_line :

                file.write(header_line)

            file.writelines(data_lines)

            print("=" * 50)
            print(f"✅ Success! User information for id {contact_id} has been updated and saved.")
            print("=" * 50)

    except Exception as e :
        print(f"❌ An error occurred while writing to the file: {e}")
    
        return None
    
def send_feedback(contact_id) :

    file_name = 'Feedback.txt'

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print("💬 Feedback and Suggestions Center 💬")
    print("-" * 45)

    feedback_text = input("Please write your feedback/suggestions (or leave blank to cancel):\n> ").strip()

    if not feedback_text :

        print("🚫 No feedback submitted. Thank you.")
        return
    
    log_entry = f"{timestamp},{contact_id},{feedback_text}\n"

    try :
    
        if not os.path.exists(file_name) :

            print ('File Not Found. Creating New File...')

            with open (file_name, 'w', encoding= 'utf-8') as file :

                file.write('Time|Email|Feedback\n')

                file.write(log_entry)

        else :

            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(log_entry)
            
        # Success message
        print("-" * 45)
        print("✅ Success! Your feedback has been successfully received. We appreciate your time.")

    except Exception as e :

        print(f"❌ An error occurred while saving the feedback: {e}")

def contact_us():
    """Displays all official and social contact channels."""
    
    print("📞 Contact Us & Support 📞")
    print("=" * 55)
    print("For sales, support, or inquiries, please use the following channels:")
    print("-" * 55)

    print("### Official Contact ###")
    print("📧 Email Support: support@DCM.com") 
    print("☎️ Phone (Sales): +20 100 123 4567")
    print("📍 Main Office: 123 Autostrad St, New Cairo, Egypt")
    print("-" * 55)

    print("--- Social Media & Messaging ---")
    print("🔵 Facebook: DCMOfficial")
    print("📸 Instagram: @DCMEG")
    print("🟢 WhatsApp: +20 124 879 2353 (Direct chat)")
    print("💬 Telegram: t.me/DCMSupport")
    print("🖥️ Website: www.DCM.com") 
    
    print("=" * 55)

def show_features():

    print("--- (Available Features) ---")
    for index, feature in enumerate(Available_features, start= 1) :
        print(f'- {index}. {feature}')
    print("-" * 30)

def main_menu() :

    show_features()

    while True :

        print ('Hello, How can i help you?')

        choice = input ().strip().capitalize()

        if choice in ('Add', 'A') :

            add_contact()

        elif choice in ('Delete', 'Dl') :

            contact_id = input('Enter the ID you want to delete: ').strip()
            delete_contact(contact_id)  

        elif choice in ('View', 'V') :

            view_contact()

        elif choice in ('Search contacts', 'Sc', 'S') :

            search_contacts()

        elif choice in ('Update info', 'Up', 'Ui', 'U') :

            contact_id = input('Enter the ID of the contact you want to update: ').strip()

            update_info(contact_id)

        elif choice in ('Feedback', 'Fb', 'F') :

            contact_id = input('Enter the ID : ').strip()

            send_feedback(contact_id)

        elif choice in ('Contact us', 'Cu') :

            contact_us()

        elif choice in ('Features', 'Menu', 'Help', 'F', 'M', 'H') :

            show_features()

        elif choice in Termination_Terms :

            print('Exiting...')

            break

        else :

            print ('Invalid choice.') 

            show_features()

if __name__ == '__main__' :

    main_menu()

