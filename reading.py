# import json
# import os
# path = os.getcwd()
# print(path)
# orgpath = os.path.join(path,"Test")
# print(orgpath)
# data = json.loads(
#             open(os.path.join(orgpath, "data.json"), "r").read())
# tags = json.loads(
#             open(os.path.join(orgpath, "tags.json"), "r").read())

# # print(data["layout"]["sections"][0]["valves"])
# name = "403ARS0LI010TV"
# for i in range(0,len(tags)):
#     if name in tags[i]["name"]:
#         print(tags[i]["initial"])
# print(tags)


# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QProgressBar, QVBoxLayout, QWidget
# from PyQt6.QtGui import QColor, QPainter, QPen
# from PyQt6.QtCore import Qt

# class CustomProgressBar(QProgressBar):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setOrientation(Qt.Orientation.Vertical)  # Set the orientation to vertical

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.RenderHint.Antialiasing)
#         rect = self.rect()
        
#         # Draw the background
#         painter.setPen(QPen(Qt.PenStyle.NoPen))
#         painter.setBrush(QColor(255, 255, 255))
#         painter.drawRect(rect)
        
#         # Draw the filled part vertically
#         progress_height = int(rect.height() * self.value() / self.maximum())
#         painter.setBrush(QColor(0, 255, 0))
#         painter.drawRect(0, rect.height() - progress_height, rect.width(), progress_height)
        
#         # Draw the text
#         painter.setPen(QPen(QColor(0, 0, 0)))
#         painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, f"{self.value()}%")

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Custom Vertical Progress Bar Example")

#         # Create a CustomProgressBar
#         self.progress_bar = CustomProgressBar()
#         self.progress_bar.setRange(0, 100)
#         self.progress_bar.setValue(75)  # Set initial value to 75

#         # Create a layout and add the progress bar to it
#         layout = QVBoxLayout()
#         layout.addWidget(self.progress_bar)

#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())


# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QProgressBar, QVBoxLayout, QWidget
# from PyQt6.QtGui import QColor, QPainter, QPen, QPolygon
# from PyQt6.QtCore import Qt, QPoint

# class CustomProgressBar(QProgressBar):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setOrientation(Qt.Orientation.Vertical)  # Set the orientation to vertical

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.RenderHint.Antialiasing)
#         rect = self.rect()
        
#         # Draw the background
#         painter.setPen(QPen(Qt.PenStyle.NoPen))
#         painter.setBrush(QColor(255, 255, 255))
#         painter.drawRect(rect)
        
#         # Draw the filled part vertically
#         progress_height = int(rect.height() * self.value() / self.maximum())
#         painter.setBrush(QColor(0, 255, 0))
#         painter.drawRect(0, rect.height() - progress_height, rect.width(), progress_height)
        
#         # Draw the text
#         painter.setPen(QPen(QColor(0, 0, 0)))
#         painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, f"{self.value()}%")

#         # Draw the triangle pointer
#         triangle_height = rect.height() - progress_height
#         triangle = QPolygon([
#             QPoint(rect.width(), triangle_height - 5),
#             QPoint(rect.width() + 10, triangle_height),
#             QPoint(rect.width(), triangle_height + 5)
#         ])
#         painter.setBrush(QColor(255, 0, 0))
#         painter.drawPolygon(triangle)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Custom Vertical Progress Bar with Triangle Pointer")

#         # Create a CustomProgressBar
#         self.progress_bar = CustomProgressBar()
#         self.progress_bar.setRange(0, 100)
#         self.progress_bar.setValue(75)  # Set initial value to 75

#         # Create a layout and add the progress bar to it
#         layout = QVBoxLayout()
#         layout.addWidget(self.progress_bar)

#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())



# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QProgressBar, QVBoxLayout, QWidget
# from PyQt6.QtGui import QColor, QPainter, QPen, QPolygon
# from PyQt6.QtCore import Qt, QPoint

# class CustomProgressBar(QProgressBar):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setOrientation(Qt.Orientation.Vertical)  # Set the orientation to vertical

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.RenderHint.Antialiasing)
#         rect = self.rect()
        
#         # Draw the background
#         painter.setPen(QPen(Qt.PenStyle.NoPen))
#         painter.setBrush(QColor(255, 255, 255))
#         painter.drawRect(rect)
        
#         # Draw the filled part vertically
#         progress_height = int(rect.height() * self.value() / self.maximum())
#         painter.setBrush(QColor(0, 255, 0))
#         painter.drawRect(0, rect.height() - progress_height, rect.width(), progress_height)
        
#         # Draw the triangle pointer
#         triangle_height = rect.height() - progress_height
#         triangle = QPolygon([
#             QPoint(rect.width() + 5, triangle_height - 5),
#             QPoint(rect.width() + 15, triangle_height),
#             QPoint(rect.width() + 5, triangle_height + 5)
#         ])
#         painter.setBrush(QColor(255, 0, 0))
#         painter.drawPolygon(triangle)
        
#         # Draw the text
#         painter.setPen(QPen(QColor(0, 0, 0)))
#         text_rect = rect.adjusted(rect.width() + 20, 0, rect.width() + 50, 0)
#         painter.drawText(text_rect, Qt.AlignmentFlag.AlignVCenter, f"{self.value()}%")

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Custom Vertical Progress Bar with Triangle Pointer")

#         # Create a CustomProgressBar
#         self.progress_bar = CustomProgressBar()
#         self.progress_bar.setRange(0, 100)
#         self.progress_bar.setValue(75)  # Set initial value to 75

#         # Create a layout and add the progress bar to it
#         layout = QVBoxLayout()
#         layout.addWidget(self.progress_bar)

#         # Create a central widget and set the layout
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())


import pandas as pd
import os
from OpcClient import OpcClient as opc

current = os.getcwd()
newopcpath = os.path.join(current,"new opc")
tags = pd.read_csv(newopcpath+"\\tags.csv")
instance = opc("opc.tcp://DESKTOP-LEQCA9B:4841")
def ReadingFile():
    newtags = [[] for i in range(0,2)]
    for i in tags["tag"]:
        newtags[0].append(i)
        # print(i)
        newtags[1].append(instance.getValue(i))
    return newtags
instance.getValue("407EDTIMER")
# file = ReadingFile()
# print(file)


# from opcua import Client

# client = Client("opc.tcp://DESKTOP-LEQCA9B:4841")
# # namespaces = client.get_namespace_array()
# # print(namespaces)
# # node = client.get_node("ns=0;i=1")  # Example: Server Status
# # value = node.get_value()
# # print(f"Value: {value}")
# try:
#     client.connect()
#     node = client.get_node(f"ns=2;s=407EDTIMER").get_value()
#     print(node)
# finally:
#     client.disconnect()