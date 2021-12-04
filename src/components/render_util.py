# TODO move this funcition into the cell class and use them there
def center_text(box_size, text_size):
    return (box_size[0] - text_size[0]) / 2, (box_size[1] - text_size[1]) / 2


def get_text_dimensions(text, font):
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text).getbbox()[2]
    text_height = font.getmask(text).getbbox()[3] + descent

    return text_width, text_height
