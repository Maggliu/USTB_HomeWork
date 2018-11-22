'''此文件为数学工具类，用于计算基站覆盖范围和最大下行速率'''
import math
from fileread import *
class MathWork:
    def __init__(self):
        '''hotnoise:热噪声;wide:带宽;gate：门限值;f:工作频率;baseStations：可用于绘制的基站位置数据'''
        self.const0=46.3
        self.const1=33.9
        self.const2=13.82
        self.Cm=3
        self.const3=44.9
        self.const4=6.55
    def setConfig(self,hot=0.0,wide=0.0,gate=0.0,f=0.0):#设置参数
        '''hotnoise:热噪声;wide:带宽;gate：门限值;f:工作频率'''
        if hot!=0.0:
            self.hotnoise=hot
        if wide!=0.0:
            self.wide=wide
        if gate!=0.0:
            self.gate=gate
        if f!=0.0:
            self.f=f
    def setBaseStation(self,baseStation):
        '''baseStations：可用于绘制的基站位置数据'''
        self.baseStations=baseStation
    def getCoverD(self):
        '''计算返回在门限值下的各基站的覆盖半径'''
        dList=[]
        for baseStation in self.baseStations:
            lgd=(-self.gate+baseStation[3]-self.const0-self.const1*math.log10(self.f)+self.const2*math.log10(baseStation[2])-self.Cm)/(self.const3-self.const4*math.log10(baseStation[2]))
            dList.append(10**lgd*1000)
        return dList
    def getSi(self,x0,y0,x1,y1,ht,Pbi):
        '''计算返回单个点对单个基站的功率'''
        d=self.__getDistance(x0,y0,x1,y1)/1000
        Si=Pbi-self.const0-self.const1*math.log10(self.f)+self.const2*math.log10(ht)-(self.const3-self.const4*math.log10(ht))*math.log10(d)-self.Cm
        return Si
    def getAllsi(self,x0,y0):
        '''计算单个点对于所有基站的功率'''
        siList=[]
        for baseStation in self.baseStations:
            temp=self.getSi(x0,y0,baseStation[0],baseStation[1],baseStation[2],baseStation[3])
            siList.append(temp)
        return siList
    def __getDistance(self,x0,y0,x1,y1):#计算点于点之间的距离
        temp=(x0-x1)**2+(y0-y1)**2
        return math.sqrt(temp)
    def getMaxDownload(self,x0,y0):
        '''#计算单个点的最大下行速率'''
        siList=self.getAllsi(x0,y0)#得到该点接收到的所有基站的功率
        maxSi=max(siList)#得到接收功率中的最大值
        maxSimW=self.dBmTomW(maxSi)#将dBm换算为mW
        siListmW=[self.dBmTomW(k) for k in siList]
        hotNoisemW=self.dBmTomW(self.hotnoise)*self.wide
        temp=self.wide*math.log2(1+maxSimW/(sum(siListmW)-maxSimW+hotNoisemW))#按香农公式计算最大下行速率
        return temp
    def dBmTomW(self,dBm):
        '''#dBm换算为mW'''
        return 10**(dBm/10)
    def getAllMaxDownload(self,x0,y0,steep,width,height):
        '''x0,y0：启始点坐标；steep：每次移动距离；width，height：需计算的宽度和高度。将width*height的矩形划分为边长steep的正方形，计算每个正方形中心的最大下行速率'''
        downloadDic={}
        rangeX=int(width/steep)
        rangeY=int(height/steep)
        for x in range(rangeX):
            for y in range(rangeY):
                downloadDic[(x,y)]=self.getMaxDownload(x0+steep*x,y0+steep*y)
        return downloadDic
#filrea=FileRead()
#mathwork=MathWork(-174,15000,-110,900,filrea.getFixedBaseStations())
