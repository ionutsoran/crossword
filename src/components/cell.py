"""
Copyright Ionut Soran 2021
Authors: [Ionut Soran]
Maintainers: [Ionut Soran]
"""
from PIL import ImageDraw


class Cell:
    """
    Class for storing and rendering information of the grid-like structure of the crossword
    """

    def __init__(self,
                 font,
                 canvas,
                 text_display,
                 background_col="white",
                 text_col="black",
                 stroke_col="black",
                 shape_rect=(0, 0),
                 shape_text=(0, 0),
                 width=20,
                 height=20):

        self.font = font
        self.text_col = text_col
        self.stroke_col = stroke_col
        self.background_col = background_col
        self.width, self.height = width, height
        self.shape_rect, self.shape_text = shape_rect, shape_text
        self._canvas = canvas
        self.text_display = text_display

    def render(self):
        canvas = self._canvas
        shape_rect = self.shape_rect
        shape_text = self.shape_text
        canvas.rectangle(shape_rect, fill=self.background_col, outline=self.text_col)
        canvas.text(shape_text, self.text_display, fill="black", font=self.font, align="middle")

