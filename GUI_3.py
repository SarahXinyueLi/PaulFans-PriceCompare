
# coding: utf-8




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
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 50, 261, 31))
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(140, 100, 261, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setMinimumDate(QDate(2018,11,1))
        self.dateTimeEdit.setMaximumDate(QDate(2018,11,30))
        #self.dateTimeEdit.setMinimumDate(QDate.currentDate().addDays(-31))
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(128, 0, 491, 41))
        self.label_3.setStyleSheet("background-color: rgb(178, 237, 216);")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 114, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 160, 114, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 160, 141, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.labellizixuan = QtWidgets.QLabel(self.centralwidget)
        self.labellizixuan.setGeometry(QtCore.QRect(20, 210, 601, 251))
        self.labellizixuan.setText("")
        self.labellizixuan.setObjectName("labellizixuan")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 30, 301, 71))
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
        
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(560, -20, 251, 201))
        self.graphicsView.setStyleSheet("background-image: url(:/iconorbit.com/public/icons/256-watermark/1604201618231992167-Shopping%20Cart%20Icon.jpg);\n"
"border-color: rgb(255, 255, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 420, 781, 111))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.toolBar = QtWidgets.QToolBar(MainWindow)
#         self.toolBar.setObjectName("toolBar")
#         MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
#         self.toolBar = QtWidgets.QToolBar(MainWindow)
#         self.toolBar.setObjectName("toolBar")
        
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
#         self.toolBar = QtWidgets.QToolBar(MainWindow)
#         self.toolBar.setObjectName("toolBar")
        
#         MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">Price Comparison Platform @ Paulfans </span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Price"))
        self.pushButton_2.setText(_translate("MainWindow", "Ratings"))
        self.pushButton_3.setText(_translate("MainWindow", "Comments Number"))
#         self.labellizixuan.setText(_translate("MainWindow", "TextLabel"))
#         self.label_4.setText(_translate("MainWindow", "TextLabel"))
#         self.label_5.setText(_translate("MainWindow", "TextLabel"))

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
        
#         self.toolBar.setWindowTitle(_translate("MainWindow"))

    def get_start_time(self,string):
        pattern=r'(\d{4})\,\s+(\d+),\s+(\d+),\s+(\d+),\s+(\d+)'
        c=re.search(pattern,string)
        if int(c.group(4))>9:
            d=str(c.group(1))+'-'+str(c.group(2))+'-'+str(c.group(3))+' '+str(c.group(4))+':'+'00:00'
        else:
            d=str(c.group(1))+'-'+str(c.group(2))+'-'+str(c.group(3))+' 0'+str(c.group(4))+':'+'00:00'
        return d

    def table(self,link,start_time):
        database_df = pd.read_csv('database.csv',index_col=['Unnamed: 0'])
        try:
            select_df = database_df[database_df['time']>=start_time]
            try:
                # get productID based on link
                productID = database_df['productID'][database_df['link'] == link][0]
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
                productID = database_df['productID'][database_df['link'] == link][0]
                select_df = select_df[['time','platformID','price']][database_df['productID'] == productID]
                select_df = select_df.dropna(axis=0)
                # plot 
                plt.figure(figsize=(10,6))
                g = sns.pointplot(y = select_df['price'],x = select_df['time'],hue = select_df['platformID'],scale=0.4)
                g.set(xticks=[])
                plt.xlabel('time period')
                plt.savefig('price.jpg')
            except:
                raise ValueError('Invalid Link')
        except:
            raise ValueError('Invalid Time')
        pixmap = QPixmap('price.jpg')  ##从QtGui中新建一个QPixmap的类
        self.labellizixuan.setPixmap(pixmap)
        
        tablestring=self.table(link,start_time)
        
        

    def _showpic2(self):
        link = self.comboBox.currentText()
        start_time=self.get_start_time(str(self.dateTimeEdit.dateTime()))
        
        database_df = pd.read_csv('database.csv',index_col=['Unnamed: 0'])
    
        # define productID based on link
        try:
            select_df = database_df[database_df['time']>=start_time]
            try:
                # get productID based on link
                productID = database_df['productID'][database_df['link'] == link][0]
                select_df = select_df[['time','platformID','rating']][database_df['productID'] == productID]
                select_df = select_df.dropna(axis=0)
                # plot 
                plt.figure(figsize=(10,6))
                g = sns.pointplot(y = select_df['rating'],x = select_df['time'],hue = select_df['platformID'],scale=0.4)
                g.set(xticks=[])
                plt.xlabel('time period')
                plt.savefig('rating.jpg')
            except:
                raise ValueError('Invalid Link')
        except:
            raise ValueError('Invalid Time')

        pixmap = QPixmap('rating.jpg')  ##从QtGui中新建一个QPixmap的类
        self.labellizixuan.setPixmap(pixmap)
        self.table(link,start_time)

    def _showpic3(self):
        link = self.comboBox.currentText()
        start_time=self.get_start_time(str(self.dateTimeEdit.dateTime()))
        
        database_df = pd.read_csv('database.csv',index_col=['Unnamed: 0'])
        # define productID based on link
        try:
            select_df = database_df[database_df['time']>=start_time]
            try:
                # get productID based on link
                productID = database_df['productID'][database_df['link'] == link][0]
                select_df = select_df[['time','platformID','commentNum']][database_df['productID'] == productID]
                select_df = select_df.dropna(axis=0)
                # plot 
                plt.figure(figsize=(10,6))
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
'''    
    def _showpic1(self):
        url = 'https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg'   ##图片链接
        pic = requests.get(url).content  ##获取图片链接的数据
        pixmap = QtGui.QPixmap()  ##从QtGui中新建一个QPixmap的类
        pixmap.loadFromData(pic)  ##pixmap装载图片数据
        self.labellizixuan.setPixmap(pixmap)  ##最终在label上显示图片
    
    
    def _showpic2(self):
#          link=self.textEdit.toPlainText()
#          startTime=self.dateTimeEdit
#             if not link:
#                 raise Exception("No link!")
#             if not startTime:
#                 raise Exception("No startTime!")
        x=range(10)
        y=range(1,11)
        plt.plot(x,y)
        plt.savefig('test.jpg')
        #pic = requests.get(url).content  ##获取图片链接的数据
        pixmap = QPixmap('test.jpg')  ##从QtGui中新建一个QPixmap的类
        self.labellizixuan.setPixmap(pixmap)
    
        
#         #url = 'https://www.thewatchforum.co.uk/uploads/monthly_2016_02/article-2011051-0CDC0FBF00000578-21_306x526.jpg.2c5e44425b0d614bca1aa4c1b13335dc.thumb.jpg.dc6c7c306af14a3a4ba3e8a6e62de159.jpg'  
#         url = 'https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg'
#         pic = requests.get(url).content  
#         pixmap = QtGui.QPixmap()  
#         pixmap.loadFromData(pic) 
#         self.label_4.setPixmap(pixmap)
#         a = str(self.dateTimeEdit)
#         self.label_4.setText(a)
#         print(self.label_4.setText(a))
#     dateEdit = QDateTimeEdit(QDate.currentDate())
# dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))
# dateEdit.setMaximumDate(QDate.currentDate().addDays(365))
# dateEdit.setDisplayFormat("yyyy.MM.dd")
#https://doc.qt.io/qtforpython/PySide2/QtWidgets/QDateTimeEdit.html
    def _showpic3(self):
        var_name = self.dateTimeEdit.dateTime()
        self.labellizixuan.setText(str(var_name))
        
#         url = 'https://pic.pimg.tw/linvincent/4ada7576c7609.jpg'
#         #url = 'https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg'
#         pic = requests.get(url).content  
#         pixmap = QtGui.QPixmap()  
#         pixmap.loadFromData(pic)  
#         self.labellizixuan.setPixmap(pixmap)
'''     
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

