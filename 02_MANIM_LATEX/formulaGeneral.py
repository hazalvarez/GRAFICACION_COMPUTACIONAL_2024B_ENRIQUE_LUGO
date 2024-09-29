#2do. Ejemplo
from manim import *
import math

class Scene3(Scene):
    def construct(self):
        #formula general
        text = MathTex(r"x = \frac {-b \pm \sqrt{b^2 - 4ac}}{2a}")
        self.add(text)
#Para ejecutar el ejemplo desde la terminal 
#manim DosM.py SecondScene -p
#manim DosM.py SecondScene -