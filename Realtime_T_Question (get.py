# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bbb.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import MySQLdb
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)




class QUESTIONSTUDENT(object):
    def __init__(self):
        self.allQuestion_vote()
    def allQuestion_vote(self):
        mydb = MySQLdb.connect(host='10.61.3.223', port=3306, user='2016FRA241G5', passwd='SzTGde9E9AxVaNXA',db='2016FRA241G5', charset='utf8')
        cur = mydb.cursor()
        call = "SELECT `Question`,`Vote` FROM `Question Table` "
        # print call
        # print cur
        cur.execute(call)
        data = cur.fetchall()
        mydb.close()
        # print data
        return data
        ############################################################################
    # หาวิธีลบคำถามที่ back กลับแล้วเข้าใหม่เปลี่ยนเป็นอันใหม่ไม่เป็น รู้คอนเสบแต่เขียนไม่เป็น ว่าที่เขียนออกมามันเริ่มเก็บ[0][1] ลงไป [1][1]ไปเรื่อยๆ
    #
    # Que = 'ควาย'
    # Que2 = '2016-11-08'
    # def Update(self,stu):
    #     self.Que = long(stu)
    #     Databaselist = self. allQuestion_vote(Que=str(stu))
    #     ID=str(Databaselist[0])

        return ID
    dataquestion=allQuestion_vote(object)
    print('%d' % (dataquestion[0][1]))
    print('%d' % (dataquestion[2][1]))

    #a="get"
    def setupUi(self, QuestionFormStudent_2,):
        QuestionFormStudent_2.setObjectName(_fromUtf8("QuestionFormStudent_2"))
        QuestionFormStudent_2.setFixedSize(240,400)#240,400
        self.centralwidget = QtGui.QWidget(QuestionFormStudent_2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.bg = QtGui.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(0, 0, 240, 400))
        self.bg.setText(_fromUtf8(""))
        self.bg.setPixmap(QtGui.QPixmap(_fromUtf8("teacherBackground_3")))
        self.bg.setObjectName(_fromUtf8("bg"))
        self.verticalLayoutWidget = QtGui.QLabel(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 200, 260))#(20, 60, 200, 260))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.QuestionFormStudent = QtGui.QTextBrowser(self.verticalLayoutWidget)
        self.QuestionFormStudent.setStyleSheet("background-color: green;")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 100, 51))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.setStyleSheet("color: white;font-size: 18pt;border: white")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.QuestionFormStudent.sizePolicy().hasHeightForWidth())
        self.QuestionFormStudent.setSizePolicy(sizePolicy)
        self.QuestionFormStudent.setObjectName(_fromUtf8("QuestionFormStudent"))
        self.verticalLayout.addWidget(self.QuestionFormStudent)
        self.back = QtGui.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(30, 330 , 50, 31)) #(30, 330 , 50, 31))
        self.back.setObjectName(_fromUtf8("back"))
        QuestionFormStudent_2.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(QuestionFormStudent_2)
        self.menubar.setGeometry(QtCore.QRect(50, 200, 331, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        QuestionFormStudent_2.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(QuestionFormStudent_2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        QuestionFormStudent_2.setStatusBar(self.statusbar)
        self.verticalLayoutWidget.setStyleSheet("background-color: green;color: white;font-size: 13pt;border: white")
        self.back.setStyleSheet("background-color:Green;color: white;font-size: 11pt;border: white")#coller
        self.retranslateUi(QuestionFormStudent_2) #blakไม่ออก
        QtCore.QMetaObject.connectSlotsByName(QuestionFormStudent_2) #blakไม่ออก

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 62, 200, 40))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        # self.lineEdit.setText(_translate("QuestionFormStudent_2", str(self.Que), None))
        try:
            self.lineEdit.setText(self.dataquestion[0][0]+'                                            %d' % (self.dataquestion[2][1])) #ขนาดข้อความที่รับมาอยู่ข่อง 1
        except:
            pass
        self.lineEdit2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit2.setGeometry(QtCore.QRect(20, 102, 200, 40))
        self.lineEdit2.setObjectName(_fromUtf8("lineEdit"))
        # self.lineEdit2.setText(_translate("QuestionFormStudent_2", str(self.Que2), None))
        try:
            self.lineEdit2.setText(self.dataquestion[1][0]+'                                               %d' % (self.dataquestion[2][1])) #ขนาดข้อความที่รับมาอยู่ข่อง2
        except:
            pass
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 142, 200, 40))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        # self.lineEdit.setText(_translate("QuestionFormStudent_2", str(self.Que), None))
        try:
            self.lineEdit.setText(self.dataquestion[2][0]+'                                                   %d'% (self.dataquestion[0][1])) #ขนาดข้อความที่รับมาอยู่ข่อง3
        except:
            pass
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 182, 200, 40))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        # self.lineEdit.setText(_translate("QuestionFormStudent_2", str(self.Que), None))
        try:
            self.lineEdit.setText(self.dataquestion[3][0]+'                                             %d'% (self.dataquestion[3][1])) #ขนาดข้อความที่รับมาอยู่ข่อง4
        except:
            pass







    def retranslateUi(self, QuestionFormStudent_2):
        QuestionFormStudent_2.setWindowTitle(_translate("QuestionFormStudent_2", "MainWindow", None))
        #self.QuestionFormStudent.setStyleSheet("background-color: white; color: red;font-size: 15pt")#สีแดง,ตัวหนังสือ15
        self.back.setText(_translate("QuestionFormStudent_2", "Back", None))
        self.QuestionFormStudent.setHtml(_translate("QuestionFormStudent_2", "Question", None))
        #self.lineEdit.setText(_translate("MainWindow", str(self.stuID), None))
        self.label_2.setText(_translate("QuestionFormStudent_2", "Question", None))












    #def ID(self,i):
     #   self.stuID  = long(self.stuID)+ i
      #  self.lineEdit.setText(_translate("QuestionFormStudent_2", str(self.stuID), None))




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    QuestionFormStudent_2 = QtGui.QMainWindow()
    ui = QUESTIONSTUDENT()
    ui.setupUi(QuestionFormStudent_2)
    QuestionFormStudent_2.show()
    sys.exit(app.exec_())





