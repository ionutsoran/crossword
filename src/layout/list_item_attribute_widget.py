from PyQt5.QtWidgets import QFrame, QLabel, QLineEdit, QPushButton, QHBoxLayout


class CrosswordsItemWidget(QFrame):

    def __init__(self, parent, index):
        super().__init__()

        self.setWindowTitle("AttributeListItem")
        self.setFixedHeight(45)
        self.setStyleSheet("background: #e6f2ff;")

        self.hbox = QHBoxLayout()

        self.button_new_item = QPushButton()
        self.button_new_item.setText("New")
        self.button_new_item.clicked.connect(self.button_new_item_clicked)

        self.label_attribute = QLabel()
        self.line_edit = QLineEdit()
        self.button_for_remove = QPushButton()

        self.hbox.addWidget(self.button_new_item)

        self.setLayout(self.hbox)

        self.parent = parent
        self.index = index

    def button_new_item_clicked(self):
        self.button_new_item.setParent(None)

        self.label_attribute.setText("Attribute")

        self.line_edit.setStyleSheet("background: white;")

        self.button_for_remove.setStyleSheet("border-image: url(F:/pycharm/crossword/src/resources/images/close.png)"
                                             " 0 0 0 0 stretch stretch;")
        self.hbox.addWidget(self.label_attribute)
        self.hbox.addWidget(self.line_edit)
        self.hbox.addWidget(self.button_for_remove)

    def line_edit_enter_pressed(self):
        self.parent.create_new_item()
