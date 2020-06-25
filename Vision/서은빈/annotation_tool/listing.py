#import the necessary packages
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file_path", required = True, help="Path to the image file")
ap.add_argument("-s", "--seg_file_path", required = True, help="Path to the seg file")
args = ap.parse_args()

path = args.file_path
seg_path = args.seg_file_path

none_lst = [10,6,7,12]

#def train_txt():


try:
	if not os.path.exists('./list'):
		os.makedirs('./list')
except OSError:
	print('Error: Creating directory of data')

with open("./list/train.txt", 'w') as output:
	for root, dirs, files in os.walk(path):
		for fname in files:
			if fname.endswith(".txt"):
				txt_path = os.path.join(root, fname)
				output.write(txt_path[:-4]+'.jpg\n')


with open("./list/train_gt.txt", 'w') as output:
	for root, dirs, files in os.walk(path):
		for fname in files:
			if fname.endswith(".txt"):
				txt_path = os.path.join(root, fname)
				output.write(txt_path[:-4]+'.jpg ')
				output.write(seg_path+txt_path[:-4]+'.png ')
				print(txt_path)
				r = open(txt_path, mode='rt')
				i = 0
				exist =[]
				while True:
					line = r.readline()
					if i == 0:
						if len(line) == none_lst[i]:
							exist.append(0)
						else:
							exist.append(1)
					elif i == 1:
						if len(line) == none_lst[i]:
							exist.append(0)
						else:
							exist.append(1)
					elif i == 2:
						if len(line) == none_lst[i]:
							exist.append(0)
						else:
							exist.append(1)
					elif i == 3:
						if len(line) == none_lst[i]:
							exist.append(0)
						else:
							exist.append(1)
					if not line:
						break
					i +=1
				for lane in exist:
					output.write(str(lane)+' ')
				output.write('\n')
					
