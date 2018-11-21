'''该文件用于读取文件和数值化，为其他类提供数据'''
class FileRead:
    def __init__(self):
        self.file=open("D:\\PythonProject\\mainWork\\beijingdata.txt",mode='r')#得到数据文件
        mesList=self.file.readlines()#将所有数据以字符串形式读入
        mesListSize=len(mesList)#获取行数
        buildings=[]
        self.buildingsF=[]#数字化后的建筑物数据
        baseStations=[]
        self.baseStationF=[]#数字化后的基站数据
        count=0#记录操作到的行数
        while mesListSize-count>0:
            temp=mesList[count].split("\t")#将单行用\t分割，得到的列表暂存入temp中
            if temp[1]==' buildings ':#如果是建筑物数据
                buildings.append(mesList[count+1:int(temp[2])+1+count])#将该建筑物的所有坐标数据依旧以字符串形式存入列表中
                count+=int(temp[2])+1#移动操作行
            else:
                baseStations.append(mesList[count+1])
                count+=2
        for building in buildings:#将字符串数据数字化，最终的结果以二维列表存储
            buildingF=[]
            for temp in building:
                x,y=temp.split('\t')
                buildingF.append(float(x))
                buildingF.append(float(y))
            self.buildingsF.append(buildingF)
        for baseStation in baseStations:
            self.baseStationF.append([float(k) for k in baseStation.split('\t')])
        self.__findMaxAndmin()
    def __findMaxAndmin(self):#计算最大和最小的坐标值
        self.maxX,self.maxY=0.0,0.0
        self.minX,self.minY=9999999.0,9999999.0
        for building in self.buildingsF:
            for temp in building[0::2]:
                if self.maxX<temp:
                    self.maxX=temp
                if self.minX>temp:
                    self.minX=temp
            for temp in building[1::2]:
                if self.maxY<temp:
                    self.maxY=temp
                if self.minY>temp:
                    self.minY=temp
    def getMaxX(self):
        return self.maxX
    def getMinX(self):
        return self.minX
    def getMaxY(self):
        return self.maxY
    def getMinY(self):
        return self.minY
    def getWidth(self):
        return self.maxX-self.minX
    def getHeight(self):
        return self.maxY-self.minY
    def getFixedBuildings(self):
        '''计算并返回用于绘制的坐标值,原点在西北角'''
        self.fixedBuildngs=[]
        for building in self.buildingsF:#逐个取出建筑物
            buildingFix=[]
            for temp in building:#逐个取出坐标点
                if building.index(temp)%2==0:#偶数个坐标，减去最小的X坐标值
                    buildingFix.append(temp-self.minX)
                else:#奇数个坐标，被最大的Y坐标值减
                    buildingFix.append(self.maxY-temp)
            self.fixedBuildngs.append(buildingFix)
        return self.fixedBuildngs
    def getFixedBaseStations(self):
        '''计算并返回用于绘制的坐标值,原点在西北角'''
        self.fixedBaseStations=[]
        for basestation in self.baseStationF:
            temp=[]
            temp.append(basestation[0]-self.minX)
            temp.append(self.maxY-basestation[1])
            temp.append(basestation[2])
            temp.append(basestation[3])
            self.fixedBaseStations.append(temp)
        return self.fixedBaseStations