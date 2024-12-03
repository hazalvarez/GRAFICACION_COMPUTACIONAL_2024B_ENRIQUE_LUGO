from manim import *

class CombinedScenes(ThreeDScene):
    def construct(self):

        self.camera.background_color = "#20958a"  # Establecer el fondo a blanco
        text = Text("GRAFICACICON COMPUTACIONAL \nActividad: 6b_plots_3D \nPRESENTO: JESUS ENRIQUE LUGO RAMIREZ ")
        self.play(FadeIn(text))
        self.wait(3)
        self.play(FadeOut(text))


        # Escena 1: CameraPosition1
        axes1 = ThreeDAxes()
        circle1 = Circle()
        self.play(FadeIn(axes1))
        self.play(Create(circle1))
        self.wait()
        self.play(FadeOut(axes1, circle1))

        # Escena 2: CameraPosition2
        axes2 = ThreeDAxes()
        circle2 = Circle()
        self.set_camera_orientation(phi=30 * DEGREES, theta=45 * DEGREES)
        self.play(FadeIn(axes2))
        self.play(Create(circle2))
        self.wait()
        self.play(FadeOut(axes2, circle2))

        # Escena 3: CameraPosition3
        axes3 = ThreeDAxes()
        circle3 = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)
        self.play(FadeIn(axes3))
        self.play(Create(circle3))
        self.wait()
        self.play(FadeOut(axes3, circle3))

        # Escena 4: CameraPosition4
        axes4 = ThreeDAxes(x_range=[-5, 5], y_range=[-5, 5], z_range=[-2, 2])
        circle4 = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6)
        self.play(FadeIn(axes4))
        self.play(Create(circle4))
        self.wait()
        self.play(FadeOut(axes4, circle4))

        # Escena 5: CameraPosition5
        axes5 = ThreeDAxes()
        circle5 = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6, gamma=30 * DEGREES)
        self.play(FadeIn(axes5))
        self.play(Create(circle5))
        self.wait()
        self.play(FadeOut(axes5, circle5))

        # Escena 6: MoveCamera1
        axes6 = ThreeDAxes()
        circle6 = Circle()
        self.play(FadeIn(axes6))
        self.play(Create(circle6))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait()
        self.play(FadeOut(axes6, circle6))

        # Escena 7: MoveCamera2
        axes7 = ThreeDAxes()
        circle7 = Circle()
        self.set_camera_orientation(phi=80 * DEGREES)
        self.play(FadeIn(axes7))
        self.play(Create(circle7))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=80 * DEGREES, theta=-PI / 2)
        self.wait()
        self.play(FadeOut(axes7, circle7))

        # Escena 8: ParametricCurve1
        axes8 = ThreeDAxes()
        curve1 = VMobject().set_points_as_corners([
            [1.2 * np.cos(u), 1.2 * np.sin(u), u / 2]
            for u in np.linspace(-TAU, TAU, 100)
        ])
        self.play(FadeIn(axes8))
        self.play(Create(curve1))
        self.wait()
        self.play(FadeOut(axes8, curve1))

        # Escena 9: ParametricCurve2
        axes9 = ThreeDAxes()
        curve2 = VMobject().set_points_as_corners([
            [1.2 * np.cos(u), 1.2 * np.sin(u), u]
            for u in np.linspace(-TAU, TAU, 100)
        ]).set_shade_in_3d(True)
        self.play(FadeIn(axes9))
        self.play(Create(curve2))
        self.wait()
        self.play(FadeOut(axes9, curve2))

        # Escena 10: SurfacesAnimation
        axes10 = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            u_range=[-PI / 2, PI / 2],
            v_range=[0, TAU],
            checkerboard_colors=[RED_D, RED_E],
            resolution=(20, 40)
        ).scale(2).set_shade_in_3d(True)
        self.play(FadeIn(axes10))
        self.play(Write(sphere))
        self.wait()
        self.play(FadeOut(axes10, sphere))

        # Escena 11: Text3D1
        axes11 = ThreeDAxes()
        text3d1 = Tex("This is a 3D text").scale(2).set_shade_in_3d(True)
        text3d1.rotate(PI / 2, axis=RIGHT)
        self.play(FadeIn(axes11, text3d1))
        self.wait()
        self.play(FadeOut(axes11, text3d1))

        # Escena 12: Text3D2
        axes12 = ThreeDAxes()
        text3d2 = Text("This is a 3D text").scale(2).rotate(PI/2, axis=RIGHT)
        self.play(FadeIn(axes12, text3d2))
        self.wait()
        self.play(FadeOut(axes12, text3d2))

"""

manim -pql 6b_plots_3D.py CombinedScenes -qh


"""