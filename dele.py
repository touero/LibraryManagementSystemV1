# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dele.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog6(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(510, 654)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 60, 121, 61))
        self.label.setToolTipDuration(-5)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 130, 251, 71))
        self.pushButton.setToolTipDuration(-1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 250, 251, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 370, 251, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 490, 251, 71))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(Dialog.delereader)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_2.clicked.connect(Dialog.deleborrow)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_3.clicked.connect(Dialog.delebooks)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton_4.clicked.connect(Dialog.menu)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "删除"))
        self.label.setText(_translate("Dialog", "删除"))
        self.pushButton.setText(_translate("Dialog", "删除读者信息表"))
        self.pushButton_2.setText(_translate("Dialog", "删除借阅信息表"))
        self.pushButton_3.setText(_translate("Dialog", "删除图书信息表"))
        self.pushButton_4.setText(_translate("Dialog", "主菜单"))
