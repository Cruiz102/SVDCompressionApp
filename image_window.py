import PySide6.QtWidgets as qw


class ShowImageWindow(qw.QWidget):
    def __init__(self) :
        super().__init__()
        self.imageLabel1 = qw.QLabel()
        




    def getImages(self, Left):
        self.imageLabel1 = Left[0]
        horizontal = qw.QHBoxLayout()
        horizontal.addWidget(self.imageLabel1)
        horizontal.addWidget(self.imageLabel1)
        self.setLayout(horizontal)
        print(Left[0])
