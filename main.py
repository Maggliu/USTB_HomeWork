'''
软件入口，初始化地图参数
'''
from uiWindow import *
if __name__ == "__main__":
    app=Applicaton()
    app.initMap(5,6)
    app.setMoveSteep(50)
    app.setZoomSteep(0.1)
    app.start()