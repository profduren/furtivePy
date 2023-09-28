
secret_message = "Hello World"
binary_secret_message = bytearray()

# get the length of the message
msgLen = len(secret_message)

binary_secret_message.extend( msgLen.to_bytes(4, "little"))
for character in secret_message:
    binary_secret_message.append(ord(character))

print(binary_secret_message)
