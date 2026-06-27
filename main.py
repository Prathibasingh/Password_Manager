print("Welcome to Secure Password Manager!")
import os

# File to store passwords
PASSWORD_FILE = 'passwords.txt'

def add_password():
    site = input("Enter the site name: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    with open(PASSWORD_FILE, 'a') as f:
        f.write(f"{site},{username},{password}\n")
    print("Password added successfully!")

def view_passwords():
    if not os.path.exists(PASSWORD_FILE):
        print("No passwords stored yet.")
        return
    with open(PASSWORD_FILE, 'r') as f:
        passwords = f.readlines()
    if not passwords:
        print("No passwords stored yet.")
        return
    print("\nStored Passwords:")
    for line in passwords:
        site, username, password = line.strip().split(',')
        print(f"Site: {site}, Username: {username}, Password: {password}")

def main():
    while True:
        print("\nSecure Password Manager")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            print("Exiting Password Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
