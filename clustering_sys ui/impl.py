import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap
from clustering_main import *
from add_img import Ui_Dialog as Form
from cluster import Ui_Dialog as Clr
from cluster_2 import Ui_Dialog as Clr_2
from cluster_3 import Ui_Dialog as Clr_3
from cluster_4 import Ui_Dialog as Clr_4
from filter import Ui_Dialog as flt
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
from PIL import Image
import os
import pandas as pd
import shutil

class App(QMainWindow):

	def __init__(self):
		super().__init__()
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.title='Neural Image Clustering System'
		self.setWindowTitle(self.title)
		#self.thumbnail_create()     #creates thumbnails to be displayed
		self.ui.clustering_btn.clicked.connect(self.clustering)      #use clustering fn when clustering_btn is clicked
		self.ui.add_img_btn.clicked.connect(self.add_img)            #use add_img fn when add_img_btn is clicked
		self.ui.cluster.clicked.connect(self.cluster_btn)
		self.ui.cluster_2.clicked.connect(self.cluster_2_btn)
		self.ui.cluster_3.clicked.connect(self.cluster_3_btn)
		self.ui.cluster_4.clicked.connect(self.cluster_4_btn)
		self.ui.filter_btn.clicked.connect(self.filter)
		self.display()

	def display(self):

		path1="/home/evil_overlord/clustering_sys/clustering_sys code/thumbnails"

		#display cluster thumbnails for building class
		disp=[]     #list created for storing the file names of thumbnails that are to be displayed
		indx=0
		img_lst=os.listdir(os.path.join(path1,'building'))
		for image in img_lst:
			address=os.path.join(path1,'building',image)
			disp.append(address)	#disp now contains addresses of all the thumbnails that are to be displayed in grid, this has to be done because QPixmap doesnt take any variable values, i.e. os.path.join wont work.
		for x in range(10):
			for y in range(10):
				if indx<len(disp):
					label=QLabel(self)
					pixmap=QPixmap(disp[indx])
					label.setPixmap(pixmap)
					self.ui.gridLayout.addWidget(label, x, y)
					indx+=1
				else:
					break

		#display cluster thumbnails for person class
		disp=[]
		indx=0
		img_lst=os.listdir(os.path.join(path1,'person'))
		for image in img_lst:
			address=os.path.join(path1,'person',image)
			disp.append(address)
		for x in range(10):
			for y in range(10):
				if indx<len(disp):
					label=QLabel(self)
					pixmap=QPixmap(disp[indx])
					label.setPixmap(pixmap)
					self.ui.gridLayout_2.addWidget(label, x, y)
					indx+=1
				else:
					break

		#display cluster thumbnails for vehicle class
		disp=[]
		indx=0
		img_lst=os.listdir(os.path.join(path1,'vehicle'))
		for image in img_lst:
			address=os.path.join(path1,'vehicle',image)
			disp.append(address)
		for x in range(10):
			for y in range(10):
				if indx<len(disp):
					label=QLabel(self)
					pixmap=QPixmap(disp[indx])
					label.setPixmap(pixmap)
					self.ui.gridLayout_3.addWidget(label, x, y)
					indx+=1
				else:
					break
		
		#display cluster thumbnails for weapon class
		disp=[]
		indx=0
		img_lst=os.listdir(os.path.join(path1,'weapon'))
		for image in img_lst:
			address=os.path.join(path1,'weapon',image)
			disp.append(address)
		for x in range(10):
			for y in range(10):
				if indx<len(disp):
					label=QLabel(self)
					pixmap=QPixmap(disp[indx])
					label.setPixmap(pixmap)
					self.ui.gridLayout_4.addWidget(label, x, y)
					indx+=1
				else:
					break

		self.show()

	def thumbnail_create(self):
		path2="/home/evil_overlord/clustering_sys/clustering_sys code"
		size=(30,30)     #size of thumbnail
		for file in os.listdir(os.path.join(path2,'clusters')):
			with open(os.path.join(path2,'clusters',file),"r") as f:
				lst=f.readlines()
				for i in lst:
					i=i.split('\n')[0]    #removing the \n suffix from each element of list
					image=Image.open(os.path.join(path2,'database',i))
					image.thumbnail(size)
					image.save(os.path.join(path2,'thumbnails',file.split('.')[0],i))

	def clustering(self):
		#Loading the self-trained DL model
		path3="/home/evil_overlord/clustering_sys/clustering_sys code"
		#model=torch.load(os.path.join(path3,'dl_models','res50(balanced)64-120.pth'))    #loading the self-trained DL model on custom dataset.

		if len(os.listdir(os.path.join(path3,"add_new"))) == 0:

			msg=QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setText("No Input")
			msg.setInformativeText("Add new images to be clustered first")
			msg.setWindowTitle("Error")
			msg.exec_()

		else:
			
			#Renaming the new images in add_new according to the images in dataset folder
			n=len(os.listdir(os.path.join(path3,"database")))   #'n' stores the number of images in database folder
			p=n              # used later as a count for writing image names in clustering files
			imgset=[]
			l=os.listdir(os.path.join(path3,"add_new"))
			print('old l',l)
			for i in l:
				os.rename(os.path.join(path3,"add_new",i),os.path.join(path3,'database',str(n)+'.jpg'))    #renames images in 'add_new' in order
				imgset.append(str(n)+'.jpg')
				n+=1

			print(imgset)
			
			#Defining the transforms that are to be applied to the image for inference.
			transform=transforms.Compose([
				transforms.Resize(256),
				transforms.CenterCrop(224),
				transforms.ToTensor(),
				transforms.Normalize(
					mean=[0.485, 0.456, 0.406],
					std=[0.229, 0.224, 0.225])
			])

			tensors=[]      #List of tensors of images present in database folder
			for im in imgset:
				img=Image.open(os.path.join(path3,'database',im))   #Opening image using PIL
				img_t=transform(img)
				batch_t=torch.unsqueeze(img_t,0)
				tensors.append(batch_t)

			#Extracting probabilities and storing it in probslist.
			prob_main=[[]]*3
			lvl1=os.listdir(os.path.join(path3,'dl_models/ensemble_model/level1'))
			m_cnt=0
			for m in lvl1:
				#for gpu
				#model=torch.load(os.path.join(path3,'dl_models/ensemble_model/level1',m))    #loading the self-trained DL model on custom dataset.
				#for cpu
				model=torch.load(os.path.join(path3,'dl_models/ensemble_model/level1',m), map_location='cpu')
				probslist=[]      #created list for storing probabilities, later on will be stored to csv file.
				model.eval()
				for t in tensors:
					#for gpu
					#b = t.to(torch.device("cuda"))   #send the tensor to gpu i.e. cuda, basically converting tensor to cuda tensor.
					#for cpu
					b = t.to(torch.device("cpu"))
					out=model(b)
					percentage=torch.nn.functional.softmax(out, dim=1)[0]*100 #calcuating percentage by probability*100, probability is provided by softmax fn.
					for value in percentage:
						probslist.append(float(value))
				prob_main[m_cnt]=list(probslist)
				m_cnt+=1

			lvl2=os.listdir(os.path.join(path3,'dl_models/ensemble_model/level2'))
			for m in lvl2:
				#for gpu
				#model=torch.load(os.path.join(path3,'dl_models/ensemble_model/level2',m))    #loading the self-trained DL model on custom dataset.
				#for cpu
				model=torch.load(os.path.join(path3,'dl_models/ensemble_model/level2',m), map_location='cpu')
				probslist=[]      #created list for storing probabilities, later on will be stored to csv file.
				model.eval()
				for t in tensors:
					#for gpu
					#b = t.to(torch.device("cuda"))   #send the tensor to gpu i.e. cuda, basically converting tensor to cuda tensor.
					#for cpu
					b = t.to(torch.device("cpu"))
					out=model(b)
					percentage=torch.nn.functional.softmax(out, dim=1)[0]*100 #calcuating percentage by probability*100, probability is provided by softmax fn.
					for value in percentage:
						probslist.append(float(value))
				prob_main[m_cnt]=list(probslist)
				m_cnt+=1			

			#print(prob_main)

			prob_res=[]
			for i in range(len(prob_main[0])):
				prob_res.append(max(prob_main[0][i],prob_main[1][i]))

			#print('lvl1',prob_res)
			
			p_indx=1
			w_indx=3
			cnt=0
			while cnt < len(prob_main[2]):
				#for person
				if prob_res[p_indx] > 0.2:    #threshold to consider level2 person values
					prob_res[p_indx] = max(prob_res[p_indx],prob_main[2][cnt])
				p_indx+=4
				cnt+=1
				#for weapon
				if prob_res[w_indx] > 2.1:    #threshold to consider level2 weapon values
					prob_res[w_indx] = max(prob_res[w_indx],prob_main[2][cnt])
				w_indx+=4
				cnt+=1

			#print('lvl2',prob_res)
			
			blst=[]
			plst=[]
			vlst=[]
			wlst=[]
			#above 4 list contain probabilies of each class separately.
			i=0
			while i<len(prob_res):
				blst.append(prob_res[i])
				plst.append(prob_res[i+1])
				vlst.append(prob_res[i+2])
				wlst.append(prob_res[i+3])
				i=i+4

			#Creating the dataframe and exporting it to a csv file containing probabilities from inference.
			df=pd.DataFrame({'Imagename':imgset,'building':blst,'person':plst,'vehicle':vlst,'weapon':wlst})
			print(df)

			#creates txt files in cluster folder and populates them with respective filenames i.e. classes.
			i=p
			collst=list(df.columns)
			rowct=len(df.iloc[:,0])
			while i-p<rowct:
				lst=list(df.iloc[i-p,1:5])
				m=max(lst)
				ind=lst.index(m)+1
				colname=collst[ind]
				print('max',m,colname)
				with open(os.path.join(path3,'clusters/'+colname+'.txt'), 'a') as f:
					f.write("%s.jpg\n" %i)
				i=i+1

			self.thumbnail_create()
			self.display()

			try:
				filename='log_data.csv'
				df_main=pd.read_csv(os.path.join(path3,filename))
			except:
				df_main=pd.DataFrame()

			df_main=pd.concat([df_main, df], ignore_index=True, sort=True) #appends the df of images in add_new folder to df_main which contains all images in dataset folder
			df_main.to_csv(os.path.join(path3,'log_data.csv'), index=None, header=True)     #saves df_main as log_data.csv


	def add_img(self):
		dialog=QtWidgets.QDialog()
		dialog.ui=Form()
		dialog.ui.setupUi(dialog)
		dialog.exec_()
		dialog.show()

	def cluster_btn(self):
		dialog=QtWidgets.QDialog()
		dialog.ui=Clr()
		dialog.ui.setupUi(dialog)
		dialog.exec_()
		dialog.show()

	def cluster_2_btn(self):
		dialog=QtWidgets.QDialog()
		dialog.ui=Clr_2()
		dialog.ui.setupUi(dialog)
		dialog.exec_()
		dialog.show()

	def cluster_3_btn(self):
		dialog=QtWidgets.QDialog()
		dialog.ui=Clr_3()
		dialog.ui.setupUi(dialog)
		dialog.exec_()
		dialog.show()

	def cluster_4_btn(self):
		dialog=QtWidgets.QDialog()
		dialog.ui=Clr_4()
		dialog.ui.setupUi(dialog)
		dialog.exec_()
		dialog.show()

	def filter(self):
		dialog=QtWidgets.QDialog()
		dialog.ui=flt()
		dialog.ui.setupUi(dialog)
		dialog.exec_()
		dialog.show()

#Main
if __name__=="__main__":
	app=QApplication(sys.argv)
	w=App()
	w.show()
	sys.exit(app.exec_())