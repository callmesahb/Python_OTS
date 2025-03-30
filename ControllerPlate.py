from PyQt6 import QtWidgets, QtGui, QtCore
from controllerbar import TriangleWidget
from Store import Store
import sys


class ControllerPlate(QtWidgets.QWidget):
    ChangePosValve = QtCore.pyqtSignal(float)
    changeHandtype = QtCore.pyqtSignal(str)
    updatevalues = QtCore.pyqtSignal(dict,list)
    def __init__(self,name:str,pvvalue:list,variableid,store:Store):
        super().__init__()
        # self.setFixedSize(250,400)
        self.name = name
        self.pvvalues = pvvalue
        self.variableid = variableid
        self.store = store
        self.store.updatevalues.connect(self.upandsettingvaluesofcontroller)
        self.setWindowTitle("Controller")
        self._initUI()
    def _initUI(self):
        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.setContentsMargins(0,0,0,0)
        self.setLayout(self.vlayout)
        self.namee = QtWidgets.QLabel("403ARS0PIC001",self)
        hline = QtWidgets.QFrame()
        self.vlayout.addWidget(self.namee)
        hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        hline.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.vlayout.addWidget(hline)
        self.settingProgressbar()
    def settingProgressbar(self):
        hlayout = QtWidgets.QHBoxLayout()
        self.Unittag = QtWidgets.QLabel("%",self)
        hlayout.addWidget(self.Unittag)
        self.Progressbar = TriangleWidget()
        self.Progressbar.setminmaxvalue(0,100)
        hlayout.addWidget(self.Progressbar)
        self.vlayout.addLayout(hlayout)
        hline = QtWidgets.QFrame()
        hline.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        hline.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.vlayout.addWidget(hline)
        self.SettingPlaceVariables(cas= 0)
        
    def SettingPlaceVariables(self,cas):
        hlayout_sp = QtWidgets.QHBoxLayout()
        self.SP = QtWidgets.QLabel("SP", self)
        self.SPValue = QtWidgets.QLineEdit("", self)
        hlayout_sp.addWidget(self.SP)
        hlayout_sp.addWidget(self.SPValue)


        hlayout_pv = QtWidgets.QHBoxLayout()
        self.PV = QtWidgets.QLabel("PV", self)
        self.PVValue = QtWidgets.QLineEdit("", self)
        self.PVValue.setReadOnly(True)
        hlayout_pv.addWidget(self.PV)
        hlayout_pv.addWidget(self.PVValue)


        hlayout_op = QtWidgets.QHBoxLayout()
        self.OP = QtWidgets.QLabel("OP(%)", self)
        self.OPValue = QtWidgets.QLineEdit("", self)
        hlayout_op.addWidget(self.OP)
        hlayout_op.addWidget(self.OPValue)

        if cas == 1:
            hlayout_md = QtWidgets.QHBoxLayout()
            self.MD = QtWidgets.QLabel("MD", self)
            self.MDComboBox = QtWidgets.QComboBox(self)
            self.MDComboBox.addItems(["CAS", "NORMAL", "AUTO"])
            hlayout_md.addWidget(self.MD)
            hlayout_md.addWidget(self.MDComboBox)
        if cas == 0:
            hlayout_md = QtWidgets.QHBoxLayout()
            self.MD = QtWidgets.QLabel("MD", self)
            self.MDComboBox = QtWidgets.QComboBox(self)
            self.MDComboBox.addItems(["NORMAL", "AUTO"])
            hlayout_md.addWidget(self.MD)
            hlayout_md.addWidget(self.MDComboBox)
        
        hlayout_md.addWidget(self.MD)
        # hlayout_md.addWidget(self.MDattr)
        
        self.Accept = QtWidgets.QPushButton("APPLY",self)
        self.Accept.clicked.connect(self.UpdateOP)


        self.vlayout.addLayout(hlayout_sp)
        self.vlayout.addLayout(hlayout_pv)
        self.vlayout.addLayout(hlayout_op)
        self.vlayout.addLayout(hlayout_md)
        self.vlayout.addWidget(self.Accept)
        
        self.setWindowTitle(self.name)
        self.ChangePosValve.emit(self.pvvalues[2])
        
    def UpdateOP(self):
        # Updating pvvalues[2] to the value in OPValue
        new_op_value = float(self.OPValue.text()) if self.OPValue.text() else self.pvvalues[2]
        self.ChangePosValve.emit(new_op_value)
    def ChangingHandType(self):
        new_type = self.MD.text()
        self.changeHandtype.emit(new_type)
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Enter or event.key() == QtCore.Qt.Key.Key_Return:
            self.UpdateOP()
            
    @QtCore.pyqtSlot(dict,list)
    def upandsettingvaluesofcontroller(self,data,tags):
        Varid = self.variableid.replace("OP","")
        sp = Varid + "SP"
        pv = Varid + "PV"
        op = Varid + "OP"
        tv = Varid + "TV"
        spvalue = data[sp]
        pvvalue = data[pv]
        opvalue = data[op]
        tvvalue = data[tv]
        # print(f"{Varid}:{tvvalue}")
        if tvvalue == 0.0:
            self.OPValue.setReadOnly(True)
            self.PVValue.setReadOnly(True)
        else:
            self.OPValue.setReadOnly(False)
            self.PVValue.setReadOnly(False)
        self.SPValue.setText(str(round(spvalue,2)))
        self.PVValue.setText(str(round(pvvalue,2)))
        self.OPValue.setText(str(round(opvalue,2)))
        
        self.Progressbar.progress.setValue(int(pvvalue))
        self.Progressbar.setRightValue(int(pvvalue))
        