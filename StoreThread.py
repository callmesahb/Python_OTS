from PyQt6 import QtCore

class StoreThread(QtCore.QThread):
    data_ready = QtCore.pyqtSignal(dict,list)
    
    def __init__(self,opc,csvfile,tag,parent = None):
        super().__init__(parent)
        self.opc = opc
        self.csvfile = csvfile
        self.tag = tag
        self.running = True
        
    def run(self):
        while self.running:
            newtags = {i: self.opc.getValue(i) for i in self.csvfile["tag"]}
            self.data_ready.emit(newtags,self.tag)
            QtCore.QThread.sleep(2)
        
    def stop(self):
        self.running = False