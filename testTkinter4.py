from tkinter import *
import xlrd
from PIL import Image,ImageDraw,ImageFont
import os
from tkinter import filedialog


#打开xlsx文件
def open_excel(file= 'character.xlsx'):
   try:
     file = path.get()
     data = xlrd.open_workbook(file)
     return data
   except Exception as e:
     print(e)

#寻找汉字     
def excel_table_byname(by_name='汉字序号',character="就"):
    if(savePath.get() == ''):
       messagebox.showinfo(message='请先点击菜单栏“保存”，设置图片存储路径！')
       return 
    character = ch.get()
    by_name = sheet.get()
    data = open_excel()
    table = data.sheet_by_name(by_name)
    targetList = []
    if(selectType.get() == 'single'):
       for i in range(1,table.nrows):
           if(character == table.cell(i,1).value):
               targetList = table.row_values(i)
               drawCharacter(targetList)
               break         
       print(targetList)
    elif(selectType.get() == 'multiple'):
       for i in range(1,table.nrows):
          targetList = table.row_values(i)
          drawCharacter(targetList)
   
   
#画图
def drawCharacter(targetList):
    width = 320
    height = 480

    #build font obj
    font0 = ImageFont.truetype('C:/Windows/Fonts/STXIHEI.TTF',40)
    font1 = ImageFont.truetype('C:/Windows/Fonts/STLITI.TTF',100)
    font2 = ImageFont.truetype('C:/Windows/Fonts/STKAITI.TTF',60)
    
    image = Image.open(picPath.get()) 
    #build draw obj
    draw = ImageDraw.Draw(image)
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
    image.save(savePath.get() + ('\汉字[{}].jpg'.format(int(targetList[0])-1)), 'jpeg')

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def openFile():
   path.set(filedialog.askopenfilename())

def picFile():
   picPath.set(filedialog.askopenfilename())

def saveFile():
   savePath.set(filedialog.askdirectory())
   print(savePath.get())

def setSheet():
   filename = filedialog.asksaveasfilename()

root = Tk()
root.title("部件拆分器")
#---菜单---
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="打开文件", command=openFile)
filemenu.add_command(label="打开表格", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="退出", command=root.quit)
menubar.add_cascade(label="打开", menu=filemenu)

savemenu = Menu(menubar, tearoff=0)
savemenu.add_command(label="图片存储路径", command=saveFile)
savemenu.add_command(label="图片存储格式", command=donothing)
savemenu.add_separator()
savemenu.add_command(label="模版图片路径", command=picFile)
menubar.add_cascade(label="设置", menu=savemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="帮助目录", command=donothing)
helpmenu.add_command(label="关于...", command=donothing)
menubar.add_cascade(label="帮助", menu=helpmenu)

#---主界面---
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#---汉字输入---
ttk.Label(mainframe, text="请输入汉字：").grid(column=1, row=4, sticky=W)
ch = StringVar()
ch_entry = ttk.Entry(mainframe,width=7, textvariable=ch)
ch_entry.grid(column=2, row=4, sticky=(W, E))
ch_entry.state(['disabled'])

#---文件路径输入---
ttk.Label(mainframe, text="请输入文件路径：").grid(column=1, row=2, sticky=W)
path = StringVar()
savePath = StringVar()
picPath = StringVar()
path_entry = ttk.Entry(mainframe,width=30, textvariable=path)
path_entry.grid(column=2, row=2, sticky=(W, E))
path_entry.state(['disabled'])
#---表格名称输入---
ttk.Label(mainframe, text="请输入表格名称：").grid(column=1, row=3, sticky=W)
sheet = StringVar()
sheet_entry = ttk.Entry(mainframe,width=30, textvariable=sheet)
sheet_entry.grid(column=2, row=3, sticky=(W, E))
sheet_entry.state(['disabled'])
#---拆分模式选择---
ttk.Label(mainframe, text="请选择拆分模式：").grid(column=1, row=1, sticky=W)
selectType = StringVar()
single = ttk.Radiobutton(mainframe, text='单字拆分',command=lambda :(ch_entry.state(['!disabled']),path_entry.state(['!disabled']),sheet_entry.state(['!disabled'])),variable=selectType,value='single')
single.grid(column=2, row=1)
multiple = ttk.Radiobutton(mainframe, text='批量拆分',command=lambda :(ch_entry.state(['disabled']),path_entry.state(['!disabled']),sheet_entry.state(['!disabled'])),variable=selectType,value='multiple')
multiple.grid(column=3, row=1)
#---按钮---
ttk.Button(mainframe, text="制作图片", command=excel_table_byname).grid(column=1, row=5)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.config(menu=menubar)
root.mainloop()
