# 📚 Digital Contacts Manager (Python CLI)

### A foundational Python project showcasing core language skills and file persistence.

This project is a simple Command Line Interface (CLI) application developed in Python. It simulates a basic address book system, allowing users to manage contacts and store them persistently in a text file.

## ✨ Key Features

The application provides a main menu with the following core functionalities:

* **Add Contact:** Prompts the user for Name, Age, Country, and Phone Number, saving the record to a file.

* **View All Contacts:** Reads and displays all saved contacts in a clear, numbered list format.

* **Smart Search:** Allows searching for a contact using a name or part of any field (search is case-insensitive).

* **Persistent Storage:** Data is safely stored and retrieved between program runs using File Handling.

## 🛠️ Technologies & Skills Demonstrated

This project is a practical demonstration of fundamental Python programming concepts, which are crucial for any aspiring developer:

| Skill / Concept | Description | 
| ----- | ----- | 
| **Functions (Modularity)** | The project is structured using dedicated functions (`add_contact`, `contacts`, `main_menu`) to keep the code organized and readable. | 
| **File Handling** | Safe and persistent data storage is achieved using Python's native file modes (`'r'` for reading, `'a'` for appending) within `with open()` blocks. | 
| **OS Module** | Advanced file path management using `os.chdir()` ensures the application runs correctly regardless of the user's current directory. | 
| **Control Flow** | A robust menu system is implemented using `while True` loops and conditional logic (`if/elif`). | 
| **String Methods** | Utilizing `.strip()`, `.lower()`, and `.capitalize()` for effective data cleaning and implementing case-insensitive search logic. | 

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed on your system.

### How to Run

1. Download the main Python file (`digital address book.py`) to a local folder.

2. Open your terminal or Git Bash inside that folder.

3. Run the application using the following command:

python "digital address book.py"


4. Follow the interactive prompts in the main menu.

## 💡 Future Development Plans

1. **Error Handling (`try/except`):** Implement robust input validation (e.g., preventing program crash if non-numeric input is entered for age).

2. **CRUD Operations:** Add functionality to fully complete the CRUD cycle by allowing user