from PIL import Image,ImageFilter

im = Image.open('D:/1.png')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')
