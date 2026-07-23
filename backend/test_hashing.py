from app.core.security import hash_password, verify_password

password = "airline123"

h1 = hash_password(password)
h2 = hash_password(password)

print("Hash 1:", h1)
print("Hash 2:", h2)
print("Same password, same hash?", h1 == h2)
print()
print("Correct password:", verify_password("airline123", h1))
print("Wrong password:  ", verify_password("wrongpass", h1))
print("Cross-check h2:  ", verify_password("airline123", h2))