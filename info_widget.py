# This Python file uses the following encoding: utf-8
import PySide6.QtWidgets as qw
import PySide6.QtCore as qc

class InfoWidget(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(153,153,153)")

        qertical = qw.QVBoxLayout()
        label1 = qw.QLabel("Esto es el Widget de la Info aqui esta la info de las imagenes")
        label2 = qw.QLabel("d")
        label3 = qw.QLabel("qw")
        qertical.addWidget(label1)
        qertical.addWidget(label2)
        qertical.addWidget(label3)
        qertical.addWidget(qw.QLabel("as"))
        self.setLayout(qertical)
        self.setMaximumWidth(300)





# if __name__ == "__main__":
#     pass
