user_login = "adam"
user_pass = "DFG46543g"

login = input("Login:")
password = input("Password:")

if (login == user_login) and (password == user_pass):
    print("Secret is open")
else:
    print("Locked")
