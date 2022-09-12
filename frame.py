# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from mhyt import yt_download
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(513, 451)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_download = QtWidgets.QPushButton(self.centralwidget)
        self.bt_download.setGeometry(QtCore.QRect(190, 350, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.bt_download.setFont(font)
        self.bt_download.setObjectName("bt_download")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 150, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 250, 61, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txt_link = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_link.setGeometry(QtCore.QRect(40, 180, 431, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txt_link.setFont(font)
        self.txt_link.setObjectName("txt_link")
        self.txt_rename = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_rename.setGeometry(QtCore.QRect(40, 280, 311, 25))
        self.txt_rename.setObjectName("txt_rename")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 230, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(260, 60, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Purisa")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, -30, 221, 141))
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(370, 270, 66, 72))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rb_mp3 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rb_mp3.setFont(font)
        self.rb_mp3.setChecked(True)
        self.rb_mp3.setObjectName("rb_mp3")
        self.verticalLayout_2.addWidget(self.rb_mp3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.rb_mp4 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rb_mp4.setFont(font)
        self.rb_mp4.setObjectName("rb_mp4")
        self.verticalLayout_2.addWidget(self.rb_mp4)
        self.label_5.raise_()
        self.bt_download.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.txt_link.raise_()
        self.txt_rename.raise_()
        self.rb_mp3.raise_()
        self.rb_mp4.raise_()
        self.rb_mp4.raise_()
        self.rb_mp4.raise_()
        self.rb_mp3.raise_()
        self.rb_mp3.raise_()
        self.rb_mp4.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 513, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ### Button for download
        self.bt_download.clicked.connect(self.download)

    
    def download(self):
        url = self.txt_link.text()
        title = self.txt_rename.text()
        if self.rb_mp4.isChecked() == True:
            title_mp4 = title + ".mp4"
            yt_download(url,title_mp4)
        elif self.rb_mp3.isChecked() == True:
            title_mp3 = title + ".mp3"
            try:
                yt_download(url,title_mp3,ismusic=True, codec = "mp3")
            except:
                pass

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_download.setText(_translate("MainWindow", "Download"))
        self.label.setText(_translate("MainWindow", "Link:"))
        self.label_2.setText(_translate("MainWindow", "Rename:"))
        self.txt_link.setText(_translate("MainWindow", "https://www.youtube.com/watch?v=S9Um3d8pRZE"))
        self.txt_rename.setText(_translate("MainWindow", "file_name"))
        self.label_3.setText(_translate("MainWindow", "Type"))
        self.label_4.setText(_translate("MainWindow", "Download"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/youtube/youtube_download.png\"/></p></body></html>"))
        self.rb_mp3.setText(_translate("MainWindow", "mp3"))
        self.rb_mp4.setText(_translate("MainWindow", "mp4"))


### images
import youtube_image

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

