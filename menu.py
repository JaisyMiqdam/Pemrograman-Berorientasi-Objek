# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MENU(object):
    def setupUi(self, MENU):
        MENU.setObjectName("MENU")
        MENU.resize(713, 586)
        MENU.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(80, 80, 122);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"    background-color: rgb(157, 0, 0);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {    \n"
"    background-color: rgb(157, 0, 0);\n"
"\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(59, 59, 90);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {    \n"
"    background-color: rgb(157, 0, 0);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {    \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MENU)
        self.centralwidget.setStyleSheet("background-color: black;")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setStyleSheet(" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(56, 56, 85);\n"
" }")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 681, 1218))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(600, 1200))
        self.frame.setStyleSheet("background-color: rgb(90, 90, 90);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(-20, -10, 751, 91))
        self.label_4.setStyleSheet("background-color: black;\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 20, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QPushButton#searchButton {\n"
"    padding: 10px 20px;\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: #FFFFFF;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton#searchButton:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton#searchButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton#searchButton:focus {\n"
"    outline: none;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(-30, 80, 770, 31))
        self.label_14.setStyleSheet("background-color: red")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.FILMTERBARU = QtWidgets.QLabel(self.frame)
        self.FILMTERBARU.setGeometry(QtCore.QRect(40, 118, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.FILMTERBARU.setFont(font)
        self.FILMTERBARU.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.FILMTERBARU.setObjectName("FILMTERBARU")
        self.MERAH1 = QtWidgets.QLabel(self.frame)
        self.MERAH1.setGeometry(QtCore.QRect(30, 120, 600, 20))
        self.MERAH1.setAutoFillBackground(False)
        self.MERAH1.setStyleSheet("background-color: red;\n"
"    border-radius: 10px;\n"
"    padding: 5px;")
        self.MERAH1.setText("")
        self.MERAH1.setObjectName("MERAH1")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 671, 1091))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.HD1 = QtWidgets.QLabel(self.frame)
        self.HD1.setGeometry(QtCore.QRect(168, 170, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD1.setFont(font)
        self.HD1.setAutoFillBackground(False)
        self.HD1.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD1.setObjectName("HD1")
        self.HD2 = QtWidgets.QLabel(self.frame)
        self.HD2.setGeometry(QtCore.QRect(367, 170, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD2.setFont(font)
        self.HD2.setAutoFillBackground(False)
        self.HD2.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD2.setObjectName("HD2")
        self.HD3 = QtWidgets.QLabel(self.frame)
        self.HD3.setGeometry(QtCore.QRect(567, 170, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD3.setFont(font)
        self.HD3.setAutoFillBackground(False)
        self.HD3.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD3.setObjectName("HD3")
        self.FILM2 = QtWidgets.QLabel(self.frame)
        self.FILM2.setGeometry(QtCore.QRect(265, 160, 131, 181))
        self.FILM2.setText("")
        self.FILM2.setPixmap(QtGui.QPixmap(":/images/film2.png"))
        self.FILM2.setScaledContents(True)
        self.FILM2.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM2.setObjectName("FILM2")
        self.FILM3 = QtWidgets.QLabel(self.frame)
        self.FILM3.setGeometry(QtCore.QRect(465, 160, 131, 181))
        self.FILM3.setText("")
        self.FILM3.setPixmap(QtGui.QPixmap(":/images/film3.png"))
        self.FILM3.setScaledContents(True)
        self.FILM3.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM3.setObjectName("FILM3")
        self.ABU1 = QtWidgets.QLabel(self.frame)
        self.ABU1.setGeometry(QtCore.QRect(30, 150, 600, 230))
        self.ABU1.setAutoFillBackground(False)
        self.ABU1.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);\n"
"    color: #000000;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 10px;")
        self.ABU1.setText("")
        self.ABU1.setObjectName("ABU1")
        self.JUDUL1 = QtWidgets.QLabel(self.frame)
        self.JUDUL1.setGeometry(QtCore.QRect(79, 344, 105, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL1.setFont(font)
        self.JUDUL1.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL1.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL1.setObjectName("JUDUL1")
        self.JUDUL2 = QtWidgets.QLabel(self.frame)
        self.JUDUL2.setGeometry(QtCore.QRect(278, 344, 105, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL2.setFont(font)
        self.JUDUL2.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL2.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL2.setObjectName("JUDUL2")
        self.JUDUL3 = QtWidgets.QLabel(self.frame)
        self.JUDUL3.setGeometry(QtCore.QRect(480, 344, 105, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL3.setFont(font)
        self.JUDUL3.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL3.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL3.setObjectName("JUDUL3")
        self.TRENDING = QtWidgets.QLabel(self.frame)
        self.TRENDING.setGeometry(QtCore.QRect(40, 388, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.TRENDING.setFont(font)
        self.TRENDING.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.TRENDING.setObjectName("TRENDING")
        self.MERAH2 = QtWidgets.QLabel(self.frame)
        self.MERAH2.setGeometry(QtCore.QRect(30, 390, 600, 20))
        self.MERAH2.setAutoFillBackground(False)
        self.MERAH2.setStyleSheet("background-color: red;\n"
"    border-radius: 10px;\n"
"    padding: 5px;")
        self.MERAH2.setText("")
        self.MERAH2.setObjectName("MERAH2")
        self.ABU2 = QtWidgets.QLabel(self.frame)
        self.ABU2.setGeometry(QtCore.QRect(30, 420, 600, 230))
        self.ABU2.setAutoFillBackground(False)
        self.ABU2.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);\n"
"    color: #000000;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 10px;")
        self.ABU2.setText("")
        self.ABU2.setObjectName("ABU2")
        self.ABU3 = QtWidgets.QLabel(self.frame)
        self.ABU3.setGeometry(QtCore.QRect(30, 690, 600, 230))
        self.ABU3.setAutoFillBackground(False)
        self.ABU3.setStyleSheet("background-color: rgba(255, 255, 255, 0.2);\n"
"    color: #000000;\n"
"    border: none;\n"
"    padding: 10px;\n"
"    border-radius: 10px;")
        self.ABU3.setText("")
        self.ABU3.setObjectName("ABU3")
        self.MERAH3 = QtWidgets.QLabel(self.frame)
        self.MERAH3.setGeometry(QtCore.QRect(30, 660, 600, 20))
        self.MERAH3.setAutoFillBackground(False)
        self.MERAH3.setStyleSheet("background-color: red;\n"
"    border-radius: 10px;\n"
"    padding: 5px;")
        self.MERAH3.setText("")
        self.MERAH3.setObjectName("MERAH3")
        self.GARIS_6 = QtWidgets.QLabel(self.frame)
        self.GARIS_6.setGeometry(QtCore.QRect(-60, 956, 751, 5))
        self.GARIS_6.setAutoFillBackground(False)
        self.GARIS_6.setStyleSheet("background-color: red;\n"
"    border-radius: 10px;\n"
"    padding: 5px;")
        self.GARIS_6.setText("")
        self.GARIS_6.setObjectName("GARIS_6")
        self.CR = QtWidgets.QLabel(self.frame)
        self.CR.setGeometry(QtCore.QRect(0, 1140, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.CR.setFont(font)
        self.CR.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 0);\n"
"")
        self.CR.setAlignment(QtCore.Qt.AlignCenter)
        self.CR.setObjectName("CR")
        self.JUDUL6 = QtWidgets.QLabel(self.frame)
        self.JUDUL6.setGeometry(QtCore.QRect(479, 614, 105, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL6.setFont(font)
        self.JUDUL6.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL6.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL6.setObjectName("JUDUL6")
        self.HD5 = QtWidgets.QLabel(self.frame)
        self.HD5.setGeometry(QtCore.QRect(367, 440, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD5.setFont(font)
        self.HD5.setAutoFillBackground(False)
        self.HD5.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD5.setObjectName("HD5")
        self.HD6 = QtWidgets.QLabel(self.frame)
        self.HD6.setGeometry(QtCore.QRect(567, 440, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD6.setFont(font)
        self.HD6.setAutoFillBackground(False)
        self.HD6.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD6.setObjectName("HD6")
        self.FILM6 = QtWidgets.QLabel(self.frame)
        self.FILM6.setGeometry(QtCore.QRect(465, 430, 131, 181))
        self.FILM6.setText("")
        self.FILM6.setPixmap(QtGui.QPixmap(":/images/film6.png"))
        self.FILM6.setScaledContents(True)
        self.FILM6.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM6.setObjectName("FILM6")
        self.HD4 = QtWidgets.QLabel(self.frame)
        self.HD4.setGeometry(QtCore.QRect(168, 440, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD4.setFont(font)
        self.HD4.setAutoFillBackground(False)
        self.HD4.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD4.setObjectName("HD4")
        self.JUDUL4 = QtWidgets.QLabel(self.frame)
        self.JUDUL4.setGeometry(QtCore.QRect(78, 610, 105, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL4.setFont(font)
        self.JUDUL4.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL4.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL4.setObjectName("JUDUL4")
        self.JUDUL5 = QtWidgets.QLabel(self.frame)
        self.JUDUL5.setGeometry(QtCore.QRect(277, 610, 105, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL5.setFont(font)
        self.JUDUL5.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL5.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL5.setObjectName("JUDUL5")
        self.FILM5 = QtWidgets.QLabel(self.frame)
        self.FILM5.setGeometry(QtCore.QRect(265, 430, 131, 181))
        self.FILM5.setText("")
        self.FILM5.setPixmap(QtGui.QPixmap(":/images/film5.png"))
        self.FILM5.setScaledContents(True)
        self.FILM5.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM5.setObjectName("FILM5")
        self.FILM4 = QtWidgets.QLabel(self.frame)
        self.FILM4.setGeometry(QtCore.QRect(66, 430, 131, 181))
        self.FILM4.setText("")
        self.FILM4.setPixmap(QtGui.QPixmap(":/images/film4.png"))
        self.FILM4.setScaledContents(True)
        self.FILM4.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM4.setObjectName("FILM4")
        self.DESK = QtWidgets.QLabel(self.frame)
        self.DESK.setGeometry(QtCore.QRect(10, 990, 641, 141))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DESK.setFont(font)
        self.DESK.setStyleSheet("color: white; background-color: rgba(0, 0, 0, 0);\n"
"")
        self.DESK.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.DESK.setWordWrap(False)
        self.DESK.setObjectName("DESK")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(40, 85, 51, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAutoFillBackground(False)
        self.label_20.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);")
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(160, 85, 61, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(423, 85, 51, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_21.setAutoFillBackground(False)
        self.label_21.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);")
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(530, 85, 101, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.LOGO = QtWidgets.QPushButton(self.frame)
        self.LOGO.setGeometry(QtCore.QRect(1, -10, 111, 91))
        self.LOGO.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"")
        self.LOGO.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LOGO.setIcon(icon)
        self.LOGO.setIconSize(QtCore.QSize(100, 100))
        self.LOGO.setObjectName("LOGO")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(290, 85, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.TRENDING_2 = QtWidgets.QLabel(self.frame)
        self.TRENDING_2.setGeometry(QtCore.QRect(40, 658, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.TRENDING_2.setFont(font)
        self.TRENDING_2.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.TRENDING_2.setObjectName("TRENDING_2")
        self.FILM5_2 = QtWidgets.QLabel(self.frame)
        self.FILM5_2.setGeometry(QtCore.QRect(265, 700, 131, 181))
        self.FILM5_2.setText("")
        self.FILM5_2.setPixmap(QtGui.QPixmap(":/images/film8.png"))
        self.FILM5_2.setScaledContents(True)
        self.FILM5_2.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM5_2.setObjectName("FILM5_2")
        self.FILM6_2 = QtWidgets.QLabel(self.frame)
        self.FILM6_2.setGeometry(QtCore.QRect(465, 700, 131, 181))
        self.FILM6_2.setText("")
        self.FILM6_2.setPixmap(QtGui.QPixmap(":/images/film9.png"))
        self.FILM6_2.setScaledContents(True)
        self.FILM6_2.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM6_2.setObjectName("FILM6_2")
        self.JUDUL6_2 = QtWidgets.QLabel(self.frame)
        self.JUDUL6_2.setGeometry(QtCore.QRect(478, 884, 105, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL6_2.setFont(font)
        self.JUDUL6_2.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL6_2.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL6_2.setObjectName("JUDUL6_2")
        self.HD6_2 = QtWidgets.QLabel(self.frame)
        self.HD6_2.setGeometry(QtCore.QRect(567, 710, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD6_2.setFont(font)
        self.HD6_2.setAutoFillBackground(False)
        self.HD6_2.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD6_2.setObjectName("HD6_2")
        self.JUDUL4_2 = QtWidgets.QLabel(self.frame)
        self.JUDUL4_2.setGeometry(QtCore.QRect(79, 880, 105, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL4_2.setFont(font)
        self.JUDUL4_2.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL4_2.setObjectName("JUDUL4_2")
        self.FILM4_2 = QtWidgets.QLabel(self.frame)
        self.FILM4_2.setGeometry(QtCore.QRect(66, 700, 131, 181))
        self.FILM4_2.setText("")
        self.FILM4_2.setPixmap(QtGui.QPixmap(":/images/film7.png"))
        self.FILM4_2.setScaledContents(True)
        self.FILM4_2.setAlignment(QtCore.Qt.AlignCenter)
        self.FILM4_2.setObjectName("FILM4_2")
        self.HD5_2 = QtWidgets.QLabel(self.frame)
        self.HD5_2.setGeometry(QtCore.QRect(367, 710, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD5_2.setFont(font)
        self.HD5_2.setAutoFillBackground(False)
        self.HD5_2.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD5_2.setObjectName("HD5_2")
        self.JUDUL5_2 = QtWidgets.QLabel(self.frame)
        self.JUDUL5_2.setGeometry(QtCore.QRect(278, 880, 105, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.JUDUL5_2.setFont(font)
        self.JUDUL5_2.setStyleSheet("color: red;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.JUDUL5_2.setAlignment(QtCore.Qt.AlignCenter)
        self.JUDUL5_2.setObjectName("JUDUL5_2")
        self.HD4_2 = QtWidgets.QLabel(self.frame)
        self.HD4_2.setGeometry(QtCore.QRect(168, 710, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.HD4_2.setFont(font)
        self.HD4_2.setAutoFillBackground(False)
        self.HD4_2.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.HD4_2.setObjectName("HD4_2")
        self.LIHATSEMUA = QtWidgets.QPushButton(self.frame)
        self.LIHATSEMUA.setGeometry(QtCore.QRect(517, 117, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.LIHATSEMUA.setFont(font)
        self.LIHATSEMUA.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.LIHATSEMUA.setObjectName("LIHATSEMUA")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 387, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 657, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.LOGOUT = QtWidgets.QPushButton(self.frame)
        self.LOGOUT.setGeometry(QtCore.QRect(625, 25, 30, 25))
        self.LOGOUT.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.LOGOUT.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LOGOUT.setIcon(icon1)
        self.LOGOUT.setIconSize(QtCore.QSize(20, 20))
        self.LOGOUT.setObjectName("LOGOUT")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(371, 28, 25, 15))
        self.label_17.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/images/faq.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.FAQ_7 = QtWidgets.QLabel(self.frame)
        self.FAQ_7.setGeometry(QtCore.QRect(470, 23, 51, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.FAQ_7.setFont(font)
        self.FAQ_7.setAutoFillBackground(False)
        self.FAQ_7.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.FAQ_7.setObjectName("FAQ_7")
        self.FAQ_6 = QtWidgets.QLabel(self.frame)
        self.FAQ_6.setGeometry(QtCore.QRect(550, 23, 71, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.FAQ_6.setFont(font)
        self.FAQ_6.setAutoFillBackground(False)
        self.FAQ_6.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.FAQ_6.setObjectName("FAQ_6")
        self.FAQ_5 = QtWidgets.QLabel(self.frame)
        self.FAQ_5.setGeometry(QtCore.QRect(401, 22, 31, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.FAQ_5.setFont(font)
        self.FAQ_5.setAutoFillBackground(False)
        self.FAQ_5.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.FAQ_5.setObjectName("FAQ_5")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(444, 27, 24, 16))
        self.label_18.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap(":/images/gembok.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(522, 29, 25, 15))
        self.label_19.setStyleSheet("color: white;\n"
"background-color: rgba(0, 0, 0, 0);\n"
"")
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap(":/images/list.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.FILM1 = QtWidgets.QPushButton(self.frame)
        self.FILM1.setGeometry(QtCore.QRect(64, 160, 141, 181))
        self.FILM1.setStyleSheet("color: white;background-color: rgba(0, 0, 0, 0);\n"
"")
        self.FILM1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/film1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FILM1.setIcon(icon2)
        self.FILM1.setIconSize(QtCore.QSize(200, 200))
        self.FILM1.setObjectName("FILM1")
        self.label_14.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.lineEdit_2.raise_()
        self.MERAH1.raise_()
        self.FILMTERBARU.raise_()
        self.MERAH2.raise_()
        self.TRENDING.raise_()
        self.ABU2.raise_()
        self.ABU3.raise_()
        self.MERAH3.raise_()
        self.ABU1.raise_()
        self.FILM2.raise_()
        self.FILM3.raise_()
        self.HD3.raise_()
        self.HD2.raise_()
        self.JUDUL1.raise_()
        self.JUDUL3.raise_()
        self.JUDUL2.raise_()
        self.GARIS_6.raise_()
        self.CR.raise_()
        self.JUDUL6.raise_()
        self.FILM6.raise_()
        self.JUDUL4.raise_()
        self.JUDUL5.raise_()
        self.FILM5.raise_()
        self.FILM4.raise_()
        self.HD4.raise_()
        self.HD5.raise_()
        self.HD6.raise_()
        self.DESK.raise_()
        self.label_20.raise_()
        self.label_7.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.LOGO.raise_()
        self.label_8.raise_()
        self.TRENDING_2.raise_()
        self.FILM5_2.raise_()
        self.FILM6_2.raise_()
        self.JUDUL6_2.raise_()
        self.HD6_2.raise_()
        self.JUDUL4_2.raise_()
        self.FILM4_2.raise_()
        self.HD5_2.raise_()
        self.JUDUL5_2.raise_()
        self.HD4_2.raise_()
        self.LIHATSEMUA.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.LOGOUT.raise_()
        self.label_17.raise_()
        self.FAQ_7.raise_()
        self.FAQ_6.raise_()
        self.FAQ_5.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.FILM1.raise_()
        self.HD1.raise_()
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MENU.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MENU)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 21))
        self.menubar.setObjectName("menubar")
        MENU.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MENU)
        self.statusbar.setObjectName("statusbar")
        MENU.setStatusBar(self.statusbar)

        self.retranslateUi(MENU)
        QtCore.QMetaObject.connectSlotsByName(MENU)

    def retranslateUi(self, MENU):
        _translate = QtCore.QCoreApplication.translate
        MENU.setWindowTitle(_translate("MENU", "MainWindow"))
        self.lineEdit_2.setPlaceholderText(_translate("MENU", "  Search Movies"))
        self.FILMTERBARU.setText(_translate("MENU", "FILM TERBARU"))
        self.label.setText(_translate("MENU", "TextLabel"))
        self.HD1.setText(_translate("MENU", "HD"))
        self.HD2.setText(_translate("MENU", "HD"))
        self.HD3.setText(_translate("MENU", "HD"))
        self.JUDUL1.setText(_translate("MENU", "Black Clover:\n"
"Sword of the\n"
"Wizard King"))
        self.JUDUL2.setText(_translate("MENU", "Transformers:\n"
"Rise of the\n"
"Beasts (2023)"))
        self.JUDUL3.setText(_translate("MENU", "Fast X (2023)"))
        self.TRENDING.setText(_translate("MENU", "TRENDING"))
        self.CR.setText(_translate("MENU", "Copyright @2021 CNNXXI - All Rights Reserved Disclaimer: This site does not store any files\n"
" on its server. All contents are provided by non-affiliated third parties and make money online"))
        self.JUDUL6.setText(_translate("MENU", "Spider-Man:\n"
"Across the\n"
"Spider-Verse (2023)"))
        self.HD5.setText(_translate("MENU", "HD"))
        self.HD6.setText(_translate("MENU", "HD"))
        self.HD4.setText(_translate("MENU", "HD"))
        self.JUDUL4.setText(_translate("MENU", "Flash Over\n"
"(2023)"))
        self.JUDUL5.setText(_translate("MENU", "Extraction 2\n"
"(2023)"))
        self.DESK.setText(_translate("MENU", "YOUPET Streaming Film dan TV Series Subtitle Indonesia\n"
"YOUPET adalah situs web nonton streaming online download film terbaru film asia\n"
"terbaru, film barat terbaru secara gratis dan lengkap. Disini tersedia banyak\n"
"kualitas video seperti bluray, web-dl, hd, dvdrip, hdrip dan hdcam. Format video\n"
"yang kami sediakan ada mp4 mkv serta berbagai macam resolusi seperti 360p, 480p,\n"
"720p dan 1080p. Semua film yang tersedia di situs ini hanya untuk review saja.\n"
"Jika anda ingin menonton filmdengan kualitas yang lebih baik, silahkan beli DVD\n"
"resminya."))
        self.label_20.setText(_translate("MENU", "HOME"))
        self.label_7.setText(_translate("MENU", "GENRE"))
        self.label_21.setText(_translate("MENU", "YEAR"))
        self.label_22.setText(_translate("MENU", "BOX OFFICE"))
        self.label_8.setText(_translate("MENU", "COUNTRY"))
        self.TRENDING_2.setText(_translate("MENU", "DRAMA KOREA"))
        self.JUDUL6_2.setText(_translate("MENU", "Hansan: Rising\n"
"Dragon (2022)"))
        self.HD6_2.setText(_translate("MENU", "HD"))
        self.JUDUL4_2.setText(_translate("MENU", "Project Wolf\n"
"Hunting (2022)"))
        self.HD5_2.setText(_translate("MENU", "HD"))
        self.JUDUL5_2.setText(_translate("MENU", "B Cut (2022)"))
        self.HD4_2.setText(_translate("MENU", "HD"))
        self.LIHATSEMUA.setText(_translate("MENU", "LIHAT SEMUA >"))
        self.pushButton_2.setText(_translate("MENU", "LIHAT SEMUA >"))
        self.pushButton_3.setText(_translate("MENU", "LIHAT SEMUA >"))
        self.FAQ_7.setText(_translate("MENU", "DMCA"))
        self.FAQ_6.setText(_translate("MENU", "SITEMAP"))
        self.FAQ_5.setText(_translate("MENU", "FAQ"))
import res_rc
