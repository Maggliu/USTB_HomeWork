import tkinter as tk
from mymap import *
from fileread import *
from configWindow import *
from mathWork import *
import time
class Applicaton:
    def __init__(self):
        self.window=tk.Tk()
        self.__initWidget()
        self.fileReader=FileRead()
        self.buildingTag="building"
        self.baseStationTag="baseStation"
        self.leftclick='<Button-1>'
        self.configWindow=ConfigWindow()
        self.moveSteep=0
        self.zoomSteep=0
        self.__bindEvent()
    def start(self):
        self.window.mainloop()
    def initMap(self,scale,r):
        self.mapWidth=self.fileReader.getWidth()
        self.mapHeight=self.fileReader.getHeight()
        self.map=Map(self.mapWidth,self.mapHeight,self.window,scale,r)
        self.baseStations=self.fileReader.getFixedBaseStations()
        self.buildings=self.fileReader.getFixedBuildings()
        self.setBuildings(self.buildings)
        self.setBaseStation(self.baseStations)
        self.map.addBiankuan()
        self.map.setGrid(0,0,22,22)
    def reDrawBuilding(self):
        self.setBuildings(self.buildings)
        self.setBaseStation(self.baseStations)
    def setMoveSteep(self,steep):
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
    def __initWidget(self):
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
    def __bindEvent(self):
        self.rightButton.bind(self.leftclick,self.__moveRight)
        self.leftButton.bind(self.leftclick,self.__moveLeft)
        self.upButton.bind(self.leftclick,self.__moveUp)
        self.downButton.bind(self.leftclick,self.__moveDown)
        self.zoomButton.bind(self.leftclick,self.__zoom)
        self.suoxiaoButton.bind(self.leftclick,self.__souxiao)
        self.configButton.bind(self.leftclick,self.__initCongifWindow)
        self.coverFenxi.bind(self.leftclick,self.__coverFenxi)
    def __moveUp(self,event):
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
    def __initCongifWindow(self,event):
        self.configWindow.start()
    def __coverFenxi(self,event):
        self.mathWork=MathWork(self.configWindow.getConfig('RSRPgate'),self.configWindow.getConfig('flv'))
        self.map.deleteCoverC()
        for basestation in self.baseStations:
            d=self.mathWork.getCoverD(basestation[2],basestation[3])
            self.map.drawCoverCircl(basestation[0],basestation[1],d)
        self.reDrawBuilding()
app=Applicaton()
app.initMap(5,6)
app.setMoveSteep(50)
app.setZoomSteep(0.1)
app.start()