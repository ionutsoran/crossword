"""
Copyright Ionut Soran 2021. ALL RIGHTS RESERVED.
Authors: [Ionut Soran]
Maintainers: [Ionut Soran]
Utility module for cells and crossword.
"""
from PIL import ImageFont
import config
from components.custom_exceptions import FontNotFoundException
import logging

logger = logging.getLogger(__name__)


# TODO Create docstrings for all the methods in this module
# TODO Refactor this function if needed.
def center_text(box_size, text_size):
    return (box_size[0] - text_size[0]) / 2, (box_size[1] - text_size[1]) / 2


def get_text_dimensions(text, font):
    """
    TODO add docstring
    :param text:
    :param font:
    :return:
    """
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text).getbbox()[2]
    text_height = font.getmask(text).getbbox()[3] + descent

    return text_width, text_height


def get_font_from_resources(font_name, font_size):
    """
    Wrapper function for getting front from PIL Api
    :param str font_name: Font name defined in resources/fonts/
    :param font_size: Size of the font to be returned
    :return: Font object with specified parameters
    """
    try:
        font = ImageFont.truetype(str(config.FONTS_PAH / f"{font_name.upper()}.TTF"), font_size, encoding="unic")
    except FontNotFoundException:
        logger.error(f"Font {font_name} specified by caller does not exist")
        font = ImageFont.truetype(str(config.FONTS_PAH / f"ARIAL.TTF"), font_size)

    return font
