"""
Copyright Ionut Soran 2022. ALL RIGHTS RESERVED.
Authors: [Ionut Soran]
Maintainers: [Ionut Soran]
"""
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QSizePolicy, QLineEdit, QScrollArea, \
    QFrame, QCheckBox, QGridLayout, QGroupBox, QLabel, QHBoxLayout, QMenuBar, QMenu, QStatusBar, QAction, QMainWindow

from components.crossword import Crossword
from layout.crosswords_events import CrosswordsEvents
from layout.list_item_attribute_widget import CrosswordsItemWidget


class CrosswordWidget:

    def __init__(self):
        self.menuHelp = None
        self.statusbar = None
        self.actionOpen_file = None
        self.actionClear = None
        self.menuEdit = None
        self.menuFile = None
        self.menuOptions = None
        self.menubar = None
        self.button_named_save_as = None
        self.lineEdit_3 = None
        self.frame_6 = None
        self.horizontalLayout = None
        self.groupBox_4 = None
        self.frame = None
        self.frame_2 = None
        self.frame_3 = None
        self.button_named_save = None
        self.button_named_generate = None
        self.gridLayout_4 = None
        self.groupBox_2 = None
        self.label = None
        self.scrollAreaWidgetContents = None
        self.scrollArea = None
        self.lineEdit_2 = None
        self.frame_5 = None
        self.frame_4 = None
        self.checkBox_2 = None
        self.checkBox = None
        self.groupBox_3 = None
        self.gridLayout_5 = None
        self.button_named_add = None
        self.lineEdit = None
        self.button_named_set = None
        self.label_2 = None
        self.gridLayout_3 = None
        self.groupBox = None
        self.gridLayout_2 = None
        self.centralwidget = None
        self.listView = None
        self.app = QApplication(sys.argv)
        self.main_window = QMainWindow()
        self.events = CrosswordsEvents(self)
        self.crossword = Crossword(cell_x=90, cell_y=90)
        # palette = QPalette()
        # palette.setBrush(QPalette.Window, QBrush(self.bg_img))

    def setupUi(self, main_window):
        """
        UI definition for the main window
        :param main_window: QWidget
        :return:
        """
        main_window.setObjectName("MainWindow")
        main_window.resize(1086, 795)

        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.set_size_policy(QSizePolicy.Expanding, QSizePolicy.Expanding, 1, 0, True, self.groupBox, "groupBox")

        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.button_named_set = QPushButton(self.groupBox)
        self.button_named_set.setObjectName("pushButton_2")
        self.button_named_set.clicked.connect(self.events.set_clicked)
        self.button_named_set.installEventFilter(self.main_window)
        self.gridLayout_3.addWidget(self.button_named_set, 1, 2, 1, 1)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.set_size_policy(QSizePolicy.Preferred, QSizePolicy.Preferred, 1, 0, True, self.label_2, "label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.events.set_clicked)
        self.gridLayout_3.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.button_named_add = QPushButton(self.groupBox)
        self.button_named_add.setObjectName("pushButton_3")
        self.button_named_add.clicked.connect(self.events.add_clicked)

        self.gridLayout_3.addWidget(self.button_named_add, 2, 2, 1, 1)
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox = QCheckBox(self.groupBox_3)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_5.addWidget(self.checkBox, 0, 0, 1, 1)

        # self.checkBox_2 = QCheckBox(self.groupBox_3)
        # self.checkBox_2.setObjectName("checkBox_2")
        # self.gridLayout_5.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.groupBox_3)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_5 = QFrame(self.groupBox_3)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_5.addWidget(self.frame_5, 1, 1, 1, 1)

        self.gridLayout_3.addWidget(self.groupBox_3, 0, 0, 1, 3)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.returnPressed.connect(self.events.add_clicked)
        self.set_size_policy(QSizePolicy.Expanding, QSizePolicy.Fixed, 1, 0, True, self.lineEdit_2, "lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.scrollArea = QScrollArea(self.groupBox)
        self.set_size_policy(QSizePolicy.Expanding, QSizePolicy.Expanding, 0, 0, True, self.scrollArea, "scrollArea")
        self.scrollArea.setWidgetResizable(True)
        # self.listView = QListWidget()
        #
        # self.scrollAreaWidgetContents = self.listView
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 505, 373))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.scrollArea.setWidget(CrosswordsItemWidget())
        self.gridLayout_3.addWidget(self.scrollArea, 3, 0, 1, 3)
        self.label = QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.set_size_policy(QSizePolicy.Preferred, QSizePolicy.Preferred, 1, 0, True, self.label, "label")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 2)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.set_size_policy(QSizePolicy.Minimum, QSizePolicy.Minimum, 0, 0, True, self.groupBox_2, "groupBox_2")

        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.button_named_generate = QPushButton(self.groupBox_2)
        self.set_size_policy(QSizePolicy.Preferred, QSizePolicy.Fixed, 0, 0, True, self.button_named_generate, "pushButton")
        self.button_named_generate.clicked.connect(self.events.generate_clicked)
        self.gridLayout_4.addWidget(self.button_named_generate, 0, 2, 1, 1)

        self.frame_2 = QFrame(self.groupBox_2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_3 = QFrame(self.groupBox_2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4.addWidget(self.frame_3, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 3)
        self.frame = QLabel(self.centralwidget)
        self.set_size_policy(QSizePolicy.Expanding, QSizePolicy.Expanding, 2, 0, True, self.frame, "frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_6 = QFrame(self.groupBox_4)
        self.set_size_policy(QSizePolicy.Preferred, QSizePolicy.Preferred, 10, 0, True, self.frame_6, "frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_6)
        self.lineEdit_3 = QLineEdit(self.groupBox_4)

        self.set_size_policy(QSizePolicy.Expanding, QSizePolicy.Fixed, 4, 0, True, self.lineEdit_3, "lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.button_named_save_as = QPushButton(self.groupBox_4)
        self.button_named_save_as.clicked.connect(self.events.save_as_clicked)
        self.set_size_policy(QSizePolicy.Minimum, QSizePolicy.Fixed, 1, 0, True, self.button_named_save_as, "pushButton_5")
        self.horizontalLayout.addWidget(self.button_named_save_as)
        self.gridLayout_2.addWidget(self.groupBox_4, 1, 0, 1, 3)
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1086, 22))
        self.menubar.setObjectName("menubar")
        # self.menuFile = QMenu(self.menubar)
        # self.menuFile.setObjectName("menuFile")
        # self.menuEdit = QMenu(self.menubar)
        # self.menuEdit.setObjectName("menuEdit")
        # self.menuOptions = QMenu(self.menubar)
        # self.menuOptions.setObjectName("menuOptions")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        # self.actionOpen_file = QAction(main_window)
        # self.actionOpen_file.setObjectName("actionOpen_file")
        # self.actionClear = QAction(main_window)
        # self.actionClear.setObjectName("actionClear")
        # self.menuFile.addAction(self.actionOpen_file)
        # self.menuFile.addAction(self.actionClear)
        # self.menubar.addAction(self.menuFile.menuAction())
        # self.menubar.addAction(self.menuEdit.menuAction())
        # self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        """
        Translater method for Widgets that have titles based on language
        :param main_window:
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", ""))
        self.button_named_set.setText(_translate("MainWindow", "Set"))
        self.label_2.setText(_translate("MainWindow", "Main word"))
        self.button_named_add.setText(_translate("MainWindow", "Add"))
        self.groupBox_3.setTitle(_translate("MainWindow", ""))
        self.checkBox.setText(_translate("MainWindow", "Make it uncomplete"))
        #self.checkBox_2.setText(_translate("MainWindow", ""))
        self.label.setText(_translate("MainWindow", "Enter the attribute:"))
        self.groupBox_2.setTitle(_translate("MainWindow", ""))
        self.button_named_generate.setText(_translate("MainWindow", "Generate"))
        self.groupBox_4.setTitle(_translate("MainWindow", ""))
        self.button_named_save_as.setText(_translate("MainWindow", "Save as"))
        # self.menuFile.setTitle(_translate("MainWindow", "File"))
        # self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        # self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        # self.actionOpen_file.setText(_translate("MainWindow", "Open file"))
        # self.actionClear.setText(_translate("MainWindow", "Clear"))

    def set_size_policy(self, q_size_policy_w, q_size_policy_h, w_stretch_index,
                        h_stretch_index, height_for_width, widget, widget_name):
        """
        Method that sets different placement properties for a widget
        :param q_size_policy_w:
        :param q_size_policy_h:
        :param w_stretch_index: int indexes for cell horizontal spanning in groupBox
        :param h_stretch_index: int indexes for cell vertical spanning in groupBox
        :param height_for_width:
        :param widget: QWidget Object
        :param widget_name: str Name of the widget
        :return:
        """
        size_policy = QSizePolicy(q_size_policy_w, q_size_policy_h)
        size_policy.setHorizontalStretch(w_stretch_index)
        size_policy.setVerticalStretch(h_stretch_index)
        if height_for_width:
            size_policy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())

        widget.setSizePolicy(size_policy)
        widget.setObjectName(widget_name)

    def run(self):
        """
        Main running loop for the GUI
        :return:
        """
        self.setupUi(self.main_window)
        self.main_window.show()
        sys.exit(self.app.exec_())
