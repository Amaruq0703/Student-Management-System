import PyQt6.QtWidgets as pyqt
from PyQt6.QtGui import QAction
import backend
import sys


class StudentWindow(pyqt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')

        #Menu Bar
        filemenuitem = self.menuBar().addMenu('&File')
        aboutmenuitem = self.menuBar().addMenu('&About')

        addstudentaction = QAction('Add Student', self)
        addstudentaction.triggered.connect(self.insert)
        filemenuitem.addAction(addstudentaction)

        aboutaction = QAction('About', self)
        aboutmenuitem.addAction(aboutaction)

        #Table
        self.table = pyqt.QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('ID', 'Name', 'Course', 'Mobile'))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    # Displaying Data
    def loadtable(self):
        data = backend.Get.getdata(self)
        self.table.setRowCount(0)
        for rowindex, rowdata in enumerate(data):
            self.table.insertRow(rowindex)
            for colnum, celldata in enumerate(rowdata):
                self.table.setItem(rowindex, colnum , pyqt.QTableWidgetItem(str(celldata)))

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()









app = pyqt.QApplication(sys.argv)
stuwindow = StudentWindow()
stuwindow.show()
stuwindow.loadtable()
sys.exit(app.exec())
