# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 207)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.lw_1m_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_1m_btn.sizePolicy().hasHeightForWidth())
        self.lw_1m_btn.setSizePolicy(sizePolicy)
        self.lw_1m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lw_1m_btn.setFont(font)
        self.lw_1m_btn.setObjectName("lw_1m_btn")
        self.verticalLayout_4.addWidget(self.lw_1m_btn)
        self.lw_2m_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_2m_btn.sizePolicy().hasHeightForWidth())
        self.lw_2m_btn.setSizePolicy(sizePolicy)
        self.lw_2m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lw_2m_btn.setFont(font)
        self.lw_2m_btn.setObjectName("lw_2m_btn")
        self.verticalLayout_4.addWidget(self.lw_2m_btn)
        self.lw_3m_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_3m_btn.sizePolicy().hasHeightForWidth())
        self.lw_3m_btn.setSizePolicy(sizePolicy)
        self.lw_3m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lw_3m_btn.setFont(font)
        self.lw_3m_btn.setObjectName("lw_3m_btn")
        self.verticalLayout_4.addWidget(self.lw_3m_btn)
        self.lw_safe_btn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lw_safe_btn.sizePolicy().hasHeightForWidth())
        self.lw_safe_btn.setSizePolicy(sizePolicy)
        self.lw_safe_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lw_safe_btn.setFont(font)
        self.lw_safe_btn.setObjectName("lw_safe_btn")
        self.verticalLayout_4.addWidget(self.lw_safe_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.rw_1m_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rw_1m_btn.sizePolicy().hasHeightForWidth())
        self.rw_1m_btn.setSizePolicy(sizePolicy)
        self.rw_1m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rw_1m_btn.setFont(font)
        self.rw_1m_btn.setObjectName("rw_1m_btn")
        self.verticalLayout_5.addWidget(self.rw_1m_btn)
        self.rw_2m_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rw_2m_btn.sizePolicy().hasHeightForWidth())
        self.rw_2m_btn.setSizePolicy(sizePolicy)
        self.rw_2m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rw_2m_btn.setFont(font)
        self.rw_2m_btn.setObjectName("rw_2m_btn")
        self.verticalLayout_5.addWidget(self.rw_2m_btn)
        self.rw_3m_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rw_3m_btn.sizePolicy().hasHeightForWidth())
        self.rw_3m_btn.setSizePolicy(sizePolicy)
        self.rw_3m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rw_3m_btn.setFont(font)
        self.rw_3m_btn.setObjectName("rw_3m_btn")
        self.verticalLayout_5.addWidget(self.rw_3m_btn)
        self.rw_safe_btn = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rw_safe_btn.sizePolicy().hasHeightForWidth())
        self.rw_safe_btn.setSizePolicy(sizePolicy)
        self.rw_safe_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rw_safe_btn.setFont(font)
        self.rw_safe_btn.setObjectName("rw_safe_btn")
        self.verticalLayout_5.addWidget(self.rw_safe_btn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_6.setSpacing(12)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.ls_1m_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ls_1m_btn.sizePolicy().hasHeightForWidth())
        self.ls_1m_btn.setSizePolicy(sizePolicy)
        self.ls_1m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ls_1m_btn.setFont(font)
        self.ls_1m_btn.setObjectName("ls_1m_btn")
        self.verticalLayout_6.addWidget(self.ls_1m_btn)
        self.ls_2m_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ls_2m_btn.sizePolicy().hasHeightForWidth())
        self.ls_2m_btn.setSizePolicy(sizePolicy)
        self.ls_2m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ls_2m_btn.setFont(font)
        self.ls_2m_btn.setObjectName("ls_2m_btn")
        self.verticalLayout_6.addWidget(self.ls_2m_btn)
        self.ls_3m_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ls_3m_btn.sizePolicy().hasHeightForWidth())
        self.ls_3m_btn.setSizePolicy(sizePolicy)
        self.ls_3m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ls_3m_btn.setFont(font)
        self.ls_3m_btn.setObjectName("ls_3m_btn")
        self.verticalLayout_6.addWidget(self.ls_3m_btn)
        self.ls_safe_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ls_safe_btn.sizePolicy().hasHeightForWidth())
        self.ls_safe_btn.setSizePolicy(sizePolicy)
        self.ls_safe_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ls_safe_btn.setFont(font)
        self.ls_safe_btn.setObjectName("ls_safe_btn")
        self.verticalLayout_6.addWidget(self.ls_safe_btn)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_7.setSpacing(12)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.rs_1m_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rs_1m_btn.sizePolicy().hasHeightForWidth())
        self.rs_1m_btn.setSizePolicy(sizePolicy)
        self.rs_1m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rs_1m_btn.setFont(font)
        self.rs_1m_btn.setObjectName("rs_1m_btn")
        self.verticalLayout_7.addWidget(self.rs_1m_btn)
        self.rs_2m_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rs_2m_btn.sizePolicy().hasHeightForWidth())
        self.rs_2m_btn.setSizePolicy(sizePolicy)
        self.rs_2m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rs_2m_btn.setFont(font)
        self.rs_2m_btn.setObjectName("rs_2m_btn")
        self.verticalLayout_7.addWidget(self.rs_2m_btn)
        self.rs_3m_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rs_3m_btn.sizePolicy().hasHeightForWidth())
        self.rs_3m_btn.setSizePolicy(sizePolicy)
        self.rs_3m_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rs_3m_btn.setFont(font)
        self.rs_3m_btn.setObjectName("rs_3m_btn")
        self.verticalLayout_7.addWidget(self.rs_3m_btn)
        self.rs_safe_btn = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rs_safe_btn.sizePolicy().hasHeightForWidth())
        self.rs_safe_btn.setSizePolicy(sizePolicy)
        self.rs_safe_btn.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rs_safe_btn.setFont(font)
        self.rs_safe_btn.setObjectName("rs_safe_btn")
        self.verticalLayout_7.addWidget(self.rs_safe_btn)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout.addWidget(self.frame_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Левое крыло"))
        self.lw_1m_btn.setText(_translate("MainWindow", "1 метр"))
        self.lw_2m_btn.setText(_translate("MainWindow", "2 метра"))
        self.lw_3m_btn.setText(_translate("MainWindow", "3 метра"))
        self.lw_safe_btn.setText(_translate("MainWindow", "Безопасное расстояние"))
        self.label_2.setText(_translate("MainWindow", "Правое крыло"))
        self.rw_1m_btn.setText(_translate("MainWindow", "1 метр"))
        self.rw_2m_btn.setText(_translate("MainWindow", "2 метра"))
        self.rw_3m_btn.setText(_translate("MainWindow", "3 метра"))
        self.rw_safe_btn.setText(_translate("MainWindow", "Безопасное расстояние"))
        self.label_3.setText(_translate("MainWindow", "Левый стабилизатор"))
        self.ls_1m_btn.setText(_translate("MainWindow", "1 метр"))
        self.ls_2m_btn.setText(_translate("MainWindow", "2 метра"))
        self.ls_3m_btn.setText(_translate("MainWindow", "3 метра"))
        self.ls_safe_btn.setText(_translate("MainWindow", "Безопасное расстояние"))
        self.label_4.setText(_translate("MainWindow", "Правый стабилизатор"))
        self.rs_1m_btn.setText(_translate("MainWindow", "1 метр"))
        self.rs_2m_btn.setText(_translate("MainWindow", "2 метра"))
        self.rs_3m_btn.setText(_translate("MainWindow", "3 метра"))
        self.rs_safe_btn.setText(_translate("MainWindow", "Безопасное расстояние"))
