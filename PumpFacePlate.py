from PyQt6 import QtWidgets, QtGui, QtCore
import sys

class PumpFacePlate(QtWidgets.QWidget):
    PumpChangingPos = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pump")
        # self.setFixedSize(280,150)
        self.setFixedWidth(200)
        self._InitUI()
        self.settingdata()
    
    def _InitUI(self):
        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.setContentsMargins(0,0,0,0)
        self.setLayout(self.vlayout)
        
    def settingdata(self):
        self.pname = QtWidgets.QLabel("")
        self.vlayout.addWidget(self.pname)
        hline = QtWidgets.QFrame()
        hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        hline.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.vlayout.addWidget(hline)
        self.settingPV()

    def settingPV(self):
        self.radioGroupBox = QtWidgets.QGroupBox("PV                                                   OP", self)
        self.radioGroupBox.setStyleSheet("color:gray;")
        
        self.radioLayout = QtWidgets.QGridLayout()
        
        self.OPOPEN = QtWidgets.QCheckBox("", self)
        self.OPCLOSE = QtWidgets.QCheckBox("", self)
        self.Runradio = QtWidgets.QRadioButton("RUN", self)
        self.Runradio.setStyleSheet("color:black;")
        self.Runradio.setChecked(True)
        self.Stopradio = QtWidgets.QRadioButton("STOP", self)
        self.Stopradio.setStyleSheet("color:black;")
        
        self.radioLayout.addWidget(self.OPOPEN, 0, 1,QtCore.Qt.AlignmentFlag.AlignRight)
        self.radioLayout.addWidget(self.OPCLOSE, 1, 1,QtCore.Qt.AlignmentFlag.AlignRight)
        self.radioLayout.addWidget(self.Runradio, 0, 0)
        self.radioLayout.addWidget(self.Stopradio, 1, 0)

        self.radioGroupBox.setLayout(self.radioLayout)
        self.vlayout.addWidget(self.radioGroupBox)
        hline = QtWidgets.QFrame()
        hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        hline.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.vlayout.addWidget(hline)
        self.ChangingPos()
        
    def ChangingPos(self):
        vlayout = QtWidgets.QVBoxLayout()
        vvlayout = QtWidgets.QVBoxLayout()
        hlayout = QtWidgets.QHBoxLayout()
        radioLayout = QtWidgets.QGridLayout()
        remotelocal = QtWidgets.QRadioButton("LOCALMAN", self)
        pv = QtWidgets.QLabel("PV",self)
        pv.setStyleSheet("color:gray;")
        op = QtWidgets.QLabel("OP",self)
        op.setStyleSheet("color:gray;")
        
        self.pvvalue = QtWidgets.QLabel("",self)
        self.opvalue = QtWidgets.QComboBox(self)
        self.opvalue.addItems(["RUN", "STOP"])
        vlayout.addWidget(remotelocal)
        vlayout.addWidget(pv)
        vlayout.addWidget(op)
        vvlayout.addWidget(self.pvvalue)
        vvlayout.addWidget(self.opvalue)
        hlayout.addLayout(vlayout)
        hlayout.addLayout(vvlayout)
        self.vlayout.addLayout(hlayout)
        self.pvvalue.setText(self.opvalue.currentText())
        self.opvalue.currentTextChanged.connect(self.ChangingPosFunc)
        
    def ChangingPosFunc(self):
        # print()
        self.pvvalue.setText(self.opvalue.currentText())
        if self.opvalue.currentText() == "STOP":
            self.Stopradio.setChecked(True)
            self.OPCLOSE.setChecked(True)
            self.Runradio.setChecked(False)
            self.OPOPEN.setChecked(False)
            self.PumpChangingPos.emit("STOP")
        
        if self.opvalue.currentText() == "RUN":
            self.Stopradio.setChecked(False)
            self.OPCLOSE.setChecked(False)
            self.Runradio.setChecked(True)
            self.OPOPEN.setChecked(True)
            self.PumpChangingPos.emit("RUN")
        
        
        
if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        window = PumpFacePlate()
        window.show()
        sys.exit(app.exec())