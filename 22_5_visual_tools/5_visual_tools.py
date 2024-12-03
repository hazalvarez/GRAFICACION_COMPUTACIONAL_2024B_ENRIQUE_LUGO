from manim import *

class UnifiedScene(Scene):
    def construct(self):

        self.camera.background_color = "#20958a"  # Establecer el fondo a blanco
        text = Text("GRAFICACICON COMPUTACIONAL \nActividad: 5_visual_tools \nPRESENTO: JESUS ENRIQUE LUGO RAMIREZ ")
        self.play(FadeIn(text))
        self.wait(3)
        self.play(FadeOut(text))


        # MoveBraces
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=",  # 0
            r"f(x)\frac{d}{dx}g(x)",   # 1
            r"+",                      # 2
            r"g(x)\frac{d}{dx}f(x)"    # 3
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text(r"$g'f$")
        t2 = brace2.get_text(r"$f'g$")
        self.play(GrowFromCenter(brace1), FadeIn(t1))
        self.wait()
        self.play(ReplacementTransform(brace1, brace2), ReplacementTransform(t1, t2))
        self.wait()
        self.play(FadeOut(*self.mobjects), run_time=2)

        # MoveBracesCopy
        self.clear()
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", r"+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        brace1 = Brace(text[1], UP, buff=SMALL_BUFF)
        brace2 = Brace(text[3], UP, buff=SMALL_BUFF)
        t1 = brace1.get_text(r"$g'f$")
        t2 = brace2.get_text(r"$f'g$")
        self.play(GrowFromCenter(brace1), FadeIn(t1))
        self.wait()
        self.play(ReplacementTransform(brace1.copy(), brace2), ReplacementTransform(t1.copy(), t2))
        self.wait()
        self.play(FadeOut(*self.mobjects), run_time=2)

        # MoveFrameBox
        self.clear()
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", r"+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait()
        self.play(FadeOut(*self.mobjects), run_time=2)

        # MoveFrameBoxCopy
        self.clear()
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", r"+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1.copy(), framebox2, path_arc=-PI))
        self.wait()
        self.play(FadeOut(*self.mobjects), run_time=2)

        # MoveFrameBoxCopy2
        self.clear()
        text = MathTex(
            r"\frac{d}{dx}f(x)g(x)=", r"f(x)\frac{d}{dx}g(x)", r"+",
            r"g(x)\frac{d}{dx}f(x)"
        )
        framebox1 = SurroundingRectangle(text[1], buff=0.1)
        framebox2 = SurroundingRectangle(text[3], buff=0.1)
        t1 = MathTex(r"g'f")
        t2 = MathTex(r"f'g")
        t1.next_to(framebox1, UP, buff=0.1)
        t2.next_to(framebox2, UP, buff=0.1)
        self.play(Write(text))
        self.play(Create(framebox1), FadeIn(t1))
        self.wait()
        self.play(ReplacementTransform(framebox1.copy(), framebox2), ReplacementTransform(t1.copy(), t2))
        self.wait()
        self.play(FadeOut(*self.mobjects), run_time=2)

        # Arrow1
        self.clear()
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        arrow = Arrow(LEFT, RIGHT)
        step1.move_to(LEFT * 2)
        arrow.next_to(step1, RIGHT, buff=0.1)
        step2.next_to(arrow, RIGHT, buff=0.1)
        self.play(Write(step1))
        self.wait()
        self.play(GrowArrow(arrow))
        self.play(Write(step2))
        self.wait()
        self.play(FadeOut(*self.mobjects), run_time=2)

        # Arrow2
        self.clear()
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = Arrow(step1.get_right(), step2.get_left(), buff=0.1, color=RED)
        arrow2 = Arrow(step1.get_top(), step2.get_bottom(), buff=0.1, color=BLUE)
        self.play(Write(step1), Write(step2))
        self.play(GrowArrow(arrow1))
        self.play(GrowArrow(arrow2))
        self.wait()
        self.play(FadeOut(*self.mobjects), run_time=2)

        # LineAnimation
        self.clear()
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = Line(step1.get_right(), step2.get_left(), buff=0.1, color=RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1, color=BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()
        self.play(FadeOut(*self.mobjects), run_time=2)

        # DashedLineAnimation
        self.clear()
        step1 = Text("Step 1")
        step2 = Text("Step 2")
        step1.move_to(LEFT * 2 + DOWN * 2)
        step2.move_to(4 * RIGHT + 2 * UP)
        arrow1 = DashedLine(step1.get_right(), step2.get_left(), buff=0.1, color=RED)
        arrow2 = Line(step1.get_top(), step2.get_bottom(), buff=0.1, color=BLUE)
        self.play(Write(step1), Write(step2))
        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.wait()
        self.play(FadeOut(*self.mobjects), run_time=2)



"""

manim -pql 5_visual_tools.py UnifiedScene -qh


"""