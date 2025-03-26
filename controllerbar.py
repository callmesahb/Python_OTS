import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout,QProgressBar,QLabel
from PyQt6.QtGui import QPainter, QPolygon, QColor,QPalette
from PyQt6.QtCore import QTimer, QPoint,Qt
import random
class TriangleWidget(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        
        self.direction = 1
        self.y_offset = 0
        self.leftvalue=50
        self.rightValue=50
        self.centerValue=50
        self.progress = QProgressBar(self)
        self.progress.setTextVisible(False)  # Hide the text displaying the value
        # self.set_chunk_width(self.progress, 15)  # Set chunk width
        self.progress.setOrientation(Qt.Orientation.Vertical)
        self.progress.show()
        # Set the chunk color to green
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Highlight, QColor(0, 255, 0))
        self.progress.setPalette(palette)
        self.progress.setGeometry(20, 15,20, 200)
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid grey;
                background-color: black;
                border-radius: 5px;
            }
            QProgressBar::chunk {
                background-color: rgb(0,255,1);
               
            }
        """)
        self.initUI()
        # self.timer = QTimer(self)
        # self.timer.timeout.connect(self.update_position)
        # self.timer.start(100)

    def initUI(self):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setGeometry(100, 100, 110, 220)
        self.setFixedSize(110,220)
        self.setWindowTitle('Moving Triangle')
        self.label1=QLabel(parent=self)
        self.label1.setGeometry(60,0,50,20)
        self.label1.setText("_1400000")
        self.label2=QLabel(parent=self)
        self.label2.setGeometry(60,49,50,20)
        self.label2.setText("_1400000")
       
        self.label3=QLabel(parent=self)
        self.label3.setGeometry(60,98,50,20)
        self.label3.setText("_1400000")
        self.label4=QLabel(parent=self)
        self.label4.setGeometry(60,147,50,20)
        self.label4.setText("_1400000")
        self.label5=QLabel(parent=self)
        self.label5.setGeometry(60,196,50,20)
        self.label5.setText("_1400000")
        self.show()
    def update_position(self):
        self.setLeftValue(random.randint(0,100))
        self.setRightValue(-10)#random.randint(0,100))
        self.setCentervalue(random.randint(0,100))
        # self.update()    #Mohem nist
    
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_triangleR(qp)
        # self.draw_triangleL(qp)
        qp.end()

    def draw_triangleR(self, qp):
      
        y= int(self.progress.geometry().y())-50+ int(self.progress.height()) - int(self.rightValue /100 *self.progress.height())
        qp.setBrush(QColor(255, 0, 0))
        points = [
            QPoint(40, 50 + y),
            QPoint(53, 42 + y),
            QPoint(53, 57+ y)
        ]
        triangle = QPolygon(points)
        qp.drawPolygon(triangle)
    def draw_triangleL(self, qp):
        y= int(self.progress.geometry().y())-50+ int(self.progress.height()) - int(self.leftvalue /100 *self.progress.height())
        qp.setBrush(QColor(255, 255, 0))
        points = [
            QPoint(20, 50 + y),
            QPoint(7, 42 + y),
            QPoint(7, 57+ y)
        ]
        triangle = QPolygon(points)
        qp.drawPolygon(triangle)    

    def set_chunk_width(self, progress_bar, width):
        progress_bar.setStyleSheet(f"""
            QProgressBar::chunk {{
                width: {width}px;
            }}
        """)
    def setLeftValue (self,percent):
        if percent<0 :percent=0
        if percent>100: percent=100
        self.rightValue=percent
        self.update()
    def setRightValue (self,percent):
        if percent<0 :percent=0
        if percent>100: percent=100
        self.rightValue=percent
        self.update()
    def setCentervalue (self,percent):
        self.progress.setValue(int(percent))
        self.update()
    def setminmaxvalue(self,min,max):
        firstdiv=round(min,self.count_decimal_places(max))
        seconddiv=round(min+  (max-min)/4,self.count_decimal_places(max))
        thirddiv=round(min+  (max-min)/4*2,self.count_decimal_places(max))
        forthdiv=round(min+  (max-min)/4*3,self.count_decimal_places(max))
        fifthdiv=round(min+  (max-min)/4*4,self.count_decimal_places(max))
        self.label5.setText(str(firstdiv))
        self.label4.setText(str(seconddiv))
        self.label3.setText(str(thirddiv))
        self.label2.setText(str(forthdiv))
        self.label1.setText(str(fifthdiv))
    def count_decimal_places(self,number):
        number_str = str(number)
        if '.' in number_str:
            decimal_places = len(number_str.split('.')[1])
        else:
            decimal_places = 0
        if '.' in number_str:
            decimal = len(number_str.split('.')[0])
        else:
            decimal = len(number_str)
        decimal_places=decimal_places-decimal
        if decimal_places<0:  decimal_places=0   
        
        return decimal_places
def main():
    app = QApplication(sys.argv)
    ex = TriangleWidget()
    # ex.progress.setGeometry(20,15,20,200)
    # ex.progress.setValue(30)
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()