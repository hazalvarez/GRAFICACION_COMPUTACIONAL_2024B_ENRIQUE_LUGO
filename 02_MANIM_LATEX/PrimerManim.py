#1er. Ejemplo
from manim import *

class FirstScene(Scene):

    def construct(self):
        sq = Square()
        circ = Circle().set_fill(opacity=1)
        self.play(Transform(sq, circ))
        self.wait()
        
        
#codigo para ejecutar y generar escena 
#manim archivo.py NombreClase -p

#Revisado
