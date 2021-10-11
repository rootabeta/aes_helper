import getpass
import hashlib
import base64

def str2hex(string):
    hexbuilder = b''
    hexbuilder = bytes.fromhex(string)

    return hexbuilder


password = getpass.getpass("Password: ")
print("Generating AES key...")
m = hashlib.sha256()
m.update(password.encode())
hashed = m.hexdigest()
encoded = base64.b64encode(str2hex(hashed))
print(encoded.decode())
