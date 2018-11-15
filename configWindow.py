import tkinter as tk
import os
import json
class ConfigWindow:
    def __init__(self):
        self.path='mainWork\\config.json'
        self.entryLib={}
        self.configLib={}
        self.leftclick='<Button-1>'
        self.__initWidget()
        if os.path.exists(self.path):
            self.readFromFile(self.path)
    def start(self):
        self.configWindow.mainloop()
    def __initWidget(self):
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
    def __saveToFile(self,event):
        self.configLib=self.wigetDigital(self.entryLib)
        if self.configLib!=None:
            self.configFile=open(self.path,'wb+')
            self.configFile.write(json.dumps(self.configLib).encode())
            self.configFile.flush()
            self.configFile.close()
        self.configWindow.quit()
    def readFromFile(self,path):
        self.configFile=open(self.path)
        temp=self.configFile.readline()
        try:
            self.configLib=json.loads(temp)
        except TypeError:
            self.showInfo.config(text='文件格式错误')
        for key in self.entryLib.keys():
            self.entryLib[key].insert(0,self.configLib[key])
        self.configFile.close()
    def __typeErrorAlter(self,widget):
        widget.icursor(20)
        self.showInfo.config(text='输入错误')
    def wigetDigital(self,entryLib):
        tempLib={}
        for (k,v) in entryLib.items():
            try:
                tempLib[k]=float(v.get())
            except ValueError:
                self.__typeErrorAlter(entryLib[k])
                return None
        return tempLib