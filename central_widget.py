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

        # Graph Widget Coming Soon!
        #Vertical.addWidget(GraphWidget())
        self.setLayout(Vertical)
        self.setMaximumWidth(1000)

        #Slots
        self.loadToRightView = image_viewport.loadCompressedImage
        self.saveCompressImage = image_viewport.SaveCompressImage
        self.changeRankValue = image_viewport.changeRankValue
        self.changeFileName = image_viewport.changeFileName
        self.openImageWindow = image_viewport.openImageWindow
        # Signals
        self.singularValuesLength = image_viewport.SingularValuesLength

