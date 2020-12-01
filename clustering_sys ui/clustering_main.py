# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clustering_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        #MainWindow.resize(736, 721)
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.add_img_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_img_btn.setObjectName("add_img_btn")
        self.gridLayout_5.addWidget(self.add_img_btn, 0, 0, 1, 2)
        self.clustering_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clustering_btn.setObjectName("clustering_btn")
        self.gridLayout_5.addWidget(self.clustering_btn, 1, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_5.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_5.addLayout(self.gridLayout_2, 2, 1, 1, 1)
        self.cluster = QtWidgets.QPushButton(self.centralwidget)
        self.cluster.setObjectName("cluster")
        self.gridLayout_5.addWidget(self.cluster, 3, 0, 1, 1)
        self.cluster_2 = QtWidgets.QPushButton(self.centralwidget)
        self.cluster_2.setObjectName("cluster_2")
        self.gridLayout_5.addWidget(self.cluster_2, 3, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_5.addLayout(self.gridLayout_3, 4, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_5.addLayout(self.gridLayout_4, 4, 1, 1, 1)
        self.cluster_3 = QtWidgets.QPushButton(self.centralwidget)
        self.cluster_3.setObjectName("cluster_3")
        self.gridLayout_5.addWidget(self.cluster_3, 5, 0, 1, 1)
        self.cluster_4 = QtWidgets.QPushButton(self.centralwidget)
        self.cluster_4.setObjectName("cluster_4")
        self.gridLayout_5.addWidget(self.cluster_4, 5, 1, 1, 1)
        self.filter_btn = QtWidgets.QPushButton(self.centralwidget)
        self.filter_btn.setAutoRepeatDelay(300)
        self.filter_btn.setObjectName("filter_btn")
        self.gridLayout_5.addWidget(self.filter_btn, 6, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 736, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_img_btn.setText(_translate("MainWindow", "Add Images"))
        self.clustering_btn.setText(_translate("MainWindow", "Clusters"))
        self.cluster.setText(_translate("MainWindow", "Building Cluster"))
        self.cluster_2.setText(_translate("MainWindow", "Person Cluster"))
        self.cluster_3.setText(_translate("MainWindow", "Vehicle Cluster"))
        self.cluster_4.setText(_translate("MainWindow", "Weapon Cluster"))
        self.filter_btn.setText(_translate("MainWindow", "Filter"))

