from Cryptodome.Random import get_random_bytes
from base64 import b64encode

key = get_random_bytes(32)
encoded = b64encode(key).decode()
print(encoded)
