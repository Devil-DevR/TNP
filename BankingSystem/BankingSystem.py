import random
import re
import datetime
import sqlite3

conn = sqlite3.connect('banking_system.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    account_number TEXT PRIMARY KEY,
                    name TEXT,
                    dob TEXT,
                    city TEXT,
                    password TEXT,
                    initial_balance REAL,
                    contact_number TEXT,
                    email TEXT,
                    address TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS login (
                    account_number TEXT PRIMARY KEY,
                    password TEXT,
                    status TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS transaction (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    account_number TEXT,
                    transaction_type TEXT,
                    amount REAL,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

conn.commit()
conn.close()

def validate_name(name):
    return bool(re.match("^[a-zA-Z ]+$", name))

def validate_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def validate_contact_number(contact_number):
    return len(contact_number) == 10 and contact_number.isdigit()

def validate_password(password):
    return bool(re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[A-Z]).{8,}$', password))

def generate_account_number():
    return str(random.randint(1000000000, 9999999999))

def account_exists(account_number):
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE account_number = ?', (account_number,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def add_user():
    name = input("Enter name: ")
    while not validate_name(name):
        print("Invalid name. Only alphabets and spaces allowed.")
        name = input("Enter name: ")

    dob = input("Enter date of birth (YYYY-MM-DD): ")
    city = input("Enter city: ")
    
    password = input("Enter password: ")
    while not validate_password(password):
        print("Password must be at least 8 characters long, and include an uppercase letter, a lowercase letter, and a number.")
        password = input("Enter password: ")

    initial_balance = float(input("Enter initial balance (min 2000): "))
    while initial_balance < 2000:
        print("Initial balance must be at least 2000.")
        initial_balance = float(input("Enter initial balance (min 2000): "))

    contact_number = input("Enter contact number (10 digits): ")
    while not validate_contact_number(contact_number):
        print("Invalid contact number. Please enter a 10-digit number.")
        contact_number = input("Enter contact number (10 digits): ")

    email = input("Enter email address: ")
    while not validate_email(email):
        print("Invalid email format. Please enter a valid email address.")
        email = input("Enter email address: ")

    address = input("Enter address: ")

    account_number = generate_account_number()
    while account_exists(account_number):
        account_number = generate_account_number()

    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO users (account_number, name, dob, city, password, initial_balance, 
                    contact_number, email, address) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (account_number, name, dob, city, password, initial_balance, contact_number, email, address))
    cursor.execute('''INSERT INTO login (account_number, password, status) VALUES (?, ?, ?)''',
                   (account_number, password, 'Active'))
    conn.commit()
    conn.close()
    print(f"User added successfully. Your account number is {account_number}.")

def show_users():
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()

    if users:
        for user in users:
            print(f"Account Number: {user[0]}")
            print(f"Name: {user[1]}")
            print(f"DOB: {user[2]}")
            print(f"City: {user[3]}")
            print(f"Balance: {user[5]}")
            print(f"Contact Number: {user[6]}")
            print(f"Email: {user[7]}")
            print(f"Address: {user[8]}")
            print("-" * 30)
    else:
        print("No users found.")

def login():
    account_number = input("Enter your account number: ")
    password = input("Enter your password: ")

    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM login WHERE account_number = ? AND password = ?', (account_number, password))
    result = cursor.fetchone()

    if result:
        print(f"Welcome, {account_number}!")
        user_operations(account_number)
    else:
        print("Invalid account number or password.")
    conn.close()

def user_operations(account_number):
    while True:
        print("\nSelect an option:")
        print("1. Show Balance")
        print("2. Show Transactions")
        print("3. Credit Amount")
        print("4. Debit Amount")
        print("5. Transfer Amount")
        print("6. Active/Deactivate Account")
        print("7. Change Password")
        print("8. Update Profile")
        print("9. Logout")

        option = input("Enter your choice: ")

        if option == '1':
            show_balance(account_number)
        elif option == '2':
            show_transactions(account_number)
        elif option == '3':
            credit_amount(account_number)
        elif option == '4':
            debit_amount(account_number)
        elif option == '5':
            transfer_amount(account_number)
        elif option == '6':
            toggle_account_status(account_number)
        elif option == '7':
            change_password(account_number)
        elif option == '8':
            update_profile(account_number)
        elif option == '9':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def show_balance(account_number):
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT initial_balance FROM users WHERE account_number = ?', (account_number,))
    result = cursor.fetchone()
    conn.close()

    if result:
        print(f"Your current balance is: {result[0]}")
    else:
        print("Account not found.")

def show_transactions(account_number):
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transaction WHERE account_number = ? ORDER BY date DESC', (account_number,))
    transactions = cursor.fetchall()
    conn.close()

    if transactions:
        for transaction in transactions:
            print(f"ID: {transaction[0]}, Type: {transaction[2]}, Amount: {transaction[3]}, Date: {transaction[4]}")
            print("-" * 30)
    else:
        print("No transactions found.")

def credit_amount(account_number):
    amount = float(input("Enter amount to credit: "))
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT initial_balance FROM users WHERE account_number = ?', (account_number,))
    result = cursor.fetchone()

    if result:
        new_balance = result[0] + amount
        cursor.execute('UPDATE users SET initial_balance = ? WHERE account_number = ?', (new_balance, account_number))
        cursor.execute('INSERT INTO transaction (account_number, transaction_type, amount) VALUES (?, ?, ?)', 
                       (account_number, 'Credit', amount))
        conn.commit()
        conn.close()
        print(f"Amount credited successfully. New balance: {new_balance}")
    else:
        print("Account not found.")

def debit_amount(account_number):
    amount = float(input("Enter amount to debit: "))
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT initial_balance FROM users WHERE account_number = ?', (account_number,))
    result = cursor.fetchone()

    if result:
        if result[0] >= amount:
            new_balance = result[0] - amount
            cursor.execute('UPDATE users SET initial_balance = ? WHERE account_number = ?', (new_balance, account_number))
            cursor.execute('INSERT INTO transaction (account_number, transaction_type, amount) VALUES (?, ?, ?)', 
                           (account_number, 'Debit', amount))
            conn.commit()
            conn.close()
            print(f"Amount debited successfully. New balance: {new_balance}")
        else:
            print("Insufficient funds for this transaction.")
    else:
        print("Account not found.")

def transfer_amount(account_number):
    recipient_account = input("Enter recipient account number: ")
    amount = float(input("Enter amount to transfer: "))

    # Ensure recipient account exists
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT initial_balance FROM users WHERE account_number = ?', (recipient_account,))
    recipient = cursor.fetchone()

    if not recipient:
        print("Recipient account not found.")
        conn.close()
        return

    cursor.execute('SELECT initial_balance FROM users WHERE account_number = ?', (account_number,))
    sender = cursor.fetchone()

    if sender and sender[0] >= amount:
        # Update sender balance
        new_sender_balance = sender[0] - amount
        cursor.execute('UPDATE users SET initial_balance = ? WHERE account_number = ?', (new_sender_balance, account_number))

        # Update recipient balance
        new_recipient_balance = recipient[0] + amount
        cursor.execute('UPDATE users SET initial_balance = ? WHERE account_number = ?', (new_recipient_balance, recipient_account))

        # Record transaction for both sender and recipient
        cursor.execute('INSERT INTO transaction (account_number, transaction_type, amount) VALUES (?, ?, ?)', 
                       (account_number, 'Transfer Out', amount))
        cursor.execute('INSERT INTO transaction (account_number, transaction_type, amount) VALUES (?, ?, ?)', 
                       (recipient_account, 'Transfer In', amount))

        conn.commit()
        conn.close()
        print(f"Transfer successful. New balance: {new_sender_balance}")
    else:
        print("Insufficient funds for this transaction or account not found.")
    conn.close()

def toggle_account_status(account_number):
    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT status FROM login WHERE account_number = ?', (account_number,))
    result = cursor.fetchone()

    if result:
        current_status = result[0]
        new_status = 'Inactive' if current_status == 'Active' else 'Active'
        cursor.execute('UPDATE login SET status = ? WHERE account_number = ?', (new_status, account_number))
        conn.commit()
        print(f"Account status updated to {new_status}.")
    else:
        print("Account not found.")
    conn.close()

def change_password(account_number):
    old_password = input("Enter current password: ")
    new_password = input("Enter new password: ")

    # Validate new password
    while not validate_password(new_password):
        print("Password must be at least 8 characters long, and include an uppercase letter, a lowercase letter, and a number.")
        new_password = input("Enter new password: ")

    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM login WHERE account_number = ?', (account_number,))
    result = cursor.fetchone()

    if result and result[0] == old_password:
        cursor.execute('UPDATE login SET password = ? WHERE account_number = ?', (new_password, account_number))
        conn.commit()
        print("Password changed successfully.")
    else:
        print("Incorrect current password.")
    conn.close()

def update_profile(account_number):
    name = input("Enter new name (or press enter to keep current): ")
    city = input("Enter new city (or press enter to keep current): ")
    contact_number = input("Enter new contact number (or press enter to keep current): ")
    email = input("Enter new email (or press enter to keep current): ")
    address = input("Enter new address (or press enter to keep current): ")

    conn = sqlite3.connect('banking_system.db')
    cursor = conn.cursor()

    if name:
        cursor.execute('UPDATE users SET name = ? WHERE account_number = ?', (name, account_number))
    if city:
        cursor.execute('UPDATE users SET city = ? WHERE account_number = ?', (city, account_number))
    if contact_number:
        cursor.execute('UPDATE users SET contact_number = ? WHERE account_number = ?', (contact_number, account_number))
    if email:
        cursor.execute('UPDATE users SET email = ? WHERE account_number = ?', (email, account_number))
    if address:
        cursor.execute('UPDATE users SET address = ? WHERE account_number = ?', (address, account_number))

    conn.commit()
    conn.close()
    print("Profile updated successfully.")

def main():
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Add User")
        print("2. Show Users")
        print("3. Login")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_user()
        elif choice == '2':
            show_users()
        elif choice == '3':
            login()
        elif choice == '4':
            print("Thank you for using the Banking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

