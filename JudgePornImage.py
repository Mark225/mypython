import sys
from PIL import Image  

fileName = r'F:\照片\image3.jpeg'  
img = Image.open(fileName).convert('YCbCr')
 
w, h = img.size  
  
data = img.getdata()  
  
cnt = 0  
  
for i, ycbcr in enumerate(data):  
  
    y, cb, cr = ycbcr  
    #Cb[77,125] and Cr[135,168]
    if 86 <= cb <= 117 and 140 <= cr <= 168:  
  
        cnt += 1  
  
print('%s %s a porn image.'%(fileName, 'is' if cnt > w * h * 0.3 else 'is not')  )
