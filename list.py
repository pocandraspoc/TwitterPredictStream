import os

root = "/home/my/work/TwitterPredictStream/20180701_OUT"
path = ""

'''os.path.join(root, "20180701_OUT")'''

with open('big.txt', 'w') as outfile:
	for path, subdirs, files in os.walk(root):
		for name in files:
			print(os.path.join(path, name))
			with open(os.path.join(path, name)) as infile:
				for line in infile:
					outfile.write(line)

"""print(os.path.join(path, name))"""