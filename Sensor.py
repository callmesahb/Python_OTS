from PyQt6 import QtWidgets, QtGui, QtCore
from controllerbar import TriangleWidget
import sys

class Sensor(QtWidgets.QWidget):
    def __init__(self,value,store,name):
        super().__init__()
        self.setWindowTitle("")
        self.value = value
        self.name = name
        self.store = store
        self.details = self.store.SettingDetailsofsensor(name)
        self.unit = self.store.GettingUnit(name)
        print(self.unit)
        self._InitUI()
    def _InitUI(self):
        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.setContentsMargins(0,0,0,0)
        self.setLayout(self.vlayout)
        self.settingname()
        
    
    def settingname(self):
        self.sensorname = QtWidgets.QLabel("",self)
        self.vlayout.addWidget(self.sensorname)
        hline = QtWidgets.QFrame()
        hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        hline.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.vlayout.addWidget(hline)
        self.settingProgressbar()
        
    def settingProgressbar(self):
        hlayout = QtWidgets.QHBoxLayout()
        self.Unittag = QtWidgets.QLabel("barg",self)
        hlayout.addWidget(self.Unittag)
        self.Unittag.setText(self.unit)
        self.Progressbar = TriangleWidget()
        self.Progressbar.setminmaxvalue(self.details[0],self.details[1])
        self.Progressbar.progress.setValue(int(self.value))
        self.Progressbar.setRightValue(int(self.value))
        hlayout.addWidget(self.Progressbar)
        self.vlayout.addLayout(hlayout)
        hline = QtWidgets.QFrame()
        hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        hline.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.vlayout.addWidget(hline)
        self.SettingValue()
    
    def SettingValue(self):
        hlayout_op = QtWidgets.QHBoxLayout()
        self.PV = QtWidgets.QLabel("PV", self)
        self.PVValue = QtWidgets.QLabel("120", self)
        self.PVValue.setText(str(self.value))
        hlayout_op.addWidget(self.PV)
        hlayout_op.addWidget(self.PVValue)
        self.vlayout.addLayout(hlayout_op)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Sensor()
    window.show()
    sys.exit(app.exec())