#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Date:2017/3/18 22:08
author:MarkYu
'''

import xlrd
import re
from PIL import Image,ImageDraw,ImageFont
from xpinyin import Pinyin
#打开xlsx文件
def open_excel(file= 'characterTable.xls'):
   try:
     data = xlrd.open_workbook(file)
     return data
   except Exception as e:
     print(e)

#寻找汉字     
def excel_table_byname(d,file= 'characterTable.xls',by_name='汉字部件拆分表',character="就"):
    d.send(None)
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    targetList=[]
    for i in range(1,table.nrows):
        targetList = table.row_values(i)
        d.send(targetList)
        #if(i == 5):
            #break
    d.close()

   
#画图
def drawCharacter():
    width = 320
    height = 480
    #build font obj
    font0 = ImageFont.truetype('C:/Windows/Fonts/Adobe Caslon Pro/ACaslonPro-Regular.otf',100)
    font1 = ImageFont.truetype('C:/Windows/Fonts/simsun.ttc',1260)
    font2 = ImageFont.truetype('C:/Windows/Fonts/simkai.ttf',370)
    font3 = ImageFont.truetype('C:/Windows/Fonts/STLITI.TTF',150)
    while True:
        image = Image.open('model.jpg') 
        #build draw obj
        draw = ImageDraw.Draw(image)
        #传入List            
        targetList = yield
        if not targetList:
            return

        #写入编号
        num = int(targetList[0])-1
        if num < 10: 
           draw.text((1030,3090),str(int(num)),font=font0,fill=(0,0,0))
        elif num < 100:
           draw.text((1010,3090),str(int(num)),font=font0,fill=(0,0,0))
        elif num < 1000:
           draw.text((990,3090),str(int(targetList[0])-1),font=font0,fill=(0,0,0))
        else:
           draw.text((960,3090),str(int(targetList[0])-1),font=font0,fill=(0,0,0))
        #写入文字
        draw.text((430,271),targetList[1],font=font1,fill=(0,0,0))
        #写入拼音
        draw.text((957,60),Pinyin().get_pinyin(targetList[1],show_tone_marks=True),font=font3,fill=(0,0,0))
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
        print('Chatacter{}Draw successfully!'.format(int(targetList[0])-1))
        #保存图片
        image.save('E:/汉字拆分/汉字[{}].jpg'.format(int(targetList[0])-1), 'jpeg')
        r = '200 OK'

def start(file= 'characterTable.xls'):
   d = drawCharacter()
   excel_table_byname(d,file)


if __name__=="__main__":
   start()
    
