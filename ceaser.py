alphabet = 'abcdefghijklmnopqrstuvwxyz'
plaintext = input("Input the message: ")
shift = int(input("Choose a shift value: "))

def encrypt(plaintext):
	ciphertext = str()
	for character in plaintext.lower():
		if character == ' ':
			ciphertext += ' '
		else:
			shiftedCharacterIndex = (alphabet.index(character) + shift) % len(alphabet)
			ciphertext += alphabet[shiftedCharacterIndex]
	return ciphertext

ciphertext = encrypt(plaintext)

print(ciphertext)