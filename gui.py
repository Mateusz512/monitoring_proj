from math import isnan
from tkinter import *

from inputs import *
from model import TwoSourcesModel


class SingleSourceApp:

    def __init__(self,
                 title="Symulacja zbiornika z regulowanym poziomem",
                 backgroundImagePath="./assets/ZbiornikUno.png",
                 font="Calibri 18"):
        self.top = Tk()
        self.top.title(title)

        self.backgroundImage = PhotoImage(file=backgroundImagePath)
        self.initBackground(self.backgroundImage)

        self.entries = {
            "initialLevel": Entry(self.top, font=font),
            "outputDiameter": Entry(self.top, font=font),
            "tankDiameter": Entry(self.top, font=font),
            "targetLevel": Entry(self.top, font=font),
            "maxFlow": Entry(self.top, font=font),
            "maxLevel": Entry(self.top, font=font)
        }
        self.button = Button(self.top, text="Symulacja", font=font, bg='#22AA22', command=self.buttonClick)

        self.initValues()
        self.placeElements()

    def start(self):
        self.top.mainloop()

    def buttonClick(self):
        # values = {}
        # for key, entry in self.entries.items():
        #     values[key] = self.readFromEntry(entry)
        values = {key: self.readFromEntry(entry) for key, entry in self.entries.items()}

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

    def initValues(self):
        self.entries["maxFlow"].insert(END, "5.3")
        self.entries["targetLevel"].insert(END, "10")
        self.entries["tankDiameter"].insert(END, "3")
        self.entries["outputDiameter"].insert(END, "0.14")
        self.entries["initialLevel"].insert(END, "2")
        self.entries["maxLevel"].insert(END, "25")

    def placeElements(self):
        self.entries["maxFlow"].place(x=34, y=322, width=155)
        self.entries["targetLevel"].place(x=547, y=47, width=174)
        self.entries["tankDiameter"].place(x=296, y=585, width=96)
        self.entries["outputDiameter"].place(x=296, y=654, width=96)
        self.entries["initialLevel"].place(x=812, y=212, width=132)
        self.entries["maxLevel"].place(x=194, y=459, width=117)
        self.button.place(x=777, y=15, width=167)

    def readFromEntry(self, entry: Entry):
        try:
            value = float(entry.get().replace(",", "."))
            self.paintEntryValid(entry, True)
            return value
        except ValueError:
            self.paintEntryValid(entry, False)
            return float("nan")

    @staticmethod
    def paintEntryValid(entry, isValid):
        if isValid:
            entry.config({"background": "White"})
        else:
            entry.config({"background": "Red"})

    def validateValues(self, values):
        if values["targetLevel"] >= values["maxLevel"]:
            values["targetLevel"] = float("nan")
            values["maxLevel"] = float("nan")
            self.paintEntryValid(self.entries["targetLevel"], False)
            self.paintEntryValid(self.entries["maxLevel"], False)

        if values["initialLevel"] >= values["maxLevel"]:
            values["initialLevel"] = float("nan")
            values["maxLevel"] = float("nan")
            self.paintEntryValid(self.entries["initialLevel"], False)
            self.paintEntryValid(self.entries["maxLevel"], False)

        if values["outputDiameter"] >= values["tankDiameter"]:
            values["outputDiameter"] = float("nan")
            values["tankDiameter"] = float("nan")
            self.paintEntryValid(self.entries["outputDiameter"], False)
            self.paintEntryValid(self.entries["tankDiameter"], False)
