from Cryptodome.Cipher import AES
from base64 import b64decode,b64encode
import json
import sys

try:
        mode = sys.argv[1][0] #e,d
        aes_key_str = sys.argv[2]
        in_file = sys.argv[3]
        out_file = sys.argv[4]
except Exception as e:
        exit("Usage: python3 aes.py [e/d] [base64 aes key] [infile] [outfile]")


aes_key = b64decode(aes_key_str.encode())

if mode == "e":
        cipher = AES.new(aes_key,AES.MODE_CTR)
        #encrypt
        with open(in_file,"rb") as f:
                ct_bytes = cipher.encrypt(f.read())

        nonce = b64encode(cipher.nonce).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')

        with open(out_file, "w") as o:
                o.write(json.dumps({'nonce':nonce,'ciphertext':ct}))
        print("[*] Encryption complete")

elif mode == "d":
        #decrypt:
        with open(in_file,"r") as f:
                data = json.loads(f.read())

        nonce = b64decode(data['nonce'])
        ct = b64decode(data['ciphertext'])

        cipher = AES.new(aes_key,AES.MODE_CTR, nonce=nonce)
        pt = cipher.decrypt(ct)
        with open(out_file,"wb") as o:
                o.write(pt)
        print("[*] Decryption complete")
else:
        exit("Invalid mode!")
