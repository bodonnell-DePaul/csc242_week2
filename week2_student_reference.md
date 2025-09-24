# Week 2: Advanced Class Concepts - Inheritance and Method Overriding
## Student Reference Guide for CSC 242

---

## Table of Contents
1. [Class Namespaces and Attribute Resolution](#class-namespaces-and-attribute-resolution)
2. [Constructors and Default Parameters](#constructors-and-default-parameters)
3. [String Representations (__str__ and __repr__)](#string-representations)
4. [Inheritance Fundamentals](#inheritance-fundamentals)
5. [Method Overriding and Extension](#method-overriding-and-extension)
6. [Operator Overloading](#operator-overloading)
7. [Container Abstract Data Types](#container-abstract-data-types)
8. [Example Code Files](#example-code-files)
9. [Practice Exercises](#practice-exercises)

---

## Class Namespaces and Attribute Resolution

### Understanding How Python Finds Attributes

When you write `object.attribute`, Python follows a specific search pattern:

1. **Instance namespace first**: Look in the object's own `__dict__`
2. **Class namespace**: Look in the class definition
3. **Parent class namespaces**: Search up the inheritance hierarchy

```python
class Vehicle:
    """Understanding attribute resolution"""
    wheels = 4  # Class variable
    
    def __init__(self, brand):
        self.brand = brand  # Instance variable
    
    def start_engine(self):
        return f"{self.brand} engine starting..."

# Demonstrate attribute resolution
car = Vehicle("Toyota")

# Instance attribute (found in car.__dict__)
print(car.brand)  # "Toyota"

# Class attribute (found in Vehicle.__dict__)
print(car.wheels)  # 4

# Method (found in Vehicle.__dict__)
print(car.start_engine())  # "Toyota engine starting..."
```

### Namespace Exploration Tools

```python
def explore_namespaces(obj):
    """Tool to understand object namespaces"""
    print(f"Object type: {type(obj).__name__}")
    print(f"Instance attributes: {obj.__dict__}")
    print(f"Class attributes: {type(obj).__dict__.keys()}")
    print(f"Method resolution order: {type(obj).__mro__}")

# Usage
car = Vehicle("Honda")
explore_namespaces(car)
```

---

## Constructors and Default Parameters

### Flexible Constructor Design

Constructors can be designed to handle varying numbers of parameters:

```python
class Animal:
    """A flexible animal class with default parameters"""
    
    def __init__(self, species="Unknown", language="Silent", age=0):
        """Constructor with default parameters"""
        self.species = species
        self.language = language
        self.age = age
        self.energy = 100
    
    def speak(self):
        """Make the animal speak"""
        if self.language == "Silent":
            return f"The {self.species} makes no sound"
        return f"I am a {self.species} and I {self.language}"
    
    def age_up(self, years=1):
        """Age the animal by specified years"""
        self.age += years
        self.energy = max(0, self.energy - years * 5)
        print(f"{self.species} is now {self.age} years old")

# Flexible usage
dog = Animal("Dog", "Bark")
cat = Animal("Cat")  # Uses default language
mystery = Animal()   # Uses all defaults
```

### Constructor Patterns

```python
class BankAccount:
    """Demonstrating common constructor patterns"""
    
    def __init__(self, owner, balance=0.0, account_type="Checking"):
        # Validation in constructor
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Owner name must be a non-empty string")
        
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        # Attribute initialization
        self.owner = owner.strip()
        self.balance = float(balance)
        self.account_type = account_type
        self.transaction_count = 0
    
    @classmethod
    def create_savings_account(cls, owner, initial_deposit=1000.0):
        """Alternative constructor for savings accounts"""
        return cls(owner, initial_deposit, "Savings")
    
    @classmethod
    def create_from_string(cls, account_string):
        """Create account from formatted string: 'Name,Balance,Type'"""
        parts = account_string.split(',')
        if len(parts) != 3:
            raise ValueError("Invalid account string format")
        
        name, balance, acc_type = parts
        return cls(name, float(balance), acc_type)
```

---

## String Representations

### The Difference Between __str__ and __repr__

- **`__str__`**: Human-readable representation (for end users)
- **`__repr__`**: Developer-friendly representation (for debugging)

```python
class Point:
    """Demonstrating string representations"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """Human-readable string - what users see"""
        return f"Point at ({self.x}, {self.y})"
    
    def __repr__(self):
        """Developer representation - should be unambiguous"""
        return f"Point({self.x}, {self.y})"
    
    def distance_from_origin(self):
        """Calculate distance from origin"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Usage demonstration
p = Point(3, 4)
print(str(p))    # "Point at (3, 4)"
print(repr(p))   # "Point(3, 4)"
print(p)         # Uses __str__ by default
```

### Best Practices for String Methods

```python
class Student:
    """Well-designed string representations"""
    
    def __init__(self, name, student_id, gpa=0.0):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
    
    def __str__(self):
        """Clean, readable format"""
        return f"{self.name} (ID: {self.student_id}, GPA: {self.gpa:.2f})"
    
    def __repr__(self):
        """Unambiguous representation that could recreate object"""
        return f"Student('{self.name}', '{self.student_id}', {self.gpa})"
    
    def __format__(self, format_spec):
        """Custom formatting support"""
        if format_spec == 'short':
            return f"{self.name} ({self.student_id})"
        elif format_spec == 'gpa':
            return f"{self.name}: {self.gpa:.2f}"
        else:
            return str(self)

# Usage
student = Student("Alice Johnson", "A12345", 3.75)
print(f"Default: {student}")
print(f"Short: {student:short}")
print(f"GPA focus: {student:gpa}")
```

---

## Inheritance Fundamentals

### Creating Subclasses

Inheritance allows you to create new classes based on existing ones:

```python
class Vehicle:
    """Base vehicle class"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        """Start the vehicle"""
        self.is_running = True
        return f"{self.brand} {self.model} started"
    
    def stop(self):
        """Stop the vehicle"""
        self.is_running = False
        return f"{self.brand} {self.model} stopped"
    
    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    """Car inherits from Vehicle"""
    
    def __init__(self, brand, model, year, doors=4):
        super().__init__(brand, model, year)  # Call parent constructor
        self.doors = doors
        self.passengers = 0
    
    def add_passenger(self, count=1):
        """Add passengers to the car"""
        max_passengers = self.doors + 1  # Simple capacity rule
        if self.passengers + count <= max_passengers:
            self.passengers += count
            return f"Added {count} passenger(s). Total: {self.passengers}"
        else:
            return f"Cannot add {count} passengers. Capacity: {max_passengers}"
    
    def honk(self):
        """Cars can honk"""
        return "Beep beep!"

class Motorcycle(Vehicle):
    """Motorcycle inherits from Vehicle"""
    
    def __init__(self, brand, model, year, engine_size):
        super().__init__(brand, model, year)
        self.engine_size = engine_size
        self.has_sidecar = False
    
    def add_sidecar(self):
        """Add a sidecar to the motorcycle"""
        self.has_sidecar = True
        return "Sidecar attached!"
    
    def wheelie(self):
        """Motorcycles can do wheelies"""
        if self.is_running:
            return "Performing a wheelie!"
        else:
            return "Start the engine first!"
```

### The isinstance() and issubclass() Functions

```python
# Create instances
car = Car("Toyota", "Camry", 2023)
bike = Motorcycle("Harley", "Street 750", 2022, 750)

# Check instance types
print(isinstance(car, Car))        # True
print(isinstance(car, Vehicle))    # True
print(isinstance(car, Motorcycle)) # False

# Check class relationships
print(issubclass(Car, Vehicle))        # True
print(issubclass(Motorcycle, Vehicle)) # True
print(issubclass(Car, Motorcycle))     # False
```

---

## Method Overriding and Extension

### Complete Method Replacement

```python
class Shape:
    """Base shape class"""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Base implementation - to be overridden"""
        return 0
    
    def perimeter(self):
        """Base implementation - to be overridden"""
        return 0
    
    def describe(self):
        """General description"""
        return f"This is a {self.name}"

class Rectangle(Shape):
    """Rectangle completely overrides area and perimeter"""
    
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        """Override: completely new implementation"""
        return self.width * self.height
    
    def perimeter(self):
        """Override: completely new implementation"""
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle with overridden methods"""
    
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        """Override: completely new implementation"""
        import math
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Override: completely new implementation"""
        import math
        return 2 * math.pi * self.radius
```

### Method Extension (Calling Parent Methods)

```python
class Employee:
    """Base employee class"""
    
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.projects = []
    
    def add_project(self, project):
        """Add a project to employee's workload"""
        self.projects.append(project)
        print(f"{self.name} assigned to {project}")
    
    def get_info(self):
        """Get basic employee information"""
        return f"Employee: {self.name} (ID: {self.employee_id})"

class Manager(Employee):
    """Manager extends Employee"""
    
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)  # Call parent constructor
        self.department = department
        self.team_members = []
    
    def add_project(self, project):
        """Extend parent method with management duties"""
        super().add_project(project)  # Call parent method first
        print(f"Manager {self.name} will oversee {project}")
    
    def add_team_member(self, employee):
        """Manager-specific method"""
        self.team_members.append(employee)
        print(f"{employee.name} added to {self.name}'s team")
    
    def get_info(self):
        """Extend parent method with additional info"""
        base_info = super().get_info()  # Get parent information
        return f"{base_info}, Department: {self.department}, Team Size: {len(self.team_members)}"
```

---

## Operator Overloading

### Mathematical Operators

```python
class Vector:
    """A 2D vector class with operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Vector addition: v1 + v2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Can only add Vector to Vector")
    
    def __sub__(self, other):
        """Vector subtraction: v1 - v2"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Can only subtract Vector from Vector")
    
    def __mul__(self, scalar):
        """Scalar multiplication: v * scalar"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Can only multiply Vector by number")
    
    def __rmul__(self, scalar):
        """Right multiplication: scalar * v"""
        return self.__mul__(scalar)
    
    def __eq__(self, other):
        """Equality comparison: v1 == v2"""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def magnitude(self):
        """Calculate vector magnitude"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Usage examples
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)    # Vector(4, 6)
print(v1 - v2)    # Vector(2, 2)
print(v1 * 2)     # Vector(6, 8)
print(3 * v1)     # Vector(9, 12)
print(v1 == v2)   # False
```

### Comparison Operators

```python
class Grade:
    """A grade class with comparison operators"""
    
    def __init__(self, points, max_points=100):
        self.points = points
        self.max_points = max_points
    
    @property
    def percentage(self):
        """Calculate percentage"""
        return (self.points / self.max_points) * 100
    
    def __lt__(self, other):
        """Less than: grade1 < grade2"""
        return self.percentage < other.percentage
    
    def __le__(self, other):
        """Less than or equal: grade1 <= grade2"""
        return self.percentage <= other.percentage
    
    def __gt__(self, other):
        """Greater than: grade1 > grade2"""
        return self.percentage > other.percentage
    
    def __ge__(self, other):
        """Greater than or equal: grade1 >= grade2"""
        return self.percentage >= other.percentage
    
    def __eq__(self, other):
        """Equal: grade1 == grade2"""
        return abs(self.percentage - other.percentage) < 0.01
    
    def __str__(self):
        return f"{self.points}/{self.max_points} ({self.percentage:.1f}%)"

# Usage
grade1 = Grade(85, 100)
grade2 = Grade(42, 50)  # Also 84%

print(grade1 > grade2)  # True
print(grade1 == grade2) # False (85% vs 84%)
```

---

## Container Abstract Data Types

### Queue Implementation

```python
class Queue:
    """A First-In-First-Out (FIFO) container"""
    
    def __init__(self):
        """Initialize empty queue"""
        self._items = []
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        self._items.append(item)
    
    def dequeue(self):
        """Remove and return item from front of queue"""
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty queue")
        return self._items.pop(0)
    
    def front(self):
        """Return front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._items[0]
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self._items) == 0
    
    def size(self):
        """Return number of items in queue"""
        return len(self._items)
    
    def __str__(self):
        """String representation"""
        return f"Queue({self._items})"
    
    def __repr__(self):
        return f"Queue({self._items})"
    
    def __len__(self):
        """Support len() function"""
        return len(self._items)
    
    def __iter__(self):
        """Make queue iterable"""
        return iter(self._items)

# Usage
q = Queue()
q.enqueue("first")
q.enqueue("second")
q.enqueue("third")

print(f"Queue: {q}")
print(f"Size: {len(q)}")
print(f"Front: {q.front()}")
print(f"Dequeue: {q.dequeue()}")
print(f"After dequeue: {q}")
```

### Stack Implementation

```python
class Stack:
    """A Last-In-First-Out (LIFO) container"""
    
    def __init__(self):
        """Initialize empty stack"""
        self._items = []
    
    def push(self, item):
        """Add item to top of stack"""
        self._items.append(item)
    
    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise IndexError("Cannot pop from empty stack")
        return self._items.pop()
    
    def peek(self):
        """Return top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self._items) == 0
    
    def size(self):
        """Return number of items in stack"""
        return len(self._items)
    
    def __str__(self):
        """String representation (top on right)"""
        return f"Stack({self._items})"
    
    def __repr__(self):
        return f"Stack({self._items})"
    
    def __len__(self):
        """Support len() function"""
        return len(self._items)

# Usage
s = Stack()
s.push("bottom")
s.push("middle")
s.push("top")

print(f"Stack: {s}")
print(f"Peek: {s.peek()}")
print(f"Pop: {s.pop()}")
print(f"After pop: {s}")
```

---

## Example Code Files

The following Python files accompany this reference guide:

1. **`inheritance_examples.py`** - Comprehensive inheritance demonstrations
2. **`method_overriding.py`** - Method overriding and extension patterns
3. **`operator_overloading.py`** - Complete operator overloading examples
4. **`container_classes.py`** - Queue, Stack, and custom container implementations
5. **`animal_class.py`** - Progressive animal class development
6. **`in_class_exercises_week2.py`** - Interactive classroom activities

---

## Practice Exercises

### Exercise 1: Animal Hierarchy
Create an animal inheritance hierarchy with the following classes:
- `Animal` (base class) with species, age, and sound methods
- `Mammal` (inherits from Animal) with additional fur_color attribute
- `Bird` (inherits from Animal) with can_fly and wingspan attributes
- Specific animals like `Dog`, `Cat`, `Eagle`, `Penguin`

### Exercise 2: Shape Calculator
Design a shape calculation system:
- `Shape` base class with abstract area and perimeter methods
- Concrete classes: `Rectangle`, `Circle`, `Triangle`
- Each should override area and perimeter calculations
- Add comparison operators to compare shapes by area

### Exercise 3: Bank Account System
Extend the bank account example:
- `Account` base class with basic deposit/withdraw functionality
- `CheckingAccount` with overdraft protection
- `SavingsAccount` with interest calculation
- `BusinessAccount` with transaction fees

### Exercise 4: Custom Container
Create a `Deque` (double-ended queue) class:
- Support adding/removing from both ends
- Implement `append_left()`, `append_right()`, `pop_left()`, `pop_right()`
- Make it iterable and support len()

---

## Study Tips

1. **Practice Method Resolution**: Use `super()` correctly in inheritance
2. **Understand `self`**: Remember it refers to the instance calling the method
3. **Use Type Checking**: Employ `isinstance()` for robust code
4. **Design Before Coding**: Plan your class hierarchy before implementation
5. **Test Thoroughly**: Create instances and test all methods

---

## Common Pitfalls to Avoid

1. **Forgetting `super()`**: Not calling parent constructors
2. **Circular Imports**: Importing modules that import each other
3. **Mutable Default Arguments**: Using lists/dicts as default parameters
4. **Breaking Liskov Substitution**: Subclasses should be substitutable for base classes
5. **Over-engineering**: Creating unnecessarily complex hierarchies

---

*This reference guide covers the essential concepts for object-oriented programming in Python. Master these concepts to build robust, maintainable applications.*
