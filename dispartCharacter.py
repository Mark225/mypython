#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd
import re
from PIL import Image,ImageDraw,ImageFont

#打开xlsx文件
def open_excel(file= 'character.xlsx'):
   try:
     data = xlrd.open_workbook(file)
     return data
   except Exception as e:
     print(e)

#寻找汉字     
def excel_table_byname(file= 'character.xlsx',by_name='汉字序号',character="就"):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    for i in range(1,table.nrows):
        if(character == table.cell(i,2).value):
            targetList = table.row_values(i)
            break
    print(targetList)
    return targetList

   
#画图
def drawCharacter(targetList):
    width = 320
    height = 480
    image = Image.new('RGB',(width,height),(255,255,255)) 
    #build font obj
    font0 = ImageFont.truetype('C:/Windows/Fonts/STXIHEI.TTF',40)
    font1 = ImageFont.truetype('C:/Windows/Fonts/STLITI.TTF',100)
    font2 = ImageFont.truetype('C:/Windows/Fonts/STKAITI.TTF',60)
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
    #保存图片
    image.save('汉字[{}].jpg'.format(int(targetList[0])-1), 'jpeg')


if __name__=="__main__":
    #输入文字
   character = input("请输入汉字:")
   targetList = excel_table_byname(character=character)
   drawCharacter(targetList)
    
