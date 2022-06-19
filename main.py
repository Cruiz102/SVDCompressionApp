# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget
import PySide6.QtWidgets as qw
from central_widget import CentralWidget
from compress_widget import CompressWidget
from info_widget import InfoWidget



class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0,0,1920,1080)
        HorizontalLayout = qw.QHBoxLayout()
        compress_w = CompressWidget()
        central_w = CentralWidget()
        info_w = InfoWidget()
        HorizontalLayout.addWidget(compress_w)
        HorizontalLayout.addWidget(central_w)
        HorizontalLayout.addWidget(info_w)

        #Connect Signals to Slots
        compress_w.FileName.connect(central_w.loadToLeftView)
        compress_w.FileName.connect(central_w.loadToRightView)

        

        self.setLayout(HorizontalLayout)
        


if __name__ == "__main__":
    style = """

    QPushButton{
        font-size: 22px;
        background-color: rgb(182,168,168);

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
    window = Widget()
    window.setStyleSheet(style)
    window.showMaximized()
    sys.exit(app.exec())
