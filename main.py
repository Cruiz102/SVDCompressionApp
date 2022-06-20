# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
import PySide6.QtWidgets as qw
from central_widget import CentralWidget
from compress_widget import CompressWidget
from info_widget import InfoWidget



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1920,1080)
        # Widgets
        HorizontalLayout = qw.QHBoxLayout()
        compress_w = CompressWidget()
        central_w = CentralWidget()
        info_w = InfoWidget()

        HorizontalLayout.addWidget(compress_w)
        HorizontalLayout.addWidget(central_w)
        HorizontalLayout.addWidget(info_w)

        #Connect Signals to Slots
            # compress_widget
        compress_w.FileName.connect(central_w.changeFileName)
        compress_w.Compress.clicked.connect(central_w.loadToRightView)
        compress_w.SaveButtom.clicked.connect(central_w.saveCompressImage)
        compress_w.Slider.valueChanged.connect(central_w.changeRankValue)
            #image_viewport
        central_w.singularValuesLength.connect(compress_w.changeMaximumValueSlider)


        

        self.setLayout(HorizontalLayout)
        


if __name__ == "__main__":
    style = """

    QPushButton{
        font-size: 22px;
        background-color: rgb(106, 174, 234);
        border-width: 5px solid black;
        border-radius: 50x;

    }
    InfoWidget{
        background-color: rgb(153,153,153);
    }
    ImageViewport{
        background-color: rgb(97,97,97);
    }
    CompressWidget{
        background-color: rgb(153,153,153)
    }
    
    """
    app = QApplication([])
    window = MainWindow()
    window.setStyleSheet(style)
    window.showMaximized()
    sys.exit(app.exec())
