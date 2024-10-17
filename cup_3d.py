from manim import *

class Cup3DScene(ThreeDScene):
    def construct(self):
        # Set up 3D axes
        axes = ThreeDAxes()

        # Define the parametric curve for the cup's profile (rotated around y-axis)
        def cup_profile(u, v):
            radius = 1 + (u - 1) * 0.3  # Curve for the cup
            height = u
            return np.array([radius * np.cos(v), height, radius * np.sin(v)])

        # Create the surface (the body of the cup)
        cup_surface = Surface(
            lambda u, v: cup_profile(u, v),
            u_range=[0, 3],  # Height of the cup
            v_range=[0, TAU],  # Full rotation around the y-axis
            fill_opacity=0.75,
            checkerboard_colors=[BLUE_E, BLUE_D],
        )

        # Adding the handle of the cup
        handle = ParametricFunction(
            lambda t: np.array([
                1.5 * np.cos(t) + 1.5,  # Adjust to position it relative to the cup
                1.5 + np.sin(t),  # Adjust to height
                0.7 * np.sin(t)  # Smaller radius for the handle
            ]),
            t_range=[-PI / 2, PI / 2],
            color=WHITE,
            stroke_width=6
        )

        # Set up camera
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        
        # Add cup and handle to scene
        self.add(axes, cup_surface, handle)

        # Animate rotating the cup to give a 3D view
        self.play(Rotate(cup_surface, angle=PI, axis=UP, run_time=5))
        self.wait(1)

        # Instead of using self.camera.animate, use self.move_camera
        self.move_camera(phi=PI / 2, theta=PI / 3, run_time=10)
        self.wait()



