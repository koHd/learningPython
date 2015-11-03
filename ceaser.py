alphabet = 'abcdefghijklmnopqrstuvwxyz'
plaintext = input("Input the message: ")
shift = int(input("Choose a shift value: "))
ciphertext = str()

for character in plaintext.lower():
	if character == ' ':
		ciphertext += ' '
	else:
		newCharacterIndex = (alphabet.index(character) + shift) % len(alphabet)
		ciphertext += alphabet[newCharacterIndex]

print(ciphertext)