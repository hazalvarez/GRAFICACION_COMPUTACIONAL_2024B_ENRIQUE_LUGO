from manim import *
import numpy as np

class CombinedPlots(Scene):
    def construct(self):

        self.camera.background_color = "#20958a"  # Establecer el fondo a blanco
        text = Text("GRAFICACICON COMPUTACIONAL \nActividad: 6a_plots_2D \nPRESENTO: JESUS ENRIQUE LUGO RAMIREZ ")
        self.play(FadeIn(text))
        self.wait(3)
        self.play(FadeOut(text))

        # PlotGraph
        y_max = 50
        y_min = 20
        x_max = 7
        x_min = 4
        y_tick_frequency = 5
        x_tick_frequency = 0.5
        axes_color = BLUE
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            axis_config={"color": axes_color},
        )
        axes_labels = axes.get_axis_labels(x_label=Tex("x"), y_label=Tex("y"))
        axes.x_axis.add_numbers([4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])
        axes.y_axis.add_numbers([30, 40, 50])
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[5, 7])
        p = Dot().move_to(axes.c2p(x_min, y_min))
        
        self.play(FadeIn(axes), FadeIn(axes_labels), FadeIn(p))
        self.play(Create(graph), run_time=2)
        self.play(FadeOut(axes), FadeOut(axes_labels), FadeOut(p), FadeOut(graph))
        
        # Plot1
        axes = Axes(
            x_range=[0, 7, 0.5],
            y_range=[0, 50, 5],
            axis_config={"color": axes_color},
            tips=False
        )
        axes_labels = axes.get_axis_labels(x_label=Tex("x"), y_label=Tex("y"))
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[2, 4])
        
        self.play(FadeIn(axes), FadeIn(axes_labels))
        self.play(Create(graph), run_time=2)
        self.play(FadeOut(axes), FadeOut(axes_labels), FadeOut(graph))
        
        # Plot1v2
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 5],
            axis_config={"color": axes_color},
            tips=False
        ).scale(0.5).to_corner(UR)
        axes_labels = axes.get_axis_labels(x_label=Tex("x"), y_label=Tex("y"))
        graph = axes.plot(lambda x: x**2, color=GREEN, x_range=[2, 4])
        
        self.play(FadeIn(axes), FadeIn(axes_labels), Create(graph), run_time=2)
        self.play(FadeOut(axes), FadeOut(axes_labels), FadeOut(graph))
        
        # Plot2
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 5],
            axis_config={"color": axes_color},
            tips=False
        )
        axes_labels = axes.get_axis_labels(x_label=Tex("t"), y_label=Tex("f(t)"))
        graph = axes.plot(lambda x: x**2, color=GREEN)
        
        self.play(FadeIn(axes), FadeIn(axes_labels))
        self.play(Create(graph), run_time=2)
        self.play(FadeOut(axes), FadeOut(axes_labels), FadeOut(graph))
        
        # Plot3
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 5],
            axis_config={"color": axes_color},
            tips=False
        )
        axes_labels = axes.get_axis_labels(x_label=Tex("x"), y_label=Tex("y"))
        graph = axes.plot(lambda x: x**2, color=GREEN)
        
        self.play(FadeIn(axes), FadeIn(axes_labels))
        self.play(Create(graph), run_time=2)
        self.play(FadeOut(axes), FadeOut(axes_labels), FadeOut(graph))
        
        # Plot4
        axes = Axes(
            x_range=[0, 7, 1],
            y_range=[0, 50, 10],
            axis_config={"color": axes_color},
            tips=False
        )
        axes_labels = axes.get_axis_labels(x_label=Tex("x"), y_label=Tex("y"))
        graph = axes.plot(lambda x: x**2, color=GREEN)
        
        self.play(FadeIn(axes), FadeIn(axes_labels))
        self.play(Create(graph), run_time=2)
        self.play(FadeOut(axes), FadeOut(axes_labels), FadeOut(graph))
        
        # Plot5
        axes = Axes(
            x_range=[0, 7, 0.5],
            y_range=[0, 50, 10],
            axis_config={"color": axes_color},
            tips=False
        )
        x_labels = VGroup(
            Tex("3.5").scale(0.7).next_to(axes.coords_to_point(3.5, 0), DOWN),
            MathTex("\\frac{9}{2}").scale(0.7).next_to(axes.coords_to_point(4.5, 0), DOWN)
        )
        axes_labels = axes.get_axis_labels(x_label=Tex("x"), y_label=Tex("y"))
        graph = axes.plot(lambda x: x**2, color=GREEN)
        
        self.play(FadeIn(axes), FadeIn(x_labels), FadeIn(axes_labels))
        self.play(Create(graph))
        self.play(FadeOut(axes), FadeOut(x_labels), FadeOut(axes_labels), FadeOut(graph))
        
        # Plot6
        axes = Axes(
            x_range=[0, 7, 0.5],
            y_range=[0, 50, 10],
            axis_config={"color": axes_color},
            tips=False
        )
        values_x = [
            (0, "0"),
            (0.5, "0.5"),
            (1, "1"),
            (1.5, "1.5"),
            (3.35, "3.35")
        ]
        x_labels = VGroup(
            *[MathTex(x_tex).scale(0.7).next_to(axes.coords_to_point(x_val, 0), DOWN) for x_val, x_tex in values_x]
        )
        axes_labels = axes.get_axis_labels(x_label=Tex("x"), y_label=Tex("y"))
        graph = axes.plot(lambda x: x**2, color=GREEN)
        
        self.play(FadeIn(axes), FadeIn(x_labels), FadeIn(axes_labels))
        self.play(Create(graph), run_time=2)
        self.play(FadeOut(axes), FadeOut(x_labels), FadeOut(axes_labels), FadeOut(graph))
        
        # PlotSinCos
        y_max = 1.5
        y_min = -1.5
        x_max = 3 * np.pi / 2
        x_min = -3 * np.pi / 2
        y_tick_frequency = 0.5
        x_tick_frequency = np.pi / 2
        axes_color = YELLOW
        axes_color_2 = RED
        
        axes = Axes(
            x_range=[x_min, x_max, x_tick_frequency],
            y_range=[y_min, y_max, y_tick_frequency],
            y_axis_config={"color": axes_color},
            x_axis_config={"color": axes_color_2},
            tips=False
        )
        values_y = [(1, "1"), (-1, "-1")]
        y_labels = VGroup(
            *[MathTex(y_tex).scale(0.7).next_to(axes.c2p(0, y_val), LEFT) for y_val, y_tex in values_y]
        )
        values_x = [
            ("-\\frac{3\\pi}{2}", -3 * np.pi / 2),
            ("-\\pi", -np.pi),
            ("-\\frac{\\pi}{2}", -np.pi / 2),
            ("0", 0),
            ("\\frac{\\pi}{2}", np.pi / 2),
            ("\\pi", np.pi),
            ("\\frac{3\\pi}{2}", 3 * np.pi / 2)
        ]
        x_labels = VGroup(
            *[MathTex(label).scale(0.7).next_to(axes.c2p(value, 0), DOWN) for label, value in values_x]
        )
        plotSin = axes.plot(lambda x: np.sin(x), color=GREEN)
        plotCos = axes.plot(lambda x: np.cos(x), color=GRAY)
        axes_labels = axes.get_axis_labels(
            x_label=MathTex("\\theta"), y_label=MathTex("\\sin(\\theta)")
        )
        
        self.play(FadeIn(axes), FadeIn(x_labels), FadeIn(y_labels), FadeIn(axes_labels))
        self.play(Create(plotSin), Create(plotCos), run_time=2)
        self.play(FadeOut(axes), FadeOut(x_labels), FadeOut(y_labels), FadeOut(axes_labels), FadeOut(plotSin), FadeOut(plotCos))

"""
CombinedPlots

manim -pql 6a_plots_2D.py CombinedPlots 

"""