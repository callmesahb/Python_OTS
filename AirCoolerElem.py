
from PyQt6.QtWidgets import QLabel, QLineEdit, QApplication, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap,QMouseEvent
from PyQt6.QtCore import Qt,pyqtSignal,pyqtSlot
from PumpFacePlate import PumpFacePlate
import sys
import os



class Aircooler(QWidget):
    PumpChangingPos = pyqtSignal(str)
    updatevalues = pyqtSignal(dict,list)
    def __init__(self,name):
        super().__init__()
        self.setWindowTitle("Aircooler")
        self.resize(50, 40)
        self.name = name
        current_path = os.getcwd()
        images = os.path.join(current_path, "images")
        self.equip_path = os.path.join(images, "equipment")

        self.image = {}
        self.load_image()

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.faceplate = PumpFacePlate()
        self.faceplate.PumpChangingPos.connect(self.set_status)
  
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

   
        self.set_status("RUN")  

    def load_image(self):
        self.image = {
            "Ag": QPixmap(os.path.join(self.equip_path,"AirCoolerg.png")),
            "Ar": QPixmap(os.path.join(self.equip_path,"AirCoolerr.png")),
        }

    @pyqtSlot(str)
    def set_status(self, status):
        if status == "RUN":
            self.image_label.setPixmap(self.image["Ag"])
        elif status == "STOP":
            self.image_label.setPixmap(self.image["Ar"])
            
    def mousePressEvent(self, event:QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.faceplate.setWindowTitle(self.name)
            self.faceplate.pname.setText(self.name)
            self.faceplate.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aircooler()
    window.show()
    sys.exit(app.exec())