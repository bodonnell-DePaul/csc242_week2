"""
In-Class Exercises - Week 2
CSC 242 - Advanced Class Concepts

Interactive exercises for 180-minute class period covering:
- Inheritance hierarchies
- Method overriding and super()
- Operator overloading
- Container classes
- Polymorphism

Author: CSC 242 Teaching Team
"""


# ============================================================================
# EXERCISE 1: SHAPE HIERARCHY (30 minutes)
# ============================================================================

print("🔷 EXERCISE 1: Shape Hierarchy Implementation")
print("=" * 60)
print("Goal: Create a shape hierarchy with inheritance and method overriding")
print()

class Shape:
    """Base class for all shapes"""
    
    def __init__(self, name, color="white"):
        """Initialize shape with name and color"""
        # TODO: Implement constructor
        pass
    
    def area(self):
        """Calculate area - must be overridden by subclasses"""
        # TODO: Raise NotImplementedError with appropriate message
        pass
    
    def perimeter(self):
        """Calculate perimeter - must be overridden by subclasses"""
        # TODO: Raise NotImplementedError with appropriate message
        pass
    
    def describe(self):
        """Return description of the shape"""
        # TODO: Return formatted string with name, color, area, and perimeter
        pass
    
    def __str__(self):
        """String representation"""
        # TODO: Return human-readable representation
        pass


class Rectangle(Shape):
    """Rectangle shape implementation"""
    
    def __init__(self, width, height, color="white"):
        """Initialize rectangle with width, height, and color"""
        # TODO: Call parent constructor and set width/height
        pass
    
    def area(self):
        """Calculate rectangle area"""
        # TODO: Implement area calculation
        pass
    
    def perimeter(self):
        """Calculate rectangle perimeter"""
        # TODO: Implement perimeter calculation
        pass


class Circle(Shape):
    """Circle shape implementation"""
    
    def __init__(self, radius, color="white"):
        """Initialize circle with radius and color"""
        # TODO: Call parent constructor and set radius
        pass
    
    def area(self):
        """Calculate circle area"""
        # TODO: Implement area calculation (π * r²)
        import math
        pass
    
    def perimeter(self):
        """Calculate circle circumference"""
        # TODO: Implement perimeter calculation (2 * π * r)
        import math
        pass


class Triangle(Shape):
    """Triangle shape implementation"""
    
    def __init__(self, side1, side2, side3, color="white"):
        """Initialize triangle with three sides and color"""
        # TODO: Call parent constructor and set sides
        # TODO: Validate that sides can form a triangle
        pass
    
    def area(self):
        """Calculate triangle area using Heron's formula"""
        # TODO: Implement Heron's formula
        # s = (a + b + c) / 2
        # area = sqrt(s * (s-a) * (s-b) * (s-c))
        import math
        pass
    
    def perimeter(self):
        """Calculate triangle perimeter"""
        # TODO: Implement perimeter calculation
        pass


# Exercise 1 Instructions for Students:
print("""
EXERCISE 1 TASKS:
1. Complete the Shape base class:
   - Constructor should store name and color
   - area() and perimeter() should raise NotImplementedError
   - describe() should return formatted string with shape info
   - __str__() should return the shape's name

2. Complete Rectangle class:
   - Constructor should call super().__init__() properly
   - Implement area() and perimeter() methods
   - Store width and height as instance variables

3. Complete Circle class:
   - Constructor should call super().__init__() properly
   - Implement area() and perimeter() methods
   - Store radius as instance variable
   - Use math.pi for calculations

4. Complete Triangle class:
   - Constructor should validate triangle inequality
   - Implement area() using Heron's formula
   - Implement perimeter() method
   - Store three sides as instance variables

5. Test your implementation:
""")

