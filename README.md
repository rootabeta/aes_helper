# aes_helper
A helper tool to encrypt and decrypt files with AES

This tool uses the PyCrpyptodomex library to perform encryption with 256 bit AES CTR-mode symmetric encryption.

It does NOT delete the plaintext file - if you want to do that, I would suggest using something like

```bash
shred -zfun 10 in_file.txt
```
