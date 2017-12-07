#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys

def main(argv):
	words = []
	wordc = {}

	with open(argv[1]) as f:
		content = f.read().splitlines()

	for line in content:
		for word in line.split(' '):
			words.append(word)

	for word in words:
		if word in wordc:
			wordc[word] += 1
		else:
			wordc[word] = 1

	with open('Q1.txt', 'w') as f:
		i = 0
		for word in words:
			f.write(word + ' ' + str(i) + ' ' + str(wordc[word]) + '\n')
			i += 1


if __name__ == '__main__':
	try:
		main(sys.argv)
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")


