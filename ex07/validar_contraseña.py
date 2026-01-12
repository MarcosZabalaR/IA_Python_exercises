password = input("Enter a password: ")
if len(password) >= 8:
    print("Password is valid.")
else:
    print("Password is not valid.")

mayus = any(c.isupper() for c in password)
minus = any(c.islower() for c in password)
digit = any(c.isdigit() for c in password)

if mayus and minus and digit and len(password) >= 8:
    print("Password is strong.")