def test_shapes():
    """Test the shape hierarchy"""
    print("\n🧪 Testing Shape Hierarchy:")
    
    try:
        # Create shapes
        rect = Rectangle(5, 3, "blue")
        circle = Circle(4, "red")
        triangle = Triangle(3, 4, 5, "green")
        
        shapes = [rect, circle, triangle]
        
        for shape in shapes:
            print(f"  {shape.describe()}")
        
        print("✅ All tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Complete the implementation above!")

# Uncomment when ready to test:
# test_shapes()


# ============================================================================
# EXERCISE 2: MATH VECTOR CLASS (25 minutes)
# ============================================================================

print("\n" + "=" * 60)
print("🔷 EXERCISE 2: Math Vector with Operator Overloading")
print("=" * 60)
print("Goal: Create a Vector class with full operator support")
print()

class Vector:
    """Mathematical vector with operator overloading"""
    
    def __init__(self, *components):
        """Initialize vector with components"""
        # TODO: Store components as a list or tuple
        pass
    
    def __add__(self, other):
        """Vector addition: v1 + v2"""
        # TODO: Implement vector addition
        # Check dimensions match, add corresponding components
        pass
    
    def __sub__(self, other):
        """Vector subtraction: v1 - v2"""
        # TODO: Implement vector subtraction
        pass
    
    def __mul__(self, scalar):
        """Scalar multiplication: v * scalar"""
        # TODO: Implement scalar multiplication
        pass
    
    def __rmul__(self, scalar):
        """Right scalar multiplication: scalar * v"""
        # TODO: Implement right multiplication (call __mul__)
        pass
    
    def __truediv__(self, scalar):
        """Scalar division: v / scalar"""
        # TODO: Implement scalar division
        pass
    
    def __neg__(self):
        """Vector negation: -v"""
        # TODO: Implement negation (multiply by -1)
        pass
    
    def __abs__(self):
        """Vector magnitude: abs(v)"""
        # TODO: Calculate magnitude (sqrt of sum of squares)
        import math
        pass
    
    def __eq__(self, other):
        """Vector equality: v1 == v2"""
        # TODO: Check if all components are equal
        pass
    
    def __len__(self):
        """Vector dimension: len(v)"""
        # TODO: Return number of components
        pass
    
    def __getitem__(self, index):
        """Vector indexing: v[i]"""
        # TODO: Return component at index
        pass
    
    def __setitem__(self, index, value):
        """Vector assignment: v[i] = value"""
        # TODO: Set component at index
        pass
    
    def dot(self, other):
        """Dot product of two vectors"""
        # TODO: Calculate dot product (sum of component products)
        pass
    
    def normalize(self):
        """Return unit vector in same direction"""
        # TODO: Return vector divided by its magnitude
        pass
    
    def __str__(self):
        """Human-readable representation"""
        # TODO: Return formatted string like "Vector(1, 2, 3)"
        pass
    
    def __repr__(self):
        """Developer representation"""
        # TODO: Return string that could recreate the object
        pass


# Exercise 2 Instructions:
print("""
EXERCISE 2 TASKS:
1. Complete the Vector constructor to store components
2. Implement arithmetic operators (+, -, *, /, -)
3. Implement comparison operator (==)
4. Implement sequence protocol (__len__, __getitem__, __setitem__)
5. Implement mathematical methods (dot product, magnitude, normalize)
6. Test your implementation:
""")

def test_vectors():
    """Test the Vector class"""
    print("\n🧪 Testing Vector Class:")
    
    try:
        # Create vectors
        v1 = Vector(1, 2, 3)
        v2 = Vector(4, 5, 6)
        
        print(f"  v1 = {v1}")
        print(f"  v2 = {v2}")
        print(f"  v1 + v2 = {v1 + v2}")
        print(f"  v1 - v2 = {v1 - v2}")
        print(f"  v1 * 2 = {v1 * 2}")
        print(f"  |v1| = {abs(v1):.2f}")
        print(f"  v1 · v2 = {v1.dot(v2)}")
        
        print("✅ All tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Complete the implementation above!")

# Uncomment when ready to test:
# test_vectors()


