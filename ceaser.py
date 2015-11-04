import string

alphabet = 'abcdefghijklmnopqrstuvwxyz'
punctuationSymbols = set(string.punctuation)
plaintext = input("Input the message: ")
shift = int(input("Choose a shift value: "))

def encrypt(plaintext):
	ciphertext = str()
	for character in plaintext.lower():
		if character.isspace() or character in punctuationSymbols:
			ciphertext += character
		else:
			assert (character.isalpha()), "The symbol '" + character + "' is not in my alphabet. Cannot encrypt. "
			shiftedCharacterIndex = (alphabet.index(character) + shift) % len(alphabet)
			ciphertext += alphabet[shiftedCharacterIndex]
	return ciphertext

ciphertext = encrypt(plaintext)

print(ciphertext)