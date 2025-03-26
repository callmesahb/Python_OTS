
from PyQt6.QtWidgets import QLabel, QApplication, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets
import sys
import time
import random
import os
class Filter(QWidget):
    def __init__(self,name,value):
        super().__init__()
        self.setWindowTitle("filter")
        current_path = os.getcwd()
        images = os.path.join(current_path, "images")
        self.equip_path = os.path.join(images, "equipment")
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.name = name
        self.value = value

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(os.path.join(self.equip_path,"filter.png")))
        self.label.setScaledContents(True)
        
        self.checkBoxf = QtWidgets.QCheckBox(self)
        if value == 1:
            self.checkBoxf.setChecked(True)
        else:
            self.checkBoxf.setChecked(False)
        self.checkBoxf.stateChanged.connect(self.toggle_images)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.checkBoxf)
        self.setLayout(layout)
        
        
    def toggle_images(self ,state):
        if state==2:
            self.label.setPixmap(QPixmap(os.path.join(self.equip_path,"filter.png")))
        else :
            self.label.setPixmap(QPixmap(os.path.join(self.equip_path,"filter2.png")))
if __name__ == '__main__':
        app = QApplication(sys.argv)
        
        window = Filter()
        # window.setStyleSheet("background-color: lightblue;")
        window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground) 
        window.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # حذف فریم پنجره
        window.show()
        sys.exit(app.exec())

        

       