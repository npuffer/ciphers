#!/usr/bin/python

import string
import random

def init(alpha):
	slots = range(0, len(alpha))
	codebook = {}
	for i in alpha:
		j = random.randint(0, len(slots)-1)
		codebook[slots.pop(j)] = i
	return codebook

def encrypt(cleartext, codebook):
	cleartext = cleartext.lower()
	cipher = []
	words = cleartext.split()	
	for w in words:
		encword = ""
		for c in w:
			if c in string.punctuation:
				encword += c
			else:
				encword += codebook.get(string.lowercase.index(c), '')
		cipher.append(encword)
	return " ".join(cipher)

def debug(item):
	print item
	print type(item)
	print len(item)

# Main Program
alpha = list(string.ascii_lowercase)
codebook = init(alpha)
clear = raw_input("Enter Your Message: ")
cipher = encrypt(clear, codebook)
print cipher