# ============================================================================
# EXERCISE 3: CUSTOM CONTAINER (40 minutes)
# ============================================================================

print("\n" + "=" * 60)
print("🔷 EXERCISE 3: Custom SmartList Container")
print("=" * 60)
print("Goal: Create a smart list with advanced features")
print()

class SmartList:
    """A list with enhanced functionality"""
    
    def __init__(self, items=None):
        """Initialize with optional items"""
        # TODO: Initialize internal list
        pass
    
    def append(self, item):
        """Add item to end"""
        # TODO: Add item to internal list
        pass
    
    def prepend(self, item):
        """Add item to beginning"""
        # TODO: Insert item at index 0
        pass
    
    def insert_sorted(self, item):
        """Insert item in sorted position"""
        # TODO: Find correct position and insert
        pass
    
    def remove_duplicates(self):
        """Remove duplicate items while preserving order"""
        # TODO: Remove duplicates, keep first occurrence
        pass
    
    def filter(self, predicate):
        """Return new SmartList with items matching predicate"""
        # TODO: Apply predicate function to filter items
        pass
    
    def map(self, function):
        """Return new SmartList with function applied to each item"""
        # TODO: Apply function to each item
        pass
    
    def reduce(self, function, initial=None):
        """Reduce list to single value using function"""
        # TODO: Implement reduce operation
        pass
    
    def chunk(self, size):
        """Split list into chunks of given size"""
        # TODO: Return list of SmartList chunks
        pass
    
    def reverse(self):
        """Reverse the list in place"""
        # TODO: Reverse internal list
        pass
    
    def sort(self, key=None, reverse=False):
        """Sort the list in place"""
        # TODO: Sort internal list
        pass
    
    def find(self, item):
        """Find index of item, return -1 if not found"""
        # TODO: Find item index
        pass
    
    def count(self, item):
        """Count occurrences of item"""
        # TODO: Count item occurrences
        pass
    
    # Implement container protocol
    def __len__(self):
        """Length of list"""
        # TODO: Return length
        pass
    
    def __getitem__(self, index):
        """Get item by index or slice"""
        # TODO: Support indexing and slicing
        pass
    
    def __setitem__(self, index, value):
        """Set item by index"""
        # TODO: Set item at index
        pass
    
    def __delitem__(self, index):
        """Delete item by index"""
        # TODO: Delete item at index
        pass
    
    def __contains__(self, item):
        """Check if item is in list"""
        # TODO: Check membership
        pass
    
    def __iter__(self):
        """Make iterable"""
        # TODO: Return iterator
        pass
    
    def __add__(self, other):
        """Concatenate lists: list1 + list2"""
        # TODO: Concatenate with another SmartList
        pass
    
    def __mul__(self, times):
        """Repeat list: list * n"""
        # TODO: Repeat list n times
        pass
    
    def __eq__(self, other):
        """Check equality"""
        # TODO: Compare lists for equality
        pass
    
    def __str__(self):
        """String representation"""
        # TODO: Return formatted string
        pass
    
    def __repr__(self):
        """Developer representation"""
        # TODO: Return constructor call string
        pass


# Exercise 3 Instructions:
print("""
EXERCISE 3 TASKS:
1. Complete the SmartList constructor and basic methods
2. Implement advanced methods (filter, map, reduce, chunk)
3. Implement container protocol methods
4. Implement operator overloading (+, *, ==)
5. Add utility methods (find, count, remove_duplicates)
6. Test your implementation:
""")

def test_smart_list():
    """Test the SmartList class"""
    print("\n🧪 Testing SmartList:")
    
    try:
        # Create and test SmartList
        slist = SmartList([3, 1, 4, 1, 5, 9, 2, 6])
        print(f"  Original: {slist}")
        
        # Test methods
        slist.remove_duplicates()
        print(f"  No duplicates: {slist}")
        
        evens = slist.filter(lambda x: x % 2 == 0)
        print(f"  Even numbers: {evens}")
        
        doubled = slist.map(lambda x: x * 2)
        print(f"  Doubled: {doubled}")
        
        chunks = slist.chunk(3)
        print(f"  Chunks of 3: {[str(chunk) for chunk in chunks]}")
        
        print("✅ All tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Complete the implementation above!")

