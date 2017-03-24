from PIL import Image,ImageDraw,ImageFont
def drawCharacter(targetList):
    width = 320
    height = 480
    image = Image.new('RGB',(width,height),(255,255,255)) 
    #build font obj
    font0 = ImageFont.truetype('C:/Windows/Fonts/STXIHEI.TTF',40)
    font1 = ImageFont.truetype('C:/Windows/Fonts/STXINGKA.TTF',100)
    font2 = ImageFont.truetype('C:/Windows/Fonts/STKAITI.TTF',50)
    #build draw obj
    draw = ImageDraw.Draw(image)
    #fullpilxr
    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=(255,255,255))
    #写入编号
    draw.text((0,0),str(int(targetList[0])-1),font=font0,fill=(0,0,0))
    #写入文字
    draw.text((0,height/6),targetList[1],font=font1,fill=(0,0,0))
    #间隔
    gapWidth = width/5
    gapHeight = height/8
    #初始长宽
    multiWidth = 0
    multiHeight = height/2
    #写入部首
    for i in range(2,len(targetList)):
        if(targetList[i] != None):            
            draw.text((multiWidth,multiHeight),targetList[i],font=font2,fill=(0,0,0))
            multiWidth += gapWidth
            if((i-1)%5 == 0):
               multiHeight += gapHeight 
               multiWidth = 0
    #tips
    print("Draw successfully!")

    image.save('character1.jpg', 'jpeg')

def main():
    targetList = [32.0, '就', '就', '京', '尤', '亠', '口', '小', '尢',]
    drawCharacter(targetList)
if __name__=="__main__":
   main()
