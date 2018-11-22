'''地图绘制类，主要负责地图的绘制'''
import tkinter as tk
class Map:
    def __init__(self,width,height,master,scale,r):
        '''width:地图宽；height：地图高；master：地图控件的父控件；scale：缩放比例；r：基站绘制半径'''
        self.cavHeight=height/scale
        self.cavWidth=width/scale
        self.cav=tk.Canvas(master=master,height=self.cavHeight,width=self.cavWidth)#创建画布以绘制地图
        self.scale=scale
        self.r=r
        self.baseStationList=[]
        self.coverCircleList=[]
        self.downRateList=[]
        self.buildingTag="building"
    def getCanvas(self):
        return self.cav
    def setGrid(self,row,column,rowspan,columnspan):#设置画布的位置
        self.cav.grid(row=row,column=column,rowspan=rowspan,columnspan=columnspan)
    def __addBuilding(self,building):
        self.cav.create_polygon([k/self.scale for k in building],fill="",outline="black")
    def addBuildings(self,buildings):#绘制建筑物
        for building in buildings:
            self.__addBuilding(building)
    def addBaseStation(self,baseStations):#绘制基站
        for baseStation in baseStations:
            self.baseStationList.append(self.cav.create_oval(baseStation[0]/self.scale-self.r,baseStation[1]/self.scale-self.r,baseStation[0]/self.scale+self.r,baseStation[1]/self.scale+self.r,fill='red'))
        self.cav.addtag_all(self.buildingTag)
    def move(self,tag,X=20,Y=20):
        '''移动所有以tag为标签的物体，X：X方向移动距离；Y:Y方向移动距离'''
        self.cav.move(tag,X,Y)
    def zoom(self,tag,scaleX=1.1,scaleY=1.1):#
        '''缩放所有以tag为标签的物体，X：X方向缩放倍数；Y:Y方向缩放倍数'''
        self.cav.scale(tag,self.cavWidth/2,self.cavHeight/2,scaleX,scaleY)
    def addBiankuan(self):
        '''添加边框'''
        self.cav.create_rectangle(0,0,self.cavWidth,self.cavHeight,fill='')
    def deleteTag(self,tag):
        '''删除所有以tag为标签的物体'''
        self.cav.delete(tag)
    def getBaseStationList(self):
        return self.baseStationList
    def drawCoverCircl(self,x0,y0,r):
        '''绘制圆型，x0，y0圆心坐标；r：半径'''
        self.coverCircleList.append(self.cav.create_oval((x0-r)/self.scale,(y0-r)/self.scale,(x0+r)/self.scale,(y0+r)/self.scale,fill='blue'))
    def deleteCoverC(self):
        '''删除所有覆盖面积图'''
        for circle in self.coverCircleList:
            self.cav.delete(circle)
    def drawDownRec(self,x0,y0,r,rate):
        '''绘制最大下行速率格子,具体颜色还未完全确定'''
        color=int(rate/90)
        color=str(hex(color))[2:]
        if len(color)==2:
            color='0'+color
        if len(color)==1:
            color='00'+color
        self.downRateList.append(self.cav.create_rectangle((x0-r)/self.scale,(y0-r)/self.scale,(x0+r)/self.scale,(y0+r)/self.scale,fill='#'+color))
    def deletDownRate(self):
        '''删除所有最大下行速率格子'''
        for rec in self.downRateList:
            self.cav.delete(rec)