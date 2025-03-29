
from PyQt6.QtWidgets import QLabel, QLineEdit, QApplication, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap,QTransform,QMouseEvent
from PyQt6.QtCore import Qt,pyqtSignal,pyqtSlot
from PumpFacePlate import PumpFacePlate
import sys
import time
import os
import random

class DosingPump(QWidget):
        PumpChangingPos = pyqtSignal(str)
        updatevalues = pyqtSignal(dict,list)
        def __init__(self,rotated):
                super().__init__()
                self.setWindowTitle("p2")
                self.rotated = rotated
                
                self.resize(50, 40)
                self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
                self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
                self.faceplate = DosingPump
                
                current_path = os.getcwd()
                images = os.path.join(current_path, "images")
                self.equip_path = os.path.join(images, "equipment")
                
                self.faceplate = PumpFacePlate()
                self.faceplate.PumpChangingPos.connect(self.set_status)

                self.image = {}
                self.load_image()

                self.image_label = QLabel(self)
                self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
                layout = QVBoxLayout()
                layout.addWidget(self.image_label)
                self.setLayout(layout)

                self.RIGHT="right"
                self.LEFT="left"
                self.UP="up"
                self.DOWN="down"

                self.set_status("RUN")

                          


        def load_image(self):
                self.image = {
                    "p2gl": QPixmap(f"{self.equip_path}/p2gl.png"),
                    "p2rl": QPixmap(f"{self.equip_path}/p2rl.png")
                }
                if self.rotated == "up":
                    transform = QTransform().rotate(90)
                    self.image["p2gl"] = self.image["p2gl"].transformed(transform)
                    self.image["p2rl"] = self.image["p2rl"].transformed(transform)
                else:
                    self.image["p2gl"] = self.image["p2gl"]
                    self.image["p2rl"] = self.image["p2rl"]

                          
        @pyqtSlot(str)
        def set_status(self,status:str):
            match status:
                case "RUN":
                    self.image_label.setPixmap(self.image["p2gl"])
                case "STOP":
                    self.image_label.setPixmap(self.image["p2rl"])
                        
        def mousePressEvent(self, event: QMouseEvent):
            if event.button() == Qt.MouseButton.LeftButton:
                self.faceplate.show()
            return super().mousePressEvent(event)
        

if __name__ == '__main__':
        app = QApplication(sys.argv)
        
        window = DosingPump("left")
        # window.setStyleSheet("background-color: lightblue;")
        
        window.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # حذف فریم پنجره
        window.show()
        sys.exit(app.exec())
