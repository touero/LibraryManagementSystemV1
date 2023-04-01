# -*- coding: utf-8 -*-
# @Time : 2021/6/28 9:04
# @Author : Toutoutoutouer
# @Email : wes0018@aliyun.com
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, pyodbc
from PyQt5 import QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 60, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 130, 72, 15))
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(130, 50, 171, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 120, 171, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(70, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 200, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(Dialog.login)

        #ok = self.textEdit.exec()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登陆界面"))
        self.label.setText(_translate("Dialog", "用户名:"))
        self.label_2.setText(_translate("Dialog", "密码:"))
        self.pushButton.setText(_translate("Dialog", "登录"))
        self.pushButton_2.setText(_translate("Dialog", "注册"))

    def log(self):
        username = self.textEdit.text()



class methods(QtWidgets.QMainWindow,Ui_Dialog):
    def __init__(self):
        super(methods, self).__init__()
        self.setupUi(self)
    # 定义槽函数
    def login(self):
        conn = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=' + '.' + ';DATABASE=' + 'BookDB122' + ';UID=' + 'sa' + ';PWD=' + '223366')
        cursor = conn.cursor()
        sql = "SELECT * FROM login WHERE username='{}' ".format(self.username)
        print(self.username)
        cursor.execute(sql)
        loginpassword = cursor.fetchall()
        if loginpassword:
            if self.textEdit_2 == loginpassword[0][1]:
                print(loginpassword[0][1])
                print('登录成功!')
                conn.close()
            else:
                print('登陆失败!程序退出!')
                conn.close()
                exit()
        else:
            print('该账户不存在!!!')
            exit()
            conn.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow() # 创建窗体对象
    ui = methods() # 创建PyQt5设计的窗体对象
    ui.setupUi(MainWindow) # 调用PyQt5窗体的方法对窗体对象进行初始化设置
    MainWindow.show() # 显示窗体
    sys.exit(app.exec_())
