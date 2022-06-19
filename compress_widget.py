
import PySide6.QtWidgets as qw
import PySide6.QtCore as qc


class CompressWidget(qw.QWidget):
    FileName = qc.Signal(str)
    def __init__(self):
        super().__init__()

        Vertical = qw.QVBoxLayout()
        ChooseButton = qw.QPushButton(text="Choose Image")
        ChooseButton.clicked.connect(self.ChooseFile)
        self.NameLabel = qw.QLabel("Hola")
        Slider = qw.QSlider(qc.Qt.Horizontal)
        Compress = qw.QPushButton(text = "Compress")
        ExpandImages = qw.QPushButton(text = "Expand Images")
        SaveButtom = qw.QPushButton(text = "Save Images")
        Vertical.addWidget(ChooseButton)
        Vertical.addWidget(self.NameLabel,0)
        Vertical.addWidget(Slider)
        Vertical.addWidget(Compress)
        Vertical.addWidget(ExpandImages)
        Vertical.addWidget(SaveButtom)
        self.setLayout(Vertical)
        self.setMaximumWidth(200)
        self.setStyleSheet("background-color: rgb(153,153,153)")
        #Set SzePolicys
        self.NameLabel.setSizePolicy(qw.QSizePolicy(qw.QSizePolicy.Maximum,
                                                 qw.QSizePolicy.Maximum))

        



    def ChooseFile(self):
        result = qw.QFileDialog.getOpenFileName(
            caption = "Select Image",
            filter= "*png, *.jpg , *.jpeg" )
        self.FileName.emit(str(result[0]))
        self.NameLabel.setText(str(result[0]))
        return result[0]



# if __name__ == "__main__":
#     pass
