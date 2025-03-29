
from PyQt6.QtWidgets import QLabel, QLineEdit, QApplication, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap,QTransform,QMouseEvent
from PyQt6.QtCore import Qt,pyqtSignal,pyqtSlot
from ControllerPlate import ControllerPlate
import sys
import os
import numpy as np

class ControllerValve(QWidget):
        ChangePosValve = pyqtSignal(float)
        updatevalues = pyqtSignal(dict,list)
        def __init__(self,name,rotated,pvvalues,variableid,store):
                super().__init__()
                self.setWindowTitle("controllerValve")
                self.resize(50, 40)
                self.rotated = rotated
                self.name = name
                self.pvvalues = pvvalues
                self.variableid = variableid
                current_path = os.getcwd()
                images = os.path.join(current_path, "images")
                self.equip_path = os.path.join(images, "equipment")
                self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
                self.image = {}
                self.faceplate = ControllerPlate(name,pvvalues,variableid,store)
                self.load_image()

                self.image_label = QLabel(self)
                self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.faceplate.ChangePosValve.connect(self.set_status)
                layout = QVBoxLayout()
                layout.addWidget(self.image_label)
                self.setLayout(layout)
                self.load_image()
                store.updatevalues.connect(self.settingValueController)
                # repeat_count=10 
                # for i in range(repeat_count):
                #     random_number=random.choice([1,2])
                #     print(f"{random_number}")


                # self.set_status(5)
                
                
                
        def load_image(self):
            self.image = {
                "Controller_r": QPixmap(f"{self.equip_path}/cont2r.png"),
                "Controller_g": QPixmap(f"{self.equip_path}/contg2.png")
            }
            if self.rotated == "left":
                transform = QTransform().rotate(-90)
                self.image["Controller_g"] = self.image["Controller_g"].transformed(transform)
                self.image["Controller_r"] = self.image["Controller_r"].transformed(transform)
            if self.rotated == "right":
                transform = QTransform().rotate(90)
                self.image["Controller_g"] = self.image["Controller_g"].transformed(transform)
                self.image["Controller_r"] = self.image["Controller_r"].transformed(transform)
        
        @pyqtSlot(float)
        def set_status(self, status):
            match status:
                case x if 0 <= x < 1:
                    self.image_label.setPixmap(self.image["Controller_r"])
                case x if 1 <= x < 100:
                    self.image_label.setPixmap(self.image["Controller_g"])
                case _:
                    pass
                
        @pyqtSlot(dict,list)
        def settingValueController(self,data,tags):
            value = data[self.variableid]
            self.set_status(value)
            # print(value)
                    
        def mousePressEvent(self, event: QMouseEvent):
            if event.button() == Qt.MouseButton.LeftButton:
                self.faceplate.show()
            return super().mousePressEvent(event)

                        
         

             
if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = ControllerValve("0LIC","left")
        window.show()
        sys.exit(app.exec())