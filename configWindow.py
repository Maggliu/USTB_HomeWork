'''该文件为设置配置文件的窗口,原来存取配置文件'''
import tkinter as tk
import os
import json
from mathWork import *
class ConfigWindow:
    def __init__(self,mathWork):
        self.path='config.json'
        self.entryLib={}#输入控件字典
        self.configLib={}#参数字典
        self.leftclick='<Button-1>'
        self.mathWork=mathWork
        if os.path.exists(self.path):#如果配置文件存在则从配置文件读取参数
            self.readFromFile(self.path)
    def start(self):#显示窗口
        self.__initWidget()
        if self.configLib:#判断参数字典是否为空，如果有参数，则在输入控件上显示参数
            self.inintFromFile()
        self.configWindow.mainloop()
    def __initWidget(self):#私有函数，初始控件位置内容
        self.configWindow=tk.Tk()
        tk.Label(self.configWindow,text='热噪声：').grid(row=1,column=0)
        tk.Label(self.configWindow,text='带宽：').grid(row=2,column=0)
        tk.Label(self.configWindow,text='频率：').grid(row=3,column=0)
        tk.Label(self.configWindow,text='RSRP门限：').grid(row=4,column=0)
        self.entryLib['hotnoise']=tk.Entry(self.configWindow)
        self.entryLib['hotnoise'].grid(row=1,column=1,columnspan=2)
        self.entryLib['wide']=tk.Entry(self.configWindow)
        self.entryLib['wide'].grid(row=2,column=1,columnspan=2)
        self.entryLib['flv']=tk.Entry(self.configWindow)
        self.entryLib['flv'].grid(row=3,column=1,columnspan=2)
        self.entryLib['RSRPgate']=tk.Entry(self.configWindow)
        self.entryLib['RSRPgate'].grid(row=4,column=1,columnspan=2)
        self.sureButton=tk.Button(self.configWindow,text='确定')
        self.sureButton.grid(row=6,column=1,columnspan=2)
        self.sureButton.bind(self.leftclick,self.__saveToFile)
        tk.Label(self.configWindow,text='dBm/Hz').grid(row=1,column=3)
        tk.Label(self.configWindow,text='Hz').grid(row=2,column=3)
        tk.Label(self.configWindow,text='MHz').grid(row=3,column=3)
        tk.Label(self.configWindow,text='dBm').grid(row=4,column=3)
        self.showInfo=tk.Label(self.configWindow)
        self.showInfo.grid(row=7,columnspan=2)
    def __saveToFile(self,event):#私有函数，输入的参数保存到文件中，被绑定于确定按钮
        self.configLib=self.wigetDigital(self.entryLib)#获取输入控件中的数值
        if self.configLib!=None:
            self.configFile=open(self.path,'wb+')
            self.configFile.write(json.dumps(self.configLib).encode())#json化存入文件
            self.configFile.flush()
            self.configFile.close()
        self.__setMathwork()#对数学工具类中的参数进行更新
        self.configWindow.destroy()#关闭窗口
    def readFromFile(self,path):#从配置文件读取参数
        self.configFile=open(self.path)#获取文件对象
        temp=self.configFile.readline()
        try:
            self.configLib=json.loads(temp)#从文件读取到的字符串用json还原为字典
        except TypeError:#文件内容不符合时获取此异常，可以添加警示信息
            print("typeError")
        self.configFile.close()
        self.__setMathwork()#对数学工具类中的参数进行更新
    def inintFromFile(self):#从参数字典参数控件，主要是显示上次设置的内容
        for key in self.entryLib.keys():
            self.entryLib[key].insert(0,self.configLib[key])
        self.configFile.close()
    def __typeErrorAlter(self,widget):#显示输入错误信息
        widget.icursor(20)
        self.showInfo.config(text='输入错误')
    def wigetDigital(self,entryLib):#数值化输入控件内的参数
        tempLib={}
        for (k,v) in entryLib.items():#从控件字典获取控件和名字
            try:
                tempLib[k]=float(v.get())#强制转换为float型
            except ValueError:#输入不规范时捕获异常，显示输入错误信息
                self.__typeErrorAlter(entryLib[k])
                return None
        return tempLib
    def getConfig(self,key):#获取各参数的值
        print(self.configLib)
        return self.configLib[key]
    def __setMathwork(self):#对数学工具类中的参数进行更新
        self.mathWork.setConfig(hot=self.configLib['hotnoise'],wide=self.configLib['wide'],gate=self.configLib['RSRPgate'],f=self.configLib['flv'])