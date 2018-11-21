'''
该文件为主界面程序，负责UI的显示，控件事件函数的书写和绑定
'''
import tkinter as tk
from mymap import *
from fileread import *
from configWindow import *
from mathWork import *
import time
class Applicaton:
    def __init__(self):
        self.window=tk.Tk()#创建Tk窗口
        self.__initWidget()#初始化各个控件
        self.fileReader=FileRead()#实例化文件读取对象
        self.buildingTag="building"
        self.baseStationTag="baseStation"
        self.leftclick='<Button-1>'#左击事件的字符串常量
        self.baseStations=self.fileReader.getFixedBaseStations()#从文件读取对象中得到可用于绘图的基站，建筑坐标
        self.buildings=self.fileReader.getFixedBuildings()
        self.configWindow=ConfigWindow()#实例化配置窗口对象
        #实例化数学工具对象，并从配置窗口获取各参数
        self.mathWork=MathWork(self.configWindow.getConfig('hotnoise'),self.configWindow.getConfig('wide'),self.configWindow.getConfig('RSRPgate'),self.configWindow.getConfig('flv'),self.baseStations)
        self.moveSteep=0#该变量用于设定每次移动地图移动的距离
        self.zoomSteep=0#该变量用于设定每次缩放地图的比例
        self.__bindEvent()#为各控件绑定事件
    def start(self):
        '''打开主窗口'''
        self.window.mainloop()
    def initMap(self,scale,r):
        '''初始化地图，设定比例尺系数rscale和每个基站的绘制半径r'''
        self.mapWidth=self.fileReader.getWidth()#从文件读取对象获取地图的设计宽和高
        self.mapHeight=self.fileReader.getHeight()
        self.map=Map(self.mapWidth,self.mapHeight,self.window,scale,r)#实例化地图类，输入宽高等参数
        self.setBuildings(self.buildings)#为map对象设置建筑物和基站信息
        self.setBaseStation(self.baseStations)
        self.map.addBiankuan()#为地图添加边框
        self.map.setGrid(0,0,22,22)#设置地图在主窗口中的位置
    def reDrawBuilding(self):#重绘建筑物和基站，因为在绘制覆盖图后将覆盖原本的建筑物，所以通过重绘显示建筑物
        self.setBuildings(self.buildings)
        self.setBaseStation(self.baseStations)
    def setMoveSteep(self,steep):#重新设置地图参数
        self.moveSteep=steep
    def setZoomSteep(self,steep):
        self.zoomSteep=steep
    def setMapGrid(self,row=0,column=0,rowspan=1):
        self.map.setGrid(row=row,column=column,rowspan=rowspan,columnspan=columnspan)
    def setBuildings(self,buildings):
        self.map.deleteTag(self.buildingTag)
        self.map.addBuildings(buildings)
        self.buildings=buildings
    def setBaseStation(self,baseStations):
        self.map.deleteTag(self.baseStationTag)
        self.map.addBaseStation(baseStations)
        self.baseStations=baseStations
    def __initWidget(self):#私有函数，设置各控件内容和位置
        self.leftButton=tk.Button(self.window,text="左移")
        self.leftButton.grid(row=17,column=23)
        self.rightButton=tk.Button(self.window,text="右移")
        self.rightButton.grid(row=17,column=27)
        self.upButton=tk.Button(self.window,text="上移")
        self.upButton.grid(row=16,column=25)
        self.downButton=tk.Button(self.window,text="下移")
        self.downButton.grid(row=18,column=25)
        self.zoomButton=tk.Button(self.window,text="放大")
        self.zoomButton.grid(row=20,column=27)
        self.suoxiaoButton=tk.Button(self.window,text="缩小")
        self.suoxiaoButton.grid(row=20,column=23)
        self.configButton=tk.Button(self.window,text='配置')
        self.configButton.grid(row=0,column=23)
        self.coverFenxi=tk.Button(self.window,text='进行覆盖分析')
        self.coverFenxi.grid(row=1,column=23,rowspan=1,columnspan=3)
        self.downloadFenxi=tk.Button(self.window,text='进行最大下行速率分析')
        self.downloadFenxi.grid(row=2,column=23,rowspan=1,columnspan=5)
    def __bindEvent(self):#私有函数，为各控件绑定事件
        self.rightButton.bind(self.leftclick,self.__moveRight)
        self.leftButton.bind(self.leftclick,self.__moveLeft)
        self.upButton.bind(self.leftclick,self.__moveUp)
        self.downButton.bind(self.leftclick,self.__moveDown)
        self.zoomButton.bind(self.leftclick,self.__zoom)
        self.suoxiaoButton.bind(self.leftclick,self.__souxiao)
        self.configButton.bind(self.leftclick,self.__initCongifWindow)
        self.coverFenxi.bind(self.leftclick,self.__coverFenxi)
        self.downloadFenxi.bind(self.leftclick,self.__downLoadFenxi)
    def __moveUp(self,event):#完成地图各种动作的函数，被绑定于各控件上
        self.map.move(self.buildingTag,0,-self.moveSteep)
        self.map.move(self.baseStationTag,0,-self.moveSteep)
    def __moveDown(self,event):
        self.map.move(self.buildingTag,0,self.moveSteep)
        self.map.move(self.baseStationTag,0,self.moveSteep)
    def __moveRight(self,event):
        self.map.move(self.buildingTag,self.moveSteep,0)
        self.map.move(self.baseStationTag,self.moveSteep,0)
    def __moveLeft(self,event):
        self.map.move(self.buildingTag,-self.moveSteep,0)
        self.map.move(self.baseStationTag,-self.moveSteep,0)
    def __zoom(self,event):
        self.map.zoom(self.buildingTag,self.zoomSteep+1,self.zoomSteep+1)
        self.map.zoom(self.baseStationTag,self.zoomSteep+1,self.zoomSteep+1)
    def __souxiao(self,event): 
        self.map.zoom(self.buildingTag,1-self.zoomSteep,1-self.zoomSteep)
        self.map.zoom(self.baseStationTag,1-self.zoomSteep,1-self.zoomSteep)
    def __initCongifWindow(self,event):#显示配置窗口
        self.configWindow.start()
    def __coverFenxi(self,event):#进行覆盖范围的分析并绘制覆盖范围
        self.map.deleteCoverC()#进行新一次覆盖计算是先删去上一次绘制内容
        dList=self.mathWork.getCoverD()#通过数学工具类得到覆盖半径列表
        count=0
        for basestation in self.baseStations:#为各基站绘制覆盖范围
            self.map.drawCoverCircl(basestation[0],basestation[1],dList[count])
            count+=1
        self.reDrawBuilding()#重绘建筑物以显示建筑物
    def __downLoadFenxi(self,event):#进行最大下行速率的分析并绘制分析图
        self.map.deletDownRate()#进行新一次计算时先删去上一次绘制内容
        dDic=self.mathWork.getAllMaxDownload(0,0,40,self.mapWidth,self.mapHeight)#得到各区域的最大下行速率
        for (x,y),v in dDic.items():
            self.map.drawDownRec(x*40,y*40,20,v)
        self.reDrawBuilding()
