"""
Copyright Ionut Soran 2021. ALL RIGHTS RESERVED.
Authors: [Ionut Soran]
Maintainers: [Ionut Soran]
Crossword class for handling all the logic of the crossword design and rendering.
"""
from PIL import Image, ImageDraw
import config
from components.cell import Cell
from components.render_util import get_text_dimensions, center_text, get_font_from_resources
from components.cellpoint import CellPoint


class Crossword:
    """
    Crossword class for managing all the logic for calculating the final render of the input
    """

    def __init__(self, cw_image=None, cell_x=30, cell_y=30):
        """
        Initialization of the main crossword class with pre-defined settings or parameterized settings
        :param cw_image: Image size to be set up at initialization
        :param cell_x: Size of the cell on the x-axis
        :param cell_y: Size of the cell on the y-axis
        """
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
        :return: None
        """
        font = get_font_from_resources(config.FONTS["arial"]["black"], 60)

        font_stroke = get_font_from_resources(config.FONTS["arial"]["black"], 54)

        for i, element in enumerate(self._offset_dictionary):
            found = False
            for j, letter in enumerate(element["word"]):
                off_vert = element["offset"]

                shape = self._get_shape_for_cell(i, j, off_vert)

                poz_font = self._get_shape_for_font(i, j, off_vert, element["letter"], font)

                shape_font_stroke = None
                if element["letter"] == letter.upper() and not found:
                    found = True
                    shape_font_stroke = self._get_shape_for_font(i, j, off_vert,
                                                                 element["letter"], font, opt_offsetter=2)

                cell = Cell(font=font,
                            font_stroke=font_stroke,
                            canvas=self._canvas,
                            text_display=letter.upper(),
                            background_col="white",
                            text_col="black",
                            stroke_col="red",
                            shape_rect=shape,
                            shape_text=poz_font,
                            shape_text_stroke=shape_font_stroke
                            )
                self._cells.append(cell)

    def run(self, main_candidate, adjectives):
        """
        Main method for handling the event logic
        :return: None
        """
        self._main_candidate = main_candidate
        self._format_input_from_user(main_candidate, adjectives)
        if self._check_if_worth_running(main_candidate, adjectives):
            print("Its ok")
        else:
            print("Not Okay")

        self._calculate_cw_size()

        self._cw_image = Image.new(
            mode=config.IMAGE_MODE,
            size=(self._cw_width, self._cw_height),
            color=config.TRANSPARENT_BACKGROUND)

        self._canvas = ImageDraw.Draw(self._cw_image)
        self._setup_cells()

        self._render_all()

        return self._cw_image, self._cw_width, self._cw_height

    def _format_input_from_user(self, main_candidate, adjectives):
        """
        TODO Add docstring
        :param main_candidate:
        :param adjectives:
        :return:
        """
        for i in range(0, len(main_candidate)):
            adjective = adjectives[i]
            self._offset_dictionary.append({
                "letter": self._main_candidate[i].upper(),
                "word": str(adjective).upper(),
                "offset": 0
            })

    def _get_shape_for_cell(self, i, j, off_vert):
        """
        Method that calculates the position and size of the shape of the crossword cell
        :param i: the vertical offset of the crossword cell
        :param j: the horizontal offset of the crossword cell
        :param off_vert: the vertical offset in grid space size of the crossword
        :return: None
        """
        x = CellPoint([self._cell_x] * 2) \
            .set_mutliplier(values=[j - off_vert, j - off_vert + 1]) \
            .set_offset(one=self._MARGIN_X) \
            .set_offset(one=self._GLOBAL_OFFSET) \
            .to_tuple()

        y = CellPoint([self._cell_y] * 2) \
            .set_mutliplier(values=[i, i + 1]) \
            .set_offset(one=self._MARGIN_Y)\
            .to_tuple()

        return (x[0], y[0]), (x[1], y[1])

    def _get_shape_for_font(self, i=0, j=0, off_vert=0, letter="", font=None, opt_offsetter=None):
        """
        Method to calculate the position of the font letter in the crossword puzzle
        :param i: the vertical offset of the font letter
        :param j: the horizontal offset of the font letter
        :param off_vert: how many grid spaces to offset the letter
        :param letter: the actual letter to be used to calculate its size on runtime
        :param font: font object to be used by the cell renderer
        :param opt_offsetter: Optional offsetter for
        :return: None
        """
        text_width, text_height = get_text_dimensions(letter, font=font)
        text_width_off, text_height_off = center_text(
            (self._cell_x, self._cell_y),
            (text_width, text_height))

        poz_font = CellPoint([self._cell_y, self._cell_y])\
            .set_mutliplier(values=[j-off_vert, i])\
            .set_offset(values=[self._MARGIN_X, self._MARGIN_Y])\
            .set_offset(values=[self._GLOBAL_OFFSET, 0])\
            .set_offset(values=[text_width_off, text_height_off])

        if opt_offsetter:
            poz_font.set_offset(values=[-1 * abs(opt_offsetter), 0])

        return poz_font.to_tuple()

    def _set_global_image_offset(self):
        """
        Calculate the global vertical offset of the crossword grid to the left in grid size units.
        :return:
        """
        self._GLOBAL_OFFSET = self.max_left_offset * self._cell_x

    def _get_cw_width(self) -> int:
        """
        Calculate the width of the canvas.
        :return: Width of the canvas.
        """
        return (self.max_left_offset + self.max_right_offset + 1) * self._cell_y + self._MARGIN_X * 2

    def _get_cw_height(self) -> int:
        """
        Calculate the height of the canvas.
        :return: Height of the canvas.
        """
        return len(self._main_candidate) * self._cell_y + self._MARGIN_Y * 2

    def _calculate_cw_size(self):
        """
        Method to calculate the width and height of the canvas to match the size of the calculated offsets
        calculated in grid sizes.
        :return: None
        """
        self._set_offsets_for_words()
        self._calculate_max_left_offset()
        self._calculate_max_right_offset()

        self._cw_width = self._get_cw_width()
        self._cw_height = self._get_cw_height()

        self._set_global_image_offset()

    def _set_offsets_for_words(self):
        """
        Method that calculates the offsets to the left for all the descriptions words
        :return: None
        """
        off_dict = self._offset_dictionary
        for item in off_dict:
            for count, letter in enumerate(item["word"].upper()):
                if letter == item["letter"].upper():
                    item["offset"] = count
                    break

    def _calculate_max_left_offset(self):
        """
        Method that calculates the maximum offset to the left in relation to the center of the picture
        calculated in grid sizes.
        :return: None
        """
        off_dict = self._offset_dictionary
        for item in off_dict:
            self.max_left_offset = item["offset"] if item["offset"] > self.max_left_offset else self.max_left_offset

    def _calculate_max_right_offset(self):
        """
        Method that calculates the maxium offset to the right in relation to the center of the picture
        calculated in grid sizes.
        :return: None
        """
        off_dict = self._offset_dictionary
        for item in off_dict:
            r_off = len(item["word"]) - item["offset"] - 1
            if r_off > self.max_right_offset:
                self.max_right_offset = r_off

    def _render_all(self):
        """
        Method that does the rendering of all the cell in our crossword class
        Iterates over all the cell and calls their render method
        :return:
        """
        for item in self._cells:
            item.render()

    def save_image(self, img_path=config.TARGET_PATH):
        """
        Method to save the image on the local filesystem
        :param img_path:
        :return:
        """
        self._cw_image.save(img_path + ".png", "PNG", trasparency=0)

    def _check_if_worth_running(self, main_candidate, adjectives):
        """
        TODO add docstring
        :param main_candidate:
        :param adjectives:
        :return:
        """
        found = None
        for item in self._offset_dictionary:
            found = False
            for letter in item["word"]:
                if letter == item["letter"]:
                    found = True
                    break

        if found:
            return True
        return False
