
from PyQt6.QtWidgets import QLabel, QLineEdit, QApplication, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap,QMouseEvent
from PyQt6.QtCore import Qt,pyqtSignal,pyqtSlot
from PumpFacePlate import PumpFacePlate
import sys
import os
import time
import random

class NormalPump(QWidget):
        PumpChangingPos = pyqtSignal(str)
        def __init__(self,name,value):
            super().__init__()
            self.name = name
            self.value = value
            self.setWindowTitle(name)
            
            self.resize(50, 40)
            current_path = os.getcwd()
            self.faceplate = PumpFacePlate()
            self.faceplate.PumpChangingPos.connect(self.set_status)
            images = os.path.join(current_path, "images")
            self.equip_path = os.path.join(images, "equipment")
            
            self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

            self.image = {}
            self.load_image()

            self.image_label = QLabel(self)
            self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    
            layout = QVBoxLayout()
            layout.addWidget(self.image_label)
            self.setLayout(layout)

            self.RIGHT="right"
            self.LEFT="left"

            self.set_status("RUN")
                          


        def load_image(self):
                self.image = {
                    "p1g": QPixmap(os.path.join(self.equip_path,"p1.png")),
                    "p1r": QPixmap(os.path.join(self.equip_path,"p1r.png"))
                }

                          
        @pyqtSlot(str)
        def set_status(self,status):
                match status:
                    case "RUN":
                        self.image_label.setPixmap(self.image["p1g"])
                    case "STOP":
                        self.image_label.setPixmap(self.image["p1r"])
        def mousePressEvent(self, event:QMouseEvent):
            if event.button() == Qt.MouseButton.LeftButton:
                self.faceplate.setWindowTitle(self.name)
                self.faceplate.pname.setText(self.name)
                self.faceplate.show()
        

if __name__ == '__main__':
        app = QApplication(sys.argv)
        
        window = NormalPump()
        # window.setStyleSheet("background-color: lightblue;")
        window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # پس‌زمینه کاملاً شفاف
        window.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # حذف فریم پنجره
        window.show()
        sys.exit(app.exec())
