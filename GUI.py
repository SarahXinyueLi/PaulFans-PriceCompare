
# coding: utf-8

# In[ ]:


from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        #MainWindow.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 50, 261, 31))
        #self.textEdit.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 111, 31))
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(140, 100, 261, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
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
        self.pushButton_3.setGeometry(QtCore.QRect(390, 160, 114, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 601, 251))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 601, 251))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 601, 251))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.pushButton.clicked.connect(self._showpic1)
#         self.pushButton_2.clicked.connect(self._showpic2)
#         self.pushButton_3.clicked.connect(self._showpic3)
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
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
#         self.label_5.setText(_translate("MainWindow", "TextLabel"))
#         self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
    
    def _showpic1(self):
        url = 'https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg'   ##图片链接
        pic = requests.get(url).content  ##获取图片链接的数据
        pixmap = QtGui.QPixmap()  ##从QtGui中新建一个QPixmap的类
        pixmap.loadFromData(pic)  ##pixmap装载图片数据
        self.label_4.setPixmap(pixmap)  ##最终在label上显示图片
    
    
#     def _showpic2(self):
#         url = 'https://www.thewatchforum.co.uk/uploads/monthly_2016_02/article-2011051-0CDC0FBF00000578-21_306x526.jpg.2c5e44425b0d614bca1aa4c1b13335dc.thumb.jpg.dc6c7c306af14a3a4ba3e8a6e62de159.jpg'  
#         pic = requests.get(url).content  
#         pixmap = QtGui.QPixmap()  
#         pixmap.loadFromData(pic) 
#         self.label_5.setPixmap(pixmap)
    
#     def _showpic3(self):
#         url = 'https://pic.pimg.tw/linvincent/4ada7576c7609.jpg'
#         pixmap = QtGui.QPixmap()  
#         pixmap.loadFromData(pic)  
#         self.label_6.setPixmap(pixmap)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

