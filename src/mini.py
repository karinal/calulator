# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *

class operation:
    notset=0
    plus=1
    minus=2
    divide=3
    multibly=4

class mini (QWidget):
    """Minimalistic calculator 4x4"""
    def __init__(self,parent=None):
        self.op=operation.notset
        self.result=0
        self.operant1=0
        self.operant2=0
        self.out=None
        QWidget.__init__(self, parent)
        loader = QUiLoader()
        file = QFile("../ui/minimal.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()
        #connect to output
        self.out=self.ui.findChild(QObject,"lcdNumber")
        self.out.setDigitCount(10)
        QMetaObject.connectSlotsByName(self)
    def sizeHint(self):
        g=self.ui.geometry()
        return g.size()

    def operant(self,i):
        if self.op==operation.notset:
            self.operant1=self.operant1*10+int(i)
            self.display(self.operant1)
        else:
            self.operant2=self.operant2*10+int(i)
            self.display(self.operant2)
    def display(self,d):
        try:
            self.out.display(d)
        except OverflowError:
            self.op=operation.notset
            self.result=0
            self.operant1=0
            self.operant2=0
            self.out.display("OverFlow")
    @Slot()
    def on_number_0_clicked(self):
        self.operant(0)
    @Slot()
    def on_number_1_clicked(self):
        self.operant(1)
    @Slot()
    def on_number_2_clicked(self):
        self.operant(2)
    @Slot()
    def on_number_3_clicked(self):
        self.operant(3)
    @Slot()
    def on_number_4_clicked(self):
        self.operant(4)
    @Slot()
    def on_number_5_clicked(self):
        self.operant(5)
    @Slot()
    def on_number_6_clicked(self):
        self.operant(6)
    @Slot()
    def on_number_7_clicked(self):
        self.operant(7)
    @Slot()
    def on_number_8_clicked(self):
        self.operant(8)
    @Slot()
    def on_number_9_clicked(self):
        self.operant(9)
    @Slot()
    def on_Clear_clicked(self):
        if self.op==operation.notset:
            self.operant1=0
            self.display(self.operant1)
        else:
            self.operant2=0
            self.display(self.operant2)
    @Slot()
    def on_Clearall_clicked(self):
        self.op=operation.notset
        self.operant1=0
        self.operant2=0
        self.result=0
        self.display(0)
    @Slot()
    def on_divide_clicked(self):
        if self.operant1==0:
            return
        self.op=operation.divide 
        self.display(0)
    @Slot()
    def on_minus_clicked(self):
        if self.operant1==0:
            return
        self.op=operation.minus 
        self.display(0)
    @Slot()
    def on_multibly_clicked(self):
        if self.operant1==0:
            return
        self.op=operation.multibly
        self.display(0)
    @Slot()
    def on_plus_clicked(self):
        if self.operant1==0:
            return
        self.op=operation.plus
        self.display(0)
    @Slot()
    def on_Calculate_clicked(self):
        if self.op==operation.plus:
            self.result=self.operant1+self.operant2
        elif self.op==operation.minus:
            self.result=self.operant1-self.operant2
        elif self.op==operation.divide:
            self.result=self.operant1/self.operant2
        elif self.op==operation.multibly:
            self.result=self.operant1*self.operant2
        else:
            return
        self.op=operation.notset
        self.operant1=self.result
        self.operant2=0
        self.display(self.result)
        


if __name__ == "__main__":
 app = QApplication(sys.argv)
 calculator = mini()
 calculator.show()
 sys.exit(app.exec_())
 
