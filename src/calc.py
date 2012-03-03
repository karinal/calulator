"""Caculator MAIN window"""
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
import mini

class calc(QMainWindow):
    """ Main"""
    def __init__(self):
        QMainWindow.__init__(self,None)
        ##Create menu
        self.modeMinimalAct = QAction("&Minimal", self,
                               shortcut=QKeySequence(Qt.CTRL + Qt.Key_1),
                               statusTip="Minimal calculator", 
                               triggered=self.minimalMode)
        self.aboutCreditAct = QAction("&Credit", self,
                                  shortcut=QKeySequence(Qt.CTRL + Qt.Key_C),
                                  statusTip="Credits ", triggered=self.credit)
        self.modeMenu = self.menuBar().addMenu("&Mode")
        self.modeMenu.addAction(self.modeMinimalAct)
        self.modeMenu = self.menuBar().addMenu("&About")
        self.modeMenu.addAction(self.aboutCreditAct)
        

    def setCaluclator(self,calculator):
        self.setCentralWidget(calculator)
        self.adjustSize()

    def  minimalMode(self):
        #ToDo here modes
        w=self.centralWidget()
        self.setCaluclator(mini.mini(self))
        w.deleteLater()
    
        
    def credit(self):
        self.adjustSize()
        msgBox = QMessageBox()
        msgBox.setText("Copyrights Kari Nalli \n" \
                       "This SW is licensed under GPLv3 or "\
                        "later version of GPL")
        msgBox.exec_()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main=calc()
    calculator = mini.mini(main)
    main.setCaluclator(calculator)
    main.show()
    sys.exit(app.exec_())
