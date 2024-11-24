from manim import *

class AllShapes(Scene):
    def construct(self):
        # Nombre
        texto = Text("Jesús Enrique Lugo Ramírez", color=PURPLE)
        self.play(Create(texto))
        self.wait(1)
        self.play(FadeOut(texto))
        
        # Animación de figuras con un nuevo orden y colores
        self.anim(Arc(radius=0.5, color=PURPLE))  # Púrpura
        self.anim(ArcBetweenPoints([2, 0, 0], [-2, 0, 0], color=PINK))  # Rosa
        self.anim(CurvedArrow([2, 0, 0], [-2, 0, 0], color=YELLOW))  # Amarillo
        self.anim(CurvedDoubleArrow([2, 0, 0], [-2, 0, 0], color=TEAL))  # Verde azulado
        self.anim(Circle(color=RED, fill_opacity=1))  # Rojo
        self.anim(Dot(color=GREEN, fill_opacity=1))  # Verde
        self.anim(Dot(radius=0.05, color=ORANGE, fill_opacity=1))  # Naranja
        self.anim(Ellipse(color=GOLD, fill_opacity=1))  # Dorado
        self.anim(AnnularSector(color=MAROON, fill_opacity=1))  # Granate
        self.anim(Sector(color=BLUE, fill_opacity=1))  # Azul claro
        self.anim(Annulus(color=LIGHT_PINK, fill_opacity=1))  # Rosa claro
        self.anim(Line([2, 0, 0], [-2, 0, 0], color=GREEN, fill_opacity=1))  # Marrón claro
        self.anim(DashedLine([2, 0, 0], [-2, 0, 0], color=WHITE, fill_opacity=1))  # Blanco

        # Línea tangente que requiere un mobject
        c = Circle(color=YELLOW, fill_opacity=1)  # Amarillo
        self.play(Create(c))
        self.wait(1)
        self.anim(TangentLine(c, 0.2))
        self.play(FadeOut(c))

        # Otras figuras geométricas con un nuevo orden y colores
        self.anim(Elbow(color=BLUE))  # Azul
        self.anim(Arrow([2, 0, 0], [-2, 0, 0], color=YELLOW))  # Verde claro
        self.anim(Vector([1, 0, 0], color=PINK, fill_opacity=1))  # Rosa
        self.anim(DoubleArrow([2, 0, 0], [-2, 0, 0], color=RED, fill_opacity=1))  # Rojo
        self.anim(Polygon([2, 0, 0], [-2, 0, 0], [1, 1, 0], [-2, -3, 0], color=PURPLE, fill_opacity=1))  # Azul claro
        self.anim(RegularPolygon(n=5, color=GOLD, fill_opacity=1))  # Dorado
        self.anim(Triangle(color=PINK, fill_opacity=1))  # Rosa claro
        self.anim(ArrowTriangleTip(color=TEAL, fill_opacity=1))  # Verde azulado
        self.anim(Rectangle(color=PURPLE, fill_opacity=1))  # Púrpura
        self.anim(Square(color=RED, fill_opacity=1))  # Verde claro
        self.anim(RoundedRectangle(color=WHITE, fill_opacity=1))  # Blanco

    # Método para reproducir la creación y desaparición de los objetos
    def anim(self, mob):
        self.play(Create(mob))
        self.wait(1)
        self.play(FadeOut(mob))

#manim -pql tarea_lugo.py AllShapes -qh
