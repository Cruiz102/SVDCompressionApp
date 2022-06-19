# This Python file uses the following encoding: utf-8
import PySide6.QtWidgets as qw
import PySide6.QtCore as qc
import PySide6.QtGui as qg

class GraphWidget(qw.QWidget):
    def __init__(self):
        super().__init__()
        tabwidget = qw.QTabWidget()
        tabwidget.addTab(qw.QWidget(), "Plot1")
        tabwidget.addTab(qw.QWidget(), "Plot2")
        tabwidget.addTab(qw.QWidget(), "Plot3")
        tabwidget.addTab(qw.QWidget(), "Plot4")
        vbox = qw.QVBoxLayout()
        vbox.addWidget(tabwidget)
        self.setLayout(vbox)

# if __name__ == "__main__":
#     pass
