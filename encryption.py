from cryptography.fernet import Fernet

message = "hello geeks"

#key = Fernet.generate_key()


fernet = Fernet(b'c2E3A30yfsdjtP-uSmpbHMmIZl2T7Cq__LnBx1bGe-U=')

encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)
