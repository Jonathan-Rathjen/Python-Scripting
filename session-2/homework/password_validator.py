passwd = input("Please input a password: ")

has_at = False
has_space = False

for i in passwd:
    if i == "@":
        has_at = True
    elif i == " ":
        has_space = True
    else:
        continue

if len(passwd) > 7 and has_at and not has_space:
    print("That is a strong password")
else:
    print("That is a weak password, try again")