"""
Copyright Ionut Soran 2021
Authors: [Ionut Soran]
Maintainers: [Ionut Soran]
"""
from PIL import Image, ImageDraw, ImageFont
import src.config as config
from src.components.cell import Cell
from src.components.render_util import get_text_dimensions, center_text


class Crossword:
    """
    Crossword class for managing all the logic for calculating the final render of the input
    """

    def __init__(self, cw_image=None, cell_x=30, cell_y=30):
        self._cell_x, self._cell_y = cell_x, cell_y
        self._MARGIN_X, self._MARGIN_Y = 28, 28
        self._cw_width, self._cw_height = 800, 600

        self._main_candidate = ""
        self._offset_dictionary = []

        self.max_left_offset = 0
        self.max_right_offset = 0

        self._GLOBAL_OFFSET = 0

        self._cw_image = cw_image

        if self._cw_image is not None:
            self._canvas = ImageDraw.Draw(self._cw_image)
        else:
            self._canvas = None

        self._cells = []

    def _setup_cells(self):
        """
        Method to calculate the positions of each cell and letter
        :return:
        """
        # TODO Refactor this method ASAP, move the specific implementation of each type of cell in a strategy like
        b_font = ImageFont.truetype("/home/isoran/workspace/crossword/src/resources/fonts/ARIBLK.TTF", 60,
                                    encoding="unic")

        for i, element in enumerate(self._offset_dictionary):
            for j, letter in enumerate(element["word"]):
                off_vert = element["offset"]
                poz_x = ((j - off_vert) * self._cell_x + self._MARGIN_X + self._GLOBAL_OFFSET,
                         i * self._cell_y + self._MARGIN_Y)
                poz_y = ((j - off_vert + 1) * self._cell_x + self._MARGIN_X + self._GLOBAL_OFFSET,
                         (i + 1) * self._cell_y + self._MARGIN_Y)

                shape = (poz_x, poz_y)

                text_width, text_height = get_text_dimensions(element["letter"], font=b_font)
                text_width_off, text_height_off = center_text(
                    (self._cell_x, self._cell_y),
                    (text_width, text_height))

                # if element["letter"] == "i".upper():
                #     shape_font = ((j - off_vert) * self._cell_x + self._MARGIN_X +
                #                   self._GLOBAL_OFFSET + self._cell_x / 2.5,
                #                   i * self._cell_y + self._MARGIN_Y - self._cell_y / 4)
                # else:
                shape_font = ((j - off_vert) * self._cell_x + self._MARGIN_X +
                              self._GLOBAL_OFFSET + text_width_off,
                              i * self._cell_y + self._MARGIN_Y + text_height_off)

                # draw.rectangle(shape, fill="#FFFFFF", outline="black")

                # if off_vert == j:
                #     if element["letter"] == "i".upper():
                #         ##shape_font = (j * Sx + x - off_vert * Sx + global_shift + Sx / 2.5, i * Sy + y + Sy / 8)
                #         shape_font_stroke = ((j - off_vert) * self._cell_x + self._MARGIN_X -
                #                              self._GLOBAL_OFFSET + self._cell_x / 2.5 - 5,
                #                              i * self._cell_y + self._MARGIN_Y + self._cell_y / 8)
                #     else:
                #         ##shape_font = (j * Sx + x - off_vert * Sx + global_shift + Sx / 4, i * Sy + y + Sx / 8)
                #         shape_font_stroke = ((j - off_vert) * self._cell_x + self._MARGIN_X -
                #                              self._GLOBAL_OFFSET + self._cell_x / 2.5 - 20,
                #                              i * self._cell_y + self._MARGIN_Y + self._cell_y / 8)
                #     cell = Cell(font=b_font,
                #                 canvas=self._canvas,
                #                 text_display=element["letter"].upper(),
                #                 background_col="white",
                #                 text_col="black",
                #                 stroke_col="red",
                #                 shape_rect=shape,
                #                 shape_text=shape_font)
                #     self._cells.append(cell)
                # draw.text(shape_font_stroke, list_nume[i][j], fill="black", font=b_stroke, align="middle")
                # draw.text(shape_font, list_nume[i][j], fill="red", font=b_font, align="middle")

                # else:
                cell = Cell(font=b_font,
                            canvas=self._canvas,
                            text_display=letter.upper(),
                            background_col="white",
                            text_col="black",
                            stroke_col="red",
                            shape_rect=shape,
                            shape_text=shape_font)
                self._cells.append(cell)
                # draw.text(shape_font, list_nume[i][j], fill="black", font=font, align="middle")

    def run(self):
        """
        Main method for handling the event logic
        :return: None
        """
        self._get_input_from_user()

        self._calculate_cw_size()

        self._cw_image = Image.new(
            config.IMAGE_FORMAT,
            (self._cw_width, self._cw_height),
            config.TRANSPARENT_BACKGROUND)

        self._canvas = ImageDraw.Draw(self._cw_image)
        self._setup_cells()

        self._render_all()

        self._save_image()

        #value = input("Enter de cateva ori sa iesi sau apasa X din colt")

    def _get_input_from_user(self):
        self._main_candidate = input("Please enter the person's name: \n")

        for i in range(0, len(self._main_candidate)):
            adjective = input("Please enter all the descriptions: \n")
            self._offset_dictionary.append({
                "letter": self._main_candidate[i].upper(),
                "word": str(adjective).upper(),
                "offset": 0
            })

    def _set_global_image_offset(self):
        self._GLOBAL_OFFSET = self.max_left_offset * self._cell_x

    def _get_cw_width(self) -> int:
        return (self.max_left_offset + self.max_right_offset + 1) * self._cell_y + self._MARGIN_X * 2

    def _get_cw_height(self) -> int:
        return len(self._main_candidate) * self._cell_y + self._MARGIN_Y * 2

    def _calculate_cw_size(self):
        self._set_offsets_for_words()
        self._calculate_max_left_offset()
        self._calculate_max_right_offset()

        self._cw_width = self._get_cw_width()
        self._cw_height = self._get_cw_height()

        self._set_global_image_offset()

    def _set_offsets_for_words(self):
        off_dict = self._offset_dictionary
        for item in off_dict:
            for count, letter in enumerate(item["word"].upper()):
                if letter == item["letter"].upper():
                    item["offset"] = count
                    break

    def _calculate_max_left_offset(self):
        off_dict = self._offset_dictionary
        for item in off_dict:
            self.max_left_offset = item["offset"] if item["offset"] > self.max_left_offset else self.max_left_offset

    def _calculate_max_right_offset(self):
        off_dict = self._offset_dictionary
        for item in off_dict:
            r_off = len(item["word"]) - item["offset"] - 1
            if r_off > self.max_right_offset:
                self.max_right_offset = r_off

    def _render_all(self):
        for item in self._cells:
            item.render()

        self._cw_image.show()

    def _save_image(self):
        self._cw_image.save(config.IMAGE_PATH + "pupikii_poza.png", "PNG", trasparency=0)
