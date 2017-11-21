# import the library
from appJar import gui

div = []


def AgregarDiv(a):
    b = a[:]
    b.sort()
    if (not b in div and not 0 in b):
        div.append(b)


def Divisores(n,k,i=0,a=[]):
    if (i == k - 1):
        a[i] = n - (sum(a) - a[i])
        AgregarDiv(a)
        return a[-1]

    if (i == 0):
        a = [1] * k

    a[i] = 0
    b = 1
    while (b >= a[i]):
        a[i] = a[i] +1
        b = Divisores(n,k, i+1, a)

    return a[i]


# handle button events
def press(button):
    if button == "Salir":
        app.stop()
    else:
        num = app.getEntry("Numero")
        tam = app.getEntry("Tamano")
       	if ((num>10)|(num<0)):
       		app.updateListBox("list", ["Revisar numero",],select=False)
       	elif ((tam>num)|(tam<0)):
       		app.updateListBox("list", ["Revisar tamano",],select=False)
       	else:
        	Divisores(int(num),int(tam))
        	app.updateListBox("list",div,select=False)
        	del div[:]

# create a GUI variable called app
app = gui("Proyecto final", "400x400")
app.setBg("lightBlue")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Josue Jacobs y Helmuth Nistal")
app.setLabelBg("title", "lightBlue")
app.setLabelFg("title", "black")

app.addLabel("label1","Ingrese un numero de 0 a 10:")
app.addNumericEntry("Numero")
app.addLabel("label2","Ingrese el tamano de la particion:")
app.addNumericEntry("Tamano")

# link the buttons to the function called press
app.addButtons(["Calcular particiones", "Salir"], press)

app.addListBox("list", [""])

app.setFocus("Numero")

# start the GUI
app.go()