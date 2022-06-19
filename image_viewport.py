# This Python file uses the following encoding: utf-8
import PySide6.QtWidgets as qw
import PySide6.QtCore as qc
import PySide6.QtGui as qg
from PIL.ImageQt import ImageQt

from svd_Image import SVDImage
class ImageViewport(qw.QWidget):
    def __init__(self):
        super().__init__()
        horizontal = qw.QHBoxLayout()
        OriginalPixmap = qg.QPixmap(r"C:\Users\cruiz\OneDrive\Escritorio\Footooos\Slide1.jpeg")

        self.OriginalImage = qw.QLabel()
        self.CompressedImage = qw.QLabel()
        self.OriginalImage.setPixmap(OriginalPixmap)
        self.CompressedImage.setPixmap(OriginalPixmap)

        
        horizontal.addWidget(self.OriginalImage)
        horizontal.addWidget(self.CompressedImage)
        self.setLayout(horizontal)

        self.OriginalImage.setMaximumHeight(500)
        self.OriginalImage.setMaximumWidth(500)
        self.CompressedImage.setMaximumHeight(500)
        self.CompressedImage.setMaximumWidth(500)        

    def loadOriginalImage(self, filename):
        self.OriginalImage.setPixmap( qg.QPixmap( r"{}".format(filename)).scaled(500,500, qc.Qt.KeepAspectRatio)    )
    def loadCompressedImage(self,filename ):
        svd = SVDImage(r"{}".format(filename))
        rankImage = svd.RankImageSVD(50)
        im = ImageQt(rankImage)
        self.CompressedImage.setPixmap(qg.QPixmap().fromImage(im).scaled(500,500, qc.Qt.KeepAspectRatio))





# if __name__ == "__main__":
#     pass
