from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
#生成随机数字
def rndChar():
    return str(random.randint(1,100))
#打开图片
image = Image.open("E:\\python\\test.jpg")
#设置字体
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf',90)
#建立画画对象
draw = ImageDraw.Draw(image)
#在图片上画字
draw.text((image.width * 13/17,image.height/35),rndChar(),font=font,fill=(255,0,0))

image.save('test1.jpg','jpeg')
