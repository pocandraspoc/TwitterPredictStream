import os
import re
import ujson
from pprint import pprint

def strip(input_file):
	with open(input_file) as infile, open(output_file, 'w') as outfile:
		for line in infile:
			if not line.strip():
				continue
		outfile.write(line)
	infile.close()
	outfile.close()


files = os.listdir("/home/my/work/TwitterPredictStream/20180701_OUT/")
in_files = "/home/my/work/TwitterPredictStream/20180701_OUT/"

out_file = "BIG" + "_OUT_IN_"
my_list = []

for file in files:
	my_list[file] = str(in_files + file)

for file in files:
	print(in_files + file)

# tempfiles is an ordered list of temp files (open for reading)
f = open("BB8igfile.txt", "w")
for tempfile in (in_files + file):
    while True:
        data = tempfile.read(65536)
        if data:
            f.write(data)
        else:
            break