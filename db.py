import json

class Database:

    def insert(self, name, email, password):
        try:
            try:
                with open('users.json', 'r') as rf:
                    try:
                        users = json.load(rf)
                    except json.decoder.JSONDecodeError as e:
                        print(f"JSON decoding error: {e}")
                        users = {}  # Initialize an empty dictionary in case of empty or invalid file
            except FileNotFoundError:
                users = {}

            if email in users:
                return 0
            else:
                users[email] = [name, password]

            with open('users.json', 'w') as wf:
                json.dump(users, wf)
                print("Data successfully written to users.json")
                return 1
        except Exception as e:
            print(f"An error occurred: {e}")
            return -1


    def search(self,email,password):
        with open('users.json', 'r') as rf:
            users = json.load(rf)

            if email in users:
                if users[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
