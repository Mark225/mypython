from tkinter import *

class MainWindow:
    def __init__(self):
        self.frame = Tk()
        
        self.label_single = Label(self.frame,text = "请输入单个汉字:")
        self.label_multi = Label(self.frame,text = "请输入Excel表路径:")

        self.text_single = Text(self.frame,height = "1",width = 30)
        self.text_multi = Text(self.frame,height = "1",width = 30)

        self.button_ok = Button(self.frame,text = "ok",command = ,width = 10)
        self.button_cancel = Button(self.frame,text = "cancel",command = ,width = 10)

        self.label_single.grid(row = 0,column = 0)
        self.label_multi.grid(row = 1,column = 0)

        self.text_single.grid(row = 0,column = 1)
        self.text_multi.grid(row = 1,column = 1)

        self.button_ok.grid(row = 3,column = 0)
        self.button_cancel.grid(row = 3,column = 1)

        self.frame.mainloop()

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
    font0 = ImageFont.truetype('C:/Windows/Fonts/STXIHEI.TTF',40)
    font1 = ImageFont.truetype('C:/Windows/Fonts/STLITI.TTF',100)
    font2 = ImageFont.truetype('C:/Windows/Fonts/STKAITI.TTF',60)
    while True:
        image = Image.open('model.jpg') 
        #build draw obj
        draw = ImageDraw.Draw(image)
        #传入List            
        targetList = yield
        if not targetList:
            return
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
        print('Chatacter{}Draw successfully!'.format(int(targetList[0])-1))
        #保存图片
        image.save('E:/汉字拆分/汉字[{}].jpg'.format(int(targetList[0])-1), 'jpeg')
        r = '200 OK'


frame = MainWindow()
