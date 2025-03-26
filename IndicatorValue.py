import sys
from PyQt6 import QtWidgets,QtCore
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtCore import Qt

class IndicatorValue(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:black")
        self.InitUI()
        
    def InitUI(self):
        self.hlayout = QtWidgets.QHBoxLayout()
        self.setLayout(self.hlayout)
        # self.setFixedSize(200,50)
        # self.setFixedHeight(50)
        
        self.settingValue()
    def settingValue(self):
        Value = QtWidgets.QLabel("245",self)
        unit = QtWidgets.QLabel("C",self)
        Value.setStyleSheet("color:green;")
        unit.setStyleSheet("color:green")
        self.hlayout.addWidget(Value,alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.hlayout.addWidget(unit,alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = IndicatorValue()
    window.show()
    sys.exit(app.exec())