from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PIL import Image

class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 800)
        Dialog.setWindowTitle('Person Cluster')
        self.layout = QtWidgets.QHBoxLayout(Dialog)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layout.addWidget(self.scrollArea)

        path='/home/evil_overlord/clustering_sys/clustering_sys code'
        with open(os.path.join(path,'clusters','person.txt')) as f:
            img_lst=f.readlines()

        disp=[]
        for img in img_lst:
            address=os.path.join(path,'database',img.split('\n')[0])
            disp.append(address)
        range_i=int(len(disp)/5+1)
        
        btn_lst=[]
        indx=0
        button_number=0
        for i in range(range_i):
            for j in range(5):
                if indx<len(disp):
                    btn_name='button'+str(button_number)
                    self.btn_name=QtWidgets.QPushButton(Dialog)
                    self.btn_name.setIcon(QIcon(QPixmap(disp[indx])))
                    self.btn_name.setIconSize(QtCore.QSize(150,150))
                    self.gridLayout.addWidget(self.btn_name, i, j)
                    self.btn_name.clicked.connect(lambda checked, name=btn_name, image=disp[indx] : self.display(name, image))
                    button_number+=1
                    indx+=1

    def display(self, name, image):
        print(name)
        print("clicked")
        im=Image.open(image)
        im.show()