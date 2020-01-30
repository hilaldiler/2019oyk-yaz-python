def save_file(file_name, data):
    with open(file_name,"w") as file:
        file_data = ""
        for account in data:
            if file_data != "":
                file_data += "//"
            file_data += "{name}|{email}|{username}|{password}|{secret_answer}".format(
                name=account.get("name"),
                username=account.get("username"),
                password=account.get("password"),
                email=account.get("email"),
                secret_answer=account.get("secret_answer")
            )

        file.write(file_data)

def load_file(filename):

    with open(filename) as file:
        account_list =[]
        for account in file.read().split("//"):
            account_data = account.split('|')
            if len(account_data) == 5:
                account_list.append({
                    "name":account_data[0],
                    "email":account_data[1],
                    "username":account_data[2],
                    "password":account_data[3],
                    "secret_answer":account_data[4],
                })
        return account_list

def input_control(name, value_type, min=1, max=0, choices=[]):
    while True:
        has_incorrect = False
        value = input("Please enter {} (Min: {}, Max: {}) :"
                      .format(name, min, max))
        value = value.strip()
        if len(value) < min:
            has_incorrect = True
        if value_type == int:
            if not value.isdigit():
                has_incorrect = True
        if max > 0 and len(value) > max:
            has_incorrect = True

        if value_type == int:
            return_value = int(value)
        else:
            return_value = value
        if len(choices) > 0:
            if return_value not in choices:
                has_incorrect = True

        if has_incorrect:
            print('Incorrect Entry')
            continue

        return return_value

if __name__ == '__main__':
    print(input_control('Its Working!',str))