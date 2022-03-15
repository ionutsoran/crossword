from PyQt5.QtWidgets import QFrame, QVBoxLayout
from layout.list_item_attribute_widget import CrosswordsItemWidget


class CrosswordsWidget(QFrame):

    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout()
        self.item_widgets = []

    def create_item(self):
        idx = len(self.item_widgets)
        item = CrosswordsItemWidget(self, idx)
        self.item_widgets.append(item)

    def remove_item(self, idx):

        self.item_widgets[idx].SetParent(None)
        self.item_widgets.pop(idx)