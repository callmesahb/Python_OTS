
from PyQt6.QtWidgets import QLabel, QLineEdit, QApplication, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
import os



class Comprossor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Comprossor")
        self.resize(50, 40)
        current_path = os.getcwd()
        images = os.path.join(current_path, "images")
        self.equip_path = os.path.join(images, "equipment")

        self.image = {}
        self.load_image()

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

  
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

   
        self.set_status(1)  

    def load_image(self):
        self.image = {
            "Cg": QPixmap(os.path.join(self.equip_path,"comprossorg.png")),
            "Cr": QPixmap(os.path.join(self.equip_path,"comprossorr.png"))
        }

    def set_status(self, status):
        if status == 1:
            self.image_label.setPixmap(self.image["Cg"])
        elif status == 2:
            self.image_label.setPixmap(self.image["Cr"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Comprossor()
    window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    window.setWindowFlags(Qt.WindowType.FramelessWindowHint)  
    window.show()
    sys.exit(app.exec())