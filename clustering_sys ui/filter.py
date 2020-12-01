from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import pandas as pd
import os
from PIL import Image

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1100, 488)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 453, 468))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 6, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.slider_1 = QtWidgets.QSlider(Dialog)
        self.slider_1.setOrientation(QtCore.Qt.Horizontal)
        self.slider_1.setObjectName("slider_1")
        self.gridLayout.addWidget(self.slider_1, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.slider_2 = QtWidgets.QSlider(Dialog)
        self.slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.slider_2.setObjectName("slider_2")
        self.gridLayout.addWidget(self.slider_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.slider_3 = QtWidgets.QSlider(Dialog)
        self.slider_3.setOrientation(QtCore.Qt.Horizontal)
        self.slider_3.setObjectName("slider_3")
        self.gridLayout.addWidget(self.slider_3, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.slider_1.setMinimum(0)
        self.slider_1.setMaximum(100)
        self.slider_2.setMinimum(0)
        self.slider_2.setMaximum(100)
        self.slider_3.setMinimum(0)
        self.slider_3.setMaximum(100)
        self.slider_1.valueChanged.connect(self.valchange_sl1)
        self.slider_2.valueChanged.connect(self.valchange_sl2)
        self.slider_3.valueChanged.connect(self.valchange_sl3)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Person - Weapon"))
        self.label_2.setText(_translate("Dialog", "Person - Vehicle"))
        self.label_3.setText(_translate("Dialog", "Person - Building"))

    def valchange_sl1(self):
        self.slider_2.setValue(0)
        self.slider_3.setValue(0)
        for i in range(self.gridLayout_2.count()):
            self.gridLayout_2.itemAt(i).widget().deleteLater()
        c1='person'
        c2='weapon'
        val=self.slider_1.value()
        probc1=val/2
        probc2=(100-val)/2
        print(val)
        self.img_display(c1,c2,probc1,probc2)

    def valchange_sl2(self):
        self.slider_1.setValue(0)
        self.slider_3.setValue(0)
        for i in range(self.gridLayout_2.count()):
            self.gridLayout_2.itemAt(i).widget().deleteLater()
        c1='person'
        c2='vehicle'
        val=self.slider_2.value()
        probc1=val/2
        probc2=(100-val)/2
        print(val)
        self.img_display(c1,c2,probc1,probc2)

    def valchange_sl3(self):
        self.slider_1.setValue(0)
        self.slider_2.setValue(0)
        for i in range(self.gridLayout_2.count()):
            self.gridLayout_2.itemAt(i).widget().deleteLater()
        c1='person'
        c2='building'
        val=self.slider_3.value()
        probc1=val/2
        probc2=(100-val)/2
        print(val)
        self.img_display(c1,c2,probc1,probc2)
    
    def img_display(self,c1,c2,probc1,probc2):
        path="/home/evil_overlord/clustering_sys/clustering_sys code"
        filename="log_data.csv"
        df=pd.read_csv(os.path.join(path,filename))
        img_lst=list(df.iloc[:,0])

        #creating a list of list for comparison of probabilities of different classes
        classes=['building','person','vehicle','weapon']
        cmp=[[]]*2
        cmp[0]=list(df.iloc[:,classes.index(c1)+1])
        cmp[1]=list(df.iloc[:,classes.index(c2)+1])

        #probc1=40
        #probc2=40
        indx=[]
        indx1=[cmp[0].index(i) for i in cmp[0] if i>probc1]
        indx2=[cmp[1].index(i) for i in cmp[1] if i>probc2]

        #resulting images in indx
        indx=list(set(indx1) & set(indx2))
        print(indx)

        disp=[]
        for img in indx:
            address=os.path.join(path,'database',str(img)+'.jpg')
            disp.append(address)
        range_i=int(len(disp))

        btn_lst=[]
        index=0
        button_number=0
        for i in range(range_i):
            for j in range(3):
                if index<len(disp):
                    btn_name='button'+str(button_number)
                    self.btn_name=QtWidgets.QPushButton(self)
                    self.btn_name.setIcon(QIcon(QPixmap(disp[index])))
                    self.btn_name.setIconSize(QtCore.QSize(150,150))
                    self.gridLayout_2.addWidget(self.btn_name, i, j)
                    self.btn_name.clicked.connect(lambda checked, name=btn_name, image=disp[index] : self.display(name, image))
                    button_number+=1
                    index+=1

    def display(self, name, image):
        print(name)
        print('clicked')
        im=Image.open(image)
        im.show()

