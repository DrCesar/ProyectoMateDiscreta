'''
Proyecto Final de Mate Discreta

Helmuth Nistal
Josué Jacobs


Instalar el módulo Kivy mediante los siguientes comandos:
    python -m pip install --upgrade pip wheel setuptools
    python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
    python -m pip install kivy.deps.gstreamer
    python -m pip install kivy
'''
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)


div = []


def AgregarDiv(a):
    b = a[:]
    b.sort()
    if (not b in div and not 0 in b):
        div.append(b)


def Divisores(n,k=0,i=0,a=[]):
    if (k == 0):
        k = n

    if (i == k - 1):
        a[i] = n - (sum(a) - a[i])
        AgregarDiv(a)
        return a[-1]

    if (i == 0):
        a = [1] * k

    a[i] = 0
    b = 1
    while (b > a[i]):
        a[i] = a[i] +1
        b = Divisores(n,k, i+1, a)

    return a[i]




Divisores(80,3)

print(div)
print(len(div))

# class PantallaInicial(FloatLayout):
#
#     def __init__(self, **kwargs):
#         super(PantallaInicial, self).__init__(**kwargs)
#
#         self.size = (700, 500)
#
#         calcular =Button(text="Calcular", size_hint=(.5,.5), pos_hint={'x':.20, 'y':.20}, background_color=(50,50,255,3), on_press=lambda a:self.Alerta() )
#         self.add_widget(calcular)
#
#     def Alerta(serlf, instance):
#         print('funciono')
#
# class TestApp(App):
#     def build(self):
#         return PantallaInicial()
#
# TestApp().run()



