from manim import *

class MyScene(Scene):
    """A simple scene showing basic shapes and text"""
    def construct(self):
        # Create a circle and square
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        
        # Position them
        square.next_to(circle, LEFT, buff=1)
        
        # Add text
        text = Text("Hello from Manim!", color=GREEN)
        text.next_to(circle, DOWN, buff=1)
        
        # Animate
        self.play(Create(circle), Create(square))
        self.play(Write(text))
        self.wait(1)
        
        # Transform circle into square
        self.play(Transform(circle, square.copy()))
        self.wait(1)
