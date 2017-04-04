from PIL import Image,ImageDraw,ImageFont
from xpinyin import Pinyin
def drawCharacter(targetList):
    width = 2126
    height = 3402
    image = Image.open('modeltest.jpg') 
    #build font obj
    font0 = ImageFont.truetype('C:/Windows/Fonts/Adobe Caslon Pro/ACaslonPro-Regular.otf',100)
    font1 = ImageFont.truetype('C:/Windows/Fonts/STXINGKA.TTF',1260)
    font2 = ImageFont.truetype('C:/Windows/Fonts/STXINWEI.TTF',370)
    #build draw obj
    draw = ImageDraw.Draw(image)
    #写入拼音
    draw.text((0,0),Pinyin().get_pinyin(targetList[1],show_tone_marks=True),font=font0,fill=(0,0,0))
    #写入编号
    draw.text((1010,3100),str(int(targetList[0])-1),font=font0,fill=(0,0,0))
    #写入文字
    draw.text((430,271),targetList[1],font=font1,fill=(0,0,0))
    #间隔
    gapWidth = 378
    gapHeight = 373
    #初始长宽
    multiWidth = 121
    multiHeight = 1851
    #写入部首
    for i in range(2,len(targetList)):
        if(targetList[i] != None):            
            draw.text((multiWidth,multiHeight),targetList[i],font=font2,fill=(0,0,0))
            multiWidth += gapWidth
            if((i-1)%5 == 0):
               multiHeight += gapHeight 
               multiWidth = 121
    #tips
    print("Draw successfully!")

    image.save('characterTest1.jpg', 'jpeg')

def main():
    targetList = [56.0, '就', '就', '京', '尤', '亠', '口', '小', '尢',]
    drawCharacter(targetList)
if __name__=="__main__":
   main()
