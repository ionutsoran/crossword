"""
Copyright Ionut Soran 2021
Authors: [Ionut Soran]
Maintainers: [Ionut Soran]
"""


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
                 font_stroke=None,
                 shape_rect=(0, 0),
                 shape_text=(0, 0),
                 shape_text_stroke=None,
                 width=20,
                 height=20):

        self.font = font
        self.font_stroke = font_stroke
        self.text_col = text_col
        self.stroke_col = stroke_col
        self.background_col = background_col
        self.width, self.height = width, height
        self.shape_rect, self.shape_text = shape_rect, shape_text
        self.shape_text_stroke = shape_text_stroke
        self._canvas = canvas
        self.text_display = text_display

    def render(self):
        canvas = self._canvas
        shape_rect = self.shape_rect
        shape_text = self.shape_text
        shape_stroke = self.shape_text_stroke
        canvas.rectangle(shape_rect, fill=self.background_col, outline=self.text_col)
        canvas.text(shape_text, self.text_display, fill="black", font=self.font, align="middle")
        if shape_stroke:
            font = self.font_stroke if self.font_stroke else self.font
            canvas.text(shape_stroke, self.text_display, fill="red", font=font, align="middle")

