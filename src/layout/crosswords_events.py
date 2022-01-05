"""
Copyright Ionut Soran 2022. ALL RIGHTS RESERVED.
Authors: [Ionut Soran]
Maintainers: [Ionut Soran]
"""
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore


class CrosswordsEvents:

    def __init__(self, cw_widget):
        self.cw_widget = cw_widget

    def get_background_image(self, image, width, height):
        """
        TODO add docstring
        :param image:
        :param width:
        :param height:
        :return:
        """
        # noinspection PyTypeChecker
        data = image.tobytes("raw", "RGBA")
        background_img = QImage(data, width, height, QImage.Format_RGBA8888)

        return background_img

    def generate_clicked(self):
        """
        TODO add docstring
        :return:
        """
        to_gen_solution = not self.cw_widget.checkBox.isChecked()
        if self.cw_widget.lineEdit.text() and str.isalpha(self.cw_widget.lineEdit.text()):
            items = [self.cw_widget.listView.item(x).text() for x in range(self.cw_widget.listView.count())]
            cw_image, cw_width, cw_height = self.cw_widget.crossword.run(self.cw_widget.lineEdit.text(),
                                                                         items,
                                                                         to_gen_solution)

            bg_img = self.get_background_image(cw_image, cw_width, cw_height)
            self.cw_widget.frame.setPixmap(QPixmap.fromImage(bg_img))
            self.cw_widget.frame.update()
            self.cw_widget.listView.clear()
            self.set_clicked()

    def save_as_clicked(self):
        """
        TODO add docstring
        :return:
        """
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self.cw_widget.main_window, "QFileDialog.getSaveFileName()", "",
                                                  "Image Files (*.jpg *jpeg *.gif, *.png);;All Files (*)",
                                                  options=options)
        if str(filename):
            _filename = str(filename).rsplit(',', 1)
            if len(_filename) > 1:
                if not _filename[1] == "png" or _filename[1] == "jpg" or _filename[1] == "jpeg" or\
                        _filename[1] == "gif":
                    filename = filename + ".jpg"

            self.cw_widget.crossword.save_image(filename)
            self.cw_widget.lineEdit_3.setText(filename)
        else:
            self.cw_widget.lineEdit_3.setText("")

    def set_clicked(self):
        """
        TODO add docstring
        :return:
        """
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
        """
        TODO add docstring
        :return:
        """
        if self.cw_widget.lineEdit_2.text() and str.isalpha(self.cw_widget.lineEdit.text()):
            self.cw_widget.listView.addItem(self.cw_widget.lineEdit_2.text())
            self.cw_widget.lineEdit.update()
        self.cw_widget.lineEdit_2.setText("")

    def empty_cells_clicked(self):
        """
        TODO add docstring
        :return:
        """

