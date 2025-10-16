from abc import ABC, abstractmethod
import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    # 1) Overload common operators - Arithmetic operator overloading 
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.__x + other.__x, self.__y + other.__y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.__x - other.__x, self.__y - other.__y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.__x * other.__x, self.__y * other.__y)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Point):
            return Point(self.__x / other.__x, self.__y / other.__y)
        return NotImplemented

    # 1) Overload common operators - Comparison operator overloading 
    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.__x, self.__y) < (other.__x, other.__y)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Point):
            return (self.__x, self.__y) <= (other.__x, other.__y)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Point):
            return (self.__x, self.__y) > (other.__x, other.__y)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Point):
            return (self.__x, self.__y) >= (other.__x, other.__y)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.__x, self.__y) == (other.__x, other.__y)
        return NotImplemented

    def distanceToPoint(self, other):
        if isinstance(other, Point):
            dx = self.__x - other.__x
            dy = self.__y - other.__y
            return math.sqrt(dx**2 + dy**2)
        return NotImplemented
    # distanceToO(): compute the distance from the point to O
    def distanceToO(self):
        return math.sqrt(self.__x**2 + self.__y**2)

    def __str__(self):
        return f"Point({self.__x}, {self.__y})"


class Shape(ABC):
    def __init__(self, point):
        self._point = point

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return math.isclose(self.area(), other.area(), rel_tol=1e-9)

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    # 3) Compute the perimeter of a shape
    @abstractmethod
    def p(self):
        pass

    # 4) Compute the perimeter of a shape
    @abstractmethod
    def area(self):
        pass

    # 6) Check whether a given point (p) is inside a shape?
    @abstractmethod
    def inside(self, p):
        pass


class Rectangle(Shape):
    def __init__(self, point, w, h):
        super().__init__(point)
        self.__w = w
        self.__h = h

    def p(self):
        return 2 * (self.__w + self.__h)

    def area(self):
        return self.__w * self.__h

    def inside(self, p):
        if isinstance(p, Point):
            x, y = self._point.getX(), self._point.getY()
            px, py = p.getX(), p.getY()
            return x <= px <= x + self.__w and y <= py <= y + self.__h
        return NotImplemented

    def __str__(self):
        return f"Rectangle(w={self.__w}, h={self.__h}, area={self.area():.2f})"


class Square(Rectangle):
    def __init__(self, point, side):
        super().__init__(point, side, side)

    def __str__(self):
        return f"Square(side={self.area() ** 0.5:.2f}, area={self.area():.2f})"


class Circle(Shape):
    def __init__(self, point, radius):
        super().__init__(point)
        self.__radius = radius

    def p(self):
        return 2 * math.pi * self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def inside(self, p):
        if isinstance(p, Point):
            return self._point.distanceToPoint(p) <= self.__radius
        return NotImplemented

    def __str__(self):
        return f"Circle(radius={self.__radius}, area={self.area():.2f})"

# -----------TEST-----------  
if __name__ == "__main__":
    print("=== TEST POINT CLASS ===")
    p1 = Point(2, 3)
    p2 = Point(5, 7)
    p3 = Point(-1, 4)

    print("p1:", p1)
    print("p2:", p2)
    print("p3:", p3)
    print("\n-- Arithmetic operations --")
    print("p1 + p2 =", p1 + p2)
    print("p2 - p1 =", p2 - p1)
    print("p1 * p2 =", p1 * p2)
    print("p2 / p1 =", p2 / p1)
    print("\n-- Comparisons --")
    print("p1 < p2:", p1 < p2)
    print("p1 <= p2:", p1 <= p2)
    print("p1 > p2:", p1 > p2)
    print("p1 >= p2:", p1 >= p2)
    print("p1 == p2:", p1 == p2)
    print("p1 == Point(2,3):", p1 == Point(2, 3))
    print("\n-- Distance --")
    print("Distance p1→p2:", f"{p1.distanceToPoint(p2):.2f}")
    print("Distance p1→O:", f"{p1.distanceToO():.2f}")

    print("\n=== TEST SHAPE CLASSES ===")
    rect = Rectangle(Point(0, 0), 10, 5)
    sq = Square(Point(0, 0), 6)
    circ = Circle(Point(0, 0), 5)

    print(rect)
    print(sq)
    print(circ)

    print("\n-- Perimeter and Area --")
    print("Rectangle perimeter:", rect.p())
    print("Square perimeter:", sq.p())
    print("Circle perimeter:", f"{circ.p():.2f}")

    print("\n-- Point containment --")
    test_points = [Point(2, 2), Point(11, 4), Point(5, 5)]
    for p in test_points:
        print(f"{p} inside rect? {rect.inside(p)}")
        print(f"{p} inside circle? {circ.inside(p)}")

    print("\n-- Shape comparisons by area --")
    print("rect > sq:", rect > sq)
    print("rect < sq:", rect < sq)
    print("sq == rect:", sq == rect)
    print("circ > sq:", circ > sq)
    print("circ <= rect:", circ <= rect)
