import string
import argparse

alphabet = 'abcdefghijklmnopqrstuvwxyz'
punctuationSymbols = set(string.punctuation)
shift = int(input("Choose a shift value: "))

parser = argparse.ArgumentParser(description='Shift encrypt a plaintext file.')
parser.add_argument('-i', '--input', help='Input file name', required=True)
args = parser.parse_args()
plaintextFile = open(args.input)

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

ciphertextFile = open("ciphertext.txt", "w")
ciphertextFile.write(encrypt(plaintextFile.read(), shift))
