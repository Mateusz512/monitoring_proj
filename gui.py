from tkinter import *


class GuiApp:

    def __init__(self,
                 title="Symulacja zbiornika",
                 backgroundImagePath=".\\assets\\Zbiornik.png",
                 font="Calibri 18"):
        self.top = Tk()
        self.top.title(title)

        self.backgroundImage = PhotoImage(file=backgroundImagePath)
        self.initBackground(self.backgroundImage)

        self.initialLevel = Entry(self.top, font=font)
        self.alphaParam = Entry(self.top, font=font)
        self.outputArea = Entry(self.top, font=font)
        self.targetLevel = Entry(self.top, font=font)
        self.maxFlow = Entry(self.top, font=font)
        self.button = Button(self.top, text="Symulacja", font=font, bg='#22AA22', command=self.buttonClick)

        self.initValues()
        self.placeElements()

    def start(self):
        self.top.mainloop()

    def buttonClick(self):
        print("xddd")

    def initBackground(self, backgroundImage: PhotoImage):
        self.top.geometry(str(backgroundImage.width()) + "x" + str(backgroundImage.height()))
        self.top.resizable(0, 0)
        background_label = Label(self.top, image=backgroundImage)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def initValues(self):
        self.maxFlow.insert(END, "5.3")
        self.targetLevel.insert(END, "10")
        self.outputArea.insert(END, "15")
        self.alphaParam.insert(END, "0.72")
        self.initialLevel.insert(END, "2")

    def placeElements(self):
        self.maxFlow.place(x=34, y=322, width=155)
        self.targetLevel.place(x=547, y=47, width=174)
        self.outputArea.place(x=296, y=585, width=96)
        self.alphaParam.place(x=296, y=654, width=96)
        self.initialLevel.place(x=812, y=212, width=132)
        self.button.place(x=777, y=15, width=167)
