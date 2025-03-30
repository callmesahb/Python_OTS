from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot
from Store import Store
from Link import Link
from Indicator import Indicator
from valveEV import valveEV
from dosing import DosingPump
from Store import Store
from AirCoolerElem import Aircooler
from Menubar import Menu
from BPS_elem import BPS
from FilterElem import Filter
from Equipment import Equipment
from Pump import NormalPump
from controllerValve import ControllerValve
from Slider import Slider
from HAND import HAND
import os
import json

class MainWidget(QtWidgets.QWidget):
    changePageSignal = pyqtSignal(int)
    ChangingValveStatus = pyqtSignal(int)
    updatevalues = pyqtSignal(dict,list)

    def __init__(self, store: Store):
        super().__init__()
        self.rootdir = os.getcwd()
        self.imgdir = os.path.join(self.rootdir, "images")
        self.store = store
        self._initUi()
        self._addMenu()
        self._addGraphic()

    def _initUi(self):
        self.mainlayout = QtWidgets.QHBoxLayout()
        self.mainlayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.mainlayout)
    def Printing(self):
        print("SAAALLLAAAMMMM")

    def _addMenu(self):
        self.menu = Menu(self.store)
        self.mainlayout.addWidget(self.menu)
        # self.menu.left.clicked.connect(self.Printing)
    
    def updateDesc(self,desc:str):
        # print(f"Updating to {desc}")
        self.menu.desc.setText(desc)
    def updatepage(self,desc:str):
        self.menu.pagenum.setText(desc)
    def _addGraphic(self):
        self.graphicsview = QtWidgets.QGraphicsView()
        self.graphicsscene = QtWidgets.QGraphicsScene()
        self.graphicsview.setScene(self.graphicsscene)
        self.graphicsview.setStyleSheet("background-color: rgb(103, 103, 103);")
        # self.graphicsview.fitInView()
        self.mainlayout.addWidget(self.graphicsview)

    def newImage(self, img: QtGui.QPixmap) -> QtGui.QPixmap:
        img_width = img.size().width()
        img_height = img.size().height()
        screen_width = self.screen().size().width()
        screen_height = 0.88 * self.screen().size().height()

        width_scale = screen_width / img_width
        height_scale = screen_height / img_height

        self.scale = min(width_scale, height_scale)

        newimg_width = int(img_width * self.scale)
        newimg_height = int(img_height * self.scale)

        newImg = img.scaled(newimg_width, newimg_height)

        return newImg

    def createAllscenes(self, pages: list):
        self.scenes = []
        for page in pages:
            tempScene = QtWidgets.QGraphicsScene()
            img_path = os.path.join(self.rootdir, page["imageUrl"])
            mainImage = QtGui.QPixmap(img_path)
            self.scaledImage = self.newImage(mainImage)
            tempScene.addPixmap(self.scaledImage)
            for _ind in page["indicators"]:
                pos = _ind["pos"]
                name = _ind["id"]
                variableid = _ind["variableId"]
                itype = _ind["type"]
                value = self.store.SettingInitial(variableid)
                pvvalues = self.store.GettingControllerDetails(variableid)
                indi = Indicator(name, value, itype, pvvalues,self.store,variableid)
                indi.setGeometry(int(self.scale * pos["l"]), int(self.scale * pos["t"]), 80, 20)
                tempScene.addWidget(indi)
            for _link in page["links"]:
                pos = _link["pos"]
                dest = _link["to"]
                link = Link(dest)
                link.setGeometry(int(self.scale * pos["l"]), int(self.scale * pos["t"]), int(self.scale * pos["w"]),
                                 int(self.scale * pos["h"]))
                link.changePageSignal.connect(self.ChangePageByLink)
                tempScene.addWidget(link)
            for _valve in page["valves"]:
                pos = _valve["pos"]
                variableid = _valve["variableId"]
                name = _valve["id"]
                _type = _valve["type"]
                rotated = _valve["rotated"]
                valve = None

                value = self.store.setting_valueEV(variableid) if _type != "controller" else None

                if _type == "controller" and variableid in self.store.getting_names():
                    pvvalues = self.store.GettingControllerDetails(variableid)
                    valve = ControllerValve(name, rotated, pvvalues,variableid,self.store)
                    valve.set_status(pvvalues[2])
                elif _type in {"sdv", "bdv"}:
                    valve = valveEV(self.store,variableid,name, value,rotated)
                    # valve.ChangingValveStatus.connect(self.CheckingvalueSDV)
                    # valve.set_status(value)
                elif _type == "dosing":
                    valve = DosingPump(rotated)
                    valve.set_status(value)
                elif _type == "fan":
                    valve = Aircooler(name)
                    valve.set_status(value)
                elif _type == "bps":
                    valve = BPS(self.store,variableid,name, value)
                    valve.set_status(value)
                elif _type == "Filter":
                    valve = Filter(name, value)
                    valve.toggle_images(value)
                elif _type == "pump":
                    valve = NormalPump(name, value)
                    valve.set_status(value)

                if valve:
                    valve.setGeometry(
                        int(self.scale * pos["l"]),
                        int(self.scale * pos["t"]),
                        int(self.scale * pos["w"]),
                        int(self.scale * pos["h"]),
                    )
                    tempScene.addWidget(valve)
            for _slider in page["sliders"]:
                pos = _slider["pos"]
                w = pos["w"]
                h = pos["h"]
                name = _slider["id"]
                variableid = _slider["variableId"]
                pvvalues = self.store.GettingControllerDetails(variableid)
                rotated = _slider["rotated"]
                slider = Slider(rotated, w, h, pvvalues[2],name,self.store,variableid)
                slider.setGeometry(int(self.scale * pos["l"]), int(self.scale * pos["t"]), int(self.scale * pos["w"]),
                                   int(self.scale * pos["h"]))
                tempScene.addWidget(slider)
            for _eqn in page["equipments"]:
                _id = _eqn["id"]
                pos = _eqn["pos"]
                htype = _eqn["type"]
                btns = _eqn["buttons"]
                eqn = Equipment(_id,htype,btns)
                eqn.setGeometry(int(self.scale * pos["l"]), int(self.scale * pos["t"]), int(self.scale * pos["w"]),
                                   int(self.scale * pos["h"]))
                tempScene.addWidget(eqn)
            for hand in page["indicators"]:
                pos = hand["pos"]
                variableid = hand["variableId"]
                dtype = hand["type"]
                if dtype == "controller":
                    dast = HAND(self.store,variableid)
                    dast.setGeometry(int(self.scale * pos["l"])+80, int(self.scale * pos["t"])-35, 15, 20)
                    tempScene.addWidget(dast)
            self.scenes.append(tempScene)

    def SetActiveScene(self, SceneIndex: int):
        self.graphicsview.setScene(self.scenes[SceneIndex])
        # self.graphicsview.fitInView(self.scenes[SceneIndex].sceneRect(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        


    @pyqtSlot(int)
    def ChangePageByLink(self, dest):
        self.changePageSignal.emit(dest)
    
    def resizeEvent(self, a0):
        super().resizeEvent(a0)
        # self.graphicsview.fitInView(self.scenes[SceneIndex].sceneRect(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.graphicsview.fitInView(QtCore.QRectF(self.scaledImage.rect()), QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWidget()
    window.showMaximized()
    pages = json.loads(
        open(r"D:\\Petro\\New_OTS\\data\\data.json", "r").read())
    page = pages["layout"]["sections"]
    # # print(page)
    window.createAllscenes(page)
    window.SetActiveScene(0)
    # print(page)
    # window.drawPage(page)
    app.exec()