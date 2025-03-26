import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPainterPath, QColor
from PyQt6.QtCore import Qt

class CustomShapeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Shape")
        self.setGeometry(10,10,300,500)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

      
        # painter.fillRect(self.rect(), QColor(0, 0, 0)) 

        path = QPainterPath()
        path.moveTo(50, 50)
        path.lineTo(250, 50)
        path.lineTo(250, 150)
        path.lineTo(175, 150)
        path.lineTo(175, 280)
        path.lineTo(195 , 280)
        path.lineTo(230 , 250)
        path.lineTo(250, 250)
        path.lineTo(250, 420)
        path.lineTo(230, 420)
        path.lineTo(195, 390)
        path.lineTo(105, 390)
        path.lineTo(70 , 420)
        path.lineTo(50, 420)
       
        path.lineTo(50, 250)
        path.lineTo(70 , 250)
        path.lineTo(105,280)
        path.lineTo(125, 280)
        
        path.lineTo(125, 150)
        path.lineTo(50, 150)
        path.closeSubpath()

 
        painter.setBrush(QColor(0, 255, 0))  
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawPath(path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomShapeWidget()
    window.show()
    sys.exit(app.exec())
