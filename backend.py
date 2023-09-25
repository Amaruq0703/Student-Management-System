import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Write data in database

class Write:
    def __init__(self, name, course, mobile):
        self.name = name
        self.course = course
        self.mobile = mobile
    
    def writedata(self):
        row = (self.name, self.course, self.mobile)
        cursor.execute('INSERT INTO students (name, course, mobile) VALUES (?,?,?)', row)
        connection.commit()

    def editdata(self, id):
        row = (self.name, self.course, self.mobile, id)
        cursor.execute('UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?', row)
        connection.commit()


# Get data from database

class Get:
    def __init__(self):
        pass

    def getdata(self):
        cursor.execute('SELECT * FROM students')
        studentdata = cursor.fetchall()
        return studentdata


class Search:
    def __init__(self, searchname):
        self.searchname = searchname
        pass

    def searchdata(self):
        cursor.execute('SELECT * FROM students WHERE name = ?', (self.searchname,))
        namedata = cursor.fetchall()
        return namedata

class Delete:
    def __init__(self):
        pass

    def deletedata(self, id):
        cursor.execute('DELETE FROM students WHERE id = ?', (id,))
        connection.commit()