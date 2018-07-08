import os
import re
import ujson
from pprint import pprint

class JasonWrapper:

	def strip(input_file, output_file):
		with open(input_file) as infile, open(output_file, 'w') as outfile:
			for line in infile:
				if not line.strip():
					continue
				try:
					tweet = ujson.loads(str(line), )
				except ValueError:
					continue
				try:
					tweet = tweet["text"]
					if (tweet[0:3]) != "RT ": 
						tweet = re.sub(r'\n', ' ', tweet)
						tweet = re.sub(r'  ', ' ', tweet)
						outfile.write(tweet +"\n")
				except KeyError:
					continue
				continue
		infile.close()
		outfile.close()

files = os.listdir("/home/my/Downloads/20180701")

for file in files:
	in_file = "/home/my/Downloads/20180701" + "/" + file
	out_file = "20180701_OUT/" + "_OUT_" + file
	JasonWrapper.strip(in_file, out_file)