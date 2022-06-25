# This Python file uses the following encoding: utf-8
import PySide6.QtWidgets as qw
import PySide6.QtCore as qc
import os

from numpy import compress

class InfoWidget(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: rgb(153,153,153)")
        rank = 0
        originalSizeFile = 10
        compressSizeFile = 5
        currentGraphImformation = ""
        qertical = qw.QVBoxLayout()
        label1 = qw.QLabel(f"""<h1>Rank of the Image:{rank}<h1>\n
                                <h2>Original photo size file: {originalSizeFile}<h2>\n
                                 Compressed size file: {compressSizeFile}<h2>\n
                                <Compressed Percentage:{(originalSizeFile/compressSizeFile)*100}%<h2> 


                                                                """)
        label2 = qw.QLabel(f"""
                            <h1> Graph Information<h1>
                                    
                                     """)
        label3 = qw.QLabel("qw")
        qertical.addWidget(label1)
        qertical.addWidget(label2)
        qertical.addWidget(label3)
        qertical.addWidget(qw.QLabel("as"))
        self.setLayout(qertical)
        self.setMaximumWidth(300)
    def getSizeFile(self, file_1, file_2):
        os.path.getsize(r"{}".format(file_1))
        os.path.getsize(r"{}".format(file_2))





# if __name__ == "__main__":
#     pass
