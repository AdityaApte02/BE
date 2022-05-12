import pyaes, pbkdf2, binascii, os, secrets

# passowrd="84JKho$%Io43@"
# passwordSalt=os.urandom(16)
# key=pbkdf2.PBKDF2(passowrd, passwordSalt).read(32)
# print("AES Encryption Key: ",binascii.hexlify(key))

# iv=secrets.randbits(256)
# plainText="I love Krishna"
# aes=pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
# ciphertext=aes.encrypt(plainText)
# print("CipherText is : ",binascii.hexlify(ciphertext))

# aes=pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
# decrypted=aes.decrypt(ciphertext)
# print("Decrypted key: ",decrypted)




























#Attempt 1
import pyaes, pbkdf2, binascii, os, secrets

password="djfh&h3467SD*(23"
passwordSalt=os.urandom(16)
key=pbkdf2.PBKDF2(password,passwordSalt).read(32)
print("AES Encryption Key: ",binascii.hexlify(key))


iv=secrets.randbits(256)
plaintext="My name is Aditya Apte"
aes=pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext=aes.encrypt(plaintext)
print("AES ciphertext is: ",binascii.hexlify(ciphertext))


aes=pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted=aes.decrypt(ciphertext)
print("AES Decrypted text is: ",decrypted)