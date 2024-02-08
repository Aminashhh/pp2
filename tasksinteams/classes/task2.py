class MyShape:
    def __init__(self, color="red", is_filled=True):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"{self.color}({'Filled' if self.is_filled else 'Not Filled'})"


    def getArea(self):
        return 0


class Rectangle(MyShape):
    def __init__(self, color="red", is_filled=True, x_top_left=0, y_top_left=0, length=1, width=1):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def getArea(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle: {super().__str__()}, Top Left: ({self.x_top_left}, {self.y_top_left}), Length: {self.length}, Width: {self.width}"


class Circle(MyShape):
    def __init__(self, color="red", is_filled=True, x_center=0, y_center=0, radius=1):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def getArea(self):
        return 3.14 * self.radius ** 2

    def __str__(self):
        return f"Circle: {super().__str__()}, Center: ({self.x_center}, {self.y_center}), Radius: {self.radius}"

color_input = input("Enter color : ")
is_filled_input = input("Is Rectangle filled? (True/False): ")
x_top_left_input = float(input("Enter x_top_left : "))
y_top_left_input = float(input("Enter y_top_left : "))
length_input = float(input("Enter length : "))
width_input = float(input("Enter width: "))

rectangle = Rectangle(color=color_input, is_filled=is_filled_input,
                               x_top_left=x_top_left_input, y_top_left=y_top_left_input,
                               length=length_input, width=width_input)

print(rectangle)
print(f"Area: {rectangle.getArea()}")