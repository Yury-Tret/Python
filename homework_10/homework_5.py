import json


class Site:

    def __init__(self):
        try:
            self.users = self.load_data()
        except FileNotFoundError:
            self.users = {}
        self.logged_user = ''

    def load_data(self):
        with open('data.json') as file:
            return json.load(file)

    def save_data(self):
        with open('data.json', 'w') as file:
            json.dump(self.users, file)

    def register(self):
        if self.logged_user:
            print('User {} already logged in, sign out and try again'.format(self.logged_user))
            return
        name = input('Enter your name: ')
        login = input('Enter your login: ')
        password = input('Enter your password: ')
        user = {'name': name, 'login': login, 'password': password, 'signed_in': False}
        self.users[login] = user

    def sign_in(self):
        if self.logged_user:
            print('User {} already logged in'.format(self.logged_user))
            return
        login = input('Enter login: ')
        password = input('Enter password: ')
        for login_from_db in self.users:
            if login_from_db == login:
                if self.users[login_from_db]['password'] == password:
                    self.users[login_from_db]['signed_in'] = True
                    return
                else:
                    print('Incorrect password')
                    return
        print('Unknown login')

    def sign_out(self):
        if self.logged_user:
            self.users[self.logged_user]['signed_in'] = False
        else:
            print('User is not logged in')

    def check_logged_in_users(self):
        for login in self.users:
            if self.users[login]['signed_in']:
                return login

    def run(self):
        while True:
            if not self.users:
                print('Hi!')
            else:
                self.logged_user = self.check_logged_in_users()
                if not self.logged_user:
                    print('Hi!')
                else:
                    print('Hi, {}'.format(self.users[self.logged_user]['name']))

            while True:
                choice = input('''1. Registration
2. Sign in
3. Sign out
''')
                if choice == '1':
                    self.register()
                    break
                elif choice == '2':
                    self.sign_in()
                    break
                elif choice == '3':
                    self.sign_out()
                    break
                else:
                    print('Incorrect choice, try again')


try:
    site = Site()
    site.run()
except Exception as e:
    print(e)
finally:
    site.save_data()
