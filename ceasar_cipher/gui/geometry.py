from gui import styles

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __mul__(self, multiplier):
        if not isinstance(multiplier, (int, float)):
            raise TypeError("Can't multiply a vector with a non real number")

        x = self.x * multiplier
        y = self.y * multiplier
        return Vector(x, y)


    __rmul__ = __mul__


    def __floordiv__(self, divisor):
        float_vector = self * (1/divisor)
        return Vector(int(float_vector.x), int(float_vector.y))


    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError(f"Can't add a vector with a {type(other)}")
        return Vector(self.x + other.x, self.y + other.y)


    def __sub__(self, other):
        return self + (-1) * other

class GeometryBuilder():
    def __init__(self, screen):
        width, height = styles.DEFAULT_RESOLUTION
        self._shape = Vector(width, height)
        self._screen = screen
        self._position = Vector(0, 0)


    def shape(self, width, height):
        self._shape = Vector(width, height)
        return self


    def position(self, x, y):
        self._position = Vector(x, y)
        return self


    def center(self):
        screen_width = self._screen.winfo_screenwidth()
        screen_height = self._screen.winfo_screenheight()
        screen_vector = Vector(screen_width, screen_height)
        center_position = screen_vector // 2 - self._shape // 2
        self._position = center_position
        return self


    def build(self):
        shape_string = f"{self._shape.x}x{self._shape.y}"
        position_string = f"{self._position.x}+{self._position.y}"
        return f"{shape_string}+{position_string}"
