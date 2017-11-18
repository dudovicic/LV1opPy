from Tkinter import * #Tkinter grafičko sučelje
import tkFileDialog #otvara prozor za odabir datoteka
from tkFileDialog import askopenfile 
import tkMessageBox #otvara prozor za interakciju s korisnikom


def mOpen():  
    filetypes = tkFileDialog.askopenfile(filetypes=[("Text","*.txt")]) # otvara txt datoteku, zatim razdvajaj redove, odbacuje prvi niz (ime GrafObj) i cita daljnji tekst Color, points
    text = filetypes.readlines()
    for element in text:
        elementList = element.split() 
        object = elementList.pop(0)
        if object == 'Line':
            line = Line(elementList.pop(0), elementList)
            line.Draw()
        elif object == 'Polygon':
            pass
            polygon = Polygon(elementList.pop(0), elementList)
            polygon.Draw()
        elif object == 'Triangle':
            triangle = Triangle(elementList.pop(0), elementList)
            triangle.Draw()
        elif object == 'Rectangle':
            color = elementList.pop(0)
            x1 = float(elementList.pop(0))
            x2 = float(elementList.pop(0))
            h = float(elementList.pop(0))
            w = float(elementList.pop(0))
            rectangle = Rectangle(color, [x1, x2, x1 + w, x2 + h])
            rectangle.Draw()
        elif object == 'Circle':
            color = elementList.pop(0)
            x1 = float(elementList.pop(0))
            x2 = float(elementList.pop(0))
            r = float(elementList.pop(0))
            circle = Circle(color, [x1 - r, x2 + r, x1 + r, x2 - r])
            circle.Draw()
        elif object == 'Ellipse':
            color = elementList.pop(0)
            x1 = float(elementList.pop(0))
            x2 = float(elementList.pop(0))
            r1 = float(elementList.pop(0))
            r2 = float(elementList.pop(0))
            ellipse = Ellipse(color, [x1 - r1, x2 + r2, x1 + r1, x2 - r2])
            ellipse.Draw()
    filetypes.close()

def mQuit(): # zatvaranje prozora
    mExit = tkMessageBox.askokcancel(title="Quit", message="Are you sure?")
    if mExit > 0:
        tk.destroy()
        return

tk = Tk()
canvas = Canvas(tk, width=800, height=600, bg="#999999") #izgled canvasa (velicina i siva boja)
tk.title("Drawing")
canvas.pack()
menubar=Menu(tk) #stvaranje menubara
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Open",command=mOpen)
filemenu.add_command(label="Close",command=mQuit)
menubar.add_cascade(label="File", menu=filemenu)
tk.config(menu=menubar)


#klasa Graf. Objekti
class GrafObj:
    Color = 'black'
    Point = [0, 0]
    def __init__(self, Color, Point):
        self.Color = Color
        self.Point = Point
    def SetColor(self, Color):
        self.color = Color
    def GetColor(self):
        return self.Color
    def Draw(self):
        pass

 #klasa Line koja nasljeđuje klasu GrafObj
class Line(GrafObj):
    def __init__(self, Color, Point):
       GrafObj.__init__(self, Color, Point)
    def Draw(self):
        canvas.create_line(self.Point, fill=self.Color)

 #klasa Triangle koja nasljeđuje klasu Line
class Triangle(Line):
    def __init__(self, Color, Point):
         Line.__init__(self, Color, Point)
    def Draw(self):
        canvas.create_polygon(self.Point, outline=self.Color, fill="")

 #klasa Rectangle koja nasljeđuje klasu GrafObj
class Rectangle(GrafObj):
    def __init__(self, Color, Point):
       GrafObj.__init__(self, Color, Point)
    def Draw(self):
        canvas.create_rectangle(self.Point, outline=self.Color)

 #klasa Polygon koja nasljeđuje klasu GrafObj
class Polygon(GrafObj):
    def __init__(self, Color, Point):
        GrafObj.__init__(self, Color, Point)
    def Draw(self):
        canvas.create_polygon(self.Point, outline=self.Color, fill="")

 #klasa Circle koja nasljeđuje klasu GrafObj
class Circle(GrafObj):
    def __init__(self, Color, Point):
        GrafObj.__init__(self, Color, Point)
    def Draw(self):
        canvas.create_oval(self.Point, outline=self.Color)

 #klasa Ellipse koja nasljeđuje klasu GrafObj
class Ellipse(Circle):
    def __init__(self, Color, Point):
        Circle.__init__(self, Color, Point)
    def Draw(self):
        Circle.Draw(self)


tk.mainloop() #pokrećemo graf. sučelje