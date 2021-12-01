from PIL import Image, ImageDraw, ImageFont
from components.crossword import Crossword

if __name__ == "__main__":  # pragma: no cover
    cw =Crossword()
    cw.run()
    # w, h = 1280, 768
    # x, y = 28, 28
    # Sx, Sy = 90, 90
    # shape = [(x, y), (Sx, Sy)]
    # global_shift = 0
    # font = ImageFont.truetype("arial.ttf", 60)
    # b_font = ImageFont.truetype("ariblk.ttf", 60)
    # b_stroke = ImageFont.truetype("ariblk.ttf", 62)
    #
    # value = input("Please enter the person's name: \n")
    #
    # h = len(value) * Sy + 56
    #
    # list_nume = []
    # for i in range(0, len(value)):
    #     t_value = input("Please enter all the descriptions: \n")
    #     list_nume.append(str(t_value).upper())
    #
    # new_list = list_nume.copy()
    # new_list.sort(key=len, reverse=True)
    #
    # off_set_dict = {}
    # max_offset = 0
    # longest_word_offset = (9999, "")
    # for idx, item in enumerate(list_nume):
    #     if idx >= len(value):
    #         break
    #     for count, letter in enumerate(item.upper()):
    #         if letter == value[idx].upper():
    #             off_set_dict[item.upper()] = (count, letter)
    #             if count > max_offset:
    #                 max_offset = count
    #             break
    #
    # for item in list_nume:
    #     if len(item) > len(longest_word_offset[1]):
    #         if off_set_dict[item][0] < longest_word_offset[0]:
    #             longest_word_offset = (off_set_dict[item][0], item)
    #
    # w = (len(new_list[0]) + max_offset - longest_word_offset[0]) * Sy + 56
    # print(len(new_list[0]))
    # print(max_offset)
    #
    # img = Image.new('RGBA', (w, h), (255, 0, 0, 0))
    # draw = ImageDraw.Draw(img)
    #
    # global_shift = max_offset * Sx
    #
    # print(off_set_dict)
    #
    # for i in range(0, len(value)):
    #     for j in range(0, len(list_nume[i])):
    #         off_vert = off_set_dict[list_nume[i]][0]
    #         shape = [(j * Sx + x - off_vert * Sx + global_shift, i * Sy + y),
    #                  ((j + 1) * Sx + x - off_vert * Sx + global_shift, (i + 1) * Sy + y)]
    #         if list_nume[i][j] == "i".upper():
    #             shape_font = (j * Sx + x - off_vert * Sx + global_shift + Sx / 2.5, i * Sy + y + Sy / 4)
    #         else:
    #             shape_font = (j * Sx + x - off_vert * Sx + global_shift + Sx/4, i * Sy + y + Sx/4)
    #
    #         draw.rectangle(shape, fill="#FFFFFF", outline="black")
    #         if off_vert == j:
    #             if list_nume[i][j] == "i".upper():
    #                 shape_font = (j * Sx + x - off_vert * Sx + global_shift + Sx / 2.5, i * Sy + y + Sy / 8)
    #                 shape_font_stroke = (j * Sx + x - off_vert * Sx + global_shift + Sx / 2.5 - 5, i * Sy + y + Sy / 8)
    #             else:
    #                 shape_font = (j * Sx + x - off_vert * Sx + global_shift + Sx / 4, i * Sy + y + Sx / 8)
    #                 shape_font_stroke = (j * Sx + x - off_vert * Sx + global_shift + Sx / 2.5 - 20, i * Sy + y + Sy / 8)
    #             draw.text(shape_font_stroke, list_nume[i][j], fill="black", font=b_stroke, align="middle")
    #             draw.text(shape_font, list_nume[i][j], fill="red", font=b_font, align="middle")
    #         else:
    #             draw.text(shape_font, list_nume[i][j], fill="black", font=font, align="middle")

    # img.show()
    #
    # value = input("Enter de cateva ori sa iesi sau apasa X din colt")
    # img.save("pupikii_poza.png", "PNG", trasparency=0)
