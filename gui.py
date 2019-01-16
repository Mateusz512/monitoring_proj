from math import isnan
from tkinter import *

from inputs import *
from model import TwoSourcesModel


def paintEntryValid(entry, isValid):
    if isValid:
        entry.config({"background": "White"})
    else:
        entry.config({"background": "Red"})

class SingleSourceApp:

    def __init__(self,
                 title="Symulacja zbiornika z regulowanym poziomem",
                 backgroundImagePath="./assets/ZbiornikUno.png",
                 font="Calibri 18"):
        self.top = Tk()
        self.top.title(title)
        self.font = font

        self.backgroundImage = PhotoImage(file=backgroundImagePath)
        self.initBackground(self.backgroundImage)

        self.entries = {
            "initialLevel": self.buildEntry("5.3", 812, 212, 132),
            "outputDiameter": self.buildEntry("0.14", 296, 654, 96),
            "tankDiameter": self.buildEntry("3", 296, 585, 96),
            "targetLevel": self.buildEntry("10", 547, 47, 174),
            "maxFlow": self.buildEntry("5.3", 34, 322, 155),
            "maxLevel": self.buildEntry("25", 194, 459, 117)
        }
        self.button = Button(self.top, text="Symulacja", font=font, bg='#22AA22', command=self.buttonClick)
        self.button.place(x=777, y=15, width=167)

    def start(self):
        self.top.mainloop()

    def buttonClick(self):
        # values = {}
        # for key, entry in self.entries.items():
        #     values[key] = self.readFromEntry(entry)
        values = {key: self.readFromEntry(entry) for key, entry in self.entries.items()}

        self.validateValues(values)
        # check if all values are numbers
        if not [k for k, v in values.items() if isnan(v)]:
            model = TwoSourcesModel(values, step(1.0),
                                    combine(stepDown(1.0, 1.0), combine(stepDown(1.0, 2.0), stepDown(1.0, 3.0))))
            model.calculate()
            model.display()

    def initBackground(self, backgroundImage: PhotoImage):
        self.top.geometry(str(backgroundImage.width()) + "x" + str(backgroundImage.height()))
        self.top.resizable(0, 0)
        background_label = Label(self.top, image=backgroundImage)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def buildEntry(self, initialValue, x, y, width):
        entry = Entry(self.top, font=self.font)
        entry.insert(END, initialValue)
        entry.place(x=x, y=y, width=width)
        return entry

    def readFromEntry(self, entry: Entry):
        try:
            value = float(entry.get().replace(",", "."))
            paintEntryValid(entry, True)
            return value
        except ValueError:
            paintEntryValid(entry, False)
            return float("nan")

    def validateValues(self, values):
        if values["targetLevel"] >= values["maxLevel"]:
            values["targetLevel"] = float("nan")
            values["maxLevel"] = float("nan")
            paintEntryValid(self.entries["targetLevel"], False)
            paintEntryValid(self.entries["maxLevel"], False)

        if values["initialLevel"] >= values["maxLevel"]:
            values["initialLevel"] = float("nan")
            values["maxLevel"] = float("nan")
            paintEntryValid(self.entries["initialLevel"], False)
            paintEntryValid(self.entries["maxLevel"], False)

        if values["outputDiameter"] >= values["tankDiameter"]:
            values["outputDiameter"] = float("nan")
            values["tankDiameter"] = float("nan")
            paintEntryValid(self.entries["outputDiameter"], False)
            paintEntryValid(self.entries["tankDiameter"], False)
