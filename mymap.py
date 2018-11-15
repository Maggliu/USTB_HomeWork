import tkinter as tk
class Map:
    def __init__(self,width,height,master,scale,r):
        self.cavHeight=height/scale
        self.cavWidth=width/scale
        self.cav=tk.Canvas(master=master,height=self.cavHeight,width=self.cavWidth)
        self.scale=scale
        self.r=r
        self.baseStationList=[]
        self.buildingTag="building"
        self.baseStationTag="baseStation"
    def getCanvas(self):
        return self.cav
    def setGrid(self,row,column,rowspan,columnspan):
        self.cav.grid(row=row,column=column,rowspan=rowspan,columnspan=columnspan)
    def __addBuilding(self,building):
        self.cav.create_polygon([k/self.scale for k in building],fill="",outline="black")
    def addBuildings(self,buildings):
        for building in buildings:
            self.__addBuilding(building)
        self.cav.addtag_all(self.buildingTag)
    def addBaseStation(self,baseStations):
        for baseStation in baseStations:
            self.baseStationList.append(self.cav.create_oval(baseStation[0]/self.scale-self.r,baseStation[1]/self.scale-self.r,baseStation[0]/self.scale+self.r,baseStation[1]/self.scale+self.r,fill='red'))
            self.cav.addtag_closest(self.baseStationTag,baseStation[0]/self.scale,baseStation[1]/self.scale)
    def move(self,tag,X=20,Y=20):
        self.cav.move(tag,X,Y)
    def zoom(self,tag,scaleX=1.1,scaleY=1.1):
        self.cav.scale(tag,self.cavWidth/2,self.cavHeight/2,scaleX,scaleY)
    def addBiankuan(self):
        self.cav.create_rectangle(0,0,self.cavWidth,self.cavHeight,fill='')
    def deleteTag(self,tag):
        self.cav.delete(tag)
    def getBaseStationList(self):
        return self.baseStationList
    