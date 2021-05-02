import numpy as np
import cv2
import os

def read_resize(path, scale, padding_color=None, height_padding=None, width_padding=None):
	img = cv2.imread(path)

	if scale:
		img = cv2.resize(img, (scale[1], scale[0]))
	if padding_color:
		if padding_color == 'white':
			padding_color = 255
		elif padding_color == 'black':
			padding_color = 0
		else:
			padding_color = -1
		assert padding_color >=0, "Color not supported..."

		if height_padding:
			h,w = img.shape[:2]
			newImg = np.zeros((int(height_padding*h),w,3),np.uint8)
			newImg.fill(padding_color)
			img = np.vstack((img,newImg))
		if height_padding:
			h,w = img.shape[:2]
			newImg = np.zeros((h,int(width_padding*w),3),np.uint8)
			newImg.fill(padding_color)
			img = np.hstack((img,newImg))
	return img

# 
def merge(path=None, save_path=None, col=None, scale=None, padding_color=None, height_padding=0.2, width_padding=0.2):
	assert save_path is not None, 'Result save path needed...'
	assert path is not None, 'Image source path needed...'
	assert str(col).isdigit(), 'Checking length number per row...'
	if not scale:
		for f in os.listdir(path):
			scale = cv2.imread(os.path.join(path, f)).shape[:2]
	assert len(scale) == 2, 'Checking every image scale...'
	# assert padding_color is not None, 'Checking padding color: white or black is available...'
	print("Welcome to ImageMerge powered by Handsome Xie!\a")
	print("Image source path: " + path)
	assert len(os.listdir(path)) % col == 0, "check num of imgs"
	width = int(len(os.listdir(path)) / col)
	print("Row x Col: {} x {}".format(width, col))
	print("Scale: {} x {}".format(scale[0], scale[1]))

	pics = []
	all_count = 0
	count = 0
	sub_pics = []
	print("\n******\n")
	path_list = os.listdir(path)
	path_list.sort()
	for f in path_list:
		all_count += 1
		if count < col:
			sub_pics.append(read_resize(path+f, scale, padding_color, height_padding, width_padding))
		else:
			pics.append(np.hstack(sub_pics))
			sub_pics = []
			count = 0
			sub_pics.append(read_resize(path+f, scale, padding_color, height_padding, width_padding))
		count += 1
		print("processing: {}".format(f))
	print("\n******\n")
	pics.append(np.hstack(sub_pics))
	img = np.vstack(pics)
	cv2.imwrite(save_path, img)
	print("Result Image Size: {} x {}".format(img.shape[0], img.shape[1]))
	print("Image saved to: {} (If no result generated, plz check is dict made already!)".format(save_path))

if __name__ == '__main__':
	merge(path="src/", save_path="result.jpg", col=5)

