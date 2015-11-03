alphabet = 'abcdefghijklmnopqrstuvwxyz'
plaintext = input("Input the message: ")
shift = int(input("Choose a shift value: "))
ciphertext = str()

for character in plaintext.lower():
	if character == ' ':
		ciphertext += ' '
	else:
		ciphertext += alphabet[(alphabet.index(character) + shift) % len(alphabet)]

print(ciphertext)