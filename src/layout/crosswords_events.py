from PyQt5.QtGui import QImage, QPalette, QBrush, QPixmap
from PyQt5 import QtCore


class CrosswordsEvents:

    def __init__(self, cw_widget):
        self.cw_widget = cw_widget

    def get_background_image(self, image, width, height):
        # noinspection PyTypeChecker
        data = image.tobytes("raw", "RGBA")
        background_img = QImage(data, width, height, QImage.Format_RGBA8888)

        return background_img

    def generate_clicked(self):
        if self.cw_widget.lineEdit.text() and str.isalpha(self.cw_widget.lineEdit.text()):
            items = [self.cw_widget.listView.item(x).text() for x in range(self.cw_widget.listView.count())]
            cw_image, cw_width, cw_height = self.cw_widget.crossword.run(self.cw_widget.lineEdit.text(),
                                                                         items)

            bg_img = self.get_background_image(cw_image, cw_width, cw_height)
            self.cw_widget.frame.setPixmap(QPixmap.fromImage(bg_img))
            self.cw_widget.frame.update()
            self.cw_widget.listView.clear()

    def save_as_clicked(self):
        if self.cw_widget.lineEdit_3.text():
            self.cw_widget.crossword.save_image(self.cw_widget.lineEdit_3.text())
        self.cw_widget.lineEdit_3.setText("")

    def set_clicked(self):
        _translate = QtCore.QCoreApplication.translate
        if self.cw_widget.button_named_set.text() == "Set":
            self.cw_widget.lineEdit.setReadOnly(True)
            self.cw_widget.lineEdit.setEnabled(False)
            self.cw_widget.button_named_set.setText(_translate("MainWindow", "Unlock"))
        else:
            self.cw_widget.lineEdit.setReadOnly(False)
            self.cw_widget.lineEdit.setEnabled(True)
            self.cw_widget.button_named_set.setText(_translate("MainWindow", "Set"))

    def add_clicked(self):
        if self.cw_widget.lineEdit_2.text() and str.isalpha(self.cw_widget.lineEdit.text()):
            self.cw_widget.listView.addItem(self.cw_widget.lineEdit_2.text())
            self.cw_widget.lineEdit.update()
        self.cw_widget.lineEdit_2.setText("")

    # def eventFilter(self, obj, event):
    #     if event.type() == QtCore.QEvent.KeyPress and obj is self.cw_widget.lineEdit:
    #         if event.key() == QtCore.Qt.Key_Return and self.cw_widget.lineEdit.hasFocus():
    #             self.set_clicked()
    #         print("ALo?")

