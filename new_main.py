import time

from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter


class ResizingCanvas(tkinter.Canvas):
    def __init__(self,parent,**kwargs):
        tkinter.Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)


if __name__ == "__main__":  # pragma: no cover

    w, h = 1280, 768
    x, y = 28, 28
    Sx, Sy = 90, 90
    shape = [(x, y), (Sx, Sy)]
    global_shift = 0
    font = ImageFont.truetype("arial.ttf", 60)
    b_font = ImageFont.truetype("ariblk.ttf", 60)
    b_stroke = ImageFont.truetype("ariblk.ttf", 62)


    # draw.line((0, 0) + img.size, fill=128)
    # draw.line((0, img.size[1], img.size[0], 0), fill=128)
    value = input("Please enter the person's name: \n")
    #value = "Narcis".upper()
    #value = "francesco"
    #value = "miriam"
    h = len(value) * Sy + 56
    #list_nume = ["INGENIOS", "AMUZANT", "CREATIV", "CORECT", "PRIETENOS", "SINCER"]
    #list_nume = ["SUFLETIST", "PERSEVERENT", "HARNIC", "AVENTUROS", "TENACE", "INGENIOS", "ALTRUIST", "SOCIABIL", "CURIOS"]
    #list_nume = ["CALMA", "CREATIVA", "ORGANIZATA", "SINCERA", "GENEROASA", "METICULOASA"]

    list_nume = []
    for i in range(0, len(value)):
        t_value = input("Please enter all the descriptions: \n")
        list_nume.append(str(t_value).upper())

    new_list = list_nume.copy()
    new_list.sort(key=len, reverse=True)

    off_set_dict = {}
    max_offset = 0
    longest_word_offset = (9999, "")
    for idx, item in enumerate(list_nume):
        if idx >= len(value):
            break
        for count, letter in enumerate(item.upper()):
            if letter == value[idx].upper():
                off_set_dict[item.upper()] = (count, letter)
                if count > max_offset:
                    max_offset = count
                break

    for item in list_nume:
        if len(item) > len(longest_word_offset[1]):
            if off_set_dict[item][0] < longest_word_offset[0]:
                longest_word_offset = (off_set_dict[item][0], item)

    w = (len(new_list[0]) + max_offset - longest_word_offset[0]) * Sy + 56
    print(len(new_list[0]))
    print(max_offset)

    img = Image.new('RGBA', (w, h), (255, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    global_shift = max_offset * Sx

    print(off_set_dict)

    for i in range(0, len(value)):
        for j in range(0, len(list_nume[i])):
            off_vert = off_set_dict[list_nume[i]][0]
            shape = [(j * Sx + x - off_vert * Sx + global_shift, i * Sy + y),
                     ((j + 1) * Sx + x - off_vert * Sx + global_shift, (i + 1) * Sy + y)]
            if list_nume[i][j] == "i".upper():
                shape_font = (j * Sx + x - off_vert * Sx + global_shift + Sx / 2.5, i * Sy + y + Sy / 4)
            else:
                shape_font = (j * Sx + x - off_vert * Sx + global_shift + Sx/4, i * Sy + y + Sx/4)

            draw.rectangle(shape, fill="#FFFFFF", outline="black")
            if off_vert == j:
                if list_nume[i][j] == "i".upper():
                    shape_font = (j * Sx + x - off_vert * Sx + global_shift + Sx / 2.5, i * Sy + y + Sy / 8)
                    shape_font_stroke = (j * Sx + x - off_vert * Sx + global_shift + Sx / 2.5 - 5, i * Sy + y + Sy / 8)
                else:
                    shape_font = (j * Sx + x - off_vert * Sx + global_shift + Sx / 4, i * Sy + y + Sx / 8)
                    shape_font_stroke = (j * Sx + x - off_vert * Sx + global_shift + Sx / 2.5 - 20, i * Sy + y + Sy / 8)
                draw.text(shape_font_stroke, list_nume[i][j], fill="black", font=b_stroke, align="middle")
                draw.text(shape_font, list_nume[i][j], fill="red", font=b_font, align="middle")
            else:
                draw.text(shape_font, list_nume[i][j], fill="black", font=font, align="middle")

    img.show()

    value = input("Enter de cateva ori sa iesi sau apasa X din colt")
    img.save("pupikii_poza.png", "PNG", trasparency=0)
    # window = tkinter.Tk()
    # window.title("Crossword")
    # window.geometry("1200x800")
    #
    # top_frame = tkinter.Frame(window).pack()
    # bottom_frame = tkinter.Frame(window).pack(side="bottom")
    # side_bottom_frame = tkinter.Frame(window).pack(side="left")
    #
    # #frame = tkinter.Frame(window).pack(fill=tkinter.BOTH, expand=tkinter.YES)
    # cross_img = Image.open("cross_title.png").resize((900, 200))
    # cross_title = ImageTk.PhotoImage(cross_img, master=window)
    # canvas_tittle = tkinter.Canvas(top_frame, width=900, height=200)
    # canvas_tittle.create_image(20, 20, anchor="nw", image=cross_title)
    # # canvas.image = image
    # canvas_tittle.pack()
    #
    # #btn1 = tkinter.Button(top_frame, text=)
    # img = img.resize((800, 800))
    # gen_image = ImageTk.PhotoImage(img, master=window)
    # canvas = tkinter.Canvas(bottom_frame, width=800, height=800)
    # canvas.create_image(20, 20, anchor="nw", image=gen_image)
    # #canvas.image = image
    # canvas.pack(side="right")
    #
    # label_first_name = tkinter.Label(side_bottom_frame, width=80, text="Introduceti numele!").pack()
    # first_name = tkinter.Entry(side_bottom_frame, width=50).pack()
    #
    # window.mainloop()
