from math import isnan
from tkinter import *

from inputs import *
from model import OneSourceModel, TwoSourcesModel


def paintEntryValid(entry, isValid):
    if isValid:
        entry.config({"background": "White"})
    else:
        entry.config({"background": "Red"})


root = Tk()
root.withdraw()


class MainApp:

    def __init__(self,
                 title="Menu",
                 font="Calibri 18"):
        self.top = Toplevel(root)
        self.top.title(title)
        self.font = font

        self.top.geometry("330x70")
        self.top.resizable(0, 0)

        self.buttonSingle = Button(self.top, text="Jeden wlew", font=font, bg='#22AA88', command=self.startSingle)
        self.buttonSingle.place(x=10, y=10, width=150)

        self.buttonDouble = Button(self.top, text="Dwa wlewy", font=font, bg='#22AA88', command=self.startDouble)
        self.buttonDouble.place(x=170, y=10, width=150)

        self.single = None
        self.double = None

    def start(self):
            self.top.mainloop()
        

    def startSingle(self):
        self.single = SingleSourceApp()
        self.single.start()
        print("Started single")

    def startDouble(self):
        self.double = DoubleSourceApp()
        self.double.start()
        print("Start duo")


class SingleSourceApp:

    def __init__(self,
                 title="Symulacja zbiornika z regulowanym poziomem",
                 backgroundImagePath="./assets/ZbiornikUno.png",
                 font="Calibri 18"):
        self.top = Toplevel(root)
        self.top.protocol("WM_DELETE_WINDOW", self.onClose)
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
            model = OneSourceModel(values)
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
    
    def onClose(self):
        print("CLOSING")
        self.top.destroy()


class DoubleSourceApp:

    def __init__(self,
                 title="Symulacja zbiornika z dwoma wlewami",
                 backgroundImagePath="./assets/ZbiornikDuo.png",
                 font="Calibri 18"):
        self.top = Toplevel(root)
        self.top.title(title)
        self.font = font

        self.backgroundImage = PhotoImage(file=backgroundImagePath)
        self.initBackground(self.backgroundImage)

        self.entries = {
            "targetRatio": self.buildEntry("5.3", 489, 27, 231),
            "maxFlowA": self.buildEntry("12", 212, 242, 83),
            "ratioA": self.buildEntry("3.88", 212, 317, 83),
            "maxFlowB": self.buildEntry("10", 866, 242, 83),
            "ratioB": self.buildEntry("40", 866, 317, 83),
            "outputDiameter": self.buildEntry("0.14", 296, 654, 96),
            "tankDiameter": self.buildEntry("3", 296, 585, 96),
            "maxLevel": self.buildEntry("25", 194, 459, 117),
            "initialLevel": self.buildEntry("2", 846, 546, 100),
            "initialRatio": self.buildEntry("13", 846, 643, 100),
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
            print("Displaying")
            model = TwoSourcesModel(values)
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
