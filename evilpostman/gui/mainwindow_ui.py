# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/afar/Modifing_Packets_On-The-Fly_In_SCAPY/evilpostman/gui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_widget.setEnabled(True)
        self.tab_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.tab_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab_widget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tab_widget.setMouseTracking(False)
        self.tab_widget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab_widget.setElideMode(QtCore.Qt.ElideNone)
        self.tab_widget.setObjectName("tab_widget")
        self.info_tab = QtWidgets.QWidget()
        self.info_tab.setObjectName("info_tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.info_tab)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.info_label_instruction = QtWidgets.QLabel(self.info_tab)
        self.info_label_instruction.setMinimumSize(QtCore.QSize(0, 0))
        self.info_label_instruction.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.info_label_instruction.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.info_label_instruction.setWordWrap(True)
        self.info_label_instruction.setObjectName("info_label_instruction")
        self.gridLayout_6.addWidget(self.info_label_instruction, 2, 0, 1, 1)
        self.info_button_next = QtWidgets.QPushButton(self.info_tab)
        self.info_button_next.setObjectName("info_button_next")
        self.gridLayout_6.addWidget(self.info_button_next, 3, 0, 1, 1)
        self.info_label_title = QtWidgets.QLabel(self.info_tab)
        self.info_label_title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.info_label_title.setObjectName("info_label_title")
        self.gridLayout_6.addWidget(self.info_label_title, 1, 0, 1, 1)
        self.tab_widget.addTab(self.info_tab, "")
        self.capture_tab = QtWidgets.QWidget()
        self.capture_tab.setObjectName("capture_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.capture_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.cap_button_back = QtWidgets.QPushButton(self.capture_tab)
        self.cap_button_back.setObjectName("cap_button_back")
        self.gridLayout.addWidget(self.cap_button_back, 5, 0, 1, 1)
        self.cap_button_create_filter = QtWidgets.QPushButton(self.capture_tab)
        self.cap_button_create_filter.setObjectName("cap_button_create_filter")
        self.gridLayout.addWidget(self.cap_button_create_filter, 5, 1, 1, 1)
        self.cap_button_next = QtWidgets.QPushButton(self.capture_tab)
        self.cap_button_next.setObjectName("cap_button_next")
        self.gridLayout.addWidget(self.cap_button_next, 5, 3, 1, 1)
        self.cap_button_sniff = QtWidgets.QPushButton(self.capture_tab)
        self.cap_button_sniff.setObjectName("cap_button_sniff")
        self.gridLayout.addWidget(self.cap_button_sniff, 5, 2, 1, 1)
        self.cap_list_packets = QtWidgets.QTableWidget(self.capture_tab)
        self.cap_list_packets.setObjectName("cap_list_packets")
        self.cap_list_packets.setColumnCount(1)
        self.cap_list_packets.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.cap_list_packets.setHorizontalHeaderItem(0, item)
        self.gridLayout.addWidget(self.cap_list_packets, 1, 0, 1, 4)
        self.tab_widget.addTab(self.capture_tab, "")
        self.filters_tab = QtWidgets.QWidget()
        self.filters_tab.setObjectName("filters_tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.filters_tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.filters_button_create_filter = QtWidgets.QPushButton(self.filters_tab)
        self.filters_button_create_filter.setObjectName("filters_button_create_filter")
        self.gridLayout_5.addWidget(self.filters_button_create_filter, 4, 1, 1, 1)
        self.filters_button_back = QtWidgets.QPushButton(self.filters_tab)
        self.filters_button_back.setObjectName("filters_button_back")
        self.gridLayout_5.addWidget(self.filters_button_back, 4, 0, 1, 1)
        self.filters_button_next = QtWidgets.QPushButton(self.filters_tab)
        self.filters_button_next.setObjectName("filters_button_next")
        self.gridLayout_5.addWidget(self.filters_button_next, 4, 2, 1, 1)
        self.filters_list_of_filters = QtWidgets.QTableWidget(self.filters_tab)
        self.filters_list_of_filters.setObjectName("filters_list_of_filters")
        self.filters_list_of_filters.setColumnCount(3)
        self.filters_list_of_filters.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.filters_list_of_filters.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.filters_list_of_filters.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.filters_list_of_filters.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.filters_list_of_filters.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.filters_list_of_filters.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.filters_list_of_filters.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.filters_list_of_filters.setItem(0, 2, item)
        self.gridLayout_5.addWidget(self.filters_list_of_filters, 0, 0, 1, 3)
        self.tab_widget.addTab(self.filters_tab, "")
        self.modifiers_tab = QtWidgets.QWidget()
        self.modifiers_tab.setObjectName("modifiers_tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.modifiers_tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.modifiers_button_create_modifier = QtWidgets.QPushButton(self.modifiers_tab)
        self.modifiers_button_create_modifier.setObjectName("modifiers_button_create_modifier")
        self.gridLayout_4.addWidget(self.modifiers_button_create_modifier, 2, 1, 1, 1)
        self.modifiers_button_next = QtWidgets.QPushButton(self.modifiers_tab)
        self.modifiers_button_next.setObjectName("modifiers_button_next")
        self.gridLayout_4.addWidget(self.modifiers_button_next, 2, 2, 1, 1)
        self.modifiers_button_back = QtWidgets.QPushButton(self.modifiers_tab)
        self.modifiers_button_back.setObjectName("modifiers_button_back")
        self.gridLayout_4.addWidget(self.modifiers_button_back, 2, 0, 1, 1)
        self.modifiers_list_of_mods = QtWidgets.QTableWidget(self.modifiers_tab)
        self.modifiers_list_of_mods.setObjectName("modifiers_list_of_mods")
        self.modifiers_list_of_mods.setColumnCount(3)
        self.modifiers_list_of_mods.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.modifiers_list_of_mods.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.modifiers_list_of_mods.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.modifiers_list_of_mods.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.modifiers_list_of_mods.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.modifiers_list_of_mods.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.modifiers_list_of_mods.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item.setCheckState(QtCore.Qt.Checked)
        self.modifiers_list_of_mods.setItem(0, 2, item)
        self.gridLayout_4.addWidget(self.modifiers_list_of_mods, 0, 0, 1, 3)
        self.tab_widget.addTab(self.modifiers_tab, "")
        self.modified_tab = QtWidgets.QWidget()
        self.modified_tab.setObjectName("modified_tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.modified_tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.modified_button_show = QtWidgets.QPushButton(self.modified_tab)
        self.modified_button_show.setObjectName("modified_button_show")
        self.gridLayout_2.addWidget(self.modified_button_show, 1, 1, 1, 1)
        self.modified_button_back = QtWidgets.QPushButton(self.modified_tab)
        self.modified_button_back.setObjectName("modified_button_back")
        self.gridLayout_2.addWidget(self.modified_button_back, 1, 0, 1, 1)
        self.modified_button_stop = QtWidgets.QPushButton(self.modified_tab)
        self.modified_button_stop.setObjectName("modified_button_stop")
        self.gridLayout_2.addWidget(self.modified_button_stop, 1, 2, 1, 1)
        self.modified_list_packets = QtWidgets.QTableWidget(self.modified_tab)
        self.modified_list_packets.setObjectName("modified_list_packets")
        self.modified_list_packets.setColumnCount(1)
        self.modified_list_packets.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.modified_list_packets.setHorizontalHeaderItem(0, item)
        self.gridLayout_2.addWidget(self.modified_list_packets, 0, 0, 1, 3)
        self.tab_widget.addTab(self.modified_tab, "")
        self.gridLayout_3.addWidget(self.tab_widget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionETHERNET = QtWidgets.QAction(MainWindow)
        self.actionETHERNET.setObjectName("actionETHERNET")
        self.actionWLAN = QtWidgets.QAction(MainWindow)
        self.actionWLAN.setObjectName("actionWLAN")
        self.actionFiltry = QtWidgets.QAction(MainWindow)
        self.actionFiltry.setObjectName("actionFiltry")

        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(4)
        self.cap_button_sniff.clicked.connect(self.cap_button_sniff.update)
        self.cap_list_packets.cellDoubleClicked['int','int'].connect(self.cap_list_packets.selectRow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EvilPostman"))
        self.info_label_instruction.setText(_translate("MainWindow", "<html><head/><body><p><br/><br/>Modyfikacja pakietów przebiega w nasŧępujący sposób: <br/>A) Metoda szybka:<br/>B) Metoda zaawansowana: <br/><br/>1) Przechodzimy dalej i włączamy przechwytywanie pakietów:<br/>2) Sposoby tworzeni a filtrów:</p><p>Metoda szybka: <br/>Klikamy prawym przyciskiem myszy na pakiecie i wybieramy utwórz szablon. Przechodzimy do wygenerowanego filtra i wybieramy wartości które mają zostać zmodyfikowane.<br/>Następnie akceptujemy zmiany i od tego momentu pakiety będą przechwytywane i modyfikowane.</p><p>Metoda zaawansowana: <br/>Klikamy na przycisk utwórz filtry<br/>Przechodzimy do wygenerowanego filtra i wybieramy wartości które mają zostać zmodyfikowane </p><p>Następnie akceptujemy zmiany i od tego momentu pakiety będą przechwytywane<br/>i modyfikowane.</p><p>4) Wysyłamy pakiet</p></body></html>"))
        self.info_button_next.setText(_translate("MainWindow", "Dalej"))
        self.info_label_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Tryb działania modyfikatora pakietów:</span></p></body></html>"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.info_tab), _translate("MainWindow", "Informacje"))
        self.cap_button_back.setText(_translate("MainWindow", "Powrót"))
        self.cap_button_create_filter.setText(_translate("MainWindow", "Utwórz filtr na podstawie pakietu"))
        self.cap_button_next.setText(_translate("MainWindow", "Dalej"))
        self.cap_button_sniff.setText(_translate("MainWindow", "Włącz przechwytywanie pakietów"))
        item = self.cap_list_packets.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pakiet"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.capture_tab), _translate("MainWindow", "Przechwytywanie"))
        self.filters_button_create_filter.setText(_translate("MainWindow", "Utwórz filtr"))
        self.filters_button_back.setText(_translate("MainWindow", "Powrót"))
        self.filters_button_next.setText(_translate("MainWindow", "Dalej"))
        item = self.filters_list_of_filters.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.filters_list_of_filters.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nazwa filtra"))
        item = self.filters_list_of_filters.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Filtr"))
        item = self.filters_list_of_filters.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Włączony"))
        __sortingEnabled = self.filters_list_of_filters.isSortingEnabled()
        self.filters_list_of_filters.setSortingEnabled(False)
        item = self.filters_list_of_filters.item(0, 0)
        item.setText(_translate("MainWindow", "FajowyFiltr"))
        item = self.filters_list_of_filters.item(0, 1)
        item.setText(_translate("MainWindow", "TCP.src=5000"))
        self.filters_list_of_filters.setSortingEnabled(__sortingEnabled)
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.filters_tab), _translate("MainWindow", "Filtry"))
        self.modifiers_button_create_modifier.setText(_translate("MainWindow", "Utwórz modyfikator"))
        self.modifiers_button_next.setText(_translate("MainWindow", "Dalej"))
        self.modifiers_button_back.setText(_translate("MainWindow", "Powrót"))
        item = self.modifiers_list_of_mods.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.modifiers_list_of_mods.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nazwa modyfikatora"))
        item = self.modifiers_list_of_mods.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Przypisany filtr"))
        item = self.modifiers_list_of_mods.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Włączony"))
        __sortingEnabled = self.modifiers_list_of_mods.isSortingEnabled()
        self.modifiers_list_of_mods.setSortingEnabled(False)
        item = self.modifiers_list_of_mods.item(0, 0)
        item.setText(_translate("MainWindow", "FajowyFiltr"))
        item = self.modifiers_list_of_mods.item(0, 1)
        item.setText(_translate("MainWindow", "TCP.src=5000"))
        self.modifiers_list_of_mods.setSortingEnabled(__sortingEnabled)
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.modifiers_tab), _translate("MainWindow", "Modyfikatory"))
        self.modified_button_show.setText(_translate("MainWindow", "Pokaż pakiet"))
        self.modified_button_back.setText(_translate("MainWindow", "powrót"))
        self.modified_button_stop.setText(_translate("MainWindow", "Zatrzymaj działanie"))
        item = self.modified_list_packets.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Pakiet"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.modified_tab), _translate("MainWindow", "Lista zmodyfikwanych"))
        self.actionETHERNET.setText(_translate("MainWindow", "&Filtry"))
        self.actionWLAN.setText(_translate("MainWindow", "&Interfejsy"))
        self.actionFiltry.setText(_translate("MainWindow", "Filtry"))

