import cv2
from os import listdir
from os.path import isfile, join
import sys

def main():
	if len(sys.argv) < 3:
		print("please input folder path, >python ./ppm2png.py inputdir outputdir")
		sys.exit(1)
	inpath = sys.argv[1]
	outpath = sys.argv[2]

	names = [f for f in listdir(inpath) if isfile(join(inpath, f))]
	print "names"
	files = list(set(names))

	for f in files:
		tmpImg = cv2.imread(join(inpath, f))
		new_filename = f[:-4] + ".png"
		# print new_filename
		cv2.imwrite(join(outpath, new_filename), tmpImg)
	




if __name__ == "__main__":
    main()