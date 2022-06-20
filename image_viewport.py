# This Python file uses the following encoding: utf-8
import PySide6.QtWidgets as qw
import PySide6.QtCore as qc
import PySide6.QtGui as qg
from PIL.ImageQt import ImageQt
from svd_Image import SVDImage


class ImageViewport(qw.QWidget):
    ImageSignal = qc.Signal(tuple)
    SingularValuesLength = qc.Signal(int)
    def __init__(self):
        super().__init__()
        self.rankValue = 0
        self.filename = r"C:\Users\cruiz\OneDrive\Escritorio\Footooos\Slide1.jpeg"
        self.svd_data = SVDImage(r"{}".format(self.filename))
        horizontal = qw.QHBoxLayout()
        self.leftGroup = qw.QGroupBox(title= "Original")
        self.rightGroup = qw.QGroupBox(title = f"Compressed rank: {self.rankValue}")
        group1 = qw.QHBoxLayout()
        group2 = qw.QHBoxLayout()
        OriginalPixmap = qg.QPixmap(self.filename)

        self.OriginalImage = qw.QLabel()
        self.CompressedImage = qw.QLabel()
        self.OriginalImage.setPixmap(OriginalPixmap)
        self.CompressedImage.setPixmap(OriginalPixmap)

        self.leftGroup.setMaximumSize(550,550)
        self.rightGroup.setMaximumSize(550,550)
        self.leftGroup.setSizePolicy(qw.QSizePolicy(qw.QSizePolicy.Maximum,
                                                 qw.QSizePolicy.Maximum))
        self.rightGroup.setSizePolicy(qw.QSizePolicy(qw.QSizePolicy.Maximum,
                                                 qw.QSizePolicy.Maximum))


        group1.addWidget(self.OriginalImage) 
        group2.addWidget(self.CompressedImage)  
        self.leftGroup.setLayout(group1)
        self.rightGroup.setLayout(group2)

        horizontal.addWidget(self.leftGroup)
        horizontal.addWidget(self.rightGroup)
        self.setLayout(horizontal)

    def changeRankValue(self,value):
        self.rankValue = value  
    def changeFileName(self, filename):
        self.filename = filename
        self.loadOriginalImage()

    def loadOriginalImage(self):
        self.svd_data  = SVDImage(r"{}".format(self.filename))
        self.OriginalImage.setPixmap( qg.QPixmap( r"{}".format(self.filename)).scaled(550,550, qc.Qt.KeepAspectRatio))
        self.SingularValuesLength.emit(self.svd_data.singularValuesLength)
        

    def loadCompressedImage(self ):
        self.rankImage = self.svd_data.RankImageSVD(self.rankValue)
        image_qt = ImageQt(self.rankImage)
        self.CompressedImage.setPixmap(qg.QPixmap().fromImage(image_qt).scaled(550,550, qc.Qt.KeepAspectRatio))
        self.rightGroup.setTitle( f"Compressed rank: {self.rankValue}")
        # Emit Compress Image
        
    def SaveCompressImage(self):
        saveImage = qw.QFileDialog.getSaveFileName(
                    self,
                    filter=  "*png *.jpg *.jpeg" ) 
        self.rankImage.save(saveImage[0])






# if __name__ == "__main__":
#     pass
