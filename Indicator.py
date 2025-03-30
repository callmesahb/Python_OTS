import sys
from PyQt6 import QtWidgets,QtCore,QtGui
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtCore import Qt
from IndicatorValue import IndicatorValue
from ControllerPlate import ControllerPlate
from Sensor import Sensor

class Indicator(QtWidgets.QWidget):
    updatevalues = QtCore.pyqtSignal(dict,list)
    def __init__(self,name,value,itype,pvvalues,store,variableid):
        super().__init__()
        self.setStyleSheet("background-color:black")
        self.name = name
        self.value = value
        self.itype = itype
        self.pvvalues = pvvalues
        self.store = store
        self.variableid = variableid
        self.InitUI()
        
        
    def InitUI(self):
        self.hlayout = QtWidgets.QHBoxLayout()
        
        
        self.setMinimumHeight(5)
        
        self.settingValue()
    def settingValue(self):
        self.Value = QtWidgets.QLabel("245",self)
        self.Value.move(5,0)
        if self.itype == "":
            self.Value.setText(str(round(self.value,2)))
        if self.itype == "controller":
            self.Value.setText(str(round(self.pvvalues[1],2)))
        self.Value.setStyleSheet("color:#40d964; font-size:14px;")
        
    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.itype == "controller":
                self.contplate = ControllerPlate(self.name,self.pvvalues,self.variableid,self.store)
                self.contplate.show()
            if self.itype == "":
                self.sensor = Sensor(self.value,self.store,self.name,self.variableid)
                self.sensor.setWindowTitle(self.name)
                self.sensor.sensorname.setText(self.name)
                self.sensor.show()
    
    @QtCore.pyqtSlot(dict,list)
    def updatinvalue(self,data,tags):
        if self.itype == "":
            value = data[self.variableid]
            self.Value.setText(str(round(value,2)))
        if self.itype == "controller":
            value = data[self.variableid]
            print(f"{self.variableid}:{value}")

    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     brush = QBrush(QColor(0, 0, 0, 0))  # Fully transparent brush
    #     painter.setBrush(brush)
    #     painter.drawRect(self.rect())
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Indicator()
    window.show()
    sys.exit(app.exec())
