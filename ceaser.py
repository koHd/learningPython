import string
import argparse

alphabet = 'abcdefghijklmnopqrstuvwxyz'
punctuationSymbols = set(string.punctuation)
shift = int(input("Choose a shift value: "))

parser = argparse.ArgumentParser(description='Shift encrypt a plaintext file.')
parser.add_argument('-p', '--plaintext', help='Input plaintext file name', required=True)
parser.add_argument('-c', '--ciphertext', help='Name for ciphertext file', required=True)
args = parser.parse_args()
plaintextFile = open(args.plaintext)
ciphertextFile = open(args.ciphertext, "w")

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

ciphertextFile.write(encrypt(plaintextFile.read(), shift))
