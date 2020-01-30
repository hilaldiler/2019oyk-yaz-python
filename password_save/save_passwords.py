from control_library import input_control, save_file, load_file

parolalar = load_file("data_pass.txt")
while True:
    print('Please Select a Action')
    print('1- List')
    print('2- Create a new entry')
    print('3- Change')
    islem = input_control('Select', int, max=1, choices=[1, 2,3])
    if islem == 1:
        parolalar = load_file("data_pass.txt")
        print('Please select a account')
        account_number = 0
        account_id_list = []
        for i in parolalar:
            account_number += 1
            account_id_list.append(account_number)
            print("{} - {}".format(account_number, i.get('name')))

        account_id = input_control('Select Account:', int, choices=account_id_list)
        account = parolalar[account_id - 1]

        print("""
        name: {name}
        username: {username}
        password: {password}
        email: {email}
        secret_answer: {secret_answer}
        """.format(name=account.get("name"),
                   username=account.get("username"),
                   password=account.get("password"),
                   email=account.get("email"),
                   secret_answer=account.get("secret_answer")))

    elif islem == 2 :
        name = input_control('Name', str)
        username = input_control('Username', str)
        password = input_control('Password', str)
        password2 = input_control('Password Control', str, choices=[password])
        email = input_control('Email', str)
        secret_answer = input_control('Secret Answer', str)
        parolalar.append({
            "name": name,
            "username": username,
            "password": password,
            "email": email,
            "secret_answer": secret_answer
        })
        save_file("data_pass.txt",parolalar)
        parolalar = load_file("data_pass.txt")
        print('Record Saved.')
    else:
        pass