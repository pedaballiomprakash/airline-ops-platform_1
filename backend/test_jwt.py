import time
from app.core.security import create_access_token, decode_access_token

token = create_access_token(user_id=7, role="admin")
print("Token:", token)
print("Parts:", len(token.split(".")))
print()

payload = decode_access_token(token)
print("Decoded:", payload)
print()

# tamper with the payload
header, body, signature = token.split(".")
tampered = f"{header}.{body}xyz.{signature}"
print("Tampered token accepted?", decode_access_token(tampered))
print()

# wrong signature
forged = f"{header}.{body}.{signature[:-4]}AAAA"
print("Forged signature accepted?", decode_access_token(forged))
print()

# read the payload WITHOUT the secret key
import base64, json
padded = body + "=" * (-len(body) % 4)
print("Anyone can read:", json.loads(base64.urlsafe_b64decode(padded)))