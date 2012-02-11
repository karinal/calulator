# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import calc

class mini (calc):
    """Minimalistic calculator 4x4"""
    def __init__(self):
    def loadUI(self):
        loader = QUiLoader()
        file = QFile("../ui/minimal.ui")
        file.open(QFile.ReadOnly)
        myWidget = loader.load(file, self)
        file.close()
        



if __name__ == "__main__":
    calc=mini()
