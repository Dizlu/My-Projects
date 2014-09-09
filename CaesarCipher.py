#Caesar Cipher

MAX_KEY_SIZE = 26

def getMode():
	while True:
		mode = raw_input('Do you wish to encrypt or decrypt a message? ').lower()
		if mode in 'encrypt e decrypt d'.split():
			return mode
		else:
			print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
	return raw_input('Enter your message: ')

def getKey():
	key = 0
	while True:
		key = int(raw_input('Enter the key number (1- %s) ' %(MAX_KEY_SIZE)))
		if (key >= 1 and key <= MAX_KEY_SIZE):
			return key

def getTranslatedMessage(mode, message, key):
	if mode[0] == 'd':
		key = -key
	translated = ''

	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key

			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				if num < ord('a'):
					num += 26

			translated += chr(num)
		else:
			translated += symbol
	return translated

def main():
	mode = getMode()
	message = getMessage()
	key = getKey()

	print('Your translated text is: ')
	print(getTranslatedMessage(mode, message, key))

main()