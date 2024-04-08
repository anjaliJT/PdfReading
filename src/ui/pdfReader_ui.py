# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\ui\pdfReader.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1013, 768)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/stationery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QSplitter::handle {\n"
"    background: gray;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"\n"
"    background-color: transparent;\n"
"\n"
" }\n"
"\n"
"/*  QLineEdit{\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"QPlainTextEdit{\n"
"\n"
"background-color: rgb(255, 255, 255);}\n"
"\n"
"*/")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: rgb(230, 230, 230);")
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(-1, -1, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.focus_music_bttn = QtWidgets.QPushButton(self.widget)
        self.focus_music_bttn.setMinimumSize(QtCore.QSize(30, 30))
        self.focus_music_bttn.setMaximumSize(QtCore.QSize(100, 100))
        self.focus_music_bttn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.focus_music_bttn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/musical-note.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.focus_music_bttn.setIcon(icon1)
        self.focus_music_bttn.setIconSize(QtCore.QSize(50, 50))
        self.focus_music_bttn.setFlat(True)
        self.focus_music_bttn.setObjectName("focus_music_bttn")
        self.gridLayout_5.addWidget(self.focus_music_bttn, 0, 2, 1, 1)
        self.add_pdf_bttn = QtWidgets.QPushButton(self.widget)
        self.add_pdf_bttn.setMinimumSize(QtCore.QSize(30, 30))
        self.add_pdf_bttn.setMaximumSize(QtCore.QSize(100, 100))
        self.add_pdf_bttn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_pdf_bttn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/book.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_pdf_bttn.setIcon(icon2)
        self.add_pdf_bttn.setIconSize(QtCore.QSize(50, 50))
        self.add_pdf_bttn.setAutoRepeat(True)
        self.add_pdf_bttn.setFlat(True)
        self.add_pdf_bttn.setObjectName("add_pdf_bttn")
        self.gridLayout_5.addWidget(self.add_pdf_bttn, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 4, 1, 1)
        self.remove_pdf_bttn = QtWidgets.QPushButton(self.widget)
        self.remove_pdf_bttn.setMinimumSize(QtCore.QSize(30, 30))
        self.remove_pdf_bttn.setMaximumSize(QtCore.QSize(100, 100))
        self.remove_pdf_bttn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.remove_pdf_bttn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Images/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_pdf_bttn.setIcon(icon3)
        self.remove_pdf_bttn.setIconSize(QtCore.QSize(50, 50))
        self.remove_pdf_bttn.setFlat(True)
        self.remove_pdf_bttn.setObjectName("remove_pdf_bttn")
        self.gridLayout_5.addWidget(self.remove_pdf_bttn, 0, 1, 1, 1)
        self.focus_time_bttn = QtWidgets.QPushButton(self.widget)
        self.focus_time_bttn.setMinimumSize(QtCore.QSize(30, 30))
        self.focus_time_bttn.setMaximumSize(QtCore.QSize(100, 100))
        self.focus_time_bttn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.focus_time_bttn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Images/hourglass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.focus_time_bttn.setIcon(icon4)
        self.focus_time_bttn.setIconSize(QtCore.QSize(50, 50))
        self.focus_time_bttn.setFlat(True)
        self.focus_time_bttn.setObjectName("focus_time_bttn")
        self.gridLayout_5.addWidget(self.focus_time_bttn, 0, 3, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.widget_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.widget_pdf = QtWidgets.QWidget(self.splitter)
        self.widget_pdf.setObjectName("widget_pdf")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_pdf)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.widget_pdf)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setChildrenCollapsible(True)
        self.splitter_2.setObjectName("splitter_2")
        self.listWidget = QtWidgets.QListWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMinimumSize(QtCore.QSize(100, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setTabKeyNavigation(True)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(True)
        self.listWidget.setObjectName("listWidget")
        self.widget_4 = QtWidgets.QWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setStyleSheet("background-color: rgb(202, 255, 187);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.search_widget = QtWidgets.QWidget(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_widget.sizePolicy().hasHeightForWidth())
        self.search_widget.setSizePolicy(sizePolicy)
        self.search_widget.setMinimumSize(QtCore.QSize(100, 0))
        self.search_widget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.search_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_widget.setObjectName("search_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.search_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.search_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_4.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.search_bttn = QtWidgets.QPushButton(self.search_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_bttn.sizePolicy().hasHeightForWidth())
        self.search_bttn.setSizePolicy(sizePolicy)
        self.search_bttn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_bttn.setStyleSheet("background-color:transparent;")
        self.search_bttn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Images/find.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_bttn.setIcon(icon5)
        self.search_bttn.setIconSize(QtCore.QSize(20, 20))
        self.search_bttn.setObjectName("search_bttn")
        self.gridLayout_4.addWidget(self.search_bttn, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.search_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 2)
        self.gridLayout_2.addWidget(self.splitter_2, 0, 1, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.splitter)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.focus_music_bttn.setToolTip(_translate("MainWindow", "Focus music"))
        self.add_pdf_bttn.setToolTip(_translate("MainWindow", "Add Pdf"))
        self.remove_pdf_bttn.setToolTip(_translate("MainWindow", "Remove Pdf"))
        self.focus_time_bttn.setToolTip(_translate("MainWindow", "Focus timer"))
from Images import res_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
