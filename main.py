# if __name__=="__main__":
#     import sys
#     app =QtWidgets.QApplication(sys.argv)
#     MainWindow=QtWidgets.QMainWindow()
#     ui=Ui_Dialog()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec())


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


Form, Window = uic.loadUiType("untitled.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

# Vlad=========================

def  add_function(self):
    self.Button0.clicked.connect(lambda:self.write_number(self.Button0.text()))

#     -----------------------------------------------------------------------

def  write_number(self,number):
    print(number)


app.exec()
