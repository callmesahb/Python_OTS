from PyQt6 import QtWidgets,QtCore,QtGui
import os
from APIs import Aspen
import sys

class Toolbar(QtWidgets.QToolBar):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AppToolbar")
        current_dir = os.getcwd()
        self.icondir = os.path.join(current_dir,"icons")
        self.setMovable(False)
        self.Run = QtGui.QAction("Run",self)
        self.Pause = QtGui.QAction("Pause",self)
        self.Rewind = QtGui.QAction("Rewind",self)
        self.Run.setIcon(QtGui.QIcon(os.path.join(self.icondir,"play.jpg")))
        self.Pause.setIcon(QtGui.QIcon(os.path.join(self.icondir,"Pause.png")))
        self.Rewind.setIcon(QtGui.QIcon(os.path.join(self.icondir,"Rewind.png")))
        self.addAction(self.Run)
        self.addAction(self.Pause)
        self.addAction(self.Rewind)
        
        self.Run.triggered.connect(self.RunAPI)
        
    def RunAPI(self):
        self.aspen = Aspen()
        self.aspen.OpenSimulationFile()
        self.aspen.Visible()
        
        
        
def window():
    app = QtWidgets.QApplication(sys.argv)
    win = Toolbar()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    window()    