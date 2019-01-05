from math import isnan
from tkinter import *

from model import Model


class GuiApp:

    def __init__(self,
                 title="Symulacja zbiornika",
                 backgroundImagePath=".\\assets\\Zbiornik.png",
                 font="Calibri 18"):
        self.top = Tk()
        self.top.title(title)

        self.backgroundImage = PhotoImage(file=backgroundImagePath)
        self.initBackground(self.backgroundImage)

        self.entries = {
            "initialLevel": Entry(self.top, font=font),
            "alphaParam": Entry(self.top, font=font),
            "outputArea": Entry(self.top, font=font),
            "targetLevel": Entry(self.top, font=font),
            "maxFlow": Entry(self.top, font=font)
        }
        self.button = Button(self.top, text="Symulacja", font=font, bg='#22AA22', command=self.buttonClick)

        self.initValues()
        self.placeElements()

    def start(self):
        self.top.mainloop()

    def buttonClick(self):
        values = {}
        for key, entry in self.entries.items():
            values[key] = self.readFromEntry(entry)

        # check if all values are numbers
        if not [k for k, v in values.items() if isnan(v)]:
            model = Model(values)
            model.calculate()
            model.display()

    def initBackground(self, backgroundImage: PhotoImage):
        self.top.geometry(str(backgroundImage.width()) + "x" + str(backgroundImage.height()))
        self.top.resizable(0, 0)
        background_label = Label(self.top, image=backgroundImage)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def initValues(self):
        self.entries["maxFlow"].insert(END, "5.3")
        self.entries["targetLevel"].insert(END, "10")
        self.entries["outputArea"].insert(END, "15")
        self.entries["alphaParam"].insert(END, "0.72")
        self.entries["initialLevel"].insert(END, "2")

    def placeElements(self):
        self.entries["maxFlow"].place(x=34, y=322, width=155)
        self.entries["targetLevel"].place(x=547, y=47, width=174)
        self.entries["outputArea"].place(x=296, y=585, width=96)
        self.entries["alphaParam"].place(x=296, y=654, width=96)
        self.entries["initialLevel"].place(x=812, y=212, width=132)
        self.button.place(x=777, y=15, width=167)

    def readFromEntry(self, entry: Entry):
        try:
            value = float(entry.get().replace(",", "."))
            entry.config({"background": "White"})
            return value
        except ValueError:
            entry.config({"background": "Red"})
            return float("nan")
