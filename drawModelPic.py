from PIL import Image,ImageDraw,ImageFont


font1 = ImageFont.truetype('C:/Windows/Fonts/STLITI.TTF',750)
image = Image.open('CharacterModel.jpg')
#build draw obj
draw = ImageDraw.Draw(image)

#写入文字
draw.text((74,555),'受',font=font1,fill=(0,0,0))
image.save('modeltest.jpg', 'jpeg')
