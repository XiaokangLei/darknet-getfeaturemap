#!/home/learner/miniconda3/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import matplotlib.image as mpimg

def process(filepath,outpath):
    for fileName in os.listdir(filepath):
        a=np.loadtxt(filepath+"/"+fileName)        
        im = Image.fromarray(np.uint8(a))
        plt.title(fileName)
        plt.imshow(im),plt.axis('off')
        im.save(outpath+"/"+fileName[:-4]+".jpg")
        #plt.savefig(outpath+"/"+fileName[:-4]+".jpg",bbox_inches="tight",transparent=True,pad_inches=0)
   
# 定义图像拼接函数
def image_compose(IMAGE_SIZE,IMAGE_ROW,IMAGE_COLUMN,image_names,IMAGE_SAVE_PATH):
    to_image = Image.new('RGB', (IMAGE_COLUMN * IMAGE_SIZE, IMAGE_ROW * IMAGE_SIZE)) #创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    for y in range(1, IMAGE_ROW + 1):
        for x in range(1, IMAGE_COLUMN + 1):
            from_image = Image.open(IMAGES_PATH + image_names[IMAGE_COLUMN * (y - 1) + x - 1]).resize(
                (IMAGE_SIZE, IMAGE_SIZE),Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * IMAGE_SIZE, (y - 1) * IMAGE_SIZE))
    return to_image.save(IMAGE_SAVE_PATH) # 保存新图
      
if __name__ == "__main__":
	outpath = "feature_pic"
	filepath="feature_txt"

	IMAGES_FORMAT = ['.jpg', '.JPG']  # 图片格式
	IMAGE_SIZE_t =   [416,208,208,104,104,52,52,26,26,13,13,13,13,13,13,13,13,13,13,26,26,26,26,26]  # 每张小图片的大小
	IMAGE_ROW_t =    [  4,  4,  4,  4,  8, 8, 8, 8,16,16,16,16,32,16,16,15,15,16, 8, 8,16,16,15,15]  # 图片间隔，也就是合并成一张图后，一共有几行
	IMAGE_COLUMN_t = [  4,  4,  8,  8,  8, 8,16,16,16,16,32,32,32,16,32,17,17,16,16,16,24,16,17,17]  # 图片间隔，也就是合并成一张图后，一共有几列
	
	count = 0
	plt.figure()
	#fpathe_0 = []
	#fpathe1_1 = []
	#for (root1, dirs1, files1) in os.walk(filepath):
	#	fpathe_0.append(dirs1)
	#fpathe_0.sort()
	#for (root2, dirs2, files2) in os.walk(outpath):
	#	fpathe1_1.append(dirs2)
	#fpathe1_1.sort()
	for fpathe,fpathe1 in zip(os.walk(filepath),os.walk(outpath)):
	#for fpathe,fpathe1 in zip(fpathe_0,fpathe1_1):
		#for f in fs:
		if(count!=0):
			plt.subplot(5,5,count)
			IMAGE_SAVE_PATH = 'feature_pic_final/'+str(count-1)+'.jpg'  # 图片转换后的地址
			process(fpathe[0],fpathe1[0])
			#print(fpathe[0],fpathe1[0])
			IMAGES_PATH = fpathe1[0] + "/"
			#IMAGES_PATH = "feature_pic/" + str(count-1) + "/"
			# 获取图片集地址下的所有图片名称
			print(IMAGES_PATH)
			number_pic = int(fpathe1[0].split("/")[1])
			print(number_pic)
			#print(count-1)
			image_names = [name for name in os.listdir(IMAGES_PATH) for item in IMAGES_FORMAT if os.path.splitext(name)[1] == item]
			print(IMAGES_PATH,len(image_names),IMAGE_SAVE_PATH,count)
			#print(IMAGE_ROW_t[count-1],IMAGE_COLUMN_t[count-1])
			print(IMAGE_ROW_t[number_pic],IMAGE_COLUMN_t[number_pic])
			# 简单的对于参数的设定和实际图片集的大小进行数量判断
			#if len(image_names) != IMAGE_ROW_t[count -1] * IMAGE_COLUMN_t[count-1]:
			#	raise ValueError("ERRO!")
			#image_compose(IMAGE_SIZE_t[count-1],IMAGE_ROW_t[count-1],IMAGE_COLUMN_t[count-1],image_names,IMAGE_SAVE_PATH) #调用函数
			
			image_compose(IMAGE_SIZE_t[number_pic],IMAGE_ROW_t[number_pic],IMAGE_COLUMN_t[number_pic],image_names,IMAGE_SAVE_PATH) #调用函数
			lena = mpimg.imread(IMAGE_SAVE_PATH)
			img = plt.imshow(lena) # 显示图片
			#img.set_cmap('hot')
			#plt.axis('off') # 不显示坐标轴
			
		#print(fpathe[0],fpathe1[0])
		count = count + 1
	plt.show()
	
 
