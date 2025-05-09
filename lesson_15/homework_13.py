class Rhombus:
    def __init__(self, side_a: float, angle_a: float):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError("The side of the rhombus must be greater than 0.")
        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError("The angle of the rhombus should be between 0 and 180 degrees")

            object.__setattr__(self, "angle_b", 180 - value)
        object.__setattr__(self, name, value)

    def __str__(self):
        return (f"Rhombus: side a = {self.side_a}, "
                f"angle a = {self.angle_a} degrees, "
                f"angle b = {self.angle_b} degrees")


diamond = Rhombus(35, 37)
print(diamond)
