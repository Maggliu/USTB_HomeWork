# 通讯软件设计文档
## 简述
本软件通过tkiner库来完成ui界面的设计和实现，完成了给定地图数据的绘制，基站信号覆盖图和最大下行速率的计算。
## 概要设计
本软件有5个主要功能模块，分别完成文件读取和数值化，地图绘制，主窗口设计及逻辑，配置窗口设计及逻辑，数学计算的功能。
## 模块分析
### 文件读取和数值模块fileread.py
#### fileread.FileRead
> def __init__(self,path): 
* 构造函数
* path:文件路径
> def getMaxX(self):
* 获取数据中最大的X轴值
> def getMinX(self):
* 获取数据中最小的X轴值
> def getMaxY(self):
* 获取数据中最大的Y轴值
> def getMinY(self):
* 获取数据中最小的Y轴值
> def getWidth(self):
* 获取地图的宽度
> def getHeight(self):
* 获取地图的高度
> def getFixedBuildings(self):
* 获取由于绘图的建筑物座标，(0,0)点为西北角，在绘制时位于左上角
>  def getFixedBaseStations(self):
* 获取由于绘图的基站座标，(0,0)点为西北角，在绘制时位于左上角
### 地图绘制模块mymap.py
#### mymap.Map
> def __init__(self,width,height,master,scale,r):
* 构造函数
* width：地图的实际宽度，单位m
* height：地图的实际高度，单位m
* master：画布组件即地图显示的父组件，决定地图在那个窗口显示
* scale：缩放比例，实际绘制宽度为width/scale
* r：绘制的基站的半径
> def getCanvas(self):
* 返回地图的画布对象
> def setGrid(self,row,column,rowspan,columnspan):
* 设置画布的位置
* row:表格布局的行数
* column：表格布局的列数
* rowspan：表格布局部件所占行数
* columnspan：表格布局部件所占列数
> def addBuildings(self,buildings):
* 绘制建筑物
* buildings：用于绘制的建筑物坐标列表
> def addBaseStation(self,baseStations):#绘制基站
* 绘制基站
* baseStations：用于绘制的基站坐标列表
> def move(self,tag,X=20,Y=20):
* 移动所有以tag为标签的物体
* X：X方向移动距离
* Y：Y方向移动距离
> def zoom(self,tag,scaleX=1.1,scaleY=1.1):#
* 缩放所有以tag为标签的物体
* X：X方向缩放倍数
* Y：Y方向缩放倍数
> def addBiankuan(self):
* 为地图添加边框
> def deleteTag(self,tag):
* 删除所有以tag为标签的物体
> def drawCoverCircl(self,x0,y0,r):
* 绘制圆型
* x0,y0：圆心坐标
* r：半径
> def deleteCoverC(self):
* 删除所有覆盖面积图
> drawDownRec(self,x0,y0,r,rate):
* 绘制最大下行速率格子,具体颜色还未完全确定
* x0,y0：格子的中心点
* r：边长的1/2
* rate：最大下行速率
> def deletDownRate(self):
* 删除所有最大下行速率格子
### 参数设置窗口模块configWindow.py
#### configWindow.ConfigWindow
> def __init__(self,mathWork):
* 构造函数
* mathWork：数学工具类的实例
> def start(self):
* 显示窗口
> def readFromFile(self,path):
* 从配置文件读取参数
* path:配置文件路径
> def getConfig(self,key):
* 获取各参数的值
* key：键值
### 数学计算工具模块mathWork.py
#### mathWork.MathWork
> def __init__(self):
* 构造函数
> def setConfig(self,hot=0.0,wide=0.0,gate=0.0,f=0.0):
* 设置各参数
* hot:热噪声
* wide:带宽
* gate：门限值
* f:工作频率
> setBaseStation(self,baseStation):
* 设置基站坐标列表
* baseStations：可用于绘制的基站位置数据
> def getCoverD(self):
* 计算返回在门限值下的各基站的覆盖半径
> getSi(self,x0,y0,x1,y1,ht,Pbi):
* 计算返回单个点对单个基站的功率
* x0,y0：移动端位置
* x1,y1：基站位置
* ht：基站高度
* Pbi：基站发射功率
> def getAllsi(self,x0,y0):
* 计算返回单个点对于所有基站的功率
* x0,y0：计算点位置
> getMaxDownload(self,x0,y0):
* 计算返回单个点的最大下行速率
> def dBmTomW(self,dBm):
* dBm换算为mW
* dBm：输入的dBm值
> getAllMaxDownload(self,x0,y0,steep,width,height):
* 将width*height的矩形分为单个边长为steep的正方形小块，计算每个小块中心的最大下行速率用于代表整个小块的最大下行速率
* x0,y0：启始点坐标
* steep：正方形小块边长
* width，height：需计算的宽度和高度
### 软件的主UI窗口模块uiWindow.py
#### uiWindow.Application
>     def __init__(self):
* 构造函数
> def start(self):
* 打开主窗口
> def reDrawBuilding(self):
* 重绘建筑物和基站，因为在绘制覆盖图后将覆盖原本的建筑物，所以通过重绘显示建筑物
> def setMoveSteep(self,steep):
* 设置每次移动地图的距离
* steep：每次移动的距离
> def setZoomSteep(self,steep):
* 设置每次缩放地图的倍数
* steep：取值0~1，每次放大1+steep倍，每次缩小1-steep倍
> def setBuildings(self,buildings):
* 设置显示的建筑物列表
* buildings：用于绘制的建筑物坐标列表
> def setBaseStation(self,baseStations):
* 设置显示的基站列表
* baseStations：用于绘制的基站坐标列表