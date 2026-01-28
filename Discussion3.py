import math
"""Problem 1. Create the constructor "__init__" method
with arguments width (an integer), height (an integer)
(1) It sets an instance variable, "width" to the passed argument, width
(2) It sets an instance variable, "height" to the passed argument, height
Problem 2. Create the "__str__" method
It returns a string, "A rectangle with width <width> and height
<height>"
for example, "A rectangle with width 3 and height 6
Problem 3. Create the "area_calculator" method
It returns the area of the rectangle (float)
Area of rectangle = length × width.
Problem 4. Create the "__eq__" method with two
arguments: self and other (an object)
It returns a boolean
True if the two rectangles have the same width
and the same height
False otherwise
"""
class Rectangle():
    # Create the constructor "__init__" method
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # YOUR CODE HERE



    # Create the "__str__" method
    def __str__(self):
        return f"A rectangle with width {self.width} and height {self.height}"

    # Create the "area_calculator" method
    def area_calculator(self):
        return float(self.width * self.height)
    


    # Create the "__eq__" method
    def __eq__(self, other):
        return self.width == other.width and self.height == other.height
        
    # 
    # Returns a boolean value

    # YOUR CODE HERE


    
    
    
    def main():
        r1 = Rectangle(10, 10)
    # call the __str__ method
        print(r1)
    # call the area_calculator method
        print("Area:", r1.area_calculator())


        r2 = Rectangle(10, 15)
        print(r2)
        print("Area:", r2.area_calculator())
    # call the __eq__ method
        print(r1 == r2)
        print()

    # you can create additional rectangle objects to 
    # test your code or learn more about how the class behaves
        pass

    if __name__ == "__main__":
        main()