import PySide6.QtWidgets as qw
import PySide6.QtCore as qc
import PySide6.QtGui as qg
from image_viewport import ImageViewport
from graph_widget import GraphWidget


class CentralWidget(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(97,97,97)")
        image_viewport = ImageViewport()
        self.loadToLeftView = image_viewport.loadOriginalImage
        self.loadToRightView = image_viewport.loadCompressedImage
        Vertical = qw.QVBoxLayout()
        Vertical.addWidget(image_viewport)
        Vertical.addWidget(GraphWidget())
        self.setLayout(Vertical)

        #Slots
        self.loadToLeftView = image_viewport.loadOriginalImage
        self.loadToRightView = image_viewport.loadCompressedImage
        # Signals
        self.ImageSignal = image_viewport.ImageSignal

