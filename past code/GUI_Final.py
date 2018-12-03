
# coding: utf-8

# In[ ]:


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re
from PyQt5.QtCore import QDate, QDateTime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.label.setObjectName("label")
        self.label.setStyleSheet("background-color: rgb(195, 34, 34);")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(140, 100, 261, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setMinimumDate(QDate(2018,11,1))
        self.dateTimeEdit.setMaximumDate(QDate(2018,11,30))

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color: rgb(195, 34, 34);")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(128, 0, 491, 41))
        self.label_3.setStyleSheet("background-color: rgb(195, 34, 34);")
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("background-color: rgb(195, 34, 34);")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 114, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: rgb(195, 34, 34);")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 160, 114, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color: rgb(195, 34, 34);")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 160, 141, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background-color: rgb(195, 34, 34);")
        self.labellizixuan = QtWidgets.QLabel(self.centralwidget)
        self.labellizixuan.setGeometry(QtCore.QRect(130, 220, 651, 201))
        self.labellizixuan.setText("")
        self.labellizixuan.setObjectName("labellizixuan")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 50, 481, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 450, 781, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("background-color: rgb(232, 232, 232);border-color: rgb(232, 232, 232);")
        MainWindow.setCentralWidget(self.centralwidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
   
        self.pushButton.clicked.connect(self._showpic1)
        self.pushButton_2.clicked.connect(self._showpic2)
        self.pushButton_3.clicked.connect(self._showpic3)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Input Link</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Start Date</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Price Comparison Platform @ Paulfans Forever</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Price"))
        self.pushButton_2.setText(_translate("MainWindow", "Ratings"))
        self.pushButton_3.setText(_translate("MainWindow", "Comments Number"))


        self.comboBox.setItemText(0, _translate("MainWindow", "https://www.amazon.com/Samsung-Electronics-UN32M4500A-32-Inch-Smart/dp/B073JP6WK4/ref=sr_1_acs_bss_1_1?s=tv&ie=UTF8&qid=1543333023&sr=1-1-acs&keywords=samsung+tv"))
        self.comboBox.setItemText(1, _translate("MainWindow", "https://www.amazon.com/Samsung-SM-N950UZKAXAA-Version-Factory-Unlocked/dp/B07536MYBQ/ref=sr_1_4?s=wireless&ie=UTF8&qid=1541726067&sr=1-4&keywords=galaxy+note"))
        self.comboBox.setItemText(2, _translate("MainWindow", "https://www.amazon.com/Nokia-3-1-Unlocked-Smartphone-T-Mobile/dp/B07DDD8PNQ/ref=sr_1_6?s=mobile-apps&ie=UTF8&qid=1541724798&sr=8-6&keywords=nokia"))
        self.comboBox.setItemText(3, _translate("MainWindow", "https://www.amazon.com/Apple-iPhone-Unlocked-Black-Version/dp/B01LYT95XR/ref=sr_1_8?s=wireless&ie=UTF8&qid=1541725701&sr=1-8&keywords=Apple+iPhone+7%2C+32GB"))
        self.comboBox.setItemText(4, _translate("MainWindow", "https://www.amazon.com/Microsoft-Surface-Intel-Core-256GB/dp/B07HZNKGDV/ref=sr_1_3?ie=UTF8&qid=1541733553&sr=8-3&keywords=microsoft+surface+pro+6"))
        self.comboBox.setItemText(5, _translate("MainWindow", "https://www.amazon.com/Flagship-Lenovo-Anti-glare-Quad-Core-Bluetooth/dp/B07DN2JG5T/ref=sr_1_4?ie=UTF8&qid=1543335827&sr=8-4&keywords=Lenovo+Laptop+IdeaPad+330"))
        self.comboBox.setItemText(6, _translate("MainWindow", "https://www.amazon.com/Premium-Dell-i7-8750H-Keyboard-Bluetooth/dp/B07GM4VHNP/ref=sr_1_1?ie=UTF8&qid=1541732861&sr=8-1&keywords=Dell+G5+Gaming+Laptop+15.6%22+Full+HD%2C+Intel+Core+i7-8750H"))
        self.comboBox.setItemText(7, _translate("MainWindow", "https://www.amazon.com/Panasonic-Microwave-NN-SN651B-Countertop-Technology/dp/B00FRD0PNC/ref=sr_1_4?s=home-garden&ie=UTF8&qid=1541723725&sr=1-4&keywords=panasonic+microwave+NN-SN651B&dpID=41-d0ePOmZL&preST=_SY300_QL70_&dpSrc=srch"))
        self.comboBox.setItemText(8, _translate("MainWindow", "https://www.amazon.com/BLACK-DECKER-BCRK17W-Compact-Refrigerator/dp/B01DZQI7B4/ref=sr_1_1?s=home-garden&ie=UTF8&qid=1543772335&sr=1-1&keywords=BLACK%2BDECKER+BCRK17W+Compact+Refrigerator+Energy+Star+Single+Door+Mini+Fridge+with+Freezer%2C+1.7+Cubic+Ft.%2C+White"))
        self.comboBox.setItemText(9, _translate("MainWindow", "https://www.amazon.com/d/Space-Heaters-Accessories/Honeywell-HCE323V-Digital-Ceramic-Heater/B00KNBKB64/ref=sr_1_2_sspa?s=home-garden&ie=UTF8&qid=1543337061&sr=1-2-spons&keywords=Lasko+Ceramic+Tower+Heater+with+Digital+Display+%26+Remote+Control&psc=1"))
        

    def get_start_time(self,string):
        pattern=r'(\d{4})\,\s+(\d+),\s+(\d+),\s+(\d+),\s+(\d+)'
        c=re.search(pattern,string)
        if int(c.group(4))>9 and int(c.group(3))>9:
            d=str(c.group(1))+'-'+str(c.group(2))+'-'+str(c.group(3))+' '+str(c.group(4))+':'+'00:00'
        elif int(c.group(4))>9 and int(c.group(3))<=9:
            d=str(c.group(1))+'-'+str(c.group(2))+'-0'+str(c.group(3))+' '+str(c.group(4))+':'+'00:00'
        elif int(c.group(4))<=9 and int(c.group(3))<=9:
            d=str(c.group(1))+'-'+str(c.group(2))+'-0'+str(c.group(3))+' 0'+str(c.group(4))+':'+'00:00'
        elif int(c.group(4))<=9 and int(c.group(3))>9:
            d=str(c.group(1))+'-'+str(c.group(2))+'-'+str(c.group(3))+' 0'+str(c.group(4))+':'+'00:00'
        return d

    def table(self,link,start_time):
        database_df = pd.read_csv('database.csv',index_col=['Unnamed: 0'])
        try:
            select_df = database_df[database_df['time']>=start_time]
            try:
                # get productID based on link
                productID = list(database_df['productID'][database_df['link'] == link])[0]
                select_df = select_df[database_df['productID'] == productID]
                table_df = pd.DataFrame()
                platform_list = ['Amazon','Walmart','Ebay','Newegg']
                for i in range(1,5):
                    platformID = i
                    platformName = platform_list[i-1]
                    productName = list(select_df['name'][select_df['platformID'] == platformID])[0]
                    try:
                        productName = productName.split()[0]+" ..."
                    except:
                        pass
                    productLink = list(select_df['link'][select_df['platformID'] == platformID])[0]
                    table_df = table_df.append(pd.Series([platformID,platformName,productName,productLink]),ignore_index=True)
                table_df.columns = ['Platform ID','Platform Name','Product Name','Product Link']
                string = table_df.to_string(sparsify=True,justify='match-parent')
                return string
            
            except:
                raise ValueError('Invalid Link')
        except:
            raise ValueError('Invalid Time')
    
    def _showpic1(self):
        link = self.comboBox.currentText()
        start_time=self.get_start_time(str(self.dateTimeEdit.dateTime()))
        
        database_df = pd.read_csv('database.csv',index_col=['Unnamed: 0'])
    
        # define productID based on link
        try:
            select_df = database_df[database_df['time']>=start_time]
            try:
                # get productID based on link
                productID = list(database_df['productID'][database_df['link'] == link])[0]
                select_df = select_df[['time','platformID','price']][database_df['productID'] == productID]
                select_df = select_df.dropna(axis=0)
                # plot 
                plt.figure(figsize=(5,2))
                g = sns.pointplot(y = select_df['price'],x = select_df['time'],hue = select_df['platformID'],scale=0.4)
                g.set(xticks=[])
                plt.xlabel('time period')
                plt.savefig('price.jpg')
            except:
                raise ValueError('Invalid Link')
        except:
            raise ValueError('Invalid Time')
        pixmap = QPixmap('price.jpg')  
        self.labellizixuan.setPixmap(pixmap)
        
        tablestring=self.table(link,start_time)
        self.textBrowser.setText(tablestring)
        
        

    def _showpic2(self):
        link = self.comboBox.currentText()
        start_time=self.get_start_time(str(self.dateTimeEdit.dateTime()))
        
        database_df = pd.read_csv('database.csv',index_col=['Unnamed: 0'])
    
        # define productID based on link
        try:
            select_df = database_df[database_df['time']>=start_time]
            try:
                # get productID based on link
                productID = list(database_df['productID'][database_df['link'] == link])[0]
                select_df = select_df[['time','platformID','rating']][database_df['productID'] == productID]
                select_df = select_df.dropna(axis=0)
                # plot 
                plt.figure(figsize=(5,2))
                g = sns.pointplot(y = select_df['rating'],x = select_df['time'],hue = select_df['platformID'],scale=0.4)
                g.set(xticks=[])
                plt.xlabel('time period')
                plt.savefig('rating.jpg')
            except:
                raise ValueError('Invalid Link')
        except:
            raise ValueError('Invalid Time')

        pixmap = QPixmap('rating.jpg') 
        self.labellizixuan.setPixmap(pixmap)
        self.table(link,start_time)
        
        tablestring=self.table(link,start_time)
        self.textBrowser.setText(tablestring)

    def _showpic3(self):
        link = self.comboBox.currentText()
        start_time=self.get_start_time(str(self.dateTimeEdit.dateTime()))
        
        database_df = pd.read_csv('database.csv',index_col=['Unnamed: 0'])
        # define productID based on link
        try:
            select_df = database_df[database_df['time']>=start_time]
            try:
                # get productID based on link
                productID = list(database_df['productID'][database_df['link'] == link])[0]
                select_df = select_df[['time','platformID','commentNum']][database_df['productID'] == productID]
                select_df = select_df.dropna(axis=0)
                # plot 
                plt.figure(figsize=(5,2))
                g = sns.pointplot(y = select_df['commentNum'],x = select_df['time'],hue = select_df['platformID'],scale=0.4)
                g.set(xticks=[])
                plt.xlabel('time period')
                plt.savefig('comment.jpg')
            except:
                raise ValueError('Invalid Link')
        except:
            raise ValueError('Invalid Time')
        pixmap = QPixmap('comment.jpg')  ##从QtGui中新建一个QPixmap的类
        self.labellizixuan.setPixmap(pixmap)
        self.table(link,start_time)
        
        tablestring=self.table(link,start_time)
        self.textBrowser.setText(tablestring)
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

