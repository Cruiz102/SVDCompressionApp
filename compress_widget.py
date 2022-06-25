
import PySide6.QtWidgets as qw
import PySide6.QtCore as qc



class CompressWidget(qw.QWidget):
    FileName = qc.Signal(str)
    def __init__(self):
        super().__init__()
        self.rankvalue = 200

        Vertical = qw.QVBoxLayout()
        ChooseButton = qw.QPushButton(text="Choose Image")
        self.NameLabel = qw.QLabel("Hola")
        self.RankLabel = qw.QLabel(f"<h2><center>{self.rankvalue}<center></h2>")
        self.Slider = qw.QSlider(qc.Qt.Horizontal)
        self.Compress = qw.QPushButton(text = "Compress")
        self.ExpandImages = qw.QPushButton(text = "Expand Images")
        self.SaveButtom = qw.QPushButton(text = "Save Images")
        Vertical.addWidget(ChooseButton)
        Vertical.addWidget(self.NameLabel)
        Vertical.addWidget(self.RankLabel)
        Vertical.addWidget(self.Slider)
        Vertical.addWidget(self.Compress)
        Vertical.addWidget(self.ExpandImages)
        Vertical.addWidget(self.SaveButtom)
        self.setLayout(Vertical)
        self.setMaximumWidth(200)
        #Set SizePolicys
        self.NameLabel.setSizePolicy(qw.QSizePolicy(qw.QSizePolicy.Maximum,
                                                 qw.QSizePolicy.Maximum))

        # Connects Buttons
     #   SaveButtom.connect(self.SaveCompressImage)
        ChooseButton.clicked.connect(self.ChooseFile)
        self.Slider.valueChanged.connect(self.changerankValue)

    # Change Style of Widgets

    
    def ChooseFile(self):
        result = qw.QFileDialog.getOpenFileName(
            caption = "Select Image",
            filter= "*png *.jpg  *.jpeg" )
        self.FileName.emit(str(result[0]))
        self.NameLabel.setText(str(result[0]))
        print(result)
        return result[0]

    def changeMaximumValueSlider(self, singularValues):
        self.Slider.setMaximum(singularValues)

    def changerankValue(self, value):
        self.rankvalue = value
        self.RankLabel.setText(f"<h2><center>{self.rankvalue}<center><h2>")


             



# if __name__ == "__main__":
#     pass
