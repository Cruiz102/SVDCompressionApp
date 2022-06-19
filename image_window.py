from PySide6.QtWidgets import QApplication, QWidget
import PySide6.QtWidgets as qw


class ShowImageWindow(qw.QWidget):
    def __init__(self):
        super().__init__()
        rank = 0
        horizontal = qw.QHBoxLayout()
        leftBox = qw.QGroupBox(title= "Original")
        rightBox = qw.QGroupBox(title= f"Compressed: rank {rank}")
        LeftImage = qw.QImage



        self.setLayout(horizontal)



        self.showMaximized()

    def getImages(self, Left, Right):
        pass
