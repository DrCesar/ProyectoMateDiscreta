# import the library
from appJar import gui

#Varibles globales donde se guardan las combianaicones posibles de n
div = []
ansFinal = []


#Al array div que contiene las combinaciones como simples números se le agrean signos mas entre cada numero y se guarda en el array ansFinal
def AgregarMas(a):
    for x in a :
        for i in range(len(x)-1):
            x[i] = str(x[i]) + "+"
    return a


#Método que recibe una posible combinación de n y revisa si esta combinación ya existe en div y que esta combinación no contenga 0 en alguna variable
def AgregarDiv(a):
    b = a[:]
    b.sort()
    if (not b in div and not 0 in b):
        div.append(b)

#Método Para encontrar los posibles Divisores de un numero n.
#   n: número que se quiere encontrar las combinaciones
#   k: cantidad de variables que componen n
#   i: variable acutal en la que se encuentra el método
#   a: array que contiene la combinación actualq que se esta construyendo
def Divisores(n,k=0,i=0,a=[]):
    if (k == 0):
        k = n

    if (i == 0):
        a = [1] * k
    a[i] = 0

    if (i == k - 1):
        a[i] = n - (sum(a) - a[i])
        AgregarDiv(a)
        return a[-1]

    b = 1
    while (b > a[i]):
        a[i] = a[i] +1
        b = Divisores(n,k, i+1, a)

    return a[i]


# handle button events
def press(button):
    if button == "Salir":
        app.stop()
    else:
        ansFinal = []
        num = app.getEntry("Numero")
        tam = app.getEntry("Tamano")
       	if ((num>10)|(num<0)):
       		app.updateListBox("list", ["Revisar numero",],select=False)
       	elif ((tam>num)):
       		app.updateListBox("list", ["Revisar tamano",],select=False)
       	else:
            if (tam == 0):
                for i in range(int(num)):
                    Divisores(int(num), i+1)
            else:
                Divisores(int(num),int(tam))
            ansFinal = AgregarMas(div)
            app.updateListBox("list",ansFinal,select=False)
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