# Uncomment when ready to test:
# test_smart_list()


# ============================================================================
# EXERCISE 4: POLYMORPHISM CHALLENGE (25 minutes)
# ============================================================================

print("\n" + "=" * 60)
print("🔷 EXERCISE 4: Animal Sounds Polymorphism")
print("=" * 60)
print("Goal: Demonstrate polymorphism with method overriding")
print()

class Animal:
    """Base animal class"""
    
    def __init__(self, name, species):
        """Initialize animal with name and species"""
        # TODO: Store name and species
        pass
    
    def make_sound(self):
        """Make generic animal sound"""
        # TODO: Return generic sound
        pass
    
    def move(self):
        """Describe how animal moves"""
        # TODO: Return generic movement
        pass
    
    def eat(self, food):
        """Describe eating behavior"""
        # TODO: Return eating description
        pass
    
    def __str__(self):
        """String representation"""
        # TODO: Return formatted animal description
        pass


class Dog(Animal):
    """Dog class with specific behaviors"""
    
    def __init__(self, name, breed="Mixed"):
        """Initialize dog with name and breed"""
        # TODO: Call parent constructor, store breed
        pass
    
    def make_sound(self):
        """Dogs bark"""
        # TODO: Return dog sound
        pass
    
    def move(self):
        """Dogs run"""
        # TODO: Return dog movement
        pass
    
    def fetch(self, item):
        """Dogs can fetch"""
        # TODO: Return fetch behavior
        pass


class Cat(Animal):
    """Cat class with specific behaviors"""
    
    def __init__(self, name, indoor=True):
        """Initialize cat with name and indoor status"""
        # TODO: Call parent constructor, store indoor status
        pass
    
    def make_sound(self):
        """Cats meow"""
        # TODO: Return cat sound
        pass
    
    def move(self):
        """Cats prowl"""
        # TODO: Return cat movement
        pass
    
    def hunt(self, prey):
        """Cats hunt"""
        # TODO: Return hunting behavior
        pass


class Bird(Animal):
    """Bird class with specific behaviors"""
    
    def __init__(self, name, can_fly=True):
        """Initialize bird with name and flying ability"""
        # TODO: Call parent constructor, store flying ability
        pass
    
    def make_sound(self):
        """Birds chirp"""
        # TODO: Return bird sound
        pass
    
    def move(self):
        """Birds fly or hop"""
        # TODO: Return bird movement based on can_fly
        pass
    
    def migrate(self, destination):
        """Birds can migrate"""
        # TODO: Return migration behavior
        pass


def animal_orchestra(animals):
    """Make all animals perform - demonstrate polymorphism"""
    print("\n🎵 Animal Orchestra Performance:")
    
    for animal in animals:
        print(f"  {animal}")
        print(f"    Sound: {animal.make_sound()}")
        print(f"    Movement: {animal.move()}")
        print(f"    Eating: {animal.eat('food')}")
        print()


# Exercise 4 Instructions:
print("""
EXERCISE 4 TASKS:
1. Complete the Animal base class with name, species, and basic methods
2. Complete Dog class inheriting from Animal:
   - Override make_sound() to return "Woof!"
   - Override move() to return "runs around"
   - Add fetch() method
3. Complete Cat class inheriting from Animal:
   - Override make_sound() to return "Meow"
   - Override move() to return "prowls silently"
   - Add hunt() method
4. Complete Bird class inheriting from Animal:
   - Override make_sound() to return "Chirp chirp"
   - Override move() based on can_fly attribute
   - Add migrate() method
5. Test polymorphism:
""")

