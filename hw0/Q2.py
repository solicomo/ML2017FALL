#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
from PIL import Image

# 低效版
# 3.91s
def fade1(img):
	with Image.open(img) as im:
		odata = im.getdata()
		ndata = list(map(lambda rgb: (int(rgb[0]/2), int(rgb[1]/2), int(rgb[2]/2)), odata))
		im.putdata(ndata)
		im.save('Q2.jpg', 'jpeg')

# 高效版
# 0.37s
def fade2(img):
	with Image.open(img) as im:
		nim = Image.eval(im, lambda x: int(x/2))
		nim.save('Q2.jpg', 'jpeg')

def main(argv):
	# 默认用高效版，第二个参数为 1 时，用低效版
	if len(argv) > 2 and argv[2] == '1':
		print('version 1\n')
		fade1(argv[1])
	else:
		fade2(argv[1])

if __name__ == '__main__':
	try:
		main(sys.argv)
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")


