import PyQt6.QtWidgets as pyqt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt
import backend
import sys


class StudentWindow(pyqt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Student Management System')
        self.setFixedWidth(500)
        self.setFixedHeight(400)

        #Menu Bar
        filemenuitem = self.menuBar().addMenu('&File')
        aboutmenuitem = self.menuBar().addMenu('&About')
        editmenuitem = self.menuBar().addMenu('&Edit')

        addstudentaction = QAction(QIcon('icons/add.png'),'Add Student', self)
        addstudentaction.triggered.connect(self.insert)
        filemenuitem.addAction(addstudentaction)

        aboutaction = QAction('About', self)
        aboutmenuitem.addAction(aboutaction)

        searchstudentaction = QAction(QIcon('icons/search.png'),'Search', self)
        searchstudentaction.triggered.connect(self.search)
        editmenuitem.addAction(searchstudentaction)

        #Tool Bar
        toolbar = pyqt.QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)

        toolbar.addAction(addstudentaction)
        toolbar.addAction(searchstudentaction)

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
    
    def search(self):
        dialog = SearchDialog()
        dialog.exec()

# Insert New Student

class InsertDialog(pyqt.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Insert Student Data')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = pyqt.QVBoxLayout()

        #Widgets
        self.stuname = pyqt.QLineEdit()
        self.stuname.setPlaceholderText('Name')
        
        self.stucourse = pyqt.QComboBox()
        self.stucourse.addItems(['Biology', 'Math', 'Astronomy', 'Physics'])

        self.stumob = pyqt.QLineEdit()
        self.stumob.setPlaceholderText('Mobile')

        subbutton = pyqt.QPushButton('Submit')
        subbutton.clicked.connect(self.addstudent)

        layout.addWidget(self.stuname)
        layout.addWidget(self.stucourse)
        layout.addWidget(self.stumob)
        layout.addWidget(subbutton)

        self.setLayout(layout)

    #Method to add student to table
    def addstudent(self):
        name = self.stuname.text()
        course = self.stucourse.itemText(self.stucourse.currentIndex())
        mobile = self.stumob.text()

        writedata = backend.Write(name=name, course=course, mobile=mobile)
        writedata.writedata()
        stuwindow.loadtable()

# Search for student name        

class SearchDialog(pyqt.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Search Student Name')
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = pyqt.QVBoxLayout()

        #Widgets
        self.searchbox = pyqt.QLineEdit()
        self.searchbox.setPlaceholderText('Name')

        searchbutton = pyqt.QPushButton('Search')
        searchbutton.clicked.connect(self.searchstudent)

        layout.addWidget(self.searchbox)
        layout.addWidget(searchbutton)

        self.setLayout(layout)

    #method to search for student by name in table

    def searchstudent(self):
        name = self.searchbox.text()
        namedata = backend.Search(name).searchdata()
        result = list(namedata)
        items = stuwindow.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            stuwindow.table.item(item.row(), 1).setSelected(True)




app = pyqt.QApplication(sys.argv)
stuwindow = StudentWindow()
stuwindow.show()
stuwindow.loadtable()
sys.exit(app.exec())