def test_polymorphism():
    """Test polymorphism with animal classes"""
    print("\n🧪 Testing Animal Polymorphism:")
    
    try:
        # Create different animals
        dog = Dog("Buddy", "Golden Retriever")
        cat = Cat("Whiskers", indoor=True)
        bird = Bird("Tweety", can_fly=True)
        penguin = Bird("Pingu", can_fly=False)
        
        # Test polymorphism
        animals = [dog, cat, bird, penguin]
        animal_orchestra(animals)
        
        # Test specific methods
        print("🎾 Special Abilities:")
        print(f"  {dog.fetch('ball')}")
        print(f"  {cat.hunt('mouse')}")
        print(f"  {bird.migrate('south')}")
        
        print("✅ All tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Complete the implementation above!")

# Uncomment when ready to test:
# test_polymorphism()


# ============================================================================
# BONUS EXERCISE: GRADEBOOK SYSTEM (20 minutes)
# ============================================================================

print("\n" + "=" * 60)
print("🔷 BONUS EXERCISE: Student Gradebook System")
print("=" * 60)
print("Goal: Create a complete gradebook with inheritance and containers")
print()

class Person:
    """Base person class"""
    
    def __init__(self, first_name, last_name, email):
        """Initialize person with basic info"""
        # TODO: Store person information
        pass
    
    def full_name(self):
        """Return full name"""
        # TODO: Return formatted full name
        pass
    
    def __str__(self):
        """String representation"""
        # TODO: Return name and email
        pass


class Student(Person):
    """Student class with grades"""
    
    def __init__(self, first_name, last_name, email, student_id):
        """Initialize student"""
        # TODO: Call parent constructor, store student_id and grades
        pass
    
    def add_grade(self, assignment, grade):
        """Add a grade for an assignment"""
        # TODO: Store grade in grades dictionary
        pass
    
    def get_grade(self, assignment):
        """Get grade for specific assignment"""
        # TODO: Return grade or None if not found
        pass
    
    def average_grade(self):
        """Calculate average of all grades"""
        # TODO: Calculate and return average
        pass
    
    def letter_grade(self):
        """Convert average to letter grade"""
        # TODO: Convert average to A/B/C/D/F
        pass
    
    def __str__(self):
        """String representation with grade info"""
        # TODO: Include student info and current average
        pass


class Instructor(Person):
    """Instructor class"""
    
    def __init__(self, first_name, last_name, email, department):
        """Initialize instructor"""
        # TODO: Call parent constructor, store department
        pass
    
    def __str__(self):
        """String representation"""
        # TODO: Include instructor info and department
        pass


class Gradebook:
    """Gradebook container class"""
    
    def __init__(self, course_name, instructor):
        """Initialize gradebook"""
        # TODO: Store course info and create students list
        pass
    
    def add_student(self, student):
        """Add student to gradebook"""
        # TODO: Add student to list
        pass
    
    def find_student(self, student_id):
        """Find student by ID"""
        # TODO: Search for student by ID
        pass
    
    def record_grade(self, student_id, assignment, grade):
        """Record grade for student"""
        # TODO: Find student and add grade
        pass
    
    def class_average(self):
        """Calculate class average"""
        # TODO: Calculate average of all student averages
        pass
    
    def grade_distribution(self):
        """Show distribution of letter grades"""
        # TODO: Count each letter grade
        pass
    
    def top_students(self, n=3):
        """Return top n students by average"""
        # TODO: Sort students by average and return top n
        pass
    
    def __len__(self):
        """Number of students"""
        # TODO: Return number of students
        pass
    
    def __iter__(self):
        """Iterate over students"""
        # TODO: Return iterator over students
        pass
    
    def __str__(self):
        """String representation"""
        # TODO: Return course info and student count
        pass


