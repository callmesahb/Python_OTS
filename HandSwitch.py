from PyQt6 import QtWidgets,QtCore
import sys

class HandSwitch(QtWidgets.QWidget):
    def __init__(self,name,btns):
        super().__init__()
        self.setWindowTitle("HandSwitch")
        self.name = name
        self.btns = btns
        self._InitUI()
        self.settingdata()
        
    def _InitUI(self):
        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.setContentsMargins(0,0,0,0)
        self.setLayout(self.vlayout)
        
    def settingdata(self):
        self.hname = QtWidgets.QLabel("403ARSP001A")
        self.vlayout.addWidget(self.hname)
        self.hname.setText(self.name)
        hline = QtWidgets.QFrame()
        hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        hline.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.vlayout.addWidget(hline)
        self.settingPV()
    
    def settingPV(self):
        self.radioGroupBox = QtWidgets.QGroupBox("PV                                                                 OP", self)
        self.radioGroupBox.setStyleSheet("color:gray;")
        
        self.radioLayout = QtWidgets.QGridLayout()
        
        self.OPOPEN = QtWidgets.QCheckBox("", self)
        # self.OPOPEN.setChecked(True)
        self.OPCLOSE = QtWidgets.QCheckBox("", self)
        self.Runradio = QtWidgets.QRadioButton(self.btns[0], self)
        self.Runradio.setStyleSheet("color:black;")
        self.Stopradio = QtWidgets.QRadioButton(self.btns[1], self)
        self.Runradio.setChecked(True)
        self.OPOPEN.setChecked(True)
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
        self.Switch()
    def Switch(self):
        vlayout = QtWidgets.QVBoxLayout()
        vvlayout = QtWidgets.QVBoxLayout()
        hlayout = QtWidgets.QHBoxLayout()
        self.remotelocal = QtWidgets.QRadioButton("LOCALMAN", self)
        pv = QtWidgets.QLabel("PV",self)
        pv.setStyleSheet("color:gray;")
        op = QtWidgets.QLabel("OP",self)
        op.setStyleSheet("color:gray;")
        self.pvvalue = QtWidgets.QLabel("",self)
        self.opvalue = QtWidgets.QComboBox(self)
        self.opvalue.addItems(["", ""])
        vlayout.addWidget(self.remotelocal)
        vlayout.addWidget(pv)
        vlayout.addWidget(op)
        # print(self.btns[0])
        self.opvalue.setItemText(0,self.btns[0])
        self.opvalue.setItemText(1,self.btns[1])
        vvlayout.addWidget(self.pvvalue)
        vvlayout.addWidget(self.opvalue)
        hlayout.addLayout(vlayout)
        hlayout.addLayout(vvlayout)
        self.vlayout.addLayout(hlayout)
        self.pvvalue.setText(self.opvalue.currentText())
        self.opvalue.setDisabled(True)
        self.opvalue.currentTextChanged.connect(self.SwitchStruct)
        self.remotelocal.toggled.connect(self.DisableWidget)
        
    def SwitchStruct(self):
        self.pvvalue.setText(self.opvalue.currentText())
        if self.opvalue.currentText() == self.opvalue.itemText(1):
            self.Stopradio.setChecked(True)
            self.OPCLOSE.setChecked(True)
            self.Runradio.setChecked(False)
            self.OPOPEN.setChecked(False)
            # self.PumpChangingPos.emit("STOP")
        
        if self.opvalue.currentText() == self.opvalue.itemText(0):
            self.Stopradio.setChecked(False)
            self.OPCLOSE.setChecked(False)
            self.Runradio.setChecked(True)
            self.OPOPEN.setChecked(True)
            # self.PumpChangingPos.emit("RUN")
    def CheckingStatusRemLoc(self) -> bool:
        return self.remotelocal.isChecked()
    
    def DisableWidget(self):
        self.status = self.CheckingStatusRemLoc()
        if self.status:
            self.opvalue.setDisabled(False)
        else:
            self.opvalue.setDisabled(True)
        self.update()
    
if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        window = HandSwitch()
        window.show()
        sys.exit(app.exec())