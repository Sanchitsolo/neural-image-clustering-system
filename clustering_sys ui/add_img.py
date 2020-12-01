from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
import os
from os import path
import shutil
import sys

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(566, 196)
        Dialog.setWindowTitle('Input dialog')
        self.labelResponse = QtWidgets.QLabel(Dialog)
        self.labelResponse.setGeometry(QtCore.QRect(10, 60, 161, 21))
        self.labelResponse.setObjectName("labelResponse")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 59, 371, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 140, 80, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.add)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.labelResponse.setText(_translate("Dialog", "Enter the address of folder"))
        self.pushButton.setText(_translate("Dialog", "Add"))

    def add(self):
        path1=self.lineEdit.text()
        path2="/home/evil_overlord/clustering_sys/clustering_sys code/add_new"
        
        if path.exists(path1):
            imgset=[]
            for (root, dirs, files) in os.walk(os.path.join(path1),topdown=True):
                for f in files:
                    imgset.append(f)
            imgset.sort()
            for image in imgset:
                shutil.copy(os.path.join(path1,image), os.path.join(path2,image))

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Invalid Path.")
            msg.setInformativeText("The path that you have mentioned doesn't exist.")
            msg.setWindowTitle("Error")
            msg.exec_()