# Bonus Exercise Instructions:
print("""
BONUS EXERCISE TASKS:
1. Complete Person base class with name and email
2. Complete Student class inheriting from Person:
   - Add student_id and grades dictionary
   - Implement grade management methods
   - Calculate averages and letter grades
3. Complete Instructor class inheriting from Person
4. Complete Gradebook container class:
   - Manage list of students
   - Record and retrieve grades
   - Calculate class statistics
   - Implement container protocol
5. Test the complete system:
""")

def test_gradebook():
    """Test the complete gradebook system"""
    print("\n🧪 Testing Gradebook System:")
    
    try:
        # Create instructor
        prof = Instructor("Dr. Jane", "Smith", "jane.smith@university.edu", "Computer Science")
        
        # Create gradebook
        gradebook = Gradebook("CSC 242 - OOP", prof)
        
        # Add students
        students = [
            Student("Alice", "Johnson", "alice@email.com", "12345"),
            Student("Bob", "Wilson", "bob@email.com", "12346"),
            Student("Carol", "Davis", "carol@email.com", "12347")
        ]
        
        for student in students:
            gradebook.add_student(student)
        
        # Record some grades
        assignments = ["Quiz 1", "Project 1", "Midterm"]
        grades = [
            ["12345", [85, 92, 88]],
            ["12346", [78, 85, 82]],
            ["12347", [95, 89, 93]]
        ]
        
        for student_id, student_grades in grades:
            for assignment, grade in zip(assignments, student_grades):
                gradebook.record_grade(student_id, assignment, grade)
        
        # Show results
        print(f"  Course: {gradebook}")
        print(f"  Class Average: {gradebook.class_average():.1f}")
        print(f"  Grade Distribution: {gradebook.grade_distribution()}")
        
        print("\n  Student Details:")
        for student in gradebook:
            print(f"    {student}")
        
        print("✅ All tests passed!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("   Complete the implementation above!")

# Uncomment when ready to test:
# test_gradebook()


# ============================================================================
# EXERCISE SOLUTIONS AND DISCUSSION
# ============================================================================

print("\n" + "=" * 60)
print("📝 EXERCISE WRAP-UP")
print("=" * 60)

print("""
🎯 LEARNING OBJECTIVES COVERED:

1. Inheritance Hierarchies:
   - Base classes and derived classes
   - super() for calling parent methods
   - Method overriding vs method overloading

2. Operator Overloading:
   - Arithmetic operators (+, -, *, /, -)
   - Comparison operators (==, <, >, etc.)
   - Container operators (__len__, __getitem__, etc.)

3. Polymorphism:
   - Same interface, different implementations
   - Dynamic method dispatch
   - Duck typing in Python

4. Container Classes:
   - Abstract Data Types (ADTs)
   - Iterator protocol implementation
   - Custom collection behaviors

5. Real-world Applications:
   - Mathematical computations (Vector class)
   - Data structures (SmartList)
   - System modeling (Gradebook)

💡 NEXT STEPS:
- Review solutions with instructor
- Discuss design patterns observed
- Explore more advanced OOP concepts
- Practice with additional exercises

🔄 FOR 180-MINUTE CLASS:
- Work through exercises progressively
- Pair programming encouraged
- Regular check-ins and discussions
- Live coding demonstrations
""")

def main():
    """Main function to run all exercises"""
    print("🚀 Starting Week 2 In-Class Exercises")
    print("=" * 60)
    
    print("📋 EXERCISE CHECKLIST:")
    print("□ Exercise 1: Shape Hierarchy (30 min)")
    print("□ Exercise 2: Vector Math (25 min)")
    print("□ Exercise 3: SmartList Container (40 min)")
    print("□ Exercise 4: Animal Polymorphism (25 min)")
    print("□ Bonus: Gradebook System (20 min)")
    
    print("\n💻 INSTRUCTIONS:")
    print("1. Work through exercises in order")
    print("2. Uncomment test functions when ready")
    print("3. Ask for help when stuck!")
    print("4. Share solutions with classmates")
    
    print("\n✨ Good luck with the exercises!")


if __name__ == "__main__":
    main()
