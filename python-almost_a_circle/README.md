python-almost_a_circle

For this particular project, I created three interconnected classes in Python to represent rectangles and squares, using my skills in object-oriented programming. To ensure their proper functionality, I wrote a test suite using the unittest module, containing three independently-developed test files. 

The three classes utilize several tools in Python, including import exceptions, private attributes, getter/setter methods, class/static methods, inheritance, file input/output, and serialization/deserialization with JSON and CSV formats.

The first class, "Base," serves as the base class for all other classes in the project. It contains private and public instance attributes, a constructor, static and class methods for handling serialization and deserialization of objects, and methods for creating and loading objects from files. It also includes a method for drawing Rectangle and Square instances in a GUI window using the turtle module.

The second class, "Rectangle," represents a rectangle and inherits from Base. It has private instance attributes for width, height, x, and y, each with its own getter/setter methods. It also has methods for computing the area of the rectangle, displaying it on the console, updating its attributes, and returning a dictionary representation of the object.

The third class, "Square," represents a square and inherits from Rectangle. It has a constructor that sets the width and height to the same value, as well as methods for updating attributes and returning a dictionary representation of the object. 

Overall, the project demonstrates the use of object-oriented programming concepts and tools in Python for creating interconnected classes representing geometric shapes.
