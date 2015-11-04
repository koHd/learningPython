import string

alphabet = 'abcdefghijklmnopqrstuvwxyz'
punctuationSymbols = set(string.punctuation)
plaintext = input("Input the message: ")
shift = int(input("Choose a shift value: "))

def shiftCharacter(character, shift):
	assert (character.isalpha()), "The symbol '" + character + "' is not in my alphabet. Cannot encrypt. "
	newCharacterIndex = (alphabet.index(character) + shift) % len(alphabet)
	newCharacter = alphabet[newCharacterIndex]
	return newCharacter

def encrypt(plaintext, shift):
	ciphertext = str()
	for character in plaintext.lower():
		if character.isspace() or character in punctuationSymbols:
			ciphertext += character
		else:
			ciphertext += shiftCharacter(character, shift)
	return ciphertext

ciphertext = encrypt(plaintext, shift)

print(ciphertext)