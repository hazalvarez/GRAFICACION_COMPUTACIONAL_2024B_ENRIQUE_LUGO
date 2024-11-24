from manim import *

class VectoresEscena(Scene):
    def construct(self):
        # Título principal
        titulo = Text("Ejemplos de Vectores Ortogonales y Paralelos")
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))

        titulo = Text("Presento: Jesus Enrique Lugo Ramirez")
        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))

        # Agregar un plano de coordenadas más amplio
        plano = NumberPlane(
            x_range=[-25, 25, 1],  # Rango en el eje x
            y_range=[-25, 25, 1],  # Rango en el eje y
            x_length=10,
            y_length=10,
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            }
        )
        self.play(Create(plano))

        # Ejemplo 1: Vectores Ortogonales
        ejemplo1_titulo = Text("Ejemplo 1: Vectores Ortogonales")
        ejemplo1_titulo.to_edge(UP)  # Colocar el título en la parte superior

        vector_a = np.array([4/5, -1/5, 0])
        vector_b = np.array([2/5, 8/5, 0])
        vec_a = Arrow(start=ORIGIN, end=vector_a, color=BLUE, buff=0)
        vec_b = Arrow(start=ORIGIN, end=vector_b, color=RED, buff=0)
        formula_ortogonal = MathTex("a_1 \\cdot b_1 + a_2 \\cdot b_2 = 0")
        resultado_ortogonal = MathTex("4 \\cdot 2 + (-1) \\cdot 8 = 0")
        resultado_texto = Text("Los vectores son ortogonales.")
        resultado_texto.to_edge(UP)

        # Animaciones en secuencia para el Ejemplo 1
        self.play(Write(ejemplo1_titulo))
        self.play(FadeOut(ejemplo1_titulo))
        self.play(GrowArrow(vec_a), GrowArrow(vec_b))
        self.play(Write(formula_ortogonal))
        self.play(Transform(formula_ortogonal, resultado_ortogonal))
        self.play(Write(resultado_texto))
        self.play(FadeOut(vec_a), FadeOut(vec_b), FadeOut(formula_ortogonal), FadeOut(resultado_texto))

        # Ejemplo 2: Vectores Paralelos
        ejemplo2_titulo = Text("Ejemplo 2: Vectores Paralelos")
        ejemplo2_titulo.to_edge(UP)
        vector_c = np.array([6/5, -18/5, 0])
        vector_d = np.array([-4/5, 12/5, 0])
        
        vec_c = Arrow(start=ORIGIN, end=vector_c, color=GREEN, buff=0)
        vec_d = Arrow(start=ORIGIN, end=vector_d, color=YELLOW, buff=0)
        formula_paralelo = MathTex("\\frac{a_1}{b_1} = \\frac{a_2}{b_2}")
        resultado_paralelo = MathTex("\\frac{6}{-4} = \\frac{-18}{12} = -1.5")
        resultado_texto2 = Text("Los vectores son paralelos.")
        resultado_texto2.to_edge(UP)

        # Animaciones en secuencia para el Ejemplo 2
        self.play(Write(ejemplo2_titulo))
        self.play(FadeOut(ejemplo2_titulo))
        self.play(GrowArrow(vec_c), GrowArrow(vec_d))
        self.play(Write(formula_paralelo))
        self.play(Transform(formula_paralelo, resultado_paralelo))
        self.play(Write(resultado_texto2))
        self.play(FadeOut(vec_c), FadeOut(vec_d), FadeOut(formula_paralelo), FadeOut(resultado_texto2))

        # Finalización con agradecimiento
        gracias = Text("Gracias")
        self.play(Write(gracias))
        self.wait(2)
        self.play(FadeOut(gracias))

# Para ejecutar este código, guarda este script como 'vectores_manim.py' y en la terminal usa:
# manim -pql vectores_manim.py VectoresEscena

