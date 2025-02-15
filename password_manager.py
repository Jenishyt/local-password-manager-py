import json
server = {}
def load_server_data():
    global server
    try:
        with open('server_data.json', 'r') as file:
            server = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        server = {}

def save_server_data():
    with open('server_data.json', 'w') as file:
        json.dump(server, file)

def start():
    load_server_data()
    try:
        a = int(input('Type 1 if you are a new user\nType 2 to login: '))
        if a == 1:
            sign_up()
        elif a == 2:
            sign_in()
        else:
            print('Invalid input :( ')
            start()
    except ValueError:
        print("Please enter a valid number")
        start()

def sign_up():
    n_username = input('Create your username: ').upper()
    n_password = input('Create password (case sensitive): ')
    if n_username not in server:
        server[n_username] = n_password
        save_server_data()
        print('Account created successfully :) ')
        sign_in()
    else:
        print(f'Username {n_username} already exists')
        sign_up()

def sign_in():
    print('-----------\nLog in ')
    u = input('Enter your username: ').upper()
    p = input('Enter your password: ')
    if u in server:
        if server[u] == p:
            print('Login successful :) ')
            logged_in(u)
        else:
            print('Wrong password, try again')
            sign_in()
    else:
        print(f'{u} not found. Try again or sign up.')
        try:
            x = int(input('Type 1 to try again OR 2 to create account: '))
            if x == 1:
                sign_in()
            elif x == 2:
                sign_up()
            else:
                print('Invalid input')
                sign_in()
        except ValueError:
            print('Please enter a valid number')
            sign_in()

def logged_in(username):
    while True:
        print(f'\nHello {username}')
        try:
            b = int(input('Enter 1 to view passwords\nEnter 2 to save new password\nEnter 3 to log out: '))
            if b == 1:
                view_passwords(username)
            elif b == 2:
                create_new(username)
            elif b == 3:
                print('Logged out successfully.')
                start()
                break
            else:
                print('Invalid input')
        except ValueError:
            print('Please enter a valid number')

def view_passwords(username):
    try:
        with open(f'{username}.json', 'r') as file:
            data = json.load(file)
            if data:
                print('--------------')
                print("Saved passwords:")
                for entry in data:
                    print(f"Website: {entry[0]}, Username: {entry[1]}, Password: {entry[2]}\n")
            else:
                print('No passwords saved.')
                i3 = int(input('type 1 to save new passwords '))
                if i3 == 1:
                    create_new(username)
                else:
                    logged_in(username)

    except (FileNotFoundError, json.JSONDecodeError):
        print('No password file found')

def create_new(username):
    n_name = input('Enter name of website: ').lower()
    n_username = input('Enter username: ').upper()
    n_password = input('Enter password: ')
    new_entry = [n_name, n_username, n_password]
    try:
        with open(f'{username}.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(new_entry)
    with open(f'{username}.json', 'w') as file:
        json.dump(data, file)
    print(f'Password for {n_name} saved successfully!')

start()



# use criptography
# try saving